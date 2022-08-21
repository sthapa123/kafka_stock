#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:50:32 2019

@author: yanyanyu
"""

import datetime as dt

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

with DAG('dag_aftertradingday',
         default_args=default_args,
         schedule_interval='0 22 * * *',
         ) as dag:

    first = BashOperator(task_id='AfterTrading',
                    bash_command='../consumer_aftertrading.sh')

first
