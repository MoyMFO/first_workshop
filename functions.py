
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import pandas as pd
import numpy as np
import data as dt 

# Read input data
data_ob = dt.ob_data

# ======================================================================================================== #
def f_descriptive_ob(data_ob:dict) -> dict:

    """
    Parameters 
    ----------

    data_ob: dict (default: None)
        Datos de entrada del libro de ordenes, es un diccionario con la siguiente estructura:
        'timestamp': objeto tipo timestamp reconocible por maquina, e.g. pd.to_datetime()
        'bid_size': volume de niveles bid
        'bid': precio de niveles bid
        'ask': precio de niveles ask
    
    Returns
    -------
        r_data: dict
            Diccionario con las metricas calculas 
            'median_ts_ob': float 
            'spread':float

    """


    # -- Median Time of OrderBook update -- #
    ob_ts = list(data_ob.keys())
    l_ts = [pd.to_datetime(i_ts) for i_ts in ob_ts]
    ob_m1 = np.median([l_ts[n_ts + 1] - l_ts[n_ts] for n_ts in range(0, len(l_ts)-1)]).total_seconds() * 1000
    print(ob_m1)

    # -- Spread, Midprice -- #
    ob_m2 = [data_ob[ob_ts[0]]['ask'][0] - data_ob[ob_ts[0]]['bid'][0] for i in range(0, len(ob_ts))]
    ob_m3 = [(data_ob[ob_ts[0]]['ask'][0] + data_ob[ob_ts[0]]['bid'][0])*0.5 for i in range(0, len(ob_ts))]

    # -- No. Price Levels -- #
    ob_m4 = [data_ob[i_ts].shape[0] for i_ts in ob_ts]
    # -- Bid_Volume, Ask_Volume, Total_Volume
    ob_m5 = [np.round(data_ob[i_ts]['bid_size'].sum(), 6) for i_ts in ob_ts]
    ob_m6 = [np.round(data_ob[i_ts]['ask_size'].sum(), 6) for i_ts in ob_ts]
    ob_m7 = [np.round(data_ob[i_ts]['bid_size'].sum() + data_ob[i_ts]['ask_size'].sum(), 6) for i_ts in ob_ts]

    # -- OrderBook Imbalance (v: volume, d: depth) -- #
    obimb = lambda v, d: np.sum(v[0][:d])/np.sum([v[0][:d], v[1][:d]])


    r_data = {'median_ts_ob': ob_m1, 'spread': ob_m2, 'midprice': ob_m3}

    return r_data
"""
numero = []
for i in range():
    numero.append(obimb(v=data_1[i], d=10))
df_data['ob_imb'] = numero
df_data['ob_imb'] = [obimb(v=data_1, d=10) for renglon in todo_dataframe]    
"""

# Time of orderbook update
# Spread, Midprice
# No. Price levels
# Bid_Volume, Ask_Volume, Total-Volume
