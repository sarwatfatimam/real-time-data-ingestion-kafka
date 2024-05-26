import json
from kafka import KafkaProducer

# A Kafka client which publishes events to Kafka cluster
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

data = ['Installed kafka-python client', 'Read about the API', 'Created a new topic called kafka-python',
        'Experimenting with flush method', 'TODO: Are events buffered if flush is not called? If so, '
                                           'how to access? If not, understand the concept again.']
for event in data:
    # publishes a message to a topic
    producer.send('kafka-python', value=event)
    # immediately sends the buffered records
    producer.flush()
