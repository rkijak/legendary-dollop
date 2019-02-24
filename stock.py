# test trial with git
# stock_analysis
import pandas as pd
import numpy as np
import datetime as datetime
from pandas_datareader import data as wb


#predefining time
start = datetime.datetime('2015, 2, 10')
end = datetime.datetime('2019, 2, 10')

# Reading in the data with pandas_datareader
petx = wb.DataReader('PETX', 'iex', start, end)
