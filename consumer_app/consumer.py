
import logging
import os
import json

from dotenv import load_dotenv
from kafka.consumer import KafkaConsumer

load_dotenv(verbose=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def main():
    print("Starting consumer", os.environ["KAFKA_BOOTSTRAP_SERVERS"])
    # Kafka consumer configuration
    kafka_bootstrap_servers = [os.environ["KAFKA_BOOTSTRAP_SERVERS"]]
    kafka_topic = "my-vehicles"
    consumer_group_id = "my-group"

    # Create Kafka consumer
    consumer = KafkaConsumer(
        kafka_topic,
        group_id=consumer_group_id,
        bootstrap_servers=kafka_bootstrap_servers,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
         value_deserializer=lambda x: x.decode('utf-8')
    )

    # Consume messages
    for message in consumer:
        try:
            kafka_message = f"""
            Message received: {message.value}
            Message key: {message.key}
            Message partition: {message.partition}
            Message offset: {message.offset}

            """
            logger.info(kafka_message)
        except Exception as e:
            logger.error(e)
if __name__ == "__main__":
    main()

