#!/bin/bash

URL='http://IP'
PORT=5000
PATH='purchase_orders'
LIMIT=10

for ((i=1; i<=$LIMIT; i++))
do
  PAYLOAD='{"id": '$i', "description": "Pedido de compra '$i'"}'
  /usr/bin/curl -s "$URL:$PORT/$PATH" -H "Content-Type: application/json" -H "Accept: */*" -d "$PAYLOAD" | /usr/bin/jq 2 > /dev/null
done