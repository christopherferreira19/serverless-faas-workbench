module github.com/christopherferreira19/serverless-faas-workbench/vhive/client

go 1.15

replace github.com/christopherferreira19/serverless-faas-workbench/vhive/client/service => ./service

require (
	github.com/christopherferreira19/serverless-faas-workbench/vhive/client/service v0.0.0-00010101000000-000000000000 // indirect
	github.com/sirupsen/logrus v1.8.0
	google.golang.org/grpc v1.32.0
	google.golang.org/protobuf v1.25.0
)
