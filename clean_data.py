import pandas as pd
from load_vcf import df


# only want the first 10 chromosomes
chromosomes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
variant_df = df.loc[df['CHROM'].isin(chromosomes)]

# only want up to first 50,000 nt, POS < 500,001 
# chose 500,000 nts since there was very minimal data when limiting the data to the first 50,000 nt
variant_df = variant_df[variant_df['POS'] < 500001]

# There is no data for the frist 500,000 nt in chromosome 1

# find the end position
# removed 1 NA from ALT_1 as it was not allowing for the END coloumn to properly format 
variant_df = variant_df[variant_df['ALT_1'].notna()] # one NA value, removed it 
variant_df['END'] = (variant_df['POS'] + (variant_df['ALT_1'].str.len() - 1)).round()

# change name of columns
variant_df = variant_df.rename({'POS':'START', 'NUMALT':'NUMNT',
 'GENEINFO':'GENENAME', 'MC':'VARIANT'}, axis = 1)

# clean the geneid column to only contain the gene name and make a new column with the gene id
variant_df[['GENENAME', 'GENEID']] = variant_df['GENENAME'].str.split(':', 1, expand=True)
# remove excess information in the GENEID coloumm
variant_df['GENEID'] = variant_df['GENEID'].str.split('|').str[0]
# clean the variant column to contain everything after "|"
variant_df['VARIANT'] = variant_df['VARIANT'].str.split('|').str[1]

