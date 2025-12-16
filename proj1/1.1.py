# "excel for python"
import pandas as pd
# visualization library
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

print(titanic.info())
# titanic.isnull() asks every single cell in the csv if it's empty
sns.heatmap(titanic.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.show()