# Unit 3 | Assignment - Py Me Up, Charlie
# PyBank by Christopher Reutz

# Import the path and CSV reading modules and open the CSV file
import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Declare variables
totmonths = 0
totamount = 0
avgchange = 0
currentavg = 0
grtincrease = 0
grtincmonth = ""
grtdecrease = 0
grtdecmonth = ""
lastrowamt = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
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

    # End of main loop

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