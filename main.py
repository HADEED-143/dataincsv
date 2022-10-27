import pandas as pd
import csv

df = pd.read_csv('Hadeed-Task-Data (1).csv', usecols=['age'])
df.head()
df.values.tolist()
print(df)
for row in df:
    age_15 = df[(df['age'] == 15)]
    print(age_15.to_csv('age_15.csv'))

    age_16 = df[(df['age'] == 16)]
    print(age_16.to_csv('age_16.csv'))

    age_17 = df[(df['age'] == 17)]
    print(age_17.to_csv('age_17.csv'))

    age_18 = df[(df['age'] == 18)]
    print(age_18.to_csv('age_18.csv'))

    age_19 = df[(df['age'] == 19)]
    print(age_19.to_csv('age_19.csv'))

    age_20 = df[(df['age'] == 20)]
    print(age_20.to_csv('age_20.csv'))

    age_21 = df[(df['age'] == 21)]
    print(age_21.to_csv('age_21.csv'))

    age_22 = df[(df['age'] == 22)]
    print(age_22.to_csv('age_22.csv'))

    age_23 = df[(df['age'] == 23)]
    print(age_23.to_csv('age_23.csv'))

    age_24 = df[(df['age'] == 24)]
    print(age_24.to_csv('age_24.csv'))

else:
    print("not in range data will not save in file")
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
