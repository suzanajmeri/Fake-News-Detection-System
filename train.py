import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle


# Load Data
df_fake = pd.read_csv("fake.csv")
df_real = pd.read_csv("authentic.csv")

# Add labels (0 = Fake, 1 = Real)
df_fake["label"] = 0
df_real["label"] = 1

# Combine datasets
df = pd.concat([df_fake, df_real], axis=0).reset_index(drop=True)


# Clean Text (basic cleaning)

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text

df["text"] = df["title"].astype(str) + " " + df["text"].astype(str)
df["text"] = df["text"].apply(clean_text)


# 3. Split Data

X = df["text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


#  Vectorization

vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

#  Train Model

model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)


#  Evaluate

y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


#  Save Model + Vectorizer

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved successfully!")