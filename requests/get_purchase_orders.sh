#!/bin/bash

HOST='IP'
PORT=5000
PATH='purchase_orders'

/usr/bin/curl -s "http://$HOST:$PORT/$PATH" | /usr/bin/jq