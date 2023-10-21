import pandas as pd
from sklearn.preprocessing import StandardScaler

# Read the dataset
df = pd.read_excel('stress_dataset.xlsx')

# Handling Missing Values
numerical_columns = ['age', 'stress_at_home', 'stress_at_work']
categorical_columns = ['Continent', 'sex_nom', 'Actual status', 'Healthcare worker Y_N', 'work_normal_asusual_yn']

# Fill missing values in numerical columns with their means
for col in numerical_columns:
    df[col].fillna(df[col].mean(), inplace=True)

# Fill missing values in categorical columns with their modes
for col in categorical_columns:
    df[col].fillna(df[col].mode().iloc[0], inplace=True)

# Encoding Categorical Variables
df = pd.get_dummies(df, columns=categorical_columns)

# Scaling Numerical Features (Optional)
scaler = StandardScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Now, the dataset is preprocessed, and you can proceed with data analysis or modeling tasks.
print(df.head())

# Save the preprocessed data to a new Excel file
df.to_excel('preprocessed_stress_dataset.xlsx', index=False)
