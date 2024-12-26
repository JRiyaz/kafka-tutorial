from kafka import KafkaConsumer

consumer = KafkaConsumer('my_topic',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         value_deserializer=lambda x: x.decode('utf-8'))

for message in consumer:
    data = message.value.decode("utf-8")
    print("Received data: ", data)