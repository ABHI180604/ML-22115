import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('future.no_silent_downcasting', True)

# Load the data from the Excel file
thyroid_data = pd.read_excel(r"Lab Session Data.xlsx", sheet_name='thyroid0387_UCI')
thyroid_data.replace('?', np.nan, inplace=True)

# Select numerical columns
numerical_columns = thyroid_data.select_dtypes(include=['int64']).columns

# Impute missing values in numerical columns
for column in numerical_columns:
    if thyroid_data[column].isnull().sum() > 0:
        if thyroid_data[column].skew() < 1:
            thyroid_data[column] = thyroid_data[column].fillna(thyroid_data[column].mean())
            print("Column: {}, Imputation Method: Mean".format(column))
        else:
            thyroid_data[column] = thyroid_data[column].fillna(thyroid_data[column].median())
            print("Column: {}, Imputation Method: Median".format(column))

# Select categorical columns
categorical_columns = thyroid_data.select_dtypes(include=['object']).columns

# Impute missing values in categorical columns
for column in categorical_columns:
    if thyroid_data[column].isnull().sum() > 0:
        thyroid_data[column] = thyroid_data[column].fillna(thyroid_data[column].mode()[0])
        print("Column: {}, Imputation Method: Mode".format(column))