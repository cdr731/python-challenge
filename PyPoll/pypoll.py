# Unit 3 | Assignment - Py Me Up, Charlie
# PyPoll by Christopher Reutz

# Import the path and CSV reading modules
import os
import csv

# Open the CVS file that contains the data
csvinputpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvinputpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip first row which is the header row
    header = next(csvreader)

    # Initial variables and lists
    candidate_names = []
    candidate_votes = []

    for vote in csvreader:

        if vote[2] not in candidate_names:
            candidate_names.append(vote[2])
            candidate_votes.append(1)
    
    print(candidate_names)
    print(candidate_votes)