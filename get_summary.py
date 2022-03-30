import pandas as pd

dataframe = pd.read_csv("surveys.csv")

desc_weight = dataframe["weight"].describe()
print(desc_weight)