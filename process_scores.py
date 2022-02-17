class Grader :
#TODO make methods and variable private/public/protected
# Define a class called Grader in the module process_scores.py. 
# The class Grader has the following members:

# The class Grader implements the following methods:
    #  __init__(list, str)
    # o Takes in the list of student responses and the correct answer string
    # o Initializes the empty lists
    #TODO
    def __init__(self, student_responses, correct_answer) :
        #  students
        # o Contains the list of students and their answers
        self.__students = student_responses 
        #  correct_key
            # o Contains the 10 correct answers
        self.__correct_key = correct_answer #(answer key)
        #  corrected_scores
            # o Contains a list of corrected students with their score and grade
        self.__corrected_scores = [] 
        #  sorted_scores
            # o Contains a list of corrected students sorted by score in descending order
        self.__sorted_scores = []

    #  compute_grade(int) ->str
        # o Based on the numerical grade, return the appropriate letter grade
        # o A: 100>=score>=90 ; B: 89>=score>=80 ; C: 79>=score>=70 D: #69>=score>=60; F: 50>=score>=0
    def __compute_grade(self, score) :
        if 100>=score and score>=90 :
            return 'A'
        elif 89>=score and score>=80 :
            return 'B'
        elif 79>=score and score>=70 :
            return 'C'
        elif 69>=score and score>=60 :
            return 'D'
        elif 59>=score and score>=0 :
            return 'F'
        else :
            raise ValueError("The given score is not valid, value over 100 or under 0 : " + score)

    #  compute_score(dict) -> int
        # o For the given student, compare their answer with correction key and return their numerical grade return the grade 
    def __compute_score(self, dict) :
        count = 0
        grade = 0
        for single_answer in dict.get("answer") :
            try :
                if single_answer == self.__correct_key[count] :
                    grade+=10
            except :
                self.__correct_key = "FFTTTTFTTT"
            count+=1
        return grade
    
    #  correct_students()
        # o Grades each student using the internal methods
        # o Populates the __corrected_scores and __sorted_scores attributes.
        # o A corrected student must have the following columns, refNber,studentID,studentFullName, score, grade\
    def correct_students(self) :
        corrected_students = []
        count = 0
        for student in self.__students :
            numerical_grade = self.__compute_score(student)
            letter_grade = self.__compute_grade(numerical_grade)
            corrected_students.append(student)
            corrected_students[count]["score"] = (numerical_grade)
            corrected_students[count]["grade"] = (letter_grade)
            count+=1
        self.__corrected_scores = corrected_students
        
    #  get_corrected_scores() -> list
        # o Returns the list of corrected students with their scores
    def get_corrected_scores(self) :
        return self.__corrected_scores
    
    #  get_sorted_scores() -> list
        # o Returns the list of corrected students with their scores sorted
    def get_sorted_scores(self) :
        self.__sorted_scores = sorted(self.__corrected_scores, key = lambda i: i['score'], reverse=True)
        return self.__sorted_scores