#!/bin/bash
cd
cd /home/sthapa/kafka_stock/pipeline
python -c 'from warehouse import main_aftertradingday; main_aftertradingday()'
