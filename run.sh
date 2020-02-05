#!/bin/sh

python3 src/hdf5_watcher.py "$2" &
curl -C - "$1" | tar xvz -C "$2"

