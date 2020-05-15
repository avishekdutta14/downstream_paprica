import pandas as pd
import os

#merging all the transposed file
path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('.ec.csv')]
for filenames in files_in_dir:
    edge_data = pd.read_csv(filenames)
    edge_data.to_csv('merged_ec_data.csv', mode='a')

#reading the file and renaming the column for finding the index later
df = pd.read_csv('merged_ec_data.csv')
df.rename(columns={'Unnamed: 0.1': 'OTU'}, inplace=True)

#retaining the columns having enzymes related to sulfur cycle

df1 = df[['OTU','1.8.1.2', '1.8.7.1', '1.8.99.1', '1.97.1.3', '1.13.11.5', '2.8.1.5', '1.8.5.2' , '2.8.1.1', '1.8.99.3', '1.8.2.1', '1.8.3.1', '3.5.5.8', '4.4.1.1', '4.4.1.8', '1.8.1.6', '4.4.1.15', '4.2.1.1', '4.4.1.2', '1.13.11.20', '3.1.6.1']]

df2 = df1[df1.OTU != 'Unnamed: 0'] # removing the columns starting with Unnamed: 0

df2 =df2.astype(float).round(0) # converting the values into floats

df2 = df2.groupby(['OTU']).sum() # adding the values from similar taxa

df2['total'] = df2.iloc[:,0] + df2.iloc[:,1] + df2.iloc[:,2] + df2.iloc[:,3] + df2.iloc[:,4] + df2.iloc[:,5] + df2.iloc[:,6] + df2.iloc[:,7] + df2.iloc[:,8] + df2.iloc[:,9] + df2.iloc[:,10] + df2.iloc[:,11] + df2.iloc[:,12] + df2.iloc[:,13] + df2.iloc[:,14] + df2.iloc[:,15] + df2.iloc[:,16] + df2.iloc[:,17] + df2.iloc[:,18] + df2.iloc[:,19] # making total

df2.drop(df2[df2.total == 0].index, inplace = True) # removing 0 from total to get exact number of taxa contributing particular cycle

df2.to_csv('sulfur.csv')

df3 = pd.read_csv('taxa_abundance.csv')

result = df2.merge(df3,on='OTU',how='left')
result.to_csv('sulfur_taxa.csv')

#print (result)


#retaining the columns having enzymes related to sulfur cycle

nitrate = df[['OTU','1.7.99.4','1.7.1.4','1.7.7.1','1.7.2.1','1.7.1.1','1.7.99.1','1.7.2.2']]
nitrate = nitrate[nitrate.OTU != 'Unnamed: 0']
nitrate = nitrate.astype(float).round(0)
nitrate = nitrate.groupby(['OTU']).sum()
nitrate['total'] = nitrate.iloc[:,0] + nitrate.iloc[:,1] + nitrate.iloc[:,2] + nitrate.iloc[:,3] + nitrate.iloc[:,4] + nitrate.iloc[:,5] + nitrate.iloc[:,6]

nitrate.drop(nitrate[nitrate.total == 0].index, inplace = True)

#print (nitrate)
nitrate.to_csv('nitrate.csv')
result1 = nitrate.merge(df3,on='OTU',how='left')
print (result1)
result1.to_csv('nitrate_taxa.csv')

os.remove ('merged_ec_data.csv') # removal of this file is required otherwise adding up starts