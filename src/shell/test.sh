#!/bin/bash
clear

file="test.sh"

res=$(echo -f "$file" 2>&1)  

echo "$res" 
