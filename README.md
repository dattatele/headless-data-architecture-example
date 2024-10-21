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

### Advantages of Headless Data Architecture
Headless data architecture provides several advantages over traditional streaming data architectures:

1. **Flexibility**: The headless data architecture allows the decoupling of data producers, processors, and consumers. This means that each component can evolve independently, which increases overall system flexibility.

2. **Cost Efficiency**: By utilizing components like Kafka, Flink, and Iceberg, the headless approach reduces data duplication and leverages efficient storage formats. The use of Apache Iceberg provides versioned, efficient table formats, reducing costs related to data governance.

3. **Monitoring**: Integrated monitoring with Prometheus and Grafana allows for real-time visibility into the pipeline, providing insights into data flow, system performance, and any potential bottlenecks.

4. **Error Proofing**: Data processing using Flink allows for exactly-once semantics, which minimizes data loss and ensures that all events are processed without errors. Kafka’s fault-tolerant architecture also helps in recovery from failures.

5. **Data Governance and Compliance**: With Apache Iceberg, all data is versioned and stored in a structured way that supports schema evolution. This simplifies tracking data lineage, making it easier to comply with data governance and compliance requirements.

6. **Single Location and No Data Copy Required**: Apache Iceberg provides a unified data lake that allows you to keep all data in a single location without needing copies. It simplifies data management, reduces costs associated with data copying, and avoids inconsistencies that can arise when multiple data copies exist.


### How It Works
1. **Data Generation**: A data generator script (`data-generator/generate_data.py`) is used to produce synthetic sales data and send it to a Kafka topic (`sales_orders`). This represents the incoming data from different systems or sensors.

2. **Kafka as Data Stream**: Apache Kafka acts as a streaming platform that captures and brokers the generated data. Kafka allows multiple producers and consumers to interact with data streams in a scalable, fault-tolerant manner. The topics (`sales_orders`, `inventory_updates`) represent specific types of events that are produced and consumed by the system.

3. **Real-time Processing with Flink**: Apache Flink consumes the streaming data from Kafka, processes it in real time, and performs necessary transformations. The Flink jobs (implemented in both Python and Java) aggregate sales data by region and compute metrics such as total sales amount.
   - In the Python implementation (`flink-python/main.py`), Flink reads data from Kafka, aggregates the total sales per region, and prints the results.
   - In the Java implementation (`flink-java/RealTimeSalesAnalytics.java`), Flink reads data from Kafka, parses the sales orders, aggregates sales per region, and outputs the results.

4. **Data Lake Storage with Iceberg**: Once the data has been processed, the aggregated results are written to Apache Iceberg, which acts as the data lake. Iceberg is used to store large volumes of data in a structured format that allows for easy querying, data versioning, and schema evolution. This ensures that both raw and processed data are retained for downstream analysis and auditing purposes.

5. **Monitoring and Visualization**: The entire pipeline is monitored using Prometheus and Grafana.
   - **Prometheus** scrapes metrics from Kafka, Flink, and other components to provide insights into system performance.
   - **Grafana** visualizes these metrics, providing dashboards such as the `Sales Analytics Dashboard`, which shows aggregated sales data by region. The dashboard (`monitoring/grafana/dashboards/sales_analytics_dashboard.json`) includes graphs that visualize the total sales by region over time.


### Prerequisites
- **Docker** and **Docker Compose** installed on your machine.
- **Java** (for Java Flink implementation).
- **Python 3.8** (for Python implementation).


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





