# -*- coding: utf-8 -*-
"""ACPS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kOyJaEYgfIMmo_w5KrSrSgFPUzmLV4H6
"""

pip install rtamt

import pandas as pd
df = pd.read_csv('trace_0.csv')
df

import sys
import rtamt

def monitor():

    y_values = df[['t', 'y']].values.tolist()

    spec = rtamt.StlDenseTimeSpecification()
    spec.name = 'Obstacle Avoidance'
    spec.declare_var('y', 'float')
    #spec.declare_var('gnt', 'float')
    #spec.declare_var('out', 'float')
    #spec.set_var_io_type('req', 'input')
    #spec.set_var_io_type('gnt', 'output')
    #spec.spec = 'out = (req>=3) implies (eventually[0:5](gnt>=3))'
    spec.spec = 'G[0, 60](y <= 4.5)'
    try:
        spec.parse()
    except rtamt.RTAMTException as err:
        print('RTAMT Exception: {}'.format(err))
        sys.exit()

    rob = spec.evaluate(['y', y_values])

    print('Robustness: {}'.format(rob))

if __name__ == '__main__':
    # Process arguments
    monitor()

pip install ydata-synthetic[streamlit]
