# 📰 Fake News Detection using NLP and Machine Learning

This project detects whether a news article is **Fake** or **Real** using Natural Language Processing and a Logistic Regression model.

## 🚀 Demo

Paste your news article and get an instant prediction using the web app powered by Streamlit.

## 📂 Project Structure

fake-news-detection/
├── data/ # Dataset (Fake.csv, True.csv)
├── train_model.py # Script to train and save model
├── predict.py # Function to make predictions
├── app.py # Streamlit app interface
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt
└── README.md

## 📊 Dataset

- Source: [Kaggle - Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- ~44,000 news articles labeled as `Fake` or `Real`

## 🧠 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Streamlit

## 📈 Model Accuracy

Achieved over **90% accuracy** on test data using Logistic Regression.

## 🔍 How to Run Locally

1. Clone the repository:
    ```
    git clone https://github.com/KUNAL152/fake-news-detection.git
    cd fake-news-detection
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Train the model:
    ```
    python train_model.py
    ```

4. Run the app:
    ```
    streamlit run app.py
    ```

## 🤖 Prediction Example

```text
"BREAKING: Scientists Confirm Water on Mars"
Prediction: Real
