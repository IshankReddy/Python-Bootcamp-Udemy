import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('33c_CSV File.csv')

# Create histogram
plt.hist(data['values'], bins=5, alpha=0.7, color='blue')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()