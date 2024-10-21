import json
import time
from kafka import KafkaProducer
from typing import Dict

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_sales_data() -> None:
    """
    Generate synthetic sales data and send to Kafka topic `sales_orders`.
    """
    while True:
        order: Dict[str, float] = {
            'order_id': time.time(),
            'region': 'North America',
            'total_amount': 100.0
        }
        producer.send('sales_orders', order)
        time.sleep(1)

if __name__ == '__main__':
    generate_sales_data()