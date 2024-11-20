import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('33a_CSV File.csv')

# Create line plot
plt.plot(data['x'], data['y'])
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()