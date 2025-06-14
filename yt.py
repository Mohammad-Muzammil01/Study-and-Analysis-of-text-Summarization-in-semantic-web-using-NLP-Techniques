import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

nltk.download('stopwords')
nltk.download('punkt')

def read_article(file_name: str) -> list:
    try:
        with open(file_name, "r") as file:
            filedata = file.readlines()

        if not filedata:
            print(f"Error: The file '{file_name}' is empty.")
            return []

        article = " ".join(filedata)
        sentences = nltk.sent_tokenize(article)
        sentences = [sentence.split(" ") for sentence in sentences]
        return sentences

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []

def sentence_similarity(sent1: list, sent2: list, stopwords: set = None) -> float:
    if stopwords is None:
        stopwords = set()

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
    all_words = list(set(sent1 + sent2))
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    similarity = 1 - cosine_distance(vector1, vector2)
    if np.isnan(similarity):
        return 0
    return similarity

def gen_sim_matrix(sentences: list, stop_words: set) -> np.ndarray:
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix

def generate_summary(file_name: str, summary_size: str = 'medium') -> str:
    stop_words = set(stopwords.words('english'))
    summarize_text = []
    sentences = read_article(file_name)

    if not sentences:
        return "Error: No valid sentences found in the file."

    total_sentences = len(sentences)
    size_ratios = {'short': 0.3, 'medium': 0.5, 'detailed': 0.7}
    ratio = size_ratios.get(summary_size, 0.5)
    min_sentences = {'short': 3, 'medium': 5, 'detailed': 7}
    min_sent = min_sentences.get(summary_size, 5)
    top_n = max(min_sent, int(total_sentences * ratio))
    top_n = min(top_n, total_sentences)

    sentence_similarity_matrix = gen_sim_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))

    return ". ".join(summarize_text)
