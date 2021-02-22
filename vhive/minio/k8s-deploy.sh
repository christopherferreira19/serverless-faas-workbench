#! /bin/bash

dir="$(readlink -f "$(dirname "$0")")"

kubectl apply -f "${dir}"/k8s/deployment.yaml
kubectl apply -f "${dir}"/k8s/service.yaml
