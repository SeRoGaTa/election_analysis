# Election Analysis

***Version 1.0.0***

---

## Overview of Project
#### A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources

- Data source: election_results.cvs
- Software: Python 3.8.8 Visual Studio Code, 1.60.2

## Summary
#### The analysis of the election show that:

- There were 369,711 votes cast in the election.
- The candidates were:
  -  Charles Casper Stockham
  -  Diana DeGette
  -  Raymon Anthony Doane
-  The candidate results were
   -  Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
   -  Diana DeGette received 73.8% of the vote and 272,892 number of votes.
   -  Raymon Anthony Doane received 3.1% of te vote and 11,606 number of votes.
-  The winer of the election was:
    -  Candidate Diana DeGette, who received 73.8% of the votes and 272,892 number of votes.

## Challenge overview

### Overview of Election Audit
#### This analysis reflects what we could get out of the Election Results csv file which contains the Country and Candidate for all Ballot IDs, with this data I was able to get insights as which candidate won the election, which county has the more turnout and the specific date as % of the poll and the amount of votes each county and candidate had.

### Election Audit Results
#### In the file "election_analysis.txt" located here [election_analysis](https://github.com/SeRoGaTa/election_analysis/blob/main/Analysis/election_analysis.txt) you will find the output of my analysis python script. 

Here is an image of it.

<img src="https://github.com/SeRoGaTa/election_analysis/blob/main/Resources/output.png" width="400">

## Challenge summary

### Election Audit Summary
#### This script was structure to be able to replicate in future runs or elections, it will help you to analyze the data in a quick way and will be adjusted to every amount of data if it remains in the same structure (structure means same columns names and positions) but with different number of rows. 

#### Using this script, we might need to adjust some part of the scripts to fit your new dataset. Here I list the parts that might need a change and how we can interpret them:
- Location of the file to open with the dataset
  - At the line 9 you see the path of where the file with the dataset in raw is located and the name of it (starting from the current directory "use PWD to see where the currently directory is pointing to"). You must add in quotes separated by commas all the folders where the file is inside to. You could see the example in the following image.
  - <img src="https://github.com/SeRoGaTa/election_analysis/blob/main/Resources/Locations.png" width="800">
- Location of the file to save the output
  - At the line 11 you see the path of where the file with the output results will be located and the name of it (starting from the current directory "use PWD to see where the currently directory is pointing to"). You must add in quotes separated by commas all the folders where the file is inside to. You could see the example in the following image.
  - <img src="https://github.com/SeRoGaTa/election_analysis/blob/main/Resources/Locations.png" width="800">
- Number of columns to use
  - At the line 48 and 51 of the code, you will find numbers inside of square brackets, these numbers represent a column index (starting from 0) that will grab from the file. In this particular case, we have the candidate’s name in the column 2 and the county name in column 1 (again starting from 0), so if this arrangement change in the new data set, you will still be able to execute it if you choose the right column from the data set for each field. You could see the example in the following image.
  - <img src="https://github.com/SeRoGaTa/election_analysis/blob/main/Resources/Columns.png" width="500"> 


#### You can locate the complete analysis python script on the following link [PyPoll_Challenge](https://github.com/SeRoGaTa/election_analysis/blob/main/PyPoll_Challenge.py) and all image used in the following folder [Resources](https://github.com/SeRoGaTa/election_analysis/tree/main/Resources)
