
"""

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires: python2 and Pandas

This script helps to extract taxonomic hierarchy and also compares the abundance of invidual taxa among different samples.
The input for this script is the output of paprica_v0.5.0 [filename.edge_data.csv (different for multiple samples)] and combine_edge_results.py script [filename.edge_tally.csv].  
Copy the script in paprica output folder and run as:
python taxa_view.py

"""


import pandas as pd
import os
import glob
import csv
import numpy as np

#Reading files having abundance

path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('.edge_tally.csv')]
for filenames in files_in_dir:
    edge_tally = pd.read_csv(filenames, header=None)

transpose = edge_tally.T
transpose.to_csv('transpose_file.csv', header=False, index=False)

#Merging files from different samples

path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('bacteria.edge_data.csv')]
for filenames in files_in_dir:
    edge_data = pd.read_csv(filenames)
    edge_data.to_csv('merged_edge_data.csv', mode='a')

#Extracting taxonomy

merged=pd.read_csv("merged_edge_data.csv")
merged.rename(columns={'Unnamed: 0.1': 'OTU'}, inplace=True)
keep_col = ['OTU','phylum','class','order','family', 'genus', 'species']
new_f = merged[keep_col]
new_f.to_csv("taxonomy.csv", index=False)

#Converting character

transpose_char=pd.read_csv("transpose_file.csv")
transpose_char.rename(columns={'Unnamed: 0': 'OTU'}, inplace=True)
transpose_char['OTU'] = transpose_char['OTU'].astype(int)
transpose_char.to_csv("transpose_file_int.csv", index=False)

#Removing strings

filter=pd.read_csv('taxonomy.csv')
filtered_file = filter[~filter.OTU.str.contains("Unnamed: 0")]
filtered_file.to_csv('taxonomy_int.csv', index=False)

#Taxa_abundance 

df1 = pd.read_csv('taxonomy_int.csv')
df2 = pd.read_csv('transpose_file_int.csv')
result = df2.merge(df1,on='OTU',how='left')
result.to_csv('taxa_abundance1.csv', index=False)

unique= pd.read_csv('taxa_abundance1.csv')
unique.drop_duplicates(subset=None, inplace=True)
unique.to_csv('taxa_abundance.csv', index=False)

import pandas as pd



group = pd.read_csv('taxa_abundance.csv')
group['phylum'].fillna('Unassigned', inplace=True)
group['class'].fillna('Unassigned', inplace=True)
group['order'].fillna('Unassigned', inplace=True)
group['family'].fillna('Unassigned', inplace=True)
group['genus'].fillna('Unassigned', inplace=True)
group['species'].fillna('Unassigned', inplace=True)
group.to_csv ('Unassigned.csv', index=False)

#Grouping phylum
phylum = pd.read_csv('Unassigned.csv')
phylum = group.groupby('phylum').sum()
phylum = phylum.drop('OTU', 1)
phylum.to_csv ('phylum.csv')


#Grouping class
df = pd.read_csv('Unassigned.csv')
df = df.groupby('class').sum()
df = df.drop('OTU', 1)
df.to_csv ('class.csv')


#Grouping order
order = group.groupby('order').sum()
order = order.drop('OTU', 1)
order.to_csv ('order.csv')


#Grouping family
family = group.groupby('family').sum()
family = family.drop('OTU', 1)
family.to_csv ('family.csv')

#Grouping genus
genus = group.groupby('genus').sum()
genus = genus.drop('OTU', 1)
genus.to_csv ('genus.csv')

#Grouping species
species = group.groupby('species').sum()
species = species.drop('OTU', 1)
species.to_csv ('species.csv')


#Deleting temporary files

os.remove ('transpose_file.csv')
os.remove ('merged_edge_data.csv')
os.remove ('taxonomy.csv')
os.remove ('transpose_file_int.csv')
os.remove ('taxonomy_int.csv')
os.remove ('taxa_abundance1.csv')
os.remove ('Unassigned.csv')
print ('The output of the file is present in taxa_abundance.csv')
