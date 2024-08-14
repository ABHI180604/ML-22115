import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the Excel file
thyroid_data = pd.read_excel(r"C:\Users\NISHANTH\Downloads\Lab Session Data.xlsx", sheet_name='thyroid0387_UCI')
thyroid_data.replace('?', np.nan, inplace=True)

# Identify binary columns
binary_columns = [col for col in thyroid_data.columns if set(thyroid_data[col].dropna().unique()) <= {'t', 'f'}]
binary_columns += [col for col in thyroid_data.columns if set(thyroid_data[col].dropna().unique()) <= {'M', 'F'}]

# Convert binary values to 0 and 1
thyroid_data[binary_columns] = thyroid_data[binary_columns].replace({'t': 1, 'f': 0, 'M': 1, 'F': 0})

# Initialize a dictionary to hold label encoders for categorical columns
label_encoders = {}

# Process categorical columns
for categorical_column in thyroid_data.select_dtypes(include=['object']).columns:
    if thyroid_data[categorical_column].isnull().sum() > 0:
        # Fill missing values with the mode of the column
        mode_value = thyroid_data[categorical_column].mode()[0]
        thyroid_data[categorical_column] = thyroid_data[categorical_column].fillna(mode_value)
    le = LabelEncoder()
    thyroid_data[categorical_column] = le.fit_transform(thyroid_data[categorical_column])
    label_encoders[categorical_column] = le

# Process numerical columns
for numerical_column in thyroid_data.select_dtypes(include=[np.number]).columns:
    if thyroid_data[numerical_column].isnull().sum() > 0:
        # Fill missing values with the mean of the column
        mean_value = thyroid_data[numerical_column].mean()
        thyroid_data[numerical_column] = thyroid_data[numerical_column].fillna(mean_value)

# Select a subset of the data for analysis
subset_data = thyroid_data.iloc[:20]

# Initialize matrices for Jaccard, Simple Matching, and Cosine Similarity
jaccard_matrix = np.zeros((20, 20))
simple_matching_matrix = np.zeros((20, 20))
cosine_similarity_matrix = np.zeros((20, 20))

# Compute similarity measures
for i in range(20):
    for j in range(20):
        if i != j:
            vector_i = subset_data.iloc[i, :].values
            vector_j = subset_data.iloc[j, :].values

            binary_vector_i = subset_data.loc[i, binary_columns].astype(int)
            binary_vector_j = subset_data.loc[j, binary_columns].astype(int)

            f11 = np.sum((binary_vector_i == 1) & (binary_vector_j == 1))
            f00 = np.sum((binary_vector_i == 0) & (binary_vector_j == 0))
            f10 = np.sum((binary_vector_i == 1) & (binary_vector_j == 0))
            f01 = np.sum((binary_vector_i == 0) & (binary_vector_j == 1))

            jaccard_matrix[i, j] = f11 / (f01 + f10 + f11)
            simple_matching_matrix[i, j] = (f11 + f00) / (f00 + f01 + f10 + f11)

            reshaped_vector_i = vector_i.reshape(1, -1)
            reshaped_vector_j = vector_j.reshape(1, -1)
            cosine_similarity_matrix[i, j] = cosine_similarity(reshaped_vector_i, reshaped_vector_j)[0][0]

# Plot the similarity matrices
fig, axs = plt.subplots(1, 3, figsize=(20, 6))

sns.heatmap(jaccard_matrix, annot=True, cmap='viridis', ax=axs[0])
axs[0].set_title('Jaccard Coefficient (JC)')

sns.heatmap(simple_matching_matrix, annot=True, cmap='viridis', ax=axs[1])
axs[1].set_title('Simple Matching Coefficient (SMC)')

sns.heatmap(cosine_similarity_matrix, annot=True, cmap='viridis', ax=axs[2])
axs[2].set_title('Cosine Similarity (COS)')

plt.show()