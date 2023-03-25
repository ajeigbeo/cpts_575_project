#examples:
#https://towardsdatascience.com/visualizing-clusters-with-pythons-matplolib-35ae03d87489
#https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
#clusters

#this implimentation will be using Hierarchical, bottom up or agglomerative clustering



#prerequisit, all nodes should be sorted based on collection date.

import csv # this library may not be necisary 
import Cleaning_Sequences
import pandas as pd
#with open('../Data/my_sequences_ncbi.csv', newline = '') as csvfile: dataObject = csv.writer(csvfile, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
sequences = pd.read_csv('../Data/my_sequences_ncbi.csv')
#sequences = Cleaning_Sequences.clean(sequences) use this method to clean and organize the date column of the dataframe
print(sequences)

#the below medthod will only pair a node with its clossest match
import Distance_Metric



print(Distance_Metric.DistanceMetric("hello", "hell"))
