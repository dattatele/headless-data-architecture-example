# Headless Data Architecture with Apache Kafka, Flink, and Iceberg

This repository demonstrates a Headless Data Architecture utilizing Apache Kafka, Apache Flink, and Apache Iceberg. The setup is designed for real-time data streaming, processing, and storage using Docker and Docker-Compose. Monitoring is provided by Prometheus and Grafana.

## Quick Start

1. **Clone the Repository**
   ```bash
   git clone <repo_url>
   cd <repo_directory>
   ```

2. **Start the Environment**
   ```bash
   docker-compose up --build
   ```

3. **Create Kafka Topics**
   ```bash
   ./scripts/create-topics.sh
   ```

4. **Deploy Flink Jobs**
   - **Python**: Use Docker container to run `flink-python/main.py`.
   - **Java**: Compile and run `flink-java/RealTimeSalesAnalytics.java`.

5. **Generate Data**
   The data generator sends synthetic sales orders to Kafka.

6. **Access Monitoring Dashboards**
   - **Prometheus**: [http://localhost:9090](http://localhost:9090)
   - **Grafana**: [http://localhost:3000](http://localhost:3000) (Default credentials: `admin` / `admin`)

## Components
- **Apache Kafka**: Event streaming backbone.
- **Apache Flink**: Real-time stream processing.
- **Apache Iceberg**: Data lake storage format.
- **Prometheus and Grafana**: Monitoring and visualization.

## Project Structure

The repository is structured as follows:

.
├── docker-compose.yml
├── kafka-setup
│   ├── Dockerfile
│   └── kafka-config
│       └── kafka-server.properties
├── flink-python
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py
├── flink-java
│   ├── Dockerfile
│   └── RealTimeSalesAnalytics.java
├── iceberg-setup
│   ├── Dockerfile
│   ├── iceberg.properties
│   └── init.sql
├── data-generator
│   ├── Dockerfile
│   └── generate_data.py
├── monitoring
│   ├── prometheus.yml
│   └── grafana
│       ├── dashboards
│       │   └── sales_analytics_dashboard.json
│       ├── Dockerfile
│       └── grafana.ini
├── README.md
└── scripts
    └── create-topics.sh


