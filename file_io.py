import csv

# get_dictionary_list(path)
    # o Reads a CSV file at the given path
    # o Returns a list of dictionaries representing the data in the CSV
def get_dictionary_list(path) :
    classroom = []
    scores_file = csv.DictReader(open(path))
    for student in scores_file :
        classroom.append(student)
    return classroom

# write_dictionary_list(path, dictionary_list)
        # o Writes a list of dictionaries to the provided path
        # o The keys of the dictionary should be used as the headers of the CSV file
        # o The values of the dictionary should be used as the rows of the CSV file
def write_dictionary_list(path, dictionary_list) :
    with open(path, 'w') as data:
        data.write(str(dictionary_list))