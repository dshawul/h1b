# Calculates H1b statistics
This program calculates H1b statistics, namely, top 10 occupations and top 10 states 
for certified visa applications given an  input database in csv format.

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

