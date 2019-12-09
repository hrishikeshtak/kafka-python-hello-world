#!/usr/bin/python3

"""Kafka Producer."""

# pylint: disable=import-error
import confluent_kafka.admin
from kafka_admin import create_topic

from confluent_kafka import Producer


CONF = {'bootstrap.servers': 'localhost:9092'}
TOPIC = 'mytopic'
# Kafka Admin client: create, view, alter, delete topics and resources.
ADMIN = confluent_kafka.admin.AdminClient(CONF)


def acked(err, msg):
    """callback or on-delivery method to give ack."""
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value().decode('utf-8')))


def publish_data(topic):
    """Publish data to a kafka topic."""

    # create kafka topic
    create_topic(ADMIN, topic)

    producer = Producer(CONF)

    # try:
    #     for i in range(1, 10):
    #         producer.produce(topic, 'myvalue: {}'.format(i), callback=acked)
    #         # Polls the producer for events and calls the
    #         # corresponding callbacks
    #         producer.poll(0.5)
    # except KeyboardInterrupt:
    #     pass

    try:
        producer.produce(topic, 'Hello World!!!', callback=acked)
        # Polls the producer for events and calls the
        # corresponding callbacks
        producer.poll(0.5)
    except KeyboardInterrupt:
        pass

    # Wait for all messages in the Producer queue to be delivered.
    producer.flush(30)


def delete_topic():
    """Delete a kafka topic."""
    ADMIN.delete_topics([TOPIC])


def main():
    """Main function to call kafka Producer."""
    publish_data(TOPIC)
    # delete_topic()


if __name__ == '__main__':
    main()
