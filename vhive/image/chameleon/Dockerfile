ARG PYTHON_BASE_IMG
FROM ${PYTHON_BASE_IMG}

RUN pip3 install --user Chameleon==3.8.1
COPY lambda_function.py ${PYTHONPATH}/
