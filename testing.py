# The data we need to retrieve
import csv
import os

# Esto es una forma de hacerlo, aquí tienes que abrir y cerrar el archivo siempre para evitar que se pierda la info que guardaste en él.

#file_to_open = '../Resources/election_results.csv'
### # Open the election results and read the file.
###election_data = open(file_to_open,'r')
### # To do: perform analysis.
### # Close the file.
###election_data = close()

# De esta forma de abrir un archivo, te ahorras el cerrarlo para que se graben los datos.

# file_to_open = os.path.join("Week 3","Asynchronous Online Lessons","Resources","election_results.csv")
# with open(file_to_open) as election_data:
#     # To do.
#     print(election_data)

# # Esto es para escribir en el archivo el \n sirve para escribir en la siguiente linea

# file_to_save = os.path.join("Week 3","Asynchronous Online Lessons","Analysis","election_analysis.csv")
# with open(file_to_save,"w") as out_file:
#     out_file.write("Countries in the election\n--------------------------\nArapahoe\nDenver\nJefferson")

    # This code will read and print just the header line must be inside the with.
    #headers= next(file_reader)
    #print(headers)


# Here we asign the path to a variable to read the file.
file_to_open = os.path.join("Week 3","Asynchronous Online Lessons","Resources","election_results.csv")
# Here we asign the path to a variable to write the file.
file_to_save = os.path.join("Week 3","Asynchronous Online Lessons","Analysis","election_analysis.csv")

# 1. The total number of votes cast.

# This code will open the file
with open(file_to_open) as election_data:
    file_reader=csv.reader(election_data)
    
    # Here I initialize to 0 the total votes variable
    total_votes = 0

    # This code will skip the header line.
    headers = next(file_reader)

    # This code will print each line of the file
    for row in file_reader:
        # In this line we add 1 to the same variable for each line of the file
        total_votes += 1

# The we print the variable    
print(total_votes)

# 2. A complete list of candidates who received votes.
candidate_option = []

with open(file_to_open) as election_data:
    file_reader=csv.reader(election_data)
    
    headers= next(file_reader)
    
    for row in file_reader:
        candidate_name = row[2]
        candidate_option.append(candidate_name)

print(candidate_option)

# 3. The percentage of votes each candidate won.

# 4. The total number of votes each candidate won.

# 5. The winner of the election based on popular vote.