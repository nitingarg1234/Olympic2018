import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
df = pd.read_csv("Medal_table.csv")
df = df.head(10)

NOC,GOLD,SILVER,BRONZE = df['NOC'].values , df['GOLD'].values , df['SILVER'].values , df['BRONZE'].values

# multiple line plot
plt.plot( NOC, GOLD,  marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4, label="GOLD")
plt.plot( NOC, SILVER,  marker='', color='olive', linewidth=2, label="SILVER")
plt.plot( NOC, BRONZE,  marker='', color='olive', linewidth=2, linestyle='dashed', label="BRONZE")
plt.legend()
plt.xticks(rotation=45)
plt.title('Medal Tally of top 10 countries')
plt.show()
