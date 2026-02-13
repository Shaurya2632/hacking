#!/bin/bash
clear

runningMode="slow"

case $runningMode in
  none) echo "Running in none mode" ;;
  fast) echo "Running in fast mode" ;;
  slow) echo "Running in slow mode" ;;
  *) echo "Unknown running mode: $runningMode" ;;
esac