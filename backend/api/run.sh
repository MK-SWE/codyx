#!/usr/bin/env bash

# Start the app server
if [ $# -lt 3 ]; then
    printf "Usage: %s <function> <host> <port>\n" $0
    exit 1
fi

set_env_vars() {
    export FLASK_APP=$(dirname $(dirname $0))/api/app.py
    export PYTHONPATH=$(dirname $(dirname $0)):$PYTHONPATH
}

dev() {
    set_env_vars
    printf "Starting the app server on host: %s and port: %s\n" $1 $2
    export FLASK_ENV=development
    flask run --host=$1 --port=$2
}

debug() {
    set_env_vars
    printf "Starting the app server on host: %s and port: %s\n" $1 $2
    export FLASK_DEBUG=1
    flask run --host=$1 --port=$2
}

"$1" "$2" "$3"
