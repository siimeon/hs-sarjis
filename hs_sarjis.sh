#!/bin/bash

wget $1 -q  --output-document=tmp.html
grep webkuva/sarjis/ tmp.html > tmp.txt
cat tmp.txt | awk -F'"' '{print $4}'
rm tmp.html
rm tmp.txt

