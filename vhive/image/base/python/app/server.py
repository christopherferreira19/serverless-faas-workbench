import sys
import os

import logging
import json
from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc
from lambda_function import lambda_handler

class Service(service_pb2_grpc.ServiceServicer):

    def Serve(self, request, context):
        event = json.loads(request.message)
        result = lambda_handler(event, {})
        if isinstance(result, str):
            message = result
        else:
            message = json.dumps(result)
        return service_pb2.Response(message = message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ServiceServicer_to_server(Service(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print("Starting server")
    serve()