#4.pyspark part
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
import json
from kafka import KafkaProducer

# Define the schema for weather data
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("city", StringType(), True),
    StructField("timeZone", IntegerType(), True),
    StructField("weatherDescription", StringType(), True),
    StructField("minTemperature", DoubleType(), True),
    StructField("maxTemperature", DoubleType(), True),
    StructField("currentHumidity", IntegerType(), True),
    StructField("windSpeed", DoubleType(), True)
])

# Function to send weather data to Kafka
def send_to_kafka(topic, message, kafka_broker='localhost:9092'):
    producer = KafkaProducer(
        bootstrap_servers=kafka_broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(topic, message)
    producer.flush()
    producer.close()

if __name__ == "__main__":
    # Kafka topic and broker
    kafka_topic = "weather_data"
    kafka_broker = "localhost:9092"

    # Weather data example
    output = {
        'id': 2643743,
        'city': 'London',
        'timeZone': 3600,
        'weatherDescription': 'few clouds',
        'minTemperature': 8.61,
        'maxTemperature': 10.05,
        'currentHumidity': 70,
        'windSpeed': 4.63
    }

    send_to_kafka(kafka_topic, output, kafka_broker)
    print("Data sent to Kafka:", output)

    # Start a Spark session
    spark = SparkSession.builder \
        .appName("ETL Pipeline") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.4") \
        .getOrCreate()

    # Read from Kafka topic
    kafka_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "weather_data") \
        .option("startingOffsets", "earliest") \
        .load()

    # Deserialize Kafka messages and filter valid rows
    parsed_df = kafka_df.selectExpr("CAST(value AS STRING)") \
        .select(from_json(col("value"), schema).alias("data")) \
        .select("data.*") \
        .filter(
            col("minTemperature").isNotNull() &
            col("maxTemperature").isNotNull() &
            col("currentHumidity").isNotNull() &
            col("windSpeed").isNotNull()
        )

    query = parsed_df.writeStream \
        .format("json") \
        .option("path", "/home/amitha/PycharmProjects/bigdataproject/output") \
        .option("checkpointLocation", "/home/amitha/PycharmProjects/bigdataproject/output") \
        .option("maxRecordsPerFile", 1) \
        .start()

    query.awaitTermination()
