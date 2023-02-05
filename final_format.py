from FASTA import variant_df

# remove unneccessary columns 
variant_df = variant_df.drop(['REF','ALT_1', 'ALT_2', 'ALT_3'], axis=1)

# reorder coloumns
variant_df = variant_df[['CHROM', 'START', 'END', 'GENENAME', 'PROTEINACC', 'FASTASEQ', 'VARIANT', 'UNIPROTID']]
