import os

import botocore
import boto3

import grpc
import service_pb2
import service_pb2_grpc

if 'MINIO_URL' in os.environ:
    MINIO_URL = os.environ['MINIO_URL']
else:
    MINIO_URL = "http://192.168.1.241:9000"

if 'MINIO_ACCESSKEYID' in os.environ:
    MINIO_ACCESSKEYID = os.environ['MINIO_ACCESSKEYID']
else:
    MINIO_ACCESSKEYID = 'minio'

if 'MINIO_SECRETACCESSKEY' in os.environ:
    MINIO_SECRETACCESSKEY = os.environ['MINIO_SECRETACCESSKEY']
else:
    MINIO_SECRETACCESSKEY = 'minio123'

def _minio_kwargs():
    return {
        'endpoint_url':          MINIO_URL,
        'aws_access_key_id':     MINIO_ACCESSKEYID,
        'aws_secret_access_key': MINIO_SECRETACCESSKEY,
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
        return Boto3VhiveClientLambda()
    else:
        raise NameError(f"[Boto3Vhive] Unsupported client {kind}")

class Boto3VhiveClientLambda:

    def invoke(self, FunctionName, InvocationType, Payload):
        print(f"Invoking {FunctionName} with payload: {Payload}")
        url = f'{FunctionName}.default.192.168.1.240.xip.io'

        channel = grpc.insecure_channel(url)
        stub = service_pb2_grpc.ServiceStub(channel)
        response = stub.Serve(service_pb2.Request(message=Payload))
        return { 'Payload': Boto3VhiveStreamingBody(response.message) }

class Boto3VhiveStreamingBody:
    def __init__(self, body):
        self._body = body
    def read(self):
        return body