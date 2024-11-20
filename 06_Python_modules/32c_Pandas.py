import pandas as pd
data = pd.read_csv("32_Csv File.csv")
filtered_data = data[data['Age'] > 28]
print(filtered_data)