#!/usr/bin/env bash

# Start the app server
if [ $# -lt 3 ]; then
    printf "Usage: %s <function> <host> <port>\n" $0
    exit 1
fi
dev() {
    printf "Starting the app server on host: %s and port: %s\n" $1 $2
    export FLASK_APP=$(dirname $0)/app.py
    flask run --host=$1 --port=$2
}
debug() {
    printf "Starting the app server on host: %s and port: %s\n" $1 $2
    export FLASK_APP=$(dirname $0)/app.py
    export FLASK_DEBUG=1
    flask run --host=$1 --port=$2
}
"$1" "$2" "$3"
