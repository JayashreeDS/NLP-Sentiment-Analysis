import streamlit as st
import joblib
import re

# Load the improved model and its matching vectorizer
model = joblib.load("sentiment_model_improved.pkl")
tfidf = joblib.load("tfidf_vectorizer_improved.pkl")


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


st.set_page_config(
    page_title="Customer Review Sentiment Analysis",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Customer Review Sentiment Analysis")

st.write(
    "Enter a customer review below to predict whether the sentiment "
    "is Negative, Neutral, or Positive."
)

review = st.text_area(
    "Enter Customer Review:",
    placeholder="Example: The product quality is excellent and I am very happy with it."
)

if st.button("Predict Sentiment"):
    if not review.strip():
        st.warning("Please enter a customer review.")
    else:
        cleaned_review = clean_text(review)
        review_tfidf = tfidf.transform([cleaned_review])
        prediction = model.predict(review_tfidf)[0]

        st.subheader("Predicted Sentiment")

        if prediction == "Positive":
            st.success("😊 Positive")
        elif prediction == "Negative":
            st.error("😞 Negative")
        else:
            st.info("😐 Neutral")
