 #Homework 2 PyPoll
 #The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
 
 #First we'll import the os module
# This will allow us to create file paths across operating systems
import os

#currentDirectory = os.getcwd()

print(currentDirectory)

# Module for reading CSV files
import csv

#csvpath = os.path.join('election_data.csv')

csvpath = '/Users/gardnerguzman/Desktop/Georgia Tech Bootcamp/Homework/python-challenge/PyPoll/Resources/election_data.csv'

votes = 0 

#Come up with formula to find candidate and move on
candidates =

#Come up with formula 

#csvpath = os.path.join('PyPoll','Resources','election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
#adding up the votes
    for Row in csvreader:
    #sum votes; make sure everything is sequential; can do everything in the same 4 loop
        votes = votes + 1
    
print(votes)

   






