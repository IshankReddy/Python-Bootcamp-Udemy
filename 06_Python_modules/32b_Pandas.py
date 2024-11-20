import pandas as pd
data = pd.read_csv("32_Csv File.csv")
selected_columns = data[['Name', 'City']]
print(selected_columns)