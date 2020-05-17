import pandas as pd
import os

path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('.ec.csv')]
for filename in files_in_dir:
    # We save an augmented filename later, 
    # so using splitext is useful for more
    # than just checking the extension.
    prefix, ext = os.path.splitext(filename)
    if ext.lower() != '.csv':
        continue
    # Load the data into a dataframe
    df = pd.read_csv(filename, 
                               header=None, 
                               index_col=None, 
                               parse_dates=False)
    # Transpose is easy, but you could do TONS
    # of data processing here. pandas is awesome.
    df_transposed = df.T
    # Save to a new file with an augmented name 
    df_transposed.to_csv(prefix+'_T'+ext, header=False, index=False)


#merging all the transposed file
path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('.ec_T.csv')]
for filenames in files_in_dir:
    edge_data = pd.read_csv(filenames)
    edge_data.to_csv('merged_ec_data.csv', mode='a')


#removal of all ec_T.csv file 

dir_name = "."
test = os.listdir(dir_name)

for item in test:
    if item.endswith("ec_T.csv"):
        os.remove(os.path.join(dir_name, item))


#reading the file and renaming the column for finding the index later
df = pd.read_csv('merged_ec_data.csv')

df1 = df.drop(['Unnamed: 0'], axis=1)

df1.rename(columns={'Unnamed: 0.1': 'OTU'}, inplace=True)

df2 = df1[df1.OTU != 'Unnamed: 0']

df3 = df2.astype(float)

df4= df3.groupby(['OTU']).sum()

df5 = pd.read_csv('taxa_abundance.csv')

result = df5.merge(df4,on='OTU',how='left')

result.to_csv('taxzyme_view.csv', index = False)

os.remove ('merged_ec_data.csv')

print("The output is in taxzyme_view.csv file")
