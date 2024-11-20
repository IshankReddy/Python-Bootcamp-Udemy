import pandas as pd
data = pd.read_csv("32_Csv File.csv")
stats = data['Age'].describe()
print(stats)