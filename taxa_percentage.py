import pandas as pd

#defining percentage function

def percentage(x):
     return x/x.sum() * 100
	
taxa = pd.read_csv('taxa_abundance.csv', index_col=0)

#applying percentage function

taxa.iloc[:, :-7] = percentage(taxa.iloc[:, :-7]) # selecting all the columns except the last seven where taxonomy is there

taxa.to_csv('taxa_abundance_percent.csv')

print("The output is in taxa_abundance_percent.csv")

