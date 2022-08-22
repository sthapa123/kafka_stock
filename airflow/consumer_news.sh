#!/bin/bash
cd
cd /home/sthapa/kafka_stock/pipeline
python -c 'from warehouse import main_realtime_news; main_realtime_news()'
