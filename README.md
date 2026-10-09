# NLP Sentiment Analysis

## Project Overview
This project analyzes customer reviews and predicts their sentiment as Positive, Negative, or Neutral using Natural Language Processing (NLP) and Machine Learning.

## Features
- Accepts customer reviews as input.
- Cleans and preprocesses review text.
- Converts text into numerical features using TF-IDF.
- Predicts sentiment using Logistic Regression.
- Displays the result through a Streamlit web application.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Streamlit
- Joblib

## Dataset
The project uses customer reviews with ratings. Ratings are converted into sentiment labels:
- Ratings 1–2: Negative
- Rating 3: Neutral
- Ratings 4–5: Positive

## Model Evaluation
The selected model was evaluated using a train-test split and classification metrics. The model achieved approximately 76.39% accuracy on the test set. Neutral sentiment classification remains a challenge.

## Run Locally
1. Clone this repository:
   `git clone https://github.com/JayashreeDS/NLP-Sentiment-Analysis.git`

2. Open the project folder:
   `cd NLP-Sentiment-Analysis`

3. Install dependencies:
   `pip install -r requirements.txt`

4. Start the application:
   `streamlit run app.py`

## Application
The application allows users to enter a customer review and view its predicted sentiment.

## Future Improvements
- Improve neutral sentiment classification.
- Evaluate additional machine learning models.
- Test the model on a larger and more diverse dataset.
