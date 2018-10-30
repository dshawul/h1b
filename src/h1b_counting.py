import argparse
import csv

def compute_stats(args):
    """
    Compute H1b statistics (top occupations and states) and save results in files
    """
    DELIM = args.delim
    with open(args.input) as csv_file:
	    # Read the header of the csv file and then find
	    # column indices to occupation, state and case status.
	    csv_reader = csv.reader(csv_file, delimiter=DELIM)
	    header = next(csv_reader)
	    try:
		    occup_index = header.index(args.occup_header)
		    state_index = header.index(args.state_header)
		    status_index = header.index(args.status_header)
	    except:
			print "Atleast one of CSV header names do not match!"
			print "See usage on how to pass header names."
			print "     python src/h1b_counting.py --help"
			return
	    
	    # Compute statistics: A record has to have certified status to be considered.
	    # We store counts in a dictionary (k,v) where the key is the name of state/occup
	    occup_count = {}
	    state_count = {}
	    occup_sum = 0.
	    state_sum = 0.
	    for row in csv_reader:
	    	if row[status_index] == "CERTIFIED":
		    	if row[occup_index] in occup_count:
		    		occup_count[row[occup_index]] = occup_count[row[occup_index]] + 1
		    	else:
		    		occup_count[row[occup_index]] = 1

		    	if row[state_index] in state_count:
		    		state_count[row[state_index]] = state_count[row[state_index]] + 1
		    	else:
		    		state_count[row[state_index]] = 1
		    	occup_sum = occup_sum + 1
		    	state_sum = state_sum + 1
	    
		# Sort results: first alphabetically and then by counts.
		# Python sorts are stable
	    occup_count = sorted(occup_count.items(), key=lambda x: (x[0]), reverse=False)
	    occup_count = sorted(occup_count, key=lambda x: (x[1]), reverse=True)
	    state_count = sorted(state_count.items(), key=lambda x: (x[0]), reverse=False)
	    state_count = sorted(state_count, key=lambda x: (x[1]), reverse=True)

	    # write top occupations
	    with open(args.occup,'w') as ofile:
		    ofile.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
		    for i in range(10):
		    	if i < len(occup_count):
		    		ofile.write(occup_count[i][0] + DELIM + 
		    			        "{}".format(occup_count[i][1]) + DELIM + 
		    			        "{:2.1%}".format(occup_count[i][1] / occup_sum) + "\n" )

	    # write top states
	    with open(args.state,'w') as ofile:
		    ofile.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
		    for i in range(10):
		    	if i < len(state_count):
		    		ofile.write(state_count[i][0] + DELIM + 
		    			        "{}".format(state_count[i][1]) + DELIM + 
		    			        "{:2.1%}".format(state_count[i][1] / state_sum) + "\n" )

def main():
    """
    Driver routines for computing requested stats
    """
    parser = argparse.ArgumentParser(description="Calculates H1B statistics")
    parser.add_argument('--input','-i', dest='input', required=True, 
    	help='Path to input file with H1B data.')
    parser.add_argument('--occup','-o', dest='occup', required=True, 
    	help='Path to file for storing top 10 occupations.')
    parser.add_argument('--state','-s', dest='state', required=True, 
    	help='Path to file for storing top 10 states.')
    parser.add_argument('--delim','-d', dest='delim', required=False, default=";",
    	help='Delimiter for the CSV input file.')
    parser.add_argument('--occup-header', dest='occup_header', required=False, default="SOC_NAME",
    	help='The column name for the occupation type.')
    parser.add_argument('--status-header', dest='status_header', required=False, default="CASE_STATUS",
    	help='The column name for the case status.')
    parser.add_argument('--state-header', dest='state_header', required=False, default="WORKSITE_STATE",
    	help='The column name for the state where the employee will work.')
    args = parser.parse_args()

    # Compute statistic on a CSV file using ";"" as delimeter
    compute_stats(args)

if __name__ == "__main__":
    main()
