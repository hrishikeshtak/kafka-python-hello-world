#!/usr/bin/python3

"""Kafka Admin client: create, view, alter, delete topics and resources."""

# pylint: disable=import-error
import confluent_kafka
import confluent_kafka.admin


def create_topic(admin,
                 topic,
                 num_partitions=1,
                 replication_factor=1,
                 timeout=10):
    """
    Create new topic if it does not exist.

    :param admin: (confluent_kafka.admin.AdminClient) admin client object
    :param toipc: (str) topic name
    :param num_partitions: (int) number of topic partitions
    :param replication_factor: (int) replication factor for topic
    :param tmeout: (int) timeout in seconds for Kafka admin requests
    """
    if topic in admin.list_topics(timeout=timeout).topics:
        print('Kafka topic already exists: {0}'.format(topic))
        return

    # create_topics is asycnhronous method, a dict of <topic,future> is
    # returned.
    topics = [confluent_kafka.admin.NewTopic(
        topic,
        num_partitions,
        replication_factor)]
    topic_futures = admin.create_topics(topics)

    # await operation to finish by calling result() on future - will
    # raise exception if error
    try:
        topic_futures[topic].result()
    except confluent_kafka.KafkaException as error:
        if error.args[0].code() != confluent_kafka.KafkaError.TOPIC_ALREADY_EXISTS:
            raise error

        # in this case the topic was created between the list_topics
        # check above and the create_topics command
        print('Kafka topic already exists: {0}'.format(topic))
    else:
        print('Kafka topic created: {0}'.format(topic))
