#!/bin/sh

python3 src/hdf5_watcher.py $1 &
curl -C - $1 | tar xvz -C $2

