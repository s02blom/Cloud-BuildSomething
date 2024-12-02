# Cloud-BuildSomething
## The to-do app

## Run

### Run containers individually
`cd Containers/Frontend`
`docker build -t cloud .`
`docker run -p 5000:5000 cloud`

### Run all in a docker compose
`cd Containers`
`docker compose -f "docker-compose.yml" up`

### Run Kubernetes
`minikube start`
`kubectl apply -f ./Kubernetics/volumes.json`
`kubectl apply -f ./Kubernetics/ToDoListner.json`

Delete: 
`kubectl delete --cascade='foreground' -f .\Kubernetics\ToDoListner.json`
`kubectl delete --cascade='foreground' -f .\Kubernetics\volumes.json`