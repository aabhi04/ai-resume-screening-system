import re
import string
import nltk
from nltk.corpus import stopwords

# Download stopwords (run once)
nltk.download("stopwords")

STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    # Lowercase
    text = text.lower()

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def remove_stopwords(text):
    words = text.split()
    filtered_words = [word for word in words if word not in STOPWORDS]
    return " ".join(filtered_words)
