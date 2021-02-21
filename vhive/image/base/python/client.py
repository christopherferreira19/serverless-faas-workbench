import sys
import os

src_path = os.path.abspath(__file__ + "/../app")
sys.path.insert(0, src_path)

import grpc
import service_pb2
import service_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = service_pb2_grpc.ServiceStub(channel)
    message = ' '.join(sys.argv[1:])
    response = stub.Serve(service_pb2.Request(message=message))
    print("Client received: " + response.message)

if __name__ == '__main__':
    run()