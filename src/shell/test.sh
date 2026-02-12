#!/bin/bash
clear

name="$1"

if [ "$name" ]; then
   echo "Your name is $name"

elif [ -n "$name" ]; then
   echo "Name can't be empty"

else 
   echo "Name not provided"

fi
