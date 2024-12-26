from json import dumps
from time import sleep

from kafka import KafkaProducer
from kafka.admin import NewTopic, KafkaAdminClient

bootstrap_servers = ['localhost:9092']
topic_name = "my-new-topic"


def serializer(x):
    return dumps(x).encode('utf-8')


producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=serializer)
topic = NewTopic(name=topic_name, num_partitions=1, replication_factor=1)
client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
client.create_topics([topic])
# client.delete_topics(['my_topic', 'my-new-topic', 'my-second-topic'])
for n in range(20):
    # producer.send('my-topic', value=dumps(data).encode('utf-8'))
    data = {"number": n}
    print(f"Sending data: {data}")
    producer.send(topic_name, value=data)
    sleep(0.5)
