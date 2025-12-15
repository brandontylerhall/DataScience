import pandas as pd
import numpy as np
import seaborn as sns

iris = sns.load_dataset("iris")

### Explore Structure ###
# First 5 rows
# print(iris.head())
# Data types, non-null counts
# print(iris.info())
# Statistical summary
# print(iris.describe())
# Dimensions
# print(iris.shape)
# Column names
# print(iris.columns)

### Basic Selection ###
# Access single column
# sepal_length = iris['sepal_length']
# print(sepal_length)
# Access by position
# first_10_rows = iris.iloc[:10]
# print(first_10_rows)
# Boolean filtering
# species_virginica = iris[iris['species'] == 'virginica']
# print(species_virginica)

### Compute basic statistics ###
# mean_sepal = iris['sepal_length'].mean()
# print(f'sepal mean:', mean_sepal)
# median_petal = iris['petal_length'].median()
# print(f'median petal:', median_petal)
