#!/bin/bash
clear
read -pr "Enter Password to crack: " password

hash=$(echo -n "$password" | md5sum | awk '{print $1}')

echo "$hash" > hash.txt

john --format=raw-md5 hash.txt