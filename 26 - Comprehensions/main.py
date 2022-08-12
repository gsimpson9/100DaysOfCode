import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
#
# for (key, value) in student_dict.items():
#     print(value)

student_df = pd.DataFrame(student_dict)

# Loop through dataframe
for (index, row) in student_df.iterrows():
    if row.score > 70:
        print(row.student)

        # student_dict = {
        #     "student": ["Angela", "James", "Lily"],
        #     "score": [56, 76, 98]
        # }

        # #Looping through dictionaries:
        # for (key, value) in student_dict.items():
        #     #Access key and value
        #     pass

        # import pandas
        # student_data_frame = pandas.DataFrame(student_dict)

        # #Loop through rows of a data frame
        # for (index, row) in student_data_frame.iterrows():
        #     #Access index and row
        #     #Access row.student or row.score
        #     pass

# PyDev console: starting.
# Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
# name = 'Graeme'
# new_list = [letter for letter in name]
# double = [num*2 for num in range(1,5)]
# names = ['Graeme', 'David', 'John', 'Beth', 'Fred', 'Elaenor']
# names
# ['Graeme', 'David', 'John', 'Beth', 'Fred', 'Elanor']
# short_names = [n for n in names if len(n) == 4]
# short_names = [n for n in names if len(n) < 5]
# upper_long_names = [n.upper() for n in names if len(n) > 4]
# students_score = {}
# import random
# student_score = {student:random.randint(0,100) for student in names}
# print(student_score)
# {'Graeme': 41, 'David': 91, 'John': 22, 'Beth': , 14'Fred': 0, 'Elanor': 51}
# student_score = {student:random.randint(0,100) for student in names}
# student.items()
# Traceback (most recent call last):
#   File "C:\Users\GraemeSimpson\AppData\Local\Programs\Python\Python310\lib\code.py", line 90, in runcode
#     exec(code, self.locals)
#   File "<input>", line 1, in <module>
# NameError: name 'student' is not defined
# student_score.items()
# dict_items([('Graeme', 45), ('David', 84), ('John', 97), ('Beth', 70), ('Fred', 41), ('Elanor', 24)])
# passed_students = {student:score for (student, score) in student_score.items() if score > 80}