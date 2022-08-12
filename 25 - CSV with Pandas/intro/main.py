# with open(r'weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open(r'weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

# Reading CSVs with pandas
data = pd.read_csv('weather_data.csv')
# DataFrame
# print(type(data))
# Series
# print(type(data['temp']))

# Output to dict
data_dict = data.to_dict()
# print(data_dict)

# Computations / descriptive stats
average_temp = data['temp'].mean()
max_temp = data['temp'].max()
# print(average_temp)
# print(max_temp)
# print(data.condition)

# Get Data in a row
monday = data[data['day'] == 'Monday']
# print(monday)

# Get row with the highest temperature
# hottest_day = data[data['temp'] == data['temp'].max()]
# OR
hottest_day = data[data.temp == data.temp.max()]
print(hottest_day)
monday_c_to_f = monday.temp * 1.8 + 32
# print(monday_c_to_f)


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "Scores": [76, 56, 65]
}

data2 = pd.DataFrame(data_dict)
data2.to_csv('new_data.csv', index=False)


