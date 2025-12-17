import pandas as pd

sales = pd.read_csv('supermarket_sales.csv')


def show_analysis(title, df_summary):
    print(f"\n--- {title} ---")
    print(df_summary.to_string(float_format="{:,.2f}".format))
    print("-" * 30)


# Question 1: Which City brings in the most gross income
city_income_df = (
    sales.groupby("City")["gross income"]
    .sum()
    .sort_values(ascending=False)
)

# Question 2: Which Payment method is most popular
payment_counts = sales['Payment'].value_counts()
show_analysis("Transaction Counts by Payment Method", payment_counts)

# Question 3: Which Product line gets the best average Ratings
prod_line_rating_df = (
    sales.groupby("Product line")["Rating"]
    .mean()
    .sort_values(ascending=False)
)
show_analysis('Which Product line gets the best average Ratings', prod_line_rating_df)

# Question 4: Who spends more on average: Members or Normies
average_sales_df = (
    sales.groupby("Customer type")["Total"]
    .mean()
    .sort_values(ascending=False)
)
show_analysis('Who spends more on average: Members or Normies', average_sales_df)

# Question 5: Which Product line makes the most gross income
prod_line_gross_df = (
    sales.groupby("Product line")["gross income"]
    .sum()
    .sort_values(ascending=False)
)
show_analysis('Which Product line makes the most gross income', prod_line_gross_df)

# Question 6: Who (Member vs Normal) buys What (Product) and How Much (Total)
q6_analysis = (
    sales.groupby(["Customer type", "Product line", "Gender"])["Total"]
    .mean()
    # .sum() # <--- Switch to this if you want "Total Money Spent" instead of "Average Receipt"
)
show_analysis('Who (Member vs Normal) buys What (Product) and How Much (Total)', q6_analysis)
