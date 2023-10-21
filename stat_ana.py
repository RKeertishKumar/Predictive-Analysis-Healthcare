import pandas as pd
from scipy.stats import ttest_ind

# Load the dataset into 'df'
df = pd.read_excel('preprocessed_stress_dataset.xlsx')  # Ensure the dataset is loaded

# Separate data into two groups: Male and Female
male_stress = df[df['sex_nom_Female'] == 1]['stress_at_work']
female_stress = df[df['sex_nom_Female'] == 0]['stress_at_work']

# Perform a two-sample t-test
t_stat, p_value = ttest_ind(male_stress, female_stress, equal_var=False)

# Interpret the results
alpha = 0.05  # Significance level
print(f'Test Statistic (t): {t_stat:.4f}')
print(f'P-value: {p_value:.4f}')

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in stress levels between males and females.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in stress levels between males and females.")
