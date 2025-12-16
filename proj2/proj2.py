import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales = pd.read_csv('supermarket_sales.csv')

# Question 1: Which City brings in the most gross income
q1 = sns.catplot(
    data=sales,
    kind='bar',
    x="City",
    y="gross income",
    estimator=sum,
    hue="City"
)

# Question 2: Which Payment method is most popular
q2 = sns.catplot(
    data=sales,
    kind='count',
    x="Payment",
    hue='Payment'
)

# Question 3: Which Product line gets the best Ratings
q3 = sns.catplot(
    data=sales,
    kind="bar",
    x='Rating',
    y='Product line',
    hue='Product line'
)

# Question 4: Who spends more on average: Members or Normies
q4 = sns.catplot(
    data=sales,
    kind="bar",
    x="Customer type",
    y="Total",
    hue="Customer type"
)

# Question 5: Which Product line makes the most gross income
q5 = sns.catplot(
    data=sales,
    kind="bar",
    x="gross income",
    y="Product line",
    estimator=sum,
    hue="Product line"
)

# Question 6: Who (Member vs Normal) buys What (Product) and How Much (Total)
q6 = sns.catplot(
    data=sales,
    kind="bar",
    x="Total",
    y="Product line",
    col="Customer type",
    hue="Product line",
    errorbar=None
)

plt.show()