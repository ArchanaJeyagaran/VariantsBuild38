import allel

# VCF file downloaded from https://www.ncbi.nlm.nih.gov/genome/guide/human/ --> ClinVar GRCH38
# load the vcs file and convert it to a dataframe, select fields of interest
df = allel.vcf_to_dataframe('GRCh38_latest_clinvar.vcf', 
fields =['variants/CHROM', 'variants/POS', 'variants/REF', 'variants/ALT', 
'variants/GENEINFO', 'variants/MC'] )