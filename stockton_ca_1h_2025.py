import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

df_stockton_ca_1h_2025 = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12621;",
                                     con=os.getenv('RSR_SVC_CONN'))

print(df_stockton_ca_1h_2025)