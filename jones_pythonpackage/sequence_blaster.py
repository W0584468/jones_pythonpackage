from Bio.Blast import NCBIWWW
from Bio import SeqIO
#check that there is an input
#check that it is in fasta format 

def sequence_blaster(fasta_path, results_path):
    fasta_path = SeqIO.read(fasta path, format='fasta')
    results_path = NCBIWW.qblast('blastn','nt',fast_path.format('fasta'))
    save_file = open(results_path, 'w')
    save_file.write(results_handle.read())
    save_file.close()
    assert os.stat(results_path).st_size !=0


    