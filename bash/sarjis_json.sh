#!/bin/bash

# Arguments:
# $1 - Name of comic
# $2 - Url to comic

url=`./hs_sarjis.sh $2`
echo {\"name\": \"$1\",  \"url\": \"$url\"}
