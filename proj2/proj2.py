import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales = pd.read_csv('supermarket_sales.csv')

# Question 1: Which City brings in the most gross income
sns.catplot(kind='bar', x="City", y="gross income", hue="City", estimator=sum, data=sales)

# Question 2: Which Payment method is most popular
sns.catplot(kind='count', x="Payment", data=sales, hue='Payment')

# Question 3: Which Product line gets the best Ratings
sns.catplot(kind="bar", data=sales, x='Product line', y='Rating', hue='Product line')

# Question 4: Who spends more on average: Members or Normies
sns.catplot(kind="bar", x="Customer type", y="Total", hue="Customer type", data=sales)

# Question 5: Which Product line makes the most gross income
sns.catplot(kind="bar", y="Product line", x="gross income", estimator=sum, data=sales, hue="Product line")

# Question 6: Who (Member vs Normal) buys What (Product) and How Much (Total)
sns.catplot(data=sales, kind="bar", x="Total", y="Product line", col="Customer type", errorbar=None, hue="Product line")