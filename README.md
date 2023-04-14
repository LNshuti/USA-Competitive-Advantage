# USA-Competitive-Advantage
Use data from the World Bank, Federal Reserve and Altas for Economic Complexity to Trade relationships between the US and Allies. 


```python
# Compare USA and China Demographics
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns

# Set up seaborn with colorblind-friendly palette and larger font size
sns.set(style="whitegrid", palette="colorblind", font_scale=1.5)

data = """
Year,Population of China,Annual Growth Rate of China (%),Population of the United States,Annual Growth Rate of the United States (%)
2010,1359859000,0.53,309349000,0.70
2011,1364921000,0.37,311718000,0.77
2012,1368558000,0.27,314058000,0.75
2013,1371495000,0.21,316204000,0.68
2014,1375388000,0.28,318563000,0.74
2015,1378665000,0.24,320897000,0.73
2016,1381963000,0.24,323128000,0.70
2017,1386050000,0.30,325719000,0.80
2018,1390094000,0.29,327170000,0.45
2019,1397175000,0.51,328240000,0.33
"""

# Load the data into a pandas DataFrame
data_string = StringIO(data)
df = pd.read_csv(data_string)

# Plot the line chart
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(df['Year'], df['Population of China'], label='Population of China', linewidth=3)
ax1.plot(df['Year'], df['Population of the United States'], label='Population of the United States', linewidth=3)
ax1.set_xlabel('Year')
ax1.set_ylabel('Population')

ax2 = ax1.twinx()
ax2.plot(df['Year'], df['Annual Growth Rate of China (%)'], label='Annual Growth Rate of China (%)', linestyle='--', linewidth=3)
ax2.plot(df['Year'], df['Annual Growth Rate of the United States (%)'], label='Annual Growth Rate of the United States (%)', linestyle='--', linewidth=3)
ax2.set_ylabel('Annual Growth Rate (%)')

# Combine legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Set the title and show the plot
plt.title('Population and Annual Growth Rate Comparison\nChina vs United States (2010-2019)')
plt.show()
```

![image](https://user-images.githubusercontent.com/13305262/231587556-d64f792e-15fb-472a-a17c-ea6d762a4ce8.png)

**Trade relationship**
----------------------

**Imports**
-----------

![image](https://user-images.githubusercontent.com/13305262/231326784-68aa4684-0841-43e4-a0ae-49e485eff4c9.png)


![image](https://user-images.githubusercontent.com/13305262/231327133-402ab1f8-7bf7-4aa5-9642-2944e22aad09.png)

**Exports**
-----------

![image](https://user-images.githubusercontent.com/13305262/231329056-a465b243-d92c-473f-a877-d3b02bb3652a.png)

![image](https://user-images.githubusercontent.com/13305262/231329260-877b3c33-93d5-4035-bd70-be99c07bbc80.png)

## References
-------------
1. https://atlas.cid.harvard.edu/
