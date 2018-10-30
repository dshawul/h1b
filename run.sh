#!/bin/bash

#
#  Call the h1b stats python program
#  Note that we propage all arguments to the python program.
#   Do a "./run.sh --help" to see usage
#
python ./src/h1b_counting.py -i ./input/h1b_input.csv  -o ./output/top_10_occupations.txt -s ./output/top_10_states.txt "$@"

