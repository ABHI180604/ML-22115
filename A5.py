import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

thyroid_data = pd.read_excel(r"C:\Users\NISHANTH\Downloads\Lab Session Data.xlsx", sheet_name='thyroid0387_UCI')
print(thyroid_data.dtypes)

categorical_columns = thyroid_data.select_dtypes(include=['object']).columns
numerical_columns = thyroid_data.select_dtypes(include=['int64']).columns

# Display unique values and suggest encoding for categorical columns
for column in categorical_columns:
    unique_values = thyroid_data[column].unique()
    print("Unique values in column", column, " ", unique_values)

    if len(unique_values) < 100:
        print(f"Suggested Encoding: Label Encoding")
        thyroid_data[column] = thyroid_data[column].astype('category').cat.codes
    else:
        print(f"Suggested Encoding: One-Hot Encoding")
        thyroid_data = pd.get_dummies(thyroid_data, columns=[column], prefix=[column])

# Display data range for numerical columns
for column in numerical_columns:
    print("Data range for numeric attributes such as", column, "is", thyroid_data[column].min(), "to", thyroid_data[column].max())

thyroid_data.replace('?', np.nan, inplace=True)

print("Number of missing values in each feature")
missing_values = thyroid_data.isnull().sum()
print(missing_values)

# Plot boxplots to identify outliers in numerical data
print("\nOutliers in Numeric Data:")
for column in numerical_columns:
    sns.boxplot(x=thyroid_data[column])
    plt.title(f"Boxplot for {column}")
    plt.show()

# Display mean and standard deviation for numerical columns
for column in numerical_columns:
    print("Mean and standard deviation for", column, "is", thyroid_data[column].mean(), "and", thyroid_data[column].std())