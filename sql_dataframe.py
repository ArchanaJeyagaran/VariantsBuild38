from sqlalchemy import Table, Column, Integer, String, MetaData, text, create_engine
from final_format import variant_df

# connect and create SQL dataframe 
engine = create_engine('sqlite:///variant_data.db', echo=True)

conn = engine.connect()

if not engine.dialect.has_table(conn, "variant_data"):
    variant_df.to_sql("variant_data", engine)