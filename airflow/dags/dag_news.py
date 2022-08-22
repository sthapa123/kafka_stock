#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:50:32 2019

@author: yanyanyu
"""

import datetime as dt
import os

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization

default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2022, 8, 18, 21, 00, 00),
    'concurrency': 1,
    'retries': 0
}

with DAG('dag_news',
         default_args=default_args,
         schedule_interval='0 22 * * *',
         ) as dag:

    exec_dir = os.environ.get("AIRFLOW__CORE__DAGS_FOLDER")
    exec_dir = os.path.abspath(os.path.join(os.path.dirname(exec_dir), '..', 'airflow'))
    exec_script = exec_dir + "/consumer_news.sh "

    if os.path.exists(exec_script.rstrip()):
        t1 = BashOperator(
            task_id='News',
            bash_command=exec_script,
            dag=dag
        )
    else:
        raise Exception("Cannot locate {}".format(exec_script))

t1
