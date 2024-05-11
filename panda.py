# pylint: disable=missing-module-docstring
import pandas as pd
data = pd.read_csv('data.csv')
age = data['age']
gender = data['gender']
race = data['race']
hour = data['hour']
category = data['activities']
option = ['min','max','median','mean','std','var']
# print(data.agg(
#   {
#     'age': option,
#     'hour': option
#   }
# ).round(4))

# test = data.groupby('race')['hour'].mean()
# print(test)

# average_hours = data.groupby('activities')['hour'].mean()
# print(average_hours)

# Filter data where 'beforeSleep' is 'Yes' and 'affectSleep' is 'Yes'
affected_sleep = data.loc[(data['beforeSleep'] == 'Yes') & (data['affectSleep'] == 'Yes')]
notAffected_sleep = data.loc[(data['beforeSleep'] == 'Yes')& (data['affectSleep'] == 'No')]
# Count the number of people
num_notAffected = len(notAffected_sleep)
num_people = len(affected_sleep)
percentage = round ((num_people / len(data)) * 100,4)

print(f'number of people not affected sleep: {num_notAffected}')
print(f"Number of people affected sleep: {num_people}")
print(f"Percentage of people affected by playing phone before sleeping: {percentage}%")
# print(age.value_counts())
# print(gender.value_counts())
# print(race.value_counts())
# print(hour.value_counts())
# print(category.value_counts())