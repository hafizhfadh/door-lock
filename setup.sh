#!/bin/bash

sudo apt-get update -y && sudo apt-get upgrade -y

sudo apt-get install -y build-essential python3 python3-pip python3-dev

pip3 install request

pip3 install RPi.GPIO