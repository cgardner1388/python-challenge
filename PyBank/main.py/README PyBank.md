# python-challenge
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#currentDirectory = os.getcwd()
#print(currentDirectory)
 
# Read the CSV File
import os
import csv

csvpath = '/Users/gardnerguzman/Desktop/Georgia Tech Bootcamp/Homework/python-challenge/PyBank/Resources/budget_data.csv'

#Define variables
Profits_Loss = []
Date = [] 
Monthly_Change = []
Total_Profit = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents; splits the data between commas
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    header = next(csvreader)
    
    for Row in csvreader:
        #Add profit losses and dates to their lists
        Date.append(Row[0])
        Profits_Loss.append(Row[1])
        #calculate total profit
    Total_Profit =  Total_Profit + Row

#calculate montlhy profit changes and iterate through the data
    for x in range(1, len(Profits_Loss)):
        Monthly_Change.append(int(Profits_Loss[x]) - int(Profits_Loss[x-1]))

#Calculations 
max_increase_profit = max(Monthly_Change)
max_decrease_profit = min(Monthly_Change)

max_increase_month = Monthly_Change.index(max(Monthly_Change)) + 1
max_decrease_month = Monthly_Change.index(min(Monthly_Change)) + 1 

#Print Statements
print ('Financial Analysis')
print ('-------------------')
print (f'Total Months: {len(Date)}')
print (f'Total: ${Total_Profit}')
print (f'Average Change: {round(sum(Monthly_Change) / len(Monthly_Change), 2)}')
print (f'Greatest Increase in Profits: {Date[max_increase_month]} (${(str(max_increase_profit))})')
print (f'Greatest Increase in Profits: {Date[max_decrease_month]} (${(str(max_decrease_profit))})')

#Output File
analysis = os.path.join

#Export to Text File
with open ('financial_analysis_data.txt','w') as text: 
    text.write ('Financial Analysis')
    text.write ('-------------------')
    text.write (f'Total Months: {len(Date)}')
    text.write (f'Total: ${Total_Profit}')
    text.write (f'Average Change: {round(sum(Monthly_Change) / len(Monthly_Change), 2)}')
    text.write (f'Greatest Increase in Profits: {Date[max_increase_month]} (${(str(max_increase_profit))})')
    text.write (f'Greatest Increase in Profits: {Date[max_decrease_month]} (${(str(max_decrease_profit))})') 
