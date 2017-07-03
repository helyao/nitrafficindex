#!/bin/bash

source /home/helyao/anaconda2/envs/py27/bin/activate py27

python --version

cd /home/helyao/github/nitrafficindex/TrafficScrapy

scrapy crawl traffic

echo 'Finish Traffic Spider\n'

# ./traffic.sh >> traffic.log 2>&1 &