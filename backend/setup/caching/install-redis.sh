#!/usr/bin/env bash
# shellcheck disable=SC1090
# This script is used to build redis image for ubuntu system
set -e

# ANSI color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Downloading stable redis version
echo -e "${GREEN}Downloading redis stable version...${NC}"
redisurl="http://download.redis.io/redis-stable.tar.gz"
curl -s -o redis-stable.tar.gz $redisurl
echo -e "${RED}redis-stable.tar.gz${NC} ${GREEN}Downloaded successfully${NC}"

# Extracting the tar file
echo -e "${GREEN}Extracting the tar file...${NC}"
sudo mkdir -p /usr/local/lib/
sudo chmod a+w /usr/local/lib/
sudo tar -xzf redis-stable.tar.gz -C /usr/local/lib/
echo -e "${GREEN}Redis Extracted successfully${NC}"

# Building redis
echo -e "${GREEN}Building redis...${NC}"
cd /usr/local/lib/redis-stable || exit
sudo apt-get update
sudo apt-get install -y make
sudo make && sudo make install
echo -e "${GREEN}Redis built successfully${NC}"

# Cleaning up
echo -e "${GREEN}Cleaning up...${NC}"
sudo rm -rf /usr/local/lib/redis-stable
sudo rm -rf redis-stable.tar.gz
echo -e "${GREEN}Adding redis to the path...${NC}"
echo "export PATH=\$PATH:/usr/local/bin/" >> ~/.bashrc
source ~/.bashrc
echo -e "${GREEN}Redis installed successfully${NC}"

# Displaying installed versions
echo -e "${GREEN}The following directories are created:${NC} $(find /usr/local/bin -name 'redis*' -print | sort)"
echo -e "${GREEN}The redis version is:${NC} $(redis-server --version)"
echo -e "${GREEN}The redis-cli version is:${NC} $(redis-cli --version)"

# Edit config to listen on all local ports
echo -e "${GREEN}Editing the redis configuration file...${NC}"
sudo cp /etc/redis/redis.conf /etc/redis/redis.conf.default
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
echo "port              6379
daemonize         yes
save              60 1
bind              127.0.0.1
tcp-keepalive     300
dbfilename        dump.rdb
dir               ./
rdbcompression    yes
" > /etc/redis/6379.conf
echo -e "${GREEN}If you want to use a different configuration file,
you can edit /etc/redis/6379.conf or you can download the official script at:
https://download.redis.io/redis-stable/utils/install_server.sh${NC}"

# Start or restart redis-server based on the status
sudo service redis-server restart || sudo service redis-server start
echo -e "${GREEN}Redis server started successfully${NC}"
echo -e "${GREEN}To check the status of redis server, run:${NC} sudo service redis-server status"
echo -e "${GREEN}To stop the redis server, run:${NC} sudo service redis-server stop"
echo -e "${GREEN}The redis server is running on port 6379${NC}"
echo -e "${GREEN}Enjoy redis!${NC}"
