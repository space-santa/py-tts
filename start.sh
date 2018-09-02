#!/bin/bash
DIR=`dirname "$(readlink -f "$0")"`
echo $DIR
source $DIR/env/bin/activate
python $DIR/src/main.py
