import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

#Query to  retrieve test_summary_unified_reporting table by colletion set ID.
df_stockton_ca_1h_2025 = pd.read_sql("select * from auto.test_summary_reporting where collection_set_id = 12621;",
                                     con=os.getenv('RSR_SVC_CONN'))

# print(df_stockton_ca_1h_2025)

#Query to join the test_types tabes with test_summary_unified_reporting table by ID.
df_stockton_ca_1h_2025 = pd.read_sql("select * from auto.vi_test_summary_unified_reporting tsr join md2.test_types tt using (test_type_id) where tsr.collection_set_id = 12621;",
                                      con=os.getenv('RSR_SVC_CONN'))

print(df_stockton_ca_1h_2025)

#Query to select only AT&T carrier.
df_stockton_ca_1h_2025_ATandT = pd.read_sql("select * from auto.vi_test_summary_unified_reporting tsr join md2.test_types tt using (test_type_id) where tsr.collection_set_id = 12621 and tsr.carrier= 'AT&T';",
                                      con=os.getenv('RSR_SVC_CONN'))

#Query to select only Dish carrier.
df_stockton_ca_1h_2025_Dish = pd.read_sql("select * from auto.vi_test_summary_unified_reporting tsr join md2.test_types tt using (test_type_id) where tsr.collection_set_id = 12621 and tsr.carrier= 'Dish';",
                                      con=os.getenv('RSR_SVC_CONN'))

#Query to select only T-Mobile carrier.
df_stockton_ca_1h_2025_T_Mobile = pd.read_sql("select * from auto.vi_test_summary_unified_reporting tsr join md2.test_types tt using (test_type_id) where tsr.collection_set_id = 12621 and tsr.carrier= 'T-Mobile';",
                                      con=os.getenv('RSR_SVC_CONN'))

#Query to select only Verizon carrier.
df_stockton_ca_1h_2025_Verizon = pd.read_sql("select * from auto.vi_test_summary_unified_reporting tsr join md2.test_types tt using (test_type_id) where tsr.collection_set_id = 12621 and tsr.carrier= 'Verizon';",
                                      con=os.getenv('RSR_SVC_CONN'))