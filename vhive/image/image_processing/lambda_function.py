import vhive
import uuid
from time import time
from PIL import Image

import ops

s3_client = vhive.client('s3')
FILE_NAME_INDEX = 2


def image_processing(file_name, image_path, operation):
    path_list = []
    start = time()
    with Image.open(image_path) as image:

        if operation == "flip_left_right":
            path_list += ops.flip_left_right(image, file_name)
        elif operation == "flip_top_bottom":
            path_list += ops.flip_top_bottom(image, file_name)
        elif operation == "rotate90":
            path_list += ops.rotate90(image, file_name)
        elif operation == "rotate180":
            path_list += ops.rotate180(image, file_name)
        elif operation == "rotate270":
            path_list += ops.rotate270(image, file_name)
        elif operation == "filter_blur":
            path_list += ops.filter_blur(image, file_name)
        elif operation == "filter_contour":
            path_list += ops.filter_contour(image, file_name)
        elif operation == "filter_sharpen":
            path_list += ops.filter_sharpen(image, file_name)
        elif operation == "gray_scale":
            path_list += ops.gray_scale(image, file_name)
        elif operation == "resize":
            path_list += ops.resize(image, file_name)
        else:
            raise NameError(f"Unknown operation {operation}")

    latency = time() - start
    return latency, path_list


def lambda_handler(event, context):
    input_bucket = event['input_bucket']
    object_key = event['object_key']
    output_bucket = event['output_bucket']
    operation = event['operation']

    download_path = '/tmp/{}{}'.format(uuid.uuid4(), object_key)

    s3_client.download_file(input_bucket, object_key, download_path)

    latency, path_list = image_processing(object_key, download_path, operation)

    for upload_path in path_list:
        s3_client.upload_file(upload_path, output_bucket, upload_path.split("/")[FILE_NAME_INDEX])

    return latency
