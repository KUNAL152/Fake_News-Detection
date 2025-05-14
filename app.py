import streamlit as st
from predict import predict_news
# Streamlit app for fake news detection

st.title("📰 Fake News Detection")
news_text = st.text_area("Paste news content below to check if it's real or fake:")

if st.button("Predict"):
    result = predict_news(news_text)
    if result == 1:
        st.success("This news is likely **REAL**.")
    else:
        st.error("This news is likely **FAKE**.")
        
st.markdown(
        """
        ### How it works:
        1. Paste the news content in the text area.
        2. Click on the "Predict" button.
        3. The model will analyze the text and provide a prediction.
        """
    )
    