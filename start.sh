#!/bin/bash

# Démarrer le producteur en arrière-plan
python producer.py &

# Démarrer le consommateur
python consumer.py &

#demarer le sparkstreaming : 
python spark_streaming.py

# if [ ! -f "/opt/airflow/airflow.db" ]; then
#   airflow db init && \
#   airflow users create \
#     --username admin \
#     --firstname admin \
#     --lastname admin \
#     --role Admin \
#     --email admin@example.com \
#     --password admin
# fi

# # Mettre à jour la base de données d'Airflow
# airflow db upgrade

# # Démarrer le serveur web Airflow
# exec airflow webserver
