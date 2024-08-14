import pandas as pd
import numpy as np

# Load the thyroid data from the Excel file
thyroid_data = pd.read_excel(r"Lab Session Data.xlsx", sheet_name='thyroid0387_UCI')
thyroid_data.replace('?', np.nan, inplace=True)
print("For thyroid sheet")

# Identify binary columns
binary_columns_thyroid = [col for col in thyroid_data.columns if set(thyroid_data[col].dropna().unique()) <= {'t', 'f'}]
binary_columns_thyroid += [col for col in thyroid_data.columns if set(thyroid_data[col].dropna().unique()) <= {'M', 'F'}]

# Replace binary values with 1 and 0
thyroid_data[binary_columns_thyroid] = thyroid_data[binary_columns_thyroid].replace({'t': 1, 'f': 0, 'M': 1, 'F': 0})

# Extract binary data for comparison
thyroid_v1 = thyroid_data.loc[0, binary_columns_thyroid].astype(int)
thyroid_v2 = thyroid_data.loc[1, binary_columns_thyroid].astype(int)

# Calculate Jaccard Coefficient (JC) and Simple Matching Coefficient (SMC) for thyroid data
f11_thyroid = np.sum((thyroid_v1 == 1) & (thyroid_v2 == 1))
f00_thyroid = np.sum((thyroid_v1 == 0) & (thyroid_v2 == 0))
f10_thyroid = np.sum((thyroid_v1 == 1) & (thyroid_v2 == 0))
f01_thyroid = np.sum((thyroid_v1 == 0) & (thyroid_v2 == 1))

jaccard_coefficient_thyroid = f11_thyroid / (f01_thyroid + f10_thyroid + f11_thyroid)
simple_matching_coefficient_thyroid = (f11_thyroid + f00_thyroid) / (f00_thyroid + f01_thyroid + f10_thyroid + f11_thyroid)

print("Jaccard Coefficient (JC):", jaccard_coefficient_thyroid)
print("Simple Matching Coefficient (SMC):", simple_matching_coefficient_thyroid)

# Load the marketing data from the Excel file
marketing_data = pd.read_excel(r"Lab Session Data.xlsx", sheet_name='marketing_campaign')
marketing_data.replace('?', np.nan, inplace=True)
print("For marketing sheet")

# Identify binary columns in marketing data
binary_columns_marketing = [col for col in marketing_data.columns if set(marketing_data[col].dropna().unique()) <= {0, 1}]

# Extract binary data for comparison
marketing_v1 = marketing_data.loc[0, binary_columns_marketing].astype(int)
marketing_v2 = marketing_data.loc[1, binary_columns_marketing].astype(int)

# Calculate Jaccard Coefficient (JC) and Simple Matching Coefficient (SMC) for marketing data
f11_marketing = np.sum((marketing_v1 == 1) & (marketing_v2 == 1))
f00_marketing = np.sum((marketing_v1 == 0) & (marketing_v2 == 0))
f10_marketing = np.sum((marketing_v1 == 1) & (marketing_v2 == 0))
f01_marketing = np.sum((marketing_v1 == 0) & (marketing_v2 == 1))

jaccard_coefficient_marketing = f11_marketing / (f01_marketing + f10_marketing + f11_marketing)
simple_matching_coefficient_marketing = (f11_marketing + f00_marketing) / (f00_marketing + f01_marketing + f10_marketing + f11_marketing)

print("Jaccard Coefficient (JC):", jaccard_coefficient_marketing)
print("Simple Matching Coefficient (SMC):", simple_matching_coefficient_marketing)