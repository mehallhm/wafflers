"""
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix


def train(corpus: list[str]) -> tuple[TfidfVectorizer, csr_matrix]:
    """
    Fits the vectorizer on the matrix, returning both the vectorizer and tf-idf

    :param corpus: A list of the documents (orgs) to fit against
    :returns: The fitted vectorizer and csr matrix
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(corpus)
    return vectorizer, tfidf


def predict(
    tfidf: csr_matrix, orgs: dict[str:str], query: str
) -> tuple[list[dict[str:str]], list[float]]:
    """
    Returns both a list of the orgs and their match similarity for a given query

    :param vectorizer: The vectorizer for the data
    :param tfdif: The vectorized org matrix
    :param orgs: A dict for the org information
    :param query: The string to match against

    :returns: A tuple with a list of org dicts and list of similarity scores, sorted
        highest to lowest
    """
    query_tfidf = TfidfVectorizer(stop_words="english").transform([query], tfidf)
    cos_sim = cosine_similarity(query_tfidf, tfidf).flatten()
    sim_scores, sorted_orgs = (
        list(t) for t in zip(*sorted(zip(cos_sim, orgs), key=lambda x: x[0]))
    )
    return sorted_orgs, sim_scores
