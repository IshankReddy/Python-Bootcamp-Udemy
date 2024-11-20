import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('33b_CSV File.csv')

# Create bar chart
plt.bar(data['category'], data['value'])
plt.title('Bar Chart Example')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()
