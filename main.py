from file_io import get_dictionary_list, write_dictionary_list
from process_scores import Grader

# In the main.py file, import the file_io.py module and Grader class from their respective modules.
# Perform the following in the main when main.py is called in python:
    # Prompt the user to provide the correct answer string and the scores file name.
        # o The user can hit enter and provide nothing, in which case, the following two default values are used.
            # filename: scores.csv
            # correct answer: ‘FFTTTTFTTT’
correct_key = input("Enter the correct answer string :\n")
for letter in correct_key :
    if letter not in ('F', 'f', 'T', 't') :
        correct_key = 'FFTTTTFTTT'
        print("An invalid key has been given, the default one will be used : FFTTTTFTTT")
        break

file_name = input("enter the file name you wish to read from :\n")
if file_name == '' :
    print("no file name provided, the default file will be used : scores.csv")
    file_name = 'scores.csv'
try :
    classroom = Grader(get_dictionary_list(file_name), correct_key)
except : 
    print("INVALID file name provided, the default file will be used : scores.csv")
    classroom = Grader(get_dictionary_list("scores.csv"), correct_key)


    # Use the Grader object to analyze the scores that have been loaded
classroom.correct_students()
    # Use the file_io module to save the report_ scores.txt
write_dictionary_list("report_scores.txt", classroom.get_corrected_scores())
    # Use the file_io module to save the report_categ_scores.txt
write_dictionary_list("report_categ_scores.txt", classroom.get_sorted_scores())