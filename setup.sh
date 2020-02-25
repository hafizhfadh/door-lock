#!/bin/bash

sudo apt-get update && sudo apt-get upgrade

sudo apt-get install build-essential python3 python3-pip python3-dev

pip3 install request

pip3 install RPi.GPIO