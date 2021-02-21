import os

import botocore
import boto3

import grpc
import service_pb2
import service_pb2_grpc

def _minio_kwargs():
    return {
        'endpoint_url':          os.environ['MINIO_URL'],
        'aws_access_key_id':     os.environ['MINIO_ACCESSKEYID'],
        'aws_secret_access_key': os.environ['MINIO_SECRETACCESSKEY'],
        'config':                botocore.client.Config(signature_version='s3v4'),
        'region_name':           'us-east-1',
    }

def resource(kind):
    if kind == 's3':
        return boto3.resource('s3', **_minio_kwargs())
    else:
        raise NameError(f"[Boto3Vhive] Unsupported resource {kind}")

def client(kind):
    if kind == 's3':
        return boto3.client('s3', **_minio_kwargs())
    elif kind == 'lambda':
        return Boto3ClientLambda()
    else:
        raise NameError(f"[Boto3Vhive] Unsupported client {kind}")

class Boto3VhiveClientLambda:

    def invoke(FunctionName, InvocationType, Payload):
        namespace_name = os.environ['VHIVE_NAMESPACE_NAME']
        gateway_url = os.environ['VHIVE_GATEWAY_URL']
        url = f'{FunctionName}.{namespace_name}.{gateway_url}'

        channel = grpc.insecure_channel(url)
        stub = service_pb2_grpc.ServiceStub(channel)
        response = stub.Serve(service_pb2.Request(message=Payload))
        return { 'Payload': response.message }

