import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

# df_stockton_ca_1h_2025 = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12621;",
#                                      con=os.getenv('RSR_SVC_CONN'))

# print(df_stockton_ca_1h_2025)


df_stockton_ca_1h_2025 = pd.read_sql("select * from auto.vi_test_summary_unified_reporting tsr join md2.test_types tt using (test_type_id) where tsr.collection_set_id = 12621;",
                                      con=os.getenv('RSR_SVC_CONN'))

print(df_stockton_ca_1h_2025)