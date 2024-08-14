import pandas as pd
import numpy as np

# Use forward slashes in the file path or use raw string
s = r"C:\Users\NISHANTH\PycharmProjects\q1\Lab Session Data.xlsx"

# Load the correct sheet name
data = pd.read_excel(s, sheet_name='Purchase data')

# Extract relevant columns for matrix A
A = data[['Candies (#)', 'Mangoes (Kg)','Milk Packets (#)']].dropna()

# Extract relevant columns for matrix C
C = data[['Payment (Rs)']].dropna()

# Convert to NumPy array
A_matrix = A.to_numpy()

# Convert to NumPy array
C_matrix = C.to_numpy()

# Print the matrix
row = A_matrix.shape[0]
col = A_matrix.shape[1]

print(A_matrix)
print(f"The Matrix A is {row}X{col}")
print(f"The number of vectors that exist in the vector space are {row}")

rank_A = np.linalg.matrix_rank(A_matrix)
print(f'The rank of the matrix is {rank_A}')

inverse_A = np.linalg.pinv(A_matrix)
X_matrix = np.dot(inverse_A, C_matrix)

print(X_matrix)

print(f"Cost of each candy: {X_matrix[0][0]}")
print(f"Cost of each mango: {X_matrix[1][0]}")
print(f"Cost of each milk packet: {X_matrix[2][0]}")
