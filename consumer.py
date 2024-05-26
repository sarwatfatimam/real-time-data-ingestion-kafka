from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('kafka-python',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='my_group')

for message in consumer:
    data = json.loads(message.value)
    print(f'Received: {data}')
