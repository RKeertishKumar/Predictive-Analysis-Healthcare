import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset into 'df' (make sure to replace 'preprocessed_stress_dataset.xlsx' with your file path)
df = pd.read_excel('preprocessed_stress_dataset.xlsx')

# Histogram for 'age'
plt.figure(figsize=(8, 6))
sns.histplot(df['age'], kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Bar plot for 'Continent'
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Continent')
plt.title('Continent Distribution')
plt.xlabel('Continent')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Box plot for 'age'
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, y='age')
plt.title('Age Distribution (Box Plot)')
plt.ylabel('Age')
plt.show()

# Pair plot for numerical features
sns.pairplot(df[['age', 'stress_at_home', 'stress_at_work']])
plt.show()

# Count plot for 'sex_nom'
sns.countplot(data=df, x='sex_nom')
plt.title('Sex Distribution')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()
