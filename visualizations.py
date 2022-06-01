
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import numpy as np
import plotly.graph_objects as go

def plot_lines(data_x, data_s1, data_s2, data_s3):

    x_data = list(range(0, len(data_x)))

    fig = go.Figure()

    fig.add_trace(go.Bar(x=x_data, y=data_s1, name='s1', width=1, marker_color='blue'))

    fig.add_trace(go.Bar(x=x_data, y=data_s1, name='s1', width=1, marker_color='red'))

    fig.add_trace(go.Bar(x=x_data, y=data_s1, name='s1', mode='line+marker' ,marker_color='black'))


    return fig.show()