#!/bin/bash

cd /home/ubuntu/SP25_DS5111_djz6nn
source env/bin/activate
make gainers SRC=yahoo
make gainers SRC=wsj
