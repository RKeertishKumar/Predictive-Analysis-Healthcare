import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset into 'df' (replace with your file path)
df = pd.read_excel('preprocessed_stress_dataset.xlsx')
plt.ioff()

# Histograms for Numerical Variables
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

# Box Plots for Numerical Variables
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
sns.boxplot(data=df, y='age')
plt.title('Age Distribution (Box Plot)')
plt.ylabel('Age')

plt.subplot(1, 3, 2)
sns.boxplot(data=df, y='stress_at_home')
plt.title('Stress at Home (Box Plot)')
plt.ylabel('Stress at Home')

plt.subplot(1, 3, 3)
sns.boxplot(data=df, y='stress_at_work')
plt.title('Stress at Work (Box Plot)')
plt.ylabel('Stress at Work')
plt.tight_layout()
plt.show()

# Count Plots for Categorical Variables
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
