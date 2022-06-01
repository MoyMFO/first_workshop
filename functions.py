
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
    # v[0] Bid volume, v[1] Ask volume 
    obimb = lambda v, d: np.sum(v.iloc[:d,0])/np.sum([v.iloc[:d,0], v.iloc[:d,1]])
    ob_m8 = [obimb(data_ob[i_ts][['bid_size','ask_size']],len(data_ob[i_ts])) for i_ts in ob_ts]

    # -- wighted-Midprice (p: price, v: volume)
    w_midprice = lambda p, v: (v.iloc[:,1]/np.sum([v.iloc[:,0], v.iloc[:,1]]))*p.iloc[:,0] + (v.iloc[:,0]/np.sum([v.iloc[:,0], v.iloc[:,1]]))*p.iloc[:,1]
    # ob_m9  = [w_midprice(data_ob[i_ts][['bid','ask']], data_ob[i_ts][['bid_size', 'ask_size']]) for i_ts in ob_ts]
    ob_m9 = [ob_m8[i_ts] * ob_m3[i_ts] for i_ts in range(0, len(ob_ts))]

    # -- VWAP (Volume-Weighted Average Price) (p: price, v: volume, d:depth)
    # p[0]:Bid price, p[1]:Ask price, v[0]: Bid volume, v[1]: Ask volume
    vwap = lambda p, v, d: np.sum(p.iloc[:d, 0] * v.iloc[:d,0] + p.iloc[:d,1] * v.iloc[:d,1]) / np.sum(v.iloc[:d,0] + v.iloc[:d,1])
    ob_m10 = [vwap(data_ob[i_ts][['bid', 'ask']], data_ob[i_ts][['bid_size', 'ask_size']], len(data_ob[i_ts])) for i_ts in ob_ts]

    r_data = {'median_ts_ob': ob_m1, 'spread': ob_m2, 'midprice': ob_m3, "Orderbook Imbalance": ob_m8, 
              'wighted-Midprice': ob_m9,'VWAP': ob_m10}

    return r_data


# -- OrderBook Imbalance (v: volume, d: depth) -- #
# v[0] Bid volume, v[1] Ask volume 
#obimb = lambda v, d: np.sum(v.iloc[:d,0])/np.sum([v.iloc[:d,0], v.iloc[:d,1]])
#ob_m8 = [obimb(data_ob[i_ts][['bid_size','ask_size']],2) for i_ts in ob_ts]

# -- wighted-Midprice (p: price, v: volume)
#w_midprice = lambda p, v: (v[1]/np.sum([v[0], v[1]]))*p[0] + (v[0]/np.sum([v[0], v[1]]))*p[1]
#w_midprice = lambda p, v: (v.iloc[:,1]/np.sum([v.iloc[:,0], v.iloc[:,1]]))*p.iloc[:,0] + (v.iloc[:,0]/np.sum([v.iloc[:,0], v.iloc[:,1]]))*p.iloc[:,1]
#ob_m9  = [w_midprice(data_ob[i_ts][['bid','ask']], data_ob[i_ts][['bid_size', 'ask_size']]) for i_ts in ob_ts]


# -- VWAP (Volume-Weighted Average Price) (p: price, v: volume, d:depth)
# p[0]:Bid price, p[1]:Ask price, v[0]: Bid volume, v[1]: Ask volume
#vwap = lambda p, v, d: np.sum(p[0][:d] * v[0][:d] + p[1][:d] * v[1][:d]) / np.sum(v[0][:d] + v[1][:d])
#vwap = lambda p, v, d: np.sum(p.iloc[:d, 0] * v.iloc[:d,0] + p.iloc[:d,1] * v.iloc[:d,1]) / np.sum(v.iloc[:d,0] + v.iloc[:d,1])
#ob_10 = [vwap(data_ob[i_ts][['bid', 'ask']], data_ob[i_ts][['bid_size', 'ask_size']], 10) for i_ts in ob_ts]
#ob_10




"""
numero = []
for i in range():
    numero.append(obimb(v=data_1[i], d=10))
df_data['ob_imb'] = numero
df_data['ob_imb'] = [obimb(v=data_1, d=10) for renglon in todo_dataframe]    

"""
