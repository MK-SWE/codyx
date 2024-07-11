#!/bin/sh

# Update the package list
apk update

# Install required packages
# Install Python3 and pip
apk add python3
apk add py3-pip
apk add py3-pycodestyle

# Install Node.js and npm
apk add nodejs
apk add npm
npm install -g semistandard
