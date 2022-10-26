import pandas as pd
import csv
df = pd.read_csv('Hadeed-Task-Data (1).csv')

agecsv18 = df[(df['age'] == 18)]
agecsv19 = df[(df['age'] == 19)]
agecsv20 = df[(df['age'] == 20)]

agecsv18.isnull()
agecsv19.isnull()
agecsv20.isnull()

agecsv18 = df.fillna(value=0)
agecsv19 = df.fillna(value=0)
agecsv20 = df.fillna(value=0)

print(agecsv18.head().to_csv('age_18.csv'))
print(agecsv19.head().to_csv('age_19.csv'))
print(agecsv20.head().to_csv('age_20.csv'))





"""
age_18 = agecsv18.to_csv('age_18.csv')
age_19 = agecsv19.to_csv('age_19.csv')
age_20 = agecsv20.to_csv('age_20.csv')

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
