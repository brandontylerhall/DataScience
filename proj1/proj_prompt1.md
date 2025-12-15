# Mini-Project 2: Titanic Data Cleaning Challenge

## **Overview**
This project focuses on the most critical (and often most time-consuming) skill in data science: **Data Cleaning**. You will be working with the famous Titanic passenger survival dataset. This dataset is messy by design, containing missing values, inconsistent data types, and potential duplicates, making it the perfect sandbox for mastering preprocessing techniques.

## **Learning Objectives**
By the end of this project, you will be able to:
- **Identify & Handle Missing Data:** Decide when to drop rows versus when to impute values.
- **Manage Duplicates:** Detect and remove redundant entries to ensure data integrity.
- **Standardize Data Types:** Convert categorical and string data into formats usable for analysis.
- **Validation:** Understand the impact of cleaning on dataset quality.

## **Resources & Data**
- **Dataset:** Titanic Passenger Survival Data (~890 rows, 12 columns).
- **Access:** Download via [Kaggle](https://www.kaggle.com/c/titanic/data) or load directly using the Python `seaborn` library (`sns.load_dataset('titanic')`).

## **Structured Workflow**
Follow these steps to complete your data cleaning pipeline:

### 1. Data Loading & Inspection
- Import necessary libraries (Pandas, NumPy, Seaborn/Matplotlib).
- Load the dataset into a DataFrame.
- Display the first 5 rows and use `.info()` and `.describe()` to get an initial overview of data types and null counts.

### 2. Handling Missing Values
- **Visualizing Gaps:** Create a heatmap or bar chart to visualize where data is missing (specifically in the `Age`, `Cabin`, and `Embarked` columns).
- **Imputation vs. Dropping:**
  - For `Age`: Impute missing values (e.g., use the mean or median age).
  - For `Cabin`: Analyze if this column has too many missing values to be useful and consider dropping it.
  - For `Embarked`: Fill missing rows with the mode (most common value).

### 3. Cleaning & Formatting
- **Duplicate Check:** Check for and remove any duplicate rows.
- **Type Conversion:** Ensure categorical columns (like `Sex` or `Embarked`) are the correct data type (category or object) and numerical columns are integers or floats.

### 4. Final Review
- Run a final check using `.isnull().sum()` to ensure no missing values remain.
- Print the shape of your cleaned DataFrame to compare it with the original raw data.