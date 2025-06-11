import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Loading the dataset, skipping the first row if it's a duplicate header
data = pd.read_csv('C:/Users/premc/Downloads/spam.csv', delimiter=',', encoding='ISO-8859-1', skiprows=1, names=['label', 'message'])
    
# Displaying the first few rows of the dataset
print("Raw data:")
print(data.head())

# Handling missing values in the 'message' column
data['message'] = data['message'].fillna('')

# Removing rows with empty messages
data = data[data['message'].str.strip() != '']

# Checking class distribution to verify if it's balanced
print(f"Class distribution:\n{data['label'].value_counts()}")

# If the dataset is empty after preprocessing, raise an error
if data.shape[0] == 0:
    raise ValueError("The dataset is empty after preprocessing. Please check the dataset.")

# Preprocessing the text data (e.g., lowercasing, removing stopwords)
vectorizer = CountVectorizer(stop_words='english')

# Spliting the data into features and labels
X = data['message']
y = data['label']

# Spliting data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Converting text data to numeric vectors using CountVectorizer
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# Initializing and train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vectors, y_train)

# Making predictions
y_pred = model.predict(X_test_vectors)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=1))
