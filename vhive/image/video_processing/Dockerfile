ARG PYTHON_BASE_IMG
FROM ${PYTHON_BASE_IMG}

RUN pip3 install --user opencv-python==4.5.1.48
COPY lambda_function.py ops.py ${PYTHONPATH}/
