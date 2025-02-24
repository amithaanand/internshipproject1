#3. kafka part
import json
from kafka import KafkaProducer, KafkaConsumer
# Example weather data to send
output = {
    'id': 2643743,
    'city': 'London',
    'timeZone': 3600,
    'weatherDescription': 'few clouds',
    'minTemperature': 15.0,  # Float, no "°C"
    'maxTemperature': 17.0,  # Float, no "°C"
    'currentHumidity': 72,   # Integer, no "%"
    'windSpeed': 4.1         # Float, no "m/s"
}

# output = {
#     'id': 2643743,
#     'city': 'London',
#     'timeZone': 3600,
#     'weatherDescription': 'few clouds',
#     'minTemperature': '15.0°C',
#     'maxTemperature': '17.0°C',
#     'currentHumidity': '72%',
#     'windSpeed': '4.1m/s'
# }

#function to send weather data to kafka
def send_to_kafka(topic, message, kafka_broker='localhost:9092'):
    producer = KafkaProducer(
        bootstrap_servers=kafka_broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(topic, message)
    producer.flush()
    producer.close()
    # print(f"Weather data sent to Kafka topic '{topic}'")

#function to consume data from kafka
def consume_from_kafka(topic, kafka_broker='localhost:9092'):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=kafka_broker,
        auto_offset_reset='latest',  # Only read new messages
        enable_auto_commit=True,
        group_id='weather_group',
        value_deserializer=lambda x: safe_json_deserialize(x)
    )
    # Poll for messages and process them
    for message in consumer:
        if message.value is None:
            print("Empty or invalid message skipped.")
            continue
        # weather_data = message.value
        process_weather_data(message.value)
        # Break after processing one message for demonstration purposes
        break

# Safe JSON deserialization that handles empty or invalid messages
def safe_json_deserialize(x):
    try:
        if x and x.strip():  # Ensure the message is not empty or just whitespace
            return json.loads(x.decode('utf-8'))
        else:
            return None
    except json.JSONDecodeError:
        print("Error decoding message, invalid JSON")
        return None

# Function to process the weather data
def process_weather_data(data):
    print(f"Received weather data: {data}")

if __name__ == "__main__":
    kafka_topic = "weather_data"
    kafka_broker = "localhost:9092"

    # Send the pre-fetched weather data to Kafka
    send_to_kafka(kafka_topic, output, kafka_broker)

    # Consume data from Kafka
    consume_from_kafka(kafka_topic, kafka_broker)

