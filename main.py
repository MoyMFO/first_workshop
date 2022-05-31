
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
print(f"Mediana del tiempo esperado para un nuevo OrderBook: {data_1['median_ts_ob']}")
