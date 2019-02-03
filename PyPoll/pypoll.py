# Unit 3 | Assignment - Py Me Up, Charlie
# PyPoll by Christopher Reutz

# Import the path and CSV reading modules
import os
import csv

# Initialize lists
candidate_names = []
candidate_votes = []
candidate_pcts = []

# Open the CVS file that contains the data
csvinputpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvinputpath, newline='') as csvfile:
    csvline = csv.reader(csvfile, delimiter=',')
    
    # Skip first row which is the header row
    header = next(csvline)

    # Loop through file
    for castvote in csvline:
        
        # Check to see if the candidate is already in the candidate_names
        # If not, append the name, give candidate one vote 
        # and set the candidate vote percentage to 0
        if castvote[2] not in candidate_names:
            candidate_names.append(castvote[2])
            candidate_votes.append(1)
            candidate_pcts.append(0)
        
        # If the candidate already in the list, add a vote
        else:
            candidate_votes[candidate_names.index(castvote[2])] += 1
    
    # End of main loop through data
# End of reading in data

# Sum up the total votes cast
total_votes = sum(candidate_votes)

# Calculate percent of the vote for each candidate
for i in range(len(candidate_pcts)):
     candidate_pcts[i] = candidate_votes[i] / total_votes * 100

# Print results
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for j in range(len(candidate_names)):
    print(f"{candidate_names[j]}: {round(candidate_pcts[j], 3)}% ({candidate_votes[j]})")
print(f"-------------------------")
print(f"Winner: {candidate_names[candidate_votes.index(max(candidate_votes))]}")
print(f"-------------------------")
