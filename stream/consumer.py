from time import sleep

from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         value_deserializer=lambda x: x.decode('utf-8'))

consumer.subscribe(topics=['my-topic'])

print("Starting consumer")
while True:
    print(f"Polling the consumer {'=' * 40}")
    if msg := consumer.poll(1000):
        for key, value in msg.items():
            for k in value:
                print("Topic: {} | Partition: {} | Offset: {} | Timestamp: {} | Key: {} | Value: {}".format(
                    k.topic, k.partition, k.offset, k.timestamp, k.key, k.value
                ))
    else:
        print("No new message.")
        break
