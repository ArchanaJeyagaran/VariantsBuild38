from pyfaidx import Fasta
from proteinacc_and_uniprotid import variant_df

# FASTA file downloaded from https://www.ncbi.nlm.nih.gov/genome/guide/human/ --> RefSeq Proteins GRCH38
# go through the protein accession numbers and find the corresponding sequences
genes = Fasta('GRCh38_latest_protein.faa')
fastaseq = []
for acc in variant_df['PROTEINACC']:
    if acc in genes:
        fastaseq.append(str(genes[acc]))
    else:
        fastaseq.append(None)

# add the FASTA sequences to the dataframe
variant_df['FASTASEQ'] = fastaseq