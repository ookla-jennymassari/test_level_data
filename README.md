# test_level_data

1- See if you can get the test-level data for this half for “Stockton-CA”. Then make a box plot of “task speed median” (or the 5th percentile task speed - this 05p will give you zero rows, why?), for the download test, with one box plot for each carrier in the carrier colors. Then make a few more “distribution” plots (e.g. swarm, strip, etc) using seaborn (not sure what you used before). In particular an “ecdf”. See if you can interpret the CDF in terms of “quantiles” and understand what that means… feel free to ask anything but google is your friend. if you get stuck i can give you some code.

2- Here’s dictionary with the carrier colors as key to help you out
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

Set Up:

Upload the analytics_base.yml.
Activate the virtual enviroment packges running the command $ conda activate analytics_base.

Create a .gitignore file and add the .env file in it.

Create a .env file and add the key access to the database 'root_device_data'

Activate the database adding the db name/host/username/pwd

Wave 01:

Find the test-level data for this half for “Stockton-CA”:

In OpsManger tool find the “Stockton-CA” ID for this half (1hf/2025). 

Run the sql to retrieve the data for the collection set:
select * from auto.test_summary_reporting where collection_set_id = 12621; 


Wave 02:

Make a box plot of “task speed median” (or the 5th percentile task speed - this 05p will give you zero rows, why?).