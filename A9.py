import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity

# Load the data from the Excel file
thyroid_data = pd.read_excel(r"C:\Users\NISHANTH\Downloads\Lab Session Data.xlsx", sheet_name='thyroid0387_UCI')
thyroid_data.replace('?', np.nan, inplace=True)

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
        vector1 = thyroid_data.iloc[0].values.reshape(1, -1)
        vector2 = thyroid_data.iloc[1].values.reshape(1, -1)

        # Calculate cosine similarity between the two vectors
        cosine_similarity_score = cosine_similarity(vector1, vector2)[0][0]

        print("Cosine Similarity:", cosine_similarity_score)