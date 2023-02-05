# Variants in Human Genome Build 38

## Summary
The pipeline creates a SQL database for the first 500,000 nucleotides of human chromosomes 1-10 against the human genome build 38

## Notes 
Chose 500,000 nts since there was very minimal data when limiting the data to the first 50,000 nt
There is no data for the frist 500,000 nts in Chromosome 1

## Data
VCF file downloaded from https://www.ncbi.nlm.nih.gov/genome/guide/human/ --> ClinVar GRCH38
FASTA file downloaded from https://www.ncbi.nlm.nih.gov/genome/guide/human/ --> RefSeq Proteins GRCH38

# Setup
Unzip the data files downloaded from NCBI to run the code 

## Queries
Run queries.py to:
1. filter the data by chromosome and segement positions (eg, Chromosome '10', Start 40000, End 100000)
2. find the chromosome with the most variants
3. find the most common variant type in each chromosome
4. find the most common variant type overall
5. find the genes with the most variants


