import dendropy
import os.path 
def sequence_reader(filepath):
    assert os.path.exists(filepath)
    sequence_set = dendropy.DnaCharacterMatrix.get(
    path=filepath
    schema='phylip'
)
    
    return(sequence_set)