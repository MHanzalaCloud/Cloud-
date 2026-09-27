#!/bin/bash
echo "=========For Loop Examle==========="

for i in 1 2 3 4 5
do 
echo "Number:$i"
done

echo ""
echo "=====Loop Via Files======="
for files in *.sh
do 
echo "Found script $files"
done
