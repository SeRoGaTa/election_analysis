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


file_to_open = os.path.join("Week 3","Asynchronous Online Lessons","Resources","election_results.csv")
file_to_save = os.path.join("Week 3","Asynchronous Online Lessons","Analysis","election_analysis.csv")

with open(file_to_open) as election_data:
    file_reader=csv.reader(election_data)
    
    headers= next(file_reader)
    print(headers)
    #for row in file_reader:
    #    print(row)


# 1. The total number of votes cast.

# 2. A complete list of candidates who received votes.

# 3. The percentage of votes each candidate won.

# 4. The total number of votes each candidate won.

# 5. The winner of the election based on popular vote.