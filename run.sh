#!/bin/sh

python3 src/hdf5_watcher.py $1 & 
(curl -s -C - $2 | tar xvz -C $1)
