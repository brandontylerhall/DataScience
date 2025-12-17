import pandas as pd

sales = pd.read_csv('supermarket_sales.csv')


def show_analysis(title, df_summary):
    print(f"\n--- {title} ---")
    print(df_summary.to_string(float_format="{:,.2f}".format))
    print("-" * 30)


"""
*** TERMINOLOGY / ACRONYMS ***
GI - Gross Income
PL - Product Line
PM - Payment Method
"""

# Question 1: Which City brings in the most GI
city_income_df = (
    sales.groupby("City")["gross income"]
    .sum()
    .sort_values(ascending=False)
)

city_income_diff1 = ((city_income_df.iloc[0] - city_income_df.iloc[1]) / city_income_df.iloc[1]) * 100
city_income_diff2 = ((city_income_df.iloc[0] - city_income_df.iloc[2]) / city_income_df.iloc[2]) * 100

# City's GI by PL
city_gi_by_pl_df = (
    sales.groupby(['City', 'Product line'])['gross income']
    .sum()
    .reset_index()
    .sort_values(by=['City', 'gross income'], ascending=[True, False])
    .set_index(['City', 'Product line'])
)


def city_gi_by_pl_deep_analysis():
    atl, atl_pl = city_gi_by_pl_df.index[0]
    atl_percentage = (city_gi_by_pl_df.iloc[0, 0] / city_income_df[atl]) * 100
    print(f"{atl}'s top PL was '{atl_pl}' which contributed to {atl_percentage:.2f}% of the city's annual GI")
    bos, bos_pl = city_gi_by_pl_df.index[6]
    bos_percentage = (city_gi_by_pl_df.iloc[6, 0] / city_income_df[bos]) * 100
    print(f"{bos}'s top PL was '{bos_pl}' which contributed to {bos_percentage:.2f}% of the city's annual GI")
    chi, chi_pl = city_gi_by_pl_df.index[12]
    chi_percentage = (city_gi_by_pl_df.iloc[12, 0] / city_income_df[chi]) * 100
    print(f"{chi}'s top PL was '{chi_pl}' which contributed to {chi_percentage:.2f}% of the city's annual GI")


# Question 2: Which PM is most popular
payment_counts = sales['Payment'].value_counts()

# Question 3: Which Product line gets the best average Ratings
prod_line_rating_df = (
    sales.groupby("Product line")["Rating"]
    .mean()
    .sort_values(ascending=False)
)

# Question 4: Who spends more on average: Members or Normies
average_sales_df = (
    sales.groupby("Customer type")["Total"]
    .mean()
    .sort_values(ascending=False)
)

# Question 5: Which Product line makes the most gross income
prod_line_gross_df = (
    sales.groupby("Product line")["gross income"]
    .sum()
    .sort_values(ascending=False)
)

# Question 6: Who (Member vs Normal) buys What (Product) and How Much (Total)
q6_analysis = (
    sales.groupby(["Customer type", "Product line", "Gender"])["Total"]
    .mean()
    # .sum() # <--- Switch to this if you want "Total Money Spent" instead of "Average Receipt"
)

show_analysis('GI by city', city_income_df)
print(f"{city_income_df.index[0]} made {city_income_diff1:,.2f}% more than {city_income_df.index[1]} and {city_income_diff2:,.2f}% more than {city_income_df.index[2]}.")
show_analysis('Which PL makes the most GI across all cities', prod_line_gross_df)
show_analysis('City GI by PL', city_gi_by_pl_df)
city_gi_by_pl_deep_analysis()
show_analysis('Which PL gets the best average ratings across all cities', prod_line_rating_df)
show_analysis("Transaction Counts by PM across all cities", payment_counts)
show_analysis('Who spends more on average: Members or Normies all cities', average_sales_df)
show_analysis('Who (Member vs Normal) buys What (PL) and how much (Total) all cities', q6_analysis)
