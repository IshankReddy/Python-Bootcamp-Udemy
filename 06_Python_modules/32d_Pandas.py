import pandas as pd
data = pd.read_csv("32_Csv File.csv")
data['Country'] = 'USA'
print(data)