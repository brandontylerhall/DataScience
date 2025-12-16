# "excel for python"
import pandas as pd
# visualization library
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

# I create a 'Figure' (the window) and 'Axes' (the sub-plots inside the window)
# nrows=1, ncols=2 means "1 row, 2 columns" (side-by-side)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# 'ax=axes[0]' tells seaborn to draw on the LEFT plot
sns.heatmap(titanic.isnull(), yticklabels=False, cbar=False, cmap='viridis', ax=axes[0])
axes[0].set_title('Missing Data: BEFORE Cleaning')

# Drop the 'deck' column (too many missing values)
# axis=1 means "column" (axis=0 would be row)
titanic.drop('deck', axis=1, inplace=True)

# Remove duplicates
# I did this here to avoid deleting duplicates due to imputation
duplicate_count = titanic.duplicated().sum()
print(f"   -> Found {duplicate_count} duplicate rows.")
titanic.drop_duplicates(inplace=True)

# Impute 'age' with the mean
# We calculate the mean first, then fill the holes
average_age = round(titanic['age'].mean(), 2)
titanic['age'] = titanic['age'].fillna(average_age)

# Fill 'embarked' with the mode (most common value)
# mode()[0] grabs the first value (usually 'S' for Southampton)
common_port = titanic['embarked'].mode()[0]
titanic['embarked'] = titanic['embarked'].fillna(common_port)

# B. Fix Data Types
# Convert 'sex' and 'embarked' to Category
# Category is basically changing it to say 0 = male, 1 = female, etc.
titanic['sex'] = titanic['sex'].astype('category')
titanic['embarked'] = titanic['embarked'].astype('category')

# Draw on the RIGHT plot (axes[1])
# titanic.isnull() asks every single cell in the csv if it's empty
sns.heatmap(titanic.isnull(), yticklabels=False, cbar=False, cmap='viridis', ax=axes[1])
axes[1].set_title('Missing Data: AFTER Cleaning')

# --- 6. FINAL VERIFICATION ---
print("\n--- FINAL DATA INFO ---")
print(titanic.info())

# This adjusts the spacing so labels don't overlap
plt.tight_layout()
# Now we call show() only ONCE at the very end
plt.show()

# index=False means we don't save the row numbers (0, 1, 2...) into the file
titanic.to_csv('titanic_clean.csv', index=False)
