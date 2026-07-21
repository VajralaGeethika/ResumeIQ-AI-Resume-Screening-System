from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# =====================================================
# Job Description Matching
# =====================================================

def calculate_jd_match(resume_text, jd_text):
    """
    Calculate the similarity between a resume
    and a job description using TF-IDF and
    Cosine Similarity.

    Returns:
        float: Matching percentage (0-100)
    """

    # -------------------------
    # Validate Input
    # -------------------------

    if not resume_text.strip() or not jd_text.strip():
        return 0.0

    # -------------------------
    # TF-IDF Vectorization
    # -------------------------

    documents = [
        resume_text,
        jd_text
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        documents
    )

    # -------------------------
    # Cosine Similarity
    # -------------------------

    similarity_score = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    # -------------------------
    # Convert to Percentage
    # -------------------------

    return round(
        similarity_score * 100,
        2
    )