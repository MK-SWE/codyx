#!/bin/sh
# Ensure the script uses Unix line endings (LF)

# Update apk and install packages
apk update

# install python packages
apk add python3
apk add py3-pip
apk add py3-pycodestyle

# install nodejs and npm
apk add nodejs 
apk add npm
npm install -g semistandard
