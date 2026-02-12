#!/bin/bash
clear

age="$1"
skill="$2"

if [ "$age" -ge 18 ] && [ "$skill" = "true" ]; then
    echo "You got licence"

elif [ "$age" -ge 18 ]; then
    echo "You got skill"

else 
    echo "Be 18 years old"

fi    
