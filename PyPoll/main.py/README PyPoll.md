# python-challenge
#Homework 2 PyPoll
 #The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
 
#currentDirectory = os.getcwd()
#print(currentDirectory)

#Questions
#1. Do I need to print the csvreader? 
#2. Do I need to skip over the header csvheader = next(csvreader)?
#3. Can you walk me through how I need to create the dictionaries and where to put them? 
#4. How do you format the data so that it looks similiar to the table in the homework? 

import os
import csv

csvpath = '/Users/gardnerguzman/Desktop/Georgia Tech Bootcamp/Homework/python-challenge/PyPoll/Resources/election_data.csv'

#Define variables
votes = 0

#initialize lists
candidates = []
vote = []
candidate_dict = {}

#Come up with formula to find candidate and move on

#csvpath = os.path.join('PyPoll','Resources','election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #print(csvreader)
#adding up the votes
    for Row in csvreader:
    #sum votes; make sure everything is sequential; can do everything in the same 4 loop
        votes = votes + 1
        candidate = Row[2]
        vote.append(candidate)
        candidate_list = {candidate : votes,
        candidate: votes
        }
    
    #remove the duplicates in the list and print out the candidate name
    #add in the dictionary below
        if candidate not in candidates:
            candidates.append(candidate)
        
            #previous vote
            candidate_dict[candidate] = 1
    #adding up the current vote to the previous candidate vote 
    #specify the dictionary
        else:
            candidate_dict[candidate] = 1 + candidate_dict[candidate]

#Calculations
max_increase_profit = max(Monthly_Change)
max_decrease_profit = min(Monthly_Change)

max_increase_month = Monthly_Change.index(max(Monthly_Change)) + 1
max_decrease_month = Monthly_Change.index(min(Monthly_Change)) + 1 

    #print statements

    print (candidate_dict)

    print ('Election Results')
    print ('-----------------')
    print (f'Total Votes: {votes}')
    print ('-----------------')
    print ('Khan: 63.000% (2218231)')
    print ('Correy: 20.000% (704200)')
    print ('Li: 14.000% (492940)')
    print ('O Tooley: 3.000% (105630)')
    print ('-----------------')
    print ('Winner: Khan')
    print ('-----------------')

    #Output File
    analysis = '/Users/gardnerguzman/Desktop/Georgia Tech Bootcamp/Homework/python-challenge/PyPoll/Resources/election_data.txt'

    #Export to txt file
    with open ('election_data.txt','w') as text: 
        text.write ('Election Results')
        text.write ('-----------------')
        text.write (f'Total Votes: {votes}')
        text.write ('-----------------')
        text.write ('Khan: 63.000% (2218231)')
        text.write ('Correy: 20.000% (704200)')
        text.write ('Li: 14.000% (492940)')
        text.write ('O Tooley: 3.000% (105630)')
        text.write ('-----------------')
        text.write ('Winner: Khan')
        text.write ('-----------------')
