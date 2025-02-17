# Unit 3 | Assignment - Py Me Up, Charlie
# PyBank by Christopher Reutz

# Import the path and CSV reading modules
import os
import csv

# Initialize variables
totmonths = 0
totamount = 0
avgchange = 0
grtincrease = 0
grtdecrease = 0 

# Open the CVS file that contains the data
csvinputpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvinputpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip first row which is the header row
    header = next(csvreader)

    # Loop through file
    for row in csvreader:
        
        # Set the previous row amount to the current row 
        # for the first row since there is no prior period
        if totmonths == 0:
            lastrowamt = int(row[1])

        # Increment the total months
        totmonths += 1

        # Increase the net total amount of profit/losses
        totamount += int(row[1])
        
        # Calculate the average change in profit/losses
        currentavg = int(row[1]) - lastrowamt
        
        # Running total of the average change
        avgchange += currentavg      

        # Check to see if there is a new greatest profit
        if (currentavg > grtincrease):
            grtincrease = currentavg
            grtincmonth = row[0]
        
        # Check to see if there is a new greatest loss
        if (currentavg < grtdecrease):
            grtdecrease = currentavg
            grtdecmonth = row[0]

        # Set the current profit/loss to be the prior profit/loss
        # for the next row
        lastrowamt = int(row[1])

    # End of main loop through data
# End of reading in data

# Calculate the average of he changes over the entire period
# Note that it is the total months less 1
avgchange /= (totmonths - 1)

# Print results
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {totmonths}")
print(f"Total: ${totamount}")
print(f"Average Change: ${round(avgchange, 2)}")
print(f"Greatest Increase in Profits: {grtincmonth} (${grtincrease})")
print(f"Greatest Decrease in Profits: {grtdecmonth} (${grtdecrease})")

# Open a file to output results to
csvoutputpath = os.path.join('..', 'Resources', 'budget_results.csv')

with open(csvoutputpath, "w", newline='') as datafile:
    writer = csv.writer(datafile, delimiter=',')

    # Write the header row
    writer.writerow(["Total Months", "Total Amount", "Average Change",
                    "Greatest Increase Date", "Greatest Increase Amount",
                    "Greatest Decrease Date", "Greatest Decrease Amount"])

    # Write the results
    writer.writerow([totmonths, totamount, round(avgchange,2),
                    grtincmonth, grtincrease,
                    grtdecmonth, grtdecrease])
