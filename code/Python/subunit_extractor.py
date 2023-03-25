"""
Vincent Lombardi
main data cleaning file
"""

import pandas as pd
import numpy as np
import csv


sequences = pd.read_csv('data/my_sequences10.csv')
c_list = []

with open('worldmap.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=",")
    next(csvfile)
    for row in read_csv:
        if row:
            c_list.append(row[0])
    csvfile.close()

# filter countries
sequences = sequences.dropna()
sequences = sequences.replace(to_replace ="United Kingdom", value ="UK")
sequences = sequences.replace(to_replace="china", value="China")
sequences = sequences.replace(to_replace="italy", value="Italy")
sequences = sequences.replace(to_replace="india", value="India")
sequences = sequences.replace(to_replace="iran", value="Iran")
sequences = sequences.replace(to_replace="United States", value="USA")
sequences = sequences.replace(to_replace="US", value="USA")
sequences = sequences.replace(to_replace="U.S. Virgin Islands", value="Virgin Islands")
sequences = sequences.replace(to_replace="Viet Nam", value="Vietnam")
sequences = sequences[sequences.country.isin(c_list)]
# count number of recurrences per month. For the world map we changed date to country
sequences['Count'] = 1

sequences["sequence"] = sequences["sequence"].str.strip()
sequences["date"] = sequences["date"].str.strip()

sequences['temp'] = sequences["sequence"] + sequences["date"]

sequences = sequences.groupby(["temp"], as_index=False).agg(
    {'country': 'first', 'sequence': 'first', 'accession': 'first', 'date': 'first', "Count": 'sum'})

sequences = sequences.drop(columns="temp")

sequences = sequences.dropna()
sequences.drop(sequences[sequences['Count'] < 10].index, inplace = True) # filter out months with low recurrence

# break sequence into subunits
sequences['NTD'] = sequences.sequence.str[13:306]
sequences['RBD'] = sequences.sequence.str[319:542]
sequences['FP'] = sequences.sequence.str[788:807]
sequences['HR1'] = sequences.sequence.str[912:965]
sequences['HR2'] = sequences.sequence.str[1163:1214]
sequences['TM'] = sequences.sequence.str[1214:1237]
sequences['CT'] = sequences.sequence.str[1237:]

sequences['CT'].replace('', np.nan, inplace=True)
seq = sequences.dropna()
seq.to_csv("data/global_month.csv", index=False)
