ARG PYTHON_BASE_IMG
FROM ${PYTHON_BASE_IMG}

RUN pip3 install --user Pillow==8.1.0
COPY lambda_function.py ops.py ${PYTHONPATH}/
