#!/bin/bash
kafka-topics.sh --create --topic sales_orders --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
kafka-topics.sh --create --topic inventory_updates --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1