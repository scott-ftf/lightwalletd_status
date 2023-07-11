import grpc
from lib import service_pb2
from lib import service_pb2_grpc
import socket
import time
import tabulate

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

# Set the maximum allowed difference in block heights
max_height_difference = 5

# Create an empty list to store the table rows
table_rows = []

# Create a secure channel and stub for each server
print("\nTesting Pirate Light Wallet servers, please standby...\n")
for url in server_urls:
    row = []

    try:
        # Resolve domain name to IP address
        ip_address = socket.gethostbyname(url.split(':')[0])
        row.append(url)
        row.append(ip_address)

        # Ping the server to check if it's up
        start_time = time.time()
        channel = grpc.secure_channel(url, grpc.ssl_channel_credentials())
        stub = service_pb2_grpc.CompactTxStreamerStub(channel)

        # Set the timeout for the ping test
        response_future = stub.GetLatestBlock.future(service_pb2.Empty())
        response = response_future.result(timeout=ping_timeout)

        ping_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        row.append(round(ping_time, 2))

        # Get the current block height
        block_height = response.height
        row.append(block_height)

        # Check block height difference with previous servers
        for prev_row in table_rows:
            prev_height = prev_row[3]  # Height is at index 3
            if abs(block_height - prev_height) > max_height_difference:
                row.append("WARN (Height out of range)")
                break

        row.append("UP")

    except (socket.gaierror, grpc.RpcError, grpc.FutureTimeoutError) as e:
        row.append("DOWN")

    table_rows.append(row)

# Generate a comparison table
headers = ["Domain", "Resolve", "Ping (ms)", "Height", "Status"]
table = tabulate.tabulate(table_rows, headers=headers)

# Print the comparison table
print("Server Report:")
print("=================")
print(table)
