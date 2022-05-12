#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#@author: Avishek Dutta, avdutta@ucsd.edu

import pandas as pd
import os
import subprocess

# reading unique tally

path = os.getcwd()
files_in_dir = [f for f in os.listdir(path) if f.endswith('.unique_tally.csv')]
for filenames in files_in_dir:
    tally = pd.read_csv(filenames, index_col=0)

samplename = list(tally.index)

tally = tally.T

tally.reset_index(inplace=True)

tally=tally.rename(columns = {'index':'sequence'})

# reading unique sequence edge map

path = os.getcwd()
files_in_dir = [f for f in os.listdir(path) if f.endswith('.seq_edge_map.csv')]
for filenames in files_in_dir:
    map = pd.read_csv(filenames, index_col=0)

map.reset_index(inplace=True)

map=map.rename(columns = {'index':'sequence'})

# reading taxon map

path = os.getcwd()
files_in_dir = [f for f in os.listdir(path) if f.endswith('taxon_map.csv')]
for filenames in files_in_dir:
    taxa = pd.read_csv(filenames, index_col=0)

taxa.reset_index(inplace=True)

taxa=taxa.rename(columns = {'index':'global_edge_num'})

# merging files

merge1 = tally.merge(map, left_on='sequence', right_on='sequence')

merge2 = merge1.merge(taxa, left_on='global_edge_num', right_on='global_edge_num', how="left")

# creating files for all samples

for x in samplename:
   
    sample = merge2[[x,'superkingdom','phylum','clade','class','order','family','genus','species','strain','taxon']]

    sample[x] = sample[x].fillna(0)

    # sample.drop(sample.index[sample[x] == 0], inplace=True)

    sample.to_csv('{}_krona.csv'.format(x), header=False, index=False, sep ='\t')

print("Creating Krona chart: This may take time depending on the number of samples.")

os.system("ktImportText -o krona_paprica.html *_krona.csv")
os.system("rm -rf *_krona.csv")

print("The output is in krona_paprica.html.")

