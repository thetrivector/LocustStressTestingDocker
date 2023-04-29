# Locust Test Environment

docker stack deploy -c compose.yaml locust
docker service scale locust_worker=10

