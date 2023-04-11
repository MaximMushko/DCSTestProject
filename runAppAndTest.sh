mvn package spring-boot:repackage

docker run -it --name redis-cache-name -p 6379:6379 redis:5.0.3

docker build -t my-app:1.0 .
docker run --name my-app -p 8080:8080 my-app:1.0

run PYTHONPATH=. pytest api_tests/tests/apitest.py