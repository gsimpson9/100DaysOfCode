import pandas as pd

# Quick group by without column headers
# data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# new_df = data.groupby('Primary Fur Color').size()
# new_df.to_csv('Count of fur colour.csv')

# Define your own column headers
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur Colour": ['Gray', 'Cinnamon', 'Black'],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

final_data = pd.DataFrame(data_dict)
final_data.to_csv('Count of fur colour.csv', index=False)
