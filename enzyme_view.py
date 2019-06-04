"""

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires: python2 and Pandas

This script helps to name the EC numbers and also extracts the genes related sulfur and nitrogen cycle
The input for this script is the combine_edge_results.py script (filename.ec_tally.csv) and enzyme_final.csv (present in the repository).  
Copy the script in the folder containing filename.ec_tally.csv and enzyme_final.csv in paprica output folder and run as:
python enzyme_view.py

"""


import pandas as pd
import os
import glob
import csv

path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('.ec_tally.csv')]
for filenames in files_in_dir:
    df = pd.read_csv(filenames, header=None)

df1 =df.T
df1.to_csv('transpose_ec.csv', header=False, index=False)

transpose=pd.read_csv("transpose_ec.csv")
transpose.rename(columns={'Unnamed: 0': 'ID'}, inplace=True)
#print (transpose)
transpose.to_csv('transpose_ec_id.csv', header=True, index=False)

df1 = pd.read_csv('transpose_ec_id.csv')
df2 = pd.read_csv('enzyme_final.csv')
result = df1.merge(df2,on='ID',how='left')
result.to_csv('enzyme_view.csv', index=False)

pe = pd.read_csv('enzyme_view.csv')
pe.set_index('ID', inplace=True)
sulfur = pe.loc[['1.8.1.2', '1.8.7.1', '1.8.99.1', '1.97.1.3', '1.13.11.18', '1.13.11.5', '2.8.1.5', '1.8.2.2', '1.8.5.2' , '2.8.1.1', '3.12.1.1', '1.8.99.3', '1.8.2.1', '1.8.3.1', '1.12.98.4', '4.4.1.6', '3.5.5.8', '4.4.1.1', '4.4.1.8', '1.8.1.6', '4.4.1.15', '4.4.1.9', '4.4.1.10', '4.2.1.1', '2.8.1.3', '4.4.1.2', '1.13.11.20', '3.1.6.1', '1.8.3.4']]
sulfur.to_csv('sulfur_cycle.csv', header=True)
nitrogen = pe.loc[['1.7.99.4', '1.9.6.1', '1.7.2.1', '1.7.99.7', '1.7.99.6', '1.7.2.2', '1.7.3.4', '1.7.99.4', '1.7.99.1', '1.7.99.8', '3.6.3.21', '3.6.3.22', '3.6.3.23', '3.6.3.26', '3.6.3.31', '3.6.3.32', '3.6.3.36', '3.6.3.37', '3.6.3.43', '1.7.1.1', '1.7.1.2', '1.7.1.3', '1.7.7.2', '1.7.7.1', '1.7.1.4', '1.4.1.2', '1.4.1.3', '1.4.1.4', '1.4.1.13', '1.4.1.14', '1.4.7.1', '6.3.1.1', '1.18.6.1', '1.19.6.1', '3.5.1.5', '6.3.4.6', '3.5.1.54']]
#nitrogen2 = pe.loc [['3.6.3.21', '3.6.3.22', '3.6.3.23', '3.6.3.26', '3.6.3.31', '3.6.3.32', '3.6.3.36', '3.6.3.37', '3.6.3.43']]
#nitrogen3 = pe.loc [['1.7.1.1', '1.7.1.2', '1.7.1.3', '1.7.7.2', '1.7.7.1', '1.7.1.4', '1.4.1.2', '1.4.1.3', '1.4.1.4', '1.4.1.13', '1.4.1.14', '1.4.7.1', '6.3.1.1', '1.18.6.1', '1.19.6.1', '3.5.1.5', '6.3.4.6', '3.5.1.54']]
nitrogen.to_csv('nitrogen_cycle.csv', header=True)

os.remove ('transpose_ec.csv')
os.remove ('transpose_ec_id.csv')

print ('The output is present in enzyme_view.csv')
print ('Note: If you get a warning stating #deprecate-loc-reindex-listlike, then some of the eznzymes are not present in your dataset')

