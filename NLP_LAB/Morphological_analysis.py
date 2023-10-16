import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

def morphological_analysis(word):
    # Porter Stemmer
    stemmer = PorterStemmer()
    stemmed_word = stemmer.stem(word)

    # WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_word = lemmatizer.lemmatize(word)

    return stemmed_word, lemmatized_word

def main():
    sentence = "The quick brown foxes jumped over the lazy dogs"

    # Tokenize the sentence into words
    words = word_tokenize(sentence)

    print("Original Word\tStem\tLemmatized")

    for word in words:
        stemmed_word, lemmatized_word = morphological_analysis(word)
        print(f"{word}\t\t{stemmed_word}\t{lemmatized_word}")

if __name__ == "__main__":
    main()