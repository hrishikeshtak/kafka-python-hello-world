#!/usr/bin/python3

""" Kafka consumer."""

# pylint: disable=import-error
from confluent_kafka import Consumer, KafkaError

SETTINGS = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}
TOPIC = 'mytopic'


def consume():
    """
    Kafka Consumer implementation.
    subscribe to topic and consume messages.
    """
    consumer = Consumer(SETTINGS)
    consumer.subscribe([TOPIC])

    try:
        while True:
            msg = consumer.poll(0.1)
            # pylint: disable=no-else-continue
            if msg is None:
                continue
            elif not msg.error():
                print('Received message: {0}'.format(
                    msg.value().decode('utf-8')))
            elif msg.error().code() == KafkaError._PARTITION_EOF:
                print('End of partition reached {0}/{1}'
                      .format(msg.topic(), msg.partition()))
            else:
                print('Error occured: {0}'.format(msg.error().str()))

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


def main():
    """main function to call consumer."""
    consume()


if __name__ == '__main__':
    main()
