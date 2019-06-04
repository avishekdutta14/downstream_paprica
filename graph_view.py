"""

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires:Python3, Pandas and matplotlib

This script helps to make graphs and percentage abundance calculations. 
This script is based on the outputs from taxa_view.py
Copy the script in the output folder of taxa_view.py
python3 graph_view.py

"""

import pandas as pd
import matplotlib.pyplot as plt

n = float(input ('Please enter the percentage above which taxa will be plotted:'))


phylum = pd.read_csv('phylum.csv', index_col=0)
phylum = phylum/phylum.sum()*100
phylum['mean'] = phylum.mean(axis=1) # adding a mean column in the dataframe
phylum_n = phylum.loc[(phylum['mean'] >= n)]

phylum.to_csv('phylum_percent.csv')
phylum_n.to_csv('phylum_percent_{}.csv'.format(n))


df = pd.read_csv('class.csv', index_col=0)
df = df/df.sum()*100
df['mean'] = df.mean(axis=1)
df_n = df.loc[(df['mean'] >=n)]
df_n.to_csv ('class_percent_{}.csv'.format(n))
df.to_csv('class_percent.csv')

df1 = pd.read_csv('order.csv', index_col=0)
df1 = df1/df1.sum()*100
df1['mean'] = df1.mean(axis=1)
df1_n = df1.loc[(df1['mean'] >=n)]
df1_n.to_csv ('order_percent_{}.csv'.format(n))
df1.to_csv('order_percent.csv')

df2 = pd.read_csv('family.csv', index_col=0)
df2 = df2/df2.sum()*100
df2['mean'] = df2.mean(axis=1)
df2_n = df2.loc[(df2['mean'] >=n)]
df2_n.to_csv ('family_percent_{}.csv'.format(n))
df2.to_csv('family_percent.csv')

df3 = pd.read_csv('genus.csv', index_col=0)
df3 = df3/df3.sum()*100
df3['mean'] = df3.mean(axis=1)
df3_n = df3.loc[(df3['mean'] >=n)]
df3_n.to_csv ('genus_percent_{}.csv'.format(n))
df3.to_csv('genus_percent.csv')


#making graph



df = pd.read_csv('phylum_percent_{}.csv'.format(n), index_col=0)
df = df.T
ax = df.plot(kind='bar', stacked=True, figsize=(18.5, 10.5))
ax.set_ylabel('Percent abundance')
ax.set_xlabel('Samples')
plt.savefig('phylum.png')

df = pd.read_csv('class_percent_{}.csv'.format(n), index_col=0)
df = df.T
ax = df.plot(kind='bar', stacked=True, figsize=(18.5, 10.5))
ax.set_ylabel('Percent abundance')
ax.set_xlabel('Samples')
plt.savefig('class.png')

df = pd.read_csv('order_percent_{}.csv'.format(n), index_col=0)
df = df.T
ax = df.plot(kind='bar', stacked=True, figsize=(18.5, 10.5))
ax.set_ylabel('Percent abundance')
ax.set_xlabel('Samples')
plt.savefig('order.png')

df = pd.read_csv('family_percent_{}.csv'.format(n), index_col=0)
df = df.T
ax = df.plot(kind='bar', stacked=True, figsize=(18.5, 10.5))
ax.set_ylabel('Percent abundance')
ax.set_xlabel('Samples')
plt.savefig('family.png')

df = pd.read_csv('genus_percent_{}.csv'.format(n), index_col=0)
df = df.T
ax = df.plot(kind='bar', stacked=True, figsize=(18.5, 10.5))
ax.set_ylabel('Percent abundance')
ax.set_xlabel('Samples')
plt.savefig('genus.png')
