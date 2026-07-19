import pandas as pd

# Load dataset
df = pd.read_csv("Student.csv")

# 1. Explore rows
print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nRandom 5 rows sample:")
print(df.sample(5))

# 2. Explore columns
print("\nColumn names:")
print(df.columns.tolist())

print("\nShape (rows, columns):")
print(df.shape)

print("\nData types of each column:")
print(df.dtypes)

# 3. Dataset information
print("\nDataset info:")
print(df.info())

print("\nStatistical summary (numerical columns):")
print(df.describe())

# 4. Missing values check
print("\nMissing values per column:")
print(df.isnull().sum())

# 5. Unique values (useful for categorical columns)
print("\nUnique values per column:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")