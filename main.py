import pandas as pd

df = pd.read_excel('stress_dataset.xlsx')
# Display the first few rows
print(df.head())

# Check data types and missing values
print(df.info())

# Summary statistics
print(df.describe())
