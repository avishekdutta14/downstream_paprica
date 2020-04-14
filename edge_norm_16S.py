import pandas as pd
import os
import glob
import csv
import numpy

path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('.unique_tally.csv')]
for filenames in files_in_dir:
    unique_tally = pd.read_csv(filenames, index_col=False)

path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('.taxon_map.csv')]
for filenames in files_in_dir:
    taxon_map = pd.read_csv(filenames)



unique_t = unique_tally.T
unique_t.to_csv("ut.csv", header=None)

unique_t = pd.read_csv("ut.csv", index_col=False)

unique_t.rename(columns={'Unnamed: 0': 'mixed'}, inplace=True)



#separating the mixed column on the basis of underscore _ as delimitor

unique_t[['Sequence','OTU']] = unique_t.mixed.str.split("_",expand=True)

unique_t.to_csv("unique_transpose.csv", index=False)

#extracting sequence and edge names and saving in a csv file
sequences = unique_t[['OTU', 'Sequence']] 

sequences.to_csv("sequences.csv", index=False)

#grouping the edges based on unqiue normalized read no.s

edge = unique_t.groupby('OTU').sum()

edge.to_csv ('normalized_edge1.csv')

#Inserting the name of first column as OTU

taxon_map.rename(columns = {list(taxon_map)[0]:'OTU'}, inplace=True)
taxon_map.to_csv("taxonomy.csv", index=False)

#inserting the taxonomy of the columns

df1 = pd.read_csv('taxonomy.csv')
df2 = pd.read_csv('normalized_edge1.csv')
result = df2.merge(df1,on='OTU',how='left')
result.to_csv('normalized_edge.csv', index=False)


#Removing temporary files

os.remove ('unique_transpose.csv')
os.remove ('normalized_edge1.csv')
os.remove ('taxonomy.csv')
os.remove ('ut.csv')
print("############################     ########################")
print("############################     ########################")    
print ("The ASVs/DNA sequences associted with each edge are present in sequences.csv file")
print ("The normalized edge based on 16S rRNA gene copy number is present in normalized_edge.csv")
print("############################     ########################")
print("############################     ########################")    
