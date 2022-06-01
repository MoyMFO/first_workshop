
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import data as dt
import functions as fn
import numpy as np
import visualizations as vz

# Read input data
data_ob = dt.ob_data

# Cantidad libros de ordenes que hay en total
n_libros = len(list(data_ob.keys()))
print(f"La cantidad total de libros de ordenes es: {n_libros}")

# OrderBook Metrics
data_1 = fn.f_descriptive_ob(data_ob=data_ob) 

# Celda 3
print(f"Mediana del tiempo esperado para un nuevo OrderBook: {data_1['median_ts_ob']}")

# Celda 4
print(f"Mediana del tiempo esperado para un nuevo OrderBook: {data_1['Orderbook Imbalance']}")

# -- Ejercicios de repaso
#data_ob[list(data_ob.keys())[1]]['bid_size'][0]

#libro_0 = data_ob[list(data_ob.keys())[0]].copy()

#libro_0.index = libro_0.index.astype(np.int64)

# Compresion de listas [elemento1, elemento2, elemento3...]
#lista_nueva = [i + 1e3 for i in list(libro_0['bid_size'])]

# Compresion diccionario {"llave 1": objeto, "llave 2": objeto ...}
#llave_nueva = {"llave_"+str(i) : list(libro_0['bid_size'])[i] for i in range(0, len(list(libro_0['bid_size'])))}

# --Plot 1-- #
plot_1 = vz.plot_lines(data_x=list(data_ob.keys()),
                       data_s1=data_1['Orderbook Imbalance'],
                       data_s2=data_1['wighted-Midprice'],
                       data_s3=data_1['VWAP'])
plot_1.show()