# Instructions to run

Inside of this git directory, to build the docker image run: 

  docker build -f ./Dockerfile -t receipt-processor-challenge .

To run the docker image:

  docker run -d --name mycontainer -p 8000:8000 receipt-processor-challenge

Then the api should be available at localhost:8000