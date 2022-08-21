#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:12:08 2019

@author: yanyanyu
"""

config = {'api_key': "V6O1POPHS5IIFR1D",
          'api_key2': "V6O1POPHS5IIFR1D",
          'secret': 'sk_856da84974a34eeb833fd6ea4b1bb419',
          'symbol': 'AAPL',
          'kafka_broker': "10.0.0.3:9092",
          # to transmit min data
          'topic_name1': 'stock_streaming1',
          # to transmit second data
          'topic_name2': "stock_streaming2",
          # to transmit news data
          'topic_name3': 'news',
          'key_space': 'stocks'}

path = '/home/sthapa/kafka_stock/pipeline/'
# path = './'
timeZone = 'US/Eastern'
