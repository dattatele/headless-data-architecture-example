docker-build:
	docker-compose build

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

create-topics:
	./scripts/create-topics.sh

start-flink-python:
	docker exec -it flink-jobmanager python /app/main.py

start-flink-java:
	docker exec -it flink-jobmanager java -cp /app/RealTimeSalesAnalytics.jar RealTimeSalesAnalytics

monitoring:
	open http://localhost:3000
	open http://localhost:9090