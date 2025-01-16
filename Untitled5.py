import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')

# Streamlit App
def main():
    st.title("PDF WordCloud Generator")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Extract text from PDF
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        st.subheader("Extracted Text")
        st.text_area("Text from PDF:", text, height=200)

        # Preprocess text
        st.subheader("Text Preprocessing")
        st.write("Steps: Lowercasing, Removing Punctuation, Removing Stopwords")
        
        # Convert text to lowercase
        text = text.lower()

        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Tokenize words
        words = word_tokenize(text)

        # Remove stopwords
        stop_words = set(stopwords.words("english"))
        filtered_words = [word for word in words if word not in stop_words and word.isalpha()]

        st.write(f"Number of words after preprocessing: {len(filtered_words)}")

        # Create WordCloud
        st.subheader("WordCloud")
        wordcloud = WordCloud(width=800, height=400, max_words=500, background_color="white").generate(" ".join(filtered_words))

        # Display WordCloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)

if __name__ == "__main__":
    main()



