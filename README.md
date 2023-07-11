
<img src="https://i.imgur.com/ly4aSer.png">

# Pirate Chain Light Wallet Server Status Tool

Use this script to check teh status of the Pirate Chain light wallet servers. It checks that the dmain names are resolvable, tests the server ping time, ensures it can get a gRPC response, and checks the current block height is similar bvetween servers.

1. Install dependencies
```bash
pip3 install tabulate grpcio-tool
```

2. clone into this repo:
```bash
git clone https://github.com/scott-ftf/lightwalletd_status.git
cd lightwalletd_status
```

3. Make any changes to the configuration settings, then run the script:
```bash
python3 lightwalletd_status.py
```



---

## (OPTIONAL) Manually Create Protocol Buffer definition files

These files are already included in the `lib` library, but to generate the Protocol Buffer definition files manually, follow these steps:

1. Install the protobuf compiler (specific to Ubuntu or Debian-based systems):

```bash
sudo apt install protobuf-compiler
```

2. Install the protobuf package:
```bash
pip3 install protobuf==3.20
```

3. Clone the lightwalletd repository:
```bash
git clone https://github.com/PirateNetwork/lightwalletd.git
```

4. Generate the Python proto definitions:
```bash
cd lightwalletd/walletrpc
python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. service.proto
python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. compact_formats.proto

```

5. Move the newly generated `service_pb2.py`, `service_pb2_grpc.py`, `compact_formats_pb2.py`, and `compact_formats_pb2_grpc.py` files to the same directory as the main script.
