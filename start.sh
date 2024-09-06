#!/bin/sh

# Install cmake
pip3 install cmake==3.29.3

# Install wheel
pip3 install wheel==0.43.0

# Wait for 5 seconds
sleep 5

# Install dlib
pip3 install dlib==19.24.6

pip3 install opencv-python-headless