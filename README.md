# downstream_paprica
for downstream analysis of paprica data

## For taxa_view.py

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires: python3 and Pandas

This script helps to extract taxonomic hierarchy and also compares the abundance of invidual taxa among different samples.
The input for this script is the output of paprica_v0.5.0 [filename.edge_data.csv (different for multiple samples)] and combine_edge_results.py script [filename.edge_tally.csv].  
Copy the script in paprica output folder and run as:
python taxa_view.py

## For taxa_view_v2.py

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires: python2 and Pandas

This script helps to extract taxonomic hierarchy and also compares the abundance of invidual taxa among different samples.
The input for this script is the output of combine_edge_results.py script [filename.edge_tally.csv and filename.taxon_map.csv]. It does not require all the edge data file as required earlier. Two files, edge_tally and taxon_map should be in the current folder where the script can be executed. This script also introduces taxon column in the taxonomic hierarchy

Copy the script in paprica output folder and run as:
python taxa_view_v2.py

## For taxa_percentage.py

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires: python3 and Pandas

This script helps to caluclate percentage abundance of different taxa from taxa_abundance.csv file (output of taxa_view_v2.py or taxa_view.py)

Copy the script in paprica output folder and run as:
python taxa_percentage.py

## For graph_view.py

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires:Python3, Pandas and matplotlib

This script helps to make graphs and percentage abundance calculations. 
This script is based on the outputs from taxa_view.py
Copy the script in the output folder of taxa_view.py
python3 graph_view.py

## For enzyme_view.py 
*This version is deprecated please use enzyme_view_v2.py.*

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires: python3 and Pandas

This script helps to name the EC numbers and also extracts the genes related sulfur and nitrogen cycle.
The input for this script is the output combine_edge_results.py script (filename.ec_tally.csv) and enzyme_final.csv (present in the repository).  
Copy the script in the folder containing filename.ec_tally.csv and enzyme_final.csv in paprica output folder and run as:
python enzyme_view.py

## For enzyme_view_v2.py (needs further verification)

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires: python3 and Pandas

Certain modifications are done to enzyme_view.py to adapt with latest version of pandas.
This script helps to name the EC numbers and also extracts the genes related sulfur and nitrogen cycle. There might be other enzymes related to sulfur and nitrogen cycle. You can also modify the script accordingly to include these enzymes.
The input for this script is the output from combine_edge_results.py (for older versions) or paprica-combine_results.py (for paprica v0.7.0)  script (filename.ec_tally.csv) and enzyme_final.csv (present in the repository).  
Copy the script in the folder containing filename.ec_tally.csv and enzyme_final.csv in paprica output folder and run as:
python enzyme_view_v2.py


## For edge_norm_16S.py 

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires: python3 and Pandas

This script generates two files, i) sequence.csv - file which contains assigned ASVs/DNA sequences to each edges and ii) normalized_edge.csv - normalized edge abundance based on 16S copy number
Input files- i)  .unique_tally.csv and ii) .taxon_map.csv

## For taxa_percentage_for_normalized_edge.py

@author: Avishek Dutta (avishekdutta14@gmail.com) 
@requires: python3 and Pandas

This script helps to calculate percentage abundance of different taxa from normalized_edge.csv file (output of edge_norm_16S.py).

## For taxzyme.py (needs further verification)

@author: Avishek Dutta (avishekdutta14@gmail.com) 
@requires: python3 and Pandas

Requires all the .ec.csv files from each samples and also require the taxa_abundance.csv (output from taxa_view.py or taxa_view_v2.py). Copy all the .ec.csv (output of paprica) file to a new folder in which only the ec files and taxa_abundance.csv is present and run the script "python taxzyme.py".

N.B.: Please note that the enzyme abundance for a particular taxon reported in the output is the cumulative abundance of the enzmye present across all the samples used for the analysis. 


## For taxpath.py (needs further verification)

@author: Avishek Dutta (avishekdutta14@gmail.com) 
@requires: python3 and Pandas

Requires all the .pathways.csv files from each samples and also require the taxa_abundance.csv (output from taxa_view.py or taxa_view_v2.py). Copy all the .pathways.csv (output of paprica) file to a new folder in which only the pathways.csv files and taxa_abundance.csv is present and run the script "python taxpath.py".

N.B.: Please note that the pathway abundance for a particular taxon reported in the output is the cumulative abundance of the pathways present across all the samples used for the analysis. 

## For pakr.py

@author: Avishek Dutta (avishekdutta14@gmail.com) 
@requires: python3, Pandas, and [Krona chart](https://github.com/marbl/Krona)

Requires unique_tally.csv, seq_edge_map.csv, and taxon_map.csv from paprica output. Install [Krona chart](https://github.com/marbl/Krona) and declare it to the PATH. Make a folder and copy unique_tally.csv, seq_edge_map.csv, and taxon_map.csv (output of paprica) and run "python pakr.py". You can also do "chmod a+x pakr.py" and "./pakr.py". Either the pakr.py should be present in the new folder containing all the three outputs of paprica, or it can also be declared in the PATH. The results will be in Krona_paprica.html

