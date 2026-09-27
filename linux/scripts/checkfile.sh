#!/bin/bash

if [ -f "$1" ]; then
    echo "File $1 exists."
    ls -l "$1"
else
    echo "File $1 does not exist."
fi
