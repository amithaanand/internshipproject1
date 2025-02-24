# Internshipproject1
Project Title: ETL Pipeline with Kafka, Spark, S3, Snowflake Overview: This project implements an ETL (Extract, Transform, Load) pipeline that retrieves data from Open Weather API, processes and cleans the data using Python scripts, utilizes Kafka for real-time data data streaming, employs Apache Spark for data processing, and finally loads the processed data into AWS S3 and then send to an analytical warehouse Snowflake.

Components: Data Extraction: Python scripts fetch data from Open Weather API endpoint and request for an API Key.

Data Processing and Cleaning: Python scripts handle data transformation and cleaning tasks to prepare it for downstream processing.

Real-time Streaming with Kafka: Data is streamed in real-time using Apache Kafka, ensuring scalable and fault-tolerant data ingestion.

Data Processing with Apache Spark: Spark jobs are employed to perform complex data transformations, aggregations, and computations on the streaming data.

AWS S3: Processed data is stored persistently in S3 Bucket, providing a fully managed, cloud-based  solution.

Technologies Used: Python: For data extraction, transformation, and cleaning. Apache Kafka: For real-time data streaming and ingestion. Apache Spark: For distributed data processing and analysis. S3: For storing processed data in AWS.


1.The project is to collect some weather details from the open weather api 
<br>
2.Using API Key convert the details of weather of a particular location into a tabular form using Python
<br>
3.store it into Kafka and use Pyspark for streaming the required data
<br>
4.Use AWS S3 as cloud storage and Snowflake as analytical warehouse

![Screenshot from 2025-02-22 23-04-14](https://github.com/user-attachments/assets/599c512c-e6fb-4cca-91cd-ce2527c54412)
