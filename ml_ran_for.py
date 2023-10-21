import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset into 'df'
df = pd.read_excel('preprocessed_stress_dataset.xlsx')  # Ensure the dataset is loaded

# Define features (X) and target (y)
X = df[['age', 'stress_at_home', 'stress_at_work', 'Continent_Europe', 'sex_nom_Female']]
y = df['work_normal_asusual_yn_usual']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier on the training data
rf_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rf_classifier.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Generate a classification report for more detailed metrics
report = classification_report(y_test, y_pred)
print(report)
