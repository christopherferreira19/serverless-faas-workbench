FROM python:3.8.1-alpine3.11

RUN apk update
RUN apk add --update --no-cache \
	gcc \
	g++ \
	cmake \
	protobuf \
	openblas-dev \
	lapack-dev \
	zlib-dev \
	libjpeg-turbo-dev

RUN pip3 install --upgrade pip
RUN pip3 install --user protobuf==3.11.3
RUN pip3 install --user grpcio==1.26.0
RUN pip3 install --user boto3==1.17.11
RUN pip3 install --user numpy==1.20.1
RUN pip3 install --user scipy==1.6.1
RUN pip3 install --user pandas==1.2.2
RUN pip3 install --user scikit-learn==0.24.1
RUN pip3 install --user sklearn
RUN ln -s \
	/root/.local/lib/python3.8/site-packages/joblib \
	/root/.local/lib/python3.8/site-packages/sklearn/externals/joblib

EXPOSE 50051
STOPSIGNAL SIGKILL
ENV PYTHONPATH "/app"
ENV PYTHONUNBUFFERED True
ADD app /${PYTHONPATH}
CMD ["/usr/local/bin/python", "/app/server.py"]
