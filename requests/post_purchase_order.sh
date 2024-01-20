#!/bin/bash

HOST='IP'
PORT=5000
PATH='purchase_orders'
PAYLOAD=$1

/usr/bin/curl -s -X POST "http://$HOST:$PORT/$PATH" -H "Content-Type: application/json" -H "Accept: */*" -d "@$PAYLOAD" | /usr/bin/jq 2> /dev/null