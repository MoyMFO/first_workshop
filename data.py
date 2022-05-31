
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""


import pandas as pd
import numpy as np
import json

# load file
f = open("orderbooks_05jul21.json")

# Convert JSON into Dictionary
orderbooks_data = json.load(f)
ob_data = orderbooks_data["bitfinex"]

#Drop None Keys
ob_data = {i_key: i_value for i_key, i_value in ob_data.items() if i_value is not None}

#Convert to DataFrame and rearange columns
ob_data = {i_ob: pd.DataFrame(ob_data[i_ob])[['bid_size','bid','ask','ask_size']]
          if  ob_data[i_ob] is not None else None for i_ob in list(ob_data.keys())}


# For largo
#i_count = 0
#l_data = []
#for i_data in ob_data.values():
#    i_count += 1
#    if i_data is None:
#        print(i_data)
#        l_data.append(i_count)

