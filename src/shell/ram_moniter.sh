#!/bin/bash

clear
freeRam=$(free -mt | grep "Total" | awk '{print $4}')
threshold=500

if [ "$freeRam" -lt $threshold ]; then
    echo "Warning, RAM is running low, free RAM is $freeRam MB"
else
    echo "free RAM is $freeRam MB"
fi

timeout 500 bash ram_moniter.sh