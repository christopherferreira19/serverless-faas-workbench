ARG PYTHON_BASE_IMG
FROM ${PYTHON_BASE_IMG}

RUN pip3 install --user pyaes
COPY lambda_function.py ${PYTHONPATH}/
