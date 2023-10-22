# import matplotlib.pyplot as plt
# import numpy as py
import pandas as pd
# from sklearn.linear_model import LinearRegression


# Download and prepare the data
data_root = "https://github.com/ageron/data/raw/main"
lifesat = pd.read_csv(data_root + "lifesat/lifesat.csv")
x = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

print(x, y)
