#!/bin/bash
# send a get request with custom data and display body
curl -s "$1" -X GET -H 'X-HolbertonSchool-User-Id: 98' 
