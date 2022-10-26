import pandas as pd
import csv

from pandas import notnull

df = pd.read_csv('Hadeed-Task-Data (1).csv')

agecsv18 = df[(df['age'] == 18)]
agecsv19 = df[(df['age'] == 19)]
agecsv20 = df[(df['age'] == 20)]


age_18 = agecsv18.head().to_csv('age_18.csv')
age_19 = agecsv19.head().to_csv('age_19.csv')
age_20 = agecsv20.head().to_csv('age_20.csv')


print(age_18)
print(age_19)
print(age_20)

"""
datacsv1 = pd.DataFrame(agecsv18.notnull())
datacsv2 = pd.DataFrame(agecsv19.notnull())
datacsv3 = pd.DataFrame(agecsv20.notnull())


with open('age_18.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(agecsv18.head())
#datacsv = pd.DataFrame(agecsv18)
with open('age_18.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(agecsv18.head())
    print(agecsv18.head())


"""
    #print(agecsv18.head())
    #csv_read = csv.reader(file)

"""
with open('age_19.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(agecsv19.head())
    print(agecsv19.head())

with open('age_20.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(agecsv20.head())
    print(agecsv20.head())

writer.to_csv('agedata_18.csv')
new_df = pd.read_csv('age_18.csv')
print(new_df)
"""