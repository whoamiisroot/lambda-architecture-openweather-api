from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

# DAG default arguments
default_args = {
    'owner': 'bouchra',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    'weather_data_pipeline',
    default_args=default_args,
    description='Automates weather data pipeline with Kafka, Spark, and Cassandra',
    schedule_interval='@daily',
    start_date=datetime(2024, 6, 10),
    catchup=False,
) as dag:

    # Task 1: Start Kafka Producer
    start_kafka_producer = BashOperator(
        task_id='start_kafka_producer',
        bash_command='docker exec spark-streaming python3 /app/producer.py',
    )

    # Task 2: Trigger Spark Streaming Job
    run_spark_streaming = BashOperator(
        task_id='run_spark_streaming',
        bash_command='docker exec spark-streaming python3 /app/spark_streaming.py',
    )

    # Task 3: Check Parquet File Output
    check_parquet_output = BashOperator(
        task_id='check_parquet_output',
        bash_command='ls -lh ./data/parquet/weather_data.parquet',
    )

    # Task 4: Verify Cassandra Data
    def check_cassandra():
        from cassandra.cluster import Cluster
        cluster = Cluster(['cassandra'])
        session = cluster.connect('weather')
        rows = session.execute('SELECT COUNT(*) FROM weather_data_history')
        for row in rows:
            print(f"Records in Cassandra: {row.count}")

    verify_cassandra_data = PythonOperator(
        task_id='verify_cassandra_data',
        python_callable=check_cassandra,
    )

    # # Task 5: Stop Kafka Producer (if necessary)
    # stop_kafka_producer = BashOperator(
    #     task_id='stop_kafka_producer',
    #     bash_command='echo "Kafka Producer execution completed!"',
    # )

    # Define task dependencies
    start_kafka_producer >> run_spark_streaming >> check_parquet_output
    check_parquet_output >> verify_cassandra_data
