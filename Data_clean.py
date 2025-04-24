import numpy as np
import pandas as pd

data = './datasets/Kangaroo.csv'
data_set = pd.read_csv(data, sep = ',')


print (data_set.info())