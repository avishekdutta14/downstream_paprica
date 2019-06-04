# downstream_paprica
for downstream analysis of paprica data

#For taxa_view.py

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires: python2 and Pandas

This script helps to extract taxonomic hierarchy and also compares the abundance of invidual taxa among different samples.
The input for this script is the output of paprica_v0.5.0 [filename.edge_data.csv (different for multiple samples)] and combine_edge_results.py script [filename.edge_tally.csv].  
Copy the script in paprica output folder and run as:
python taxa_view.py

#For graph_view.py

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires:Python3, Pandas and matplotlib

This script helps to make graphs and percentage abundance calculations. 
This script is based on the outputs from taxa_view.py
Copy the script in the output folder of taxa_view.py
python3 graph_view.py

#For enzyme_view.py

@author: Avishek Dutta (avishekdutta14@gmail.com)
@requires: python2 and Pandas

This script helps to name the EC numbers and also extracts the genes related sulfur and nitrogen cycle
The input for this script is the combine_edge_results.py script (filename.ec_tally.csv) and enzyme_final.csv (present in the repository).  
Copy the script in the folder containing filename.ec_tally.csv and enzyme_final.csv in paprica output folder and run as:
python enzyme_view.py
