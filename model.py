import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset

data = pd.read_csv("food_dataset.csv")

# Features and labels
X = data.drop("result", axis=1)
y = data["result"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")