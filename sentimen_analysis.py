import nltk
import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Download dataset
nltk.download('movie_reviews')
from nltk.corpus import movie_reviews

# Load and prepare the dataset
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# Convert dataset to DataFrame for easy manipulation
data = pd.DataFrame({
    "text": [" ".join(words) for words, label in documents],
    "label": [label for _, label in documents]
})

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

# Vectorization using TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Hyperparameter tuning using GridSearchCV
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear'],  # Use only linear kernel for simplicity
    'gamma': ['scale']
}

# SVM Model
svm_model = SVC()

grid_search = GridSearchCV(svm_model, param_grid, cv=3, scoring='accuracy', verbose=2, n_jobs=-1)
grid_search.fit(X_train_vec, y_train)

# Best parameters
print("Best Parameters:", grid_search.best_params_)
print("Best Cross-Validation Accuracy:", grid_search.best_score_)

# Train the best model
best_model = grid_search.best_estimator_

# Predictions
y_pred = best_model.predict(X_test_vec)

# Evaluate the model
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nTest Accuracy:", accuracy_score(y_test, y_pred))

# Streamlit application
def predict_sentiment(user_input):
    # Vectorize the user input text
    user_input_vec = vectorizer.transform([user_input])
    # Predict sentiment using the best model
    prediction = best_model.predict(user_input_vec)
    return "Positif" if prediction[0] == 'pos' else "Negatif"

# Streamlit Web App
def main():
    st.title("Analisis Sentimen Ulasan Film")
    st.write("Masukkan ulasan film untuk mengetahui apakah ulasan tersebut positif atau negatif.")
    
    # User input for movie review
    user_input = st.text_area("Masukkan Ulasan Film:", "")
    
    if user_input:
        sentiment = predict_sentiment(user_input)
        st.write(f"Hasil analisis: {sentiment}")
    
    # Visualizing confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Negatif', 'Positif'], yticklabels=['Negatif', 'Positif'])
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_title('Confusion Matrix')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
