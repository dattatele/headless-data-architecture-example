from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer
import json
from typing import Dict

def main() -> None:
    """
    Main function to execute the Flink streaming job for sales analytics.
    """
    env = StreamExecutionEnvironment.get_execution_environment()
    kafka_consumer = FlinkKafkaConsumer(
        topics='sales_orders',
        deserialization_schema=lambda x: json.loads(x),
        properties={'bootstrap.servers': 'localhost:9092'}
    )

    sales_stream = env.add_source(kafka_consumer)

    # Parse, Aggregate, and Output
    aggregated_stream = sales_stream.key_by(lambda x: x['region']) \
                                  .sum('total_amount')

    aggregated_stream.print()

    env.execute("Sales Analytics Job")

if __name__ == '__main__':
    main()