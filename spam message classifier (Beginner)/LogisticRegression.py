import pandas as pd

data = pd.read_csv("spam_ham_dataset.csv")

# input data
x = data["text"]
y = data["label"]

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
x_vectorized = vectorizer.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_vectorized, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy * 100, "%")

message = ["Subject: vic . odin n ^ ow berne hotbox carnal bride cutworm dyadic"]
messageVectorized = vectorizer.transform(message)
prediction = model.predict(messageVectorized)

print("\nPredicted Label for Sample Message:", prediction)

message = ["Subject: Few days left to claim your free prize! Click here now!"]
messageVectorized = vectorizer.transform(message)
prediction = model.predict(messageVectorized)

print("\nPredicted Label for Sample Message:", prediction)

message = ["Subject: Meeting rescheduled to 3 PM tomorrow. Please confirm your availability."]
messageVectorized = vectorizer.transform(message) 
prediction = model.predict(messageVectorized)

print("\nPredicted Label for Sample Message:", prediction)

