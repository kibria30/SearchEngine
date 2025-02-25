import spacy

nlp = spacy.load("en_core_web_sm")

def lemmatizeWords(text: str) -> list[str]:
    doc = nlp(text)
    lemmatized_words = [token.lemma_ for token in doc]  
    return lemmatized_words

print(lemmatizeWords("The children are running happily and studying for their exams."))
print(lemmatizeWords("The cats are chasing mice in the garden, and they seem very happy."))
