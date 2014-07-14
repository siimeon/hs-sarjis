#!/bin/bash

wget $1 -q  --output-document=tmp.html  # Download page and store it into tmp file
grep webkuva/sarjis/ tmp.html > tmp.txt # Searching img tag line and stores it into tmp file
cat tmp.txt | awk -F'"' '{print $4}'    # Prints tmp file from grep and spilits line and picks fourth element
rm tmp.html                             # Removes tmp files
rm tmp.txt

