#!/bin/bash

url=`./hs_sarjis.sh $1`
echo {\"name\": \"Fingerpori\",  \"url\": \"$url\"}
