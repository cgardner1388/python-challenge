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

# Module for reading CSV files
import csv

csvpath = os.path.join('election_data.csv')

with open('election_data.csv') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)



