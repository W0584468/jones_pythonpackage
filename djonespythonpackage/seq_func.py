import pandas as pd
import dendropy
""" This function creates a newick tree from the salamanders.json file"""

def seq_func(filepath):
    pd.options.display.max_colwidth = 1000000
    salamanders = pd.read_json(filepath)
    salamanders

    pd.options.display.max_colwidth = 1000000
    newick_tree = salamanders.newick.to_string(index=False)
    newick_tree
