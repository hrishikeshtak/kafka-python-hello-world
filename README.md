# kafka-python-hello-world
Hello World In Kafka Using Python and Docker

#### Kafka and Zookeeper installation and Starting The Server using docker-compose.           
>> $ sudo docker-compose up -d

#### Creating Producer And Consumer
> Creating a producer and consumer can be a perfect Hello, World! example to learn Kafka but there are multiple ways through which we can achieve it. Some of them are listed below:

> 1. Command line client provided as default by Kafka
> 2. kafka-python
> 3. PyKafka
> 4. confluent-kafka

we will be making use of confluent-kafka to achieve a simple producer and consumer setup in Kafka using python.

#### Install confluent-kafka dependency
>> $ pip3 install -r requirements.txt

#### Kafka Consumer
Open a new terminal and run the Kafka consumer. Consumer will be in listening stage continuously.

>> $ python3 kafka_consumer.py

#### Kafka Producer
Open a new terminal and run the Kafka Producer, which produce "Hello World!".

>> $ python3 kafka_producer.py

You can now revisit the consumer shell to check if it has received the records sent from the producer through our Kafka setup.
