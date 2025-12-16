import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import viridis

sales = pd.read_csv('supermarket_sales.csv')

# Question 1: Which City brings in the most gross income
city_sales_order = (
    sales.groupby("City")["gross income"]
    .sum()
    .sort_values(ascending=False)
    .index
)

q1 = sns.catplot(
    data=sales,
    kind='bar',
    x="City",
    y="gross income",
    estimator=sum,
    hue="City",
    palette='viridis',
    order=city_sales_order
)
q1.figure.suptitle("Gross Income by City")

# Question 2: Which Payment method is most popular
payment_order = (
    sales["Payment"]
    .value_counts()
    .index
)
q2 = sns.catplot(
    data=sales,
    kind='count',
    x="Payment",
    hue='Payment',
    palette='viridis',
    order=payment_order
)
q2.figure.suptitle("Total Sales By Payment Method")

# Question 3: Which Product line gets the best Ratings
prod_line_rating_order = (
    sales.groupby("Product line")["Rating"]
    .sum()
    .sort_values(ascending=False)
    .index
)
q3 = sns.catplot(
    data=sales,
    kind="bar",
    x='Rating',
    y='Product line',
    hue='Product line',
    palette='viridis',
    order=prod_line_rating_order
)
q3.figure.suptitle("Highest Avg Rating By Product Line")
q3.figure.subplots_adjust(top=0.9)

# Question 4: Who spends more on average: Members or Normies
average_sales_order = (
    sales.groupby("Customer type")["Total"]
    .sum()
    .sort_values(ascending=False)
    .index
)
q4 = sns.catplot(
    data=sales,
    kind="bar",
    x="Customer type",
    y="Total",
    hue="Customer type",
    palette='viridis',
    order=average_sales_order
)
q4.figure.suptitle("Average Sale Total By Customer Type")

# Question 5: Which Product line makes the most gross income
prod_line_gross_order = (
    sales.groupby("Product line")["gross income"]
    .sum()
    .sort_values(ascending=False)
    .index
)
q5 = sns.catplot(
    data=sales,
    kind="bar",
    x="gross income",
    y="Product line",
    estimator=sum,
    hue="Product line",
    palette='viridis',
    order=prod_line_gross_order
)
q5.figure.suptitle("Gross Income by Product Line")
q5.figure.subplots_adjust(top=0.9)

# Question 6: Who (Member vs Normal) buys What (Product) and How Much (Total)
q6 = sns.catplot(
    data=sales,
    kind="bar",
    x="Total",
    y="Product line",
    col="Customer type",
    hue="Gender",
    errorbar=None,
    palette='viridis'
)
q6.figure.suptitle("Total Sales By Customer Type and Product Line", y=1)
q6.figure.subplots_adjust(top=0.9)

plt.show()
