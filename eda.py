import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into 'df'
df = pd.read_excel('preprocessed_stress_dataset.xlsx')  # Ensure the dataset is loaded

# Scatter Plot between Age and Stress at Home
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='age', y='stress_at_home', hue='sex_nom_Female')
plt.title('Scatter Plot: Age vs. Stress at Home')
plt.xlabel('Age')
plt.ylabel('Stress at Home')
plt.show()

# Group and Aggregate Data
age_groups = df.groupby('sex_nom_Female')['age'].mean()
print("Average Age by Gender:")
print(age_groups)

# Distributions and Histograms
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
sns.histplot(df['age'], kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')

plt.subplot(1, 3, 2)
sns.histplot(df['stress_at_home'], kde=True)
plt.title('Stress at Home Distribution')
plt.xlabel('Stress at Home')

plt.subplot(1, 3, 3)
sns.histplot(df['stress_at_work'], kde=True)
plt.title('Stress at Work Distribution')
plt.xlabel('Stress at Work')
plt.tight_layout()
plt.show()

# Categorical Variable Count Plots
plt.figure(figsize=(14, 4))
plt.subplot(1, 3, 1)
sns.countplot(data=df, x='Continent_Europe')
plt.title('Continent Distribution')
plt.xlabel('Continent')

plt.subplot(1, 3, 2)
sns.countplot(data=df, x='sex_nom_Female')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.xticks([0, 1], ['Female', 'Male'])

plt.subplot(1, 3, 3)
sns.countplot(data=df, x='work_normal_asusual_yn_usual')
plt.title('Work Normality Distribution')
plt.xlabel('Work Normality')
plt.tight_layout()
plt.show()

# Correlation Heatmap for Numerical Variables
correlation_matrix = df[['age', 'stress_at_home', 'stress_at_work']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
