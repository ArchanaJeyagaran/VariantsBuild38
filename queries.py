from sql_dataframe import  engine
from sqlalchemy import text

# chromosome with most variants  
def most_variants_query():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT CHROM, COUNT(*) AS count FROM variant_data GROUP BY CHROM ORDER BY count DESC LIMIT 1"))
        
        for row in result:
            print(row)

# first variant in each chromosome 
def first_variant_query():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT *, MIN(START) FROM variant_data GROUP BY CHROM"))

        for row in result:
            print(row)

# most common variant type per chromosome 
def common_variant_chrom_query():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT CHROM, VARIANT FROM variant_data GROUP BY CHROM ORDER BY COUNT(VARIANT)"))

        for row in result:
            print(row)

# most common variant type overall 
def common_variant_all_query():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT VARIANT FROM variant_data GROUP BY VARIANT ORDER BY COUNT(VARIANT) DESC LIMIT 1"))

        for row in result:
            print(row)           

# genes with most variants 
def genes_most_variant_query():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT GENENAME, COUNT(*) AS count FROM variant_data GROUP BY GENENAME ORDER BY count DESC LIMIT 5"))

        for row in result:
            print(row)

# query that accepts the chromosomal and segment position as parameters
def filter_initial_query(chromosome, start, end):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM variant_data WHERE CHROM == " + chromosome + " AND " + str(start) + " < START AND " + str(end) +" > END"))

        for row in result:
            print(row)

most_variants_query()
# this query returns the chromosome with the most variants
# it takes no parameters 

first_variant_query()
# this query returns the first variant from each each chromosome
# it takes no parameters

common_variant_chrom_query()
# this query returns the most common variant type per chromosome
# it takes no parameters 

common_variant_all_query()
# this query returns the most common variant type overall
# it takes no parameters 

genes_most_variant_query()
# this query returns the top 5 most common variant type overall
# it takes no parameters 

# filter_initial_query()
# this query filters the data by chromosome, start position, and end position
# the user specifies the chromosome as a string, and start and end positions as an integer
# ex. filter_initial_query('10', 40000, 100000)