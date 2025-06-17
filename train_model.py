import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv('Crop_recommendation.csv')

# Prepare features and label
X = df.drop('label', axis=1)
y = df['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model/crop_model.pkl')

print("✅ Model trained and saved.")
