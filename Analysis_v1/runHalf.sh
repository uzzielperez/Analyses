#!/bin/bash

echo "Hi, $USER!"
echo "Running first half of analysis..."
echo "Make sure all files have been configured." 

#read -p "Press enter to continue"
#read -n 1 -s -r -p "Press any key to continue"

echo "Merging relevant files....."
python merge.py

echo "Running Chainer and Make Class...."
python runChainClass.py


