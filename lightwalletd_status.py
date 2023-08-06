import grpc
from lib import service_pb2
from lib import service_pb2_grpc
import socket
import time
import tabulate
import subprocess
import re
import os

DEBUG = False # Turn on debug for extra gRPC output

# Define a list of server URLs
server_urls = [
    "lightd1.pirate.black:443",
    "piratelightd1.cryptoforge.cc:443",
    "piratelightd2.cryptoforge.cc:443",
    "piratelightd3.cryptoforge.cc:443",
    "piratelightd4.cryptoforge.cc:443"
]

# Set the ping timeout in seconds
ping_timeout = 5

# provide more output if DEBUG = True
os.environ['GRPC_VERBOSITY'] = 'DEBUG' if DEBUG else 'ERROR'


# Create an empty list to store the table rows
table_rows = []

def icmp_ping(host):
    try:
        output = subprocess.check_output("ping -c 1 " + host, shell=True, universal_newlines=True)
        # Extract the ping time in ms using regex
        ping_time = float(re.findall(r"time=(\d+.\d+)", output)[0])
        return ping_time
    except Exception:
        return "Unreachable"


# Create a secure channel and stub for each server
print("\nTesting Pirate Light Wallet servers, please standby...\n")

# Create an empty list to store the error logs
error_logs = []

for url in server_urls:
    row = []
    host, port = url.split(':')
    port = int(port)

    try:
        # Resolve domain name to IP address
        ip_address = socket.gethostbyname(host)
        row.append(url)
        row.append(ip_address)
    except socket.gaierror as e:
        row.extend([url, "Failed", "N/A", "N/A", "N/A", "Resolve Failed"])
        error_logs.append(f"Server - {url} - Resolve Failed\n{str(e)}")
        table_rows.append(row)
        continue

    # Perform ICMP ping test
    icmp_result = icmp_ping(host)
    row.append(icmp_result)

    try:
        # Ping the server to check if it's up
        start_time = time.time()
        channel = grpc.secure_channel(url, grpc.ssl_channel_credentials())
        stub = service_pb2_grpc.CompactTxStreamerStub(channel)

        # Set the timeout for the ping test
        response_future = stub.GetLatestBlock.future(service_pb2.Empty())
        try:
            response = response_future.result(timeout=ping_timeout)
        except Exception as e:
            raise grpc.FutureTimeoutError(e)
        
        ping_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        row.append(round(ping_time, 2))
    except grpc.FutureTimeoutError as e:
        row.extend(["Timeout", "N/A", "gRPC Response Failed"])
        error_message = f"Server - {url} - gRPC Response Failed\n{str(e)}\nCode: {e.code()}\nDetails: {e.details()}"
        error_logs.append(error_message)
        table_rows.append(row)
        continue

    try:
        # Get server's lightd info
        response_future = stub.GetLightdInfo.future(service_pb2.Empty())
        response = response_future.result(timeout=ping_timeout)
        block_height = response.blockHeight
        row.append(block_height)
        row.append("OK")
    except (grpc.RpcError, grpc.FutureTimeoutError) as e:
        row.extend(["N/A", "N/A", "gRPC Failed"])
        error_logs.append(f"Server - {url} - gRPC Failed\n{str(e)}")

    table_rows.append(row)

    # Generate a comparison table
    headers = ["Domain", "Resolve", "Ping (ms)", "gRPC (ms)", "Height", "Status"]
    table = tabulate.tabulate(table_rows, headers=headers)

# Print the comparison table
print("\n\n")
print(table)

# Print the error logs
if error_logs:
    print("\nError Log:")
    print("=================\n")
    for error_log in error_logs:
        print(error_log)
