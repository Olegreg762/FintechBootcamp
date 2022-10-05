#Imports library to read csv file
import csv

# Define Variables
month = []
profit = []
profit_change= []

# Open csv file budget_file.csv
with open('./budget_data.csv') as budget_file:
    # Create variable csvbudget from csvreader
    csvbudget = csv.reader(budget_file, delimiter=',')
    # Skip header labels
    header = next(csvbudget)
    # Iterate rows of csvbudget  
    for row in csvbudget: 
        # Append month and profit to list
        month.append(row[0])
        profit.append(int(row[1]))
        # Iterate profit for monthly change
    for i in range(len(profit)-1):
        # Difference between 2 months and append change
        profit_change.append(profit[i+1]-profit[i])
        
# Logic for determining greatest increase and decrease in profits
uprofit = max(profit_change)
dprofit = min(profit_change)

# Correlate increase and decrease in to corresponding month
incre_month = profit_change.index(max(profit_change)) + 1
decre_month = profit_change.index(min(profit_change)) + 1 


# Print Analysis
print('Financial Analysis' '\n'
'----------------------------''\n'
f'Total Months: {len(month)}''\n'
f'Total: ${sum(profit):,}''\n'
f'Average Change: ${round(sum(profit_change)/len(profit_change),2):,}''\n'
f'Greatest Increase in Profits: {month[incre_month]} : ${(int(uprofit)):,}''\n'
f'Greatest Decrease in Profits: {month[decre_month]} : ${(int(dprofit)):,}')

# Output Analysis file
with open('budget_analysis.txt', 'w') as budget_analysis:

    budget_analysis.write('Financial Analysis\n'
    '----------------------------\n'
    f'Total Months: {len(month)}\n'
    f'Total: ${sum(profit):,}\n'
    f'Average Change: ${round(sum(profit_change)/len(profit_change),2):,}\n'
    f'Greatest Increase in Profits: {month[incre_month]} : ${(int(uprofit)):,}\n'
    f'Greatest Decrease in Profits: {month[decre_month]} : ${(int(dprofit)):,}\n')


