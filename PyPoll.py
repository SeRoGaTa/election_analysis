# Import 
import csv
import os

# Here we asign the path to a variable to read the file.
file_to_open = os.path.join("Week 3","Asynchronous Online Lessons","Resources","election_results.csv")

# Here we asign the path to a variable to write the file.
file_to_save = os.path.join("Week 3","Asynchronous Online Lessons","Analysis","election_analysis.csv")

# Here I initialize to 0 the total votes variable
total_votes = 0

# Here I create an empty list of candidates option
candidate_option = []

# Here I create an empty list of candidates option
candidate_votes ={}

# Here I create some variables to define the winning candidate and set them up to 0
winning_candidate = (str)
winning_count = 0
winning_percentage = 0

# This code will open the file
with open(file_to_open) as election_data:
    file_reader=csv.reader(election_data)
    
    # This code will skip the header line.
    headers = next(file_reader)

    # This code will print each line of the file
    for row in file_reader:
       
        # In this line we add 1 to the same variable for each line of the file
        total_votes += 1
        
        # In this line I grab the candidate name
        candidate_name = row[2]
       
        # In this if we check if the candidate name is already on the list, if so, we don't add it.
        if not candidate_name in candidate_option:
          
            # Here we add the name to candidate's list
            candidate_option.append(candidate_name)
            
            # In this line we add the candidate names to the dictionary and set their values to 0
            candidate_votes[candidate_name] = 0
       
        # Here we add the vote to each candidate
        candidate_votes[candidate_name] += 1

with open(file_to_save,"w") as txt_file:

    election_resuts = (
        f'Election Results\n'
        f'----------------------------------------\n'
        f'Total quantity of voters is {total_votes:,}\n'
        f'----------------------------------------\n'
    )
    
    print(election_resuts)
    txt_file.write(election_resuts)
    # The we print the variables or lists
    #print(f'\nTotal quantity of voters is {total_votes:,}\n')

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # print(f'{candidate_name}: received {vote_percentage:.1f}% of the vote with {votes:,} votes.')

        # This if will holds the winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # print(f'\nThe winning candidate is {winning_candidate} that received the {winning_percentage:.1f}% of the votes with {winning_count:,} votes.')

        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        print(candidate_results)
        txt_file.write(candidate_results)

    winning_candidate_summary = (f'----------------------------------------\n'
    f'The winning candidate is {winning_candidate} that received the {winning_percentage:.1f}% of the votes with {winning_count:,} votes.\n'
    f'----------------------------------------\n')
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)