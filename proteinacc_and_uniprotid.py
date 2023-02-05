import mygene
from clean_data import variant_df

# query to find the associated protein accession number and uniprot id based on geneid using the mygene package
mg = mygene.MyGeneInfo()
proteinacc = mg.querymany(variant_df['GENEID'], fields = ['refseq.protein', 'uniprot'] )
proteinval = []
uniprotidval = []
for val in proteinacc:
    # find the canonical protein accession number assocaiatied with the gene
    # selecting first protein in the list 
    if 'refseq' in val:
        proteinval.append(val['refseq']['protein'][0])
        
    else: 
        proteinval.append(None)
    
    # find the associated uniprot id 
    if 'uniprot' in val:
        uniprotidval.append(val['uniprot']['Swiss-Prot'])
    else: 
        uniprotidval.append(None)

# add the accession number and uniprotid to the dataframe
variant_df['PROTEINACC'] = proteinval
variant_df['UNIPROTID'] = uniprotidval

