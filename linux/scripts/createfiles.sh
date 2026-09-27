#!/bin/bash

for i in {1..5}
do 
touch file_$i.txt
echo "Creating File_$i.txt "
done

echo "All files created ..."
ls file_*.txt
