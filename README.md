"Stockton-CA Network Performance Analysis"

Analyzing network performance data for Stockton, CA, using various data visualization techniques and statistical analysis.

Set Up:

Upload the analytics_base.yml.
Activate the virtual enviroment packges running the command $ conda activate analytics_base.

Create a .gitignore file and add the .env file in it.

Create a .env file and add the key access to the database 'root_device_data'

Activate the database adding the db name/host/username/pwd

Wave 01:

Find the test-level data for this half for “Stockton-CA”:

In OpsManger tool find the “Stockton-CA” ID for this half (1hf/2025). 

The data can be retrieved from root_device_data (database), auto(schema), test_summary_reporting (table)

Run the sql to retrieve the data for the collection set:
select * from auto.test_summary_reporting where collection_set_id = 12621; 


Wave 02:

Make box plots for: “task speed median” and "task_speed_5th_percentile" by carrier using the plotly library.

The column “task speed median” is in the root_device_data (database), md2(schema), test_types(table).

Join the test_types tabes with test_summary_unified_reporting table by ID.
"select * from auto.vi_test_summary_unified_reporting tsr join md2.test_types tt using (test_type_id) where tsr.collection_set_id = 12621;"


Wave 03:

Add the dictionary with the carrier colors as key and improve the plots visualization.

carrier_color_dict = {
                        'Verizon': '#b00000',
                        'AT&T': '#067ab4',
                        'T-Mobile': '#e60076',
                        'Sprint': '#ffaa00',
                        'Dish': '#3F3F3F',
                        'EE': '#2e9b9d',
                        'O2': '#010066',
                        'Three': '#000000',
                        'Vodafone': '#f80000',
                        'O2 UK': '#010066',
                        'Three UK': '#000000',
                        'Vodafone UK': '#f80000',
                        'Sunrise': '#d0606f',
                        'Swisscom': '#5b92cc',
                        'Salt': '#56bf83',
                        'ODIDO': '#FF7621',
                        'KPN': '#FFBB00',
                        'Vodafone NL': '#f80000',
                        'KT': '#FF7621',
                        'SK Telecom': '#FFBB00',
                        'LG U+': '#f80000',
                     }


Wave 04:

Make one box plot for each carrier in the carrier colors for the download test.

Then make a few more “distribution” plots (e.g. swarm, strip, etc) using seaborn. In particular an “ecdf”.

Wave 05:

Interpret the CDF in terms of “quantiles” and understand what that means.

