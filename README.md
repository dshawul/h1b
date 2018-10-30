# Table of Contents
1. [Problem](#problem)
2. [Approach](#approach)
3. [Usage](#usage)

## Problem
A newspaper editor wants to research immigration data trends on H1B but couldn't
find existing statistics for historical data. Lets help her out with with python
scripts that will allow her to calculate the top 10 occupations and states for
certified visa applications for any year data is available.

## Approach
We want to avoid reading the whole file to memory because this is not scalable

1. Read header of the CSV format dataset and find indices to work state, occupation
and case status

2. We compute statistics (keep counts) on the fly without storing the data.
A dictionary of (k,v) pairs is kept for occupation and states. Since the number
of states (50) and types of jobs are small, the algorithms used here does not have to
be ultra efficient.

3. We then sort the dictionaries alphabetically by the key k. Since python sorts
are stable, a second sort by value v will not change orders between ties.
The reason why we can't sort once by two keys here is that the second sort is in 
ascending order. Lambda functions and comparators could be used for other sort criteria.

4. Store the results in semicolon delimitted CSV file for further processing.

## Usage
This script drives the core functionality provided by src/h1b_counting.py
All command line arguments are passed down to the python program
The usage is:

	$ ./run.sh -h
	usage: h1b_counting.py [-h] --input INPUT --occup OCCUP --state STATE
	                       [--delim DELIM] [--occup-header OCCUP_HEADER]
	                       [--status-header STATUS_HEADER]
	                       [--state-header STATE_HEADER]

	Calculates H1B statistics

	optional arguments:
	  -h, --help            show this help message and exit
	  --input INPUT, -i INPUT
	                        Path to input file with H1B data.
	  --occup OCCUP, -o OCCUP
	                        Path to file for storing top 10 occupations.
	  --state STATE, -s STATE
	                        Path to file for storing top 10 states.
	  --delim DELIM, -d DELIM
	                        Delimiter for the CSV input file.
	  --occup-header OCCUP_HEADER
	                        The column name for the occupation type.
	  --status-header STATUS_HEADER
	                        The column name for the case status.
	  --state-header STATE_HEADER
	                        The column name for the state where the employee will
	                        work.
