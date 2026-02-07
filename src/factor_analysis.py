# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
# def extract_top_factors(df, target_outcome, top_n=15):
#     positive_texts = df[df["intent"] == target_outcome]["full_text"]
#     negative_texts = df[df["intent"] != target_outcome]["full_text"]

#     vectorizer = TfidfVectorizer(
#         stop_words="english",
#         max_features=5000,
#         ngram_range=(1, 2)
#     )

#     all_texts = list(positive_texts) + list(negative_texts)
#     X = vectorizer.fit_transform(all_texts)

#     pos_matrix = X[:len(positive_texts)]
#     neg_matrix = X[len(positive_texts):]

#     pos_mean = np.asarray(pos_matrix.mean(axis=0)).flatten()
#     neg_mean = np.asarray(neg_matrix.mean(axis=0)).flatten()

#     diff = pos_mean - neg_mean

#     feature_names = np.array(vectorizer.get_feature_names_out())

#     top_indices = diff.argsort()[-top_n:][::-1]

#     top_terms = feature_names[top_indices]

#     return top_terms




# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
# def extract_top_factors(df, target_outcome, top_n=15):

#     positive_texts = df[df["intent"] == target_outcome]["full_text"]
#     negative_texts = df[df["intent"] != target_outcome]["full_text"]

#     vectorizer = TfidfVectorizer(
#         stop_words="english",
#         max_features=5000,
#         ngram_range=(1, 2)
#     )

#     all_texts = list(positive_texts) + list(negative_texts)
#     X = vectorizer.fit_transform(all_texts)

#     pos_matrix = X[:len(positive_texts)]
#     neg_matrix = X[len(positive_texts):]

#     pos_mean = np.asarray(pos_matrix.mean(axis=0)).flatten()
#     neg_mean = np.asarray(neg_matrix.mean(axis=0)).flatten()

#     diff = pos_mean - neg_mean

#     feature_names = np.array(vectorizer.get_feature_names_out())

#     top_indices = diff.argsort()[-top_n:][::-1]
#     top_terms = feature_names[top_indices]

#     return top_terms


# def extract_top_factors_from_texts(positive_texts, negative_texts, top_n=15):

#     vectorizer = TfidfVectorizer(
#         stop_words="english",
#         max_features=5000,
#         ngram_range=(1, 2)
#     )

#     all_texts = positive_texts + negative_texts
#     X = vectorizer.fit_transform(all_texts)

#     pos_matrix = X[:len(positive_texts)]
#     neg_matrix = X[len(positive_texts):]

#     pos_mean = np.asarray(pos_matrix.mean(axis=0)).flatten()
#     neg_mean = np.asarray(neg_matrix.mean(axis=0)).flatten()

#     diff = pos_mean - neg_mean

#     feature_names = np.array(vectorizer.get_feature_names_out())

#     top_indices = diff.argsort()[-top_n:][::-1]
#     top_terms = feature_names[top_indices]

#     return top_terms



# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np


# def extract_top_factors_from_texts(positive_texts, negative_texts, top_n=20):

#     vectorizer = TfidfVectorizer(
#         stop_words="english",
#         max_features=5000,
#         ngram_range=(1, 2)
#     )

#     all_texts = positive_texts + negative_texts
#     X = vectorizer.fit_transform(all_texts)

#     pos_matrix = X[:len(positive_texts)]
#     neg_matrix = X[len(positive_texts):]

#     pos_mean = np.asarray(pos_matrix.mean(axis=0)).flatten()
#     neg_mean = np.asarray(neg_matrix.mean(axis=0)).flatten()

#     diff = pos_mean - neg_mean

#     feature_names = np.array(vectorizer.get_feature_names_out())

#     top_indices = diff.argsort()[-top_n:][::-1]
#     top_terms = feature_names[top_indices]

#     return top_terms



# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
# import re

# def clean_terms(terms):

#     cleaned = []

#     for term in terms:
#         term = term.strip()

#         if len(term) < 4:
#             continue

#         if re.search(r"\d", term):
#             continue

#         if not re.search(r"[a-zA-Z]", term):
#             continue

#         words = term.split()
#         if len(words) != len(set(words)):
#             continue

#         cleaned.append(term.title())

#     return cleaned


# def extract_top_factors_from_texts(positive_texts, negative_texts, top_n=20):

#     vectorizer = TfidfVectorizer(
#         stop_words="english",
#         max_features=5000,
#         ngram_range=(1, 2)
#     )

#     all_texts = positive_texts + negative_texts
#     X = vectorizer.fit_transform(all_texts)

#     pos_matrix = X[:len(positive_texts)]
#     neg_matrix = X[len(positive_texts):]

#     pos_mean = np.asarray(pos_matrix.mean(axis=0)).flatten()
#     neg_mean = np.asarray(neg_matrix.mean(axis=0)).flatten()

#     diff = pos_mean - neg_mean

#     feature_names = np.array(vectorizer.get_feature_names_out())

#     top_indices = diff.argsort()[-top_n:][::-1]
#     top_terms = feature_names[top_indices]

#     cleaned_terms = clean_terms(top_terms)

#     return cleaned_terms[:4]



# from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
# import re


# def clean_terms(terms):

#     cleaned = []

#     for term in terms:
#         term = term.strip()

#         if len(term) < 4:
#             continue

#         if re.search(r"\d", term):
#             continue

#         # Must contain alphabet
#         if not re.search(r"[a-zA-Z]", term):
#             continue

#         words = term.split()
#         if len(words) != len(set(words)):
#             continue

#         cleaned.append(term.title())

#     return cleaned


# def extract_top_factors_from_texts(positive_texts, negative_texts, top_n=20):

#     vectorizer = TfidfVectorizer(
#         stop_words="english",
#         max_features=5000,
#         ngram_range=(1, 2)
#     )

#     all_texts = positive_texts + negative_texts
#     X = vectorizer.fit_transform(all_texts)

#     pos_matrix = X[:len(positive_texts)]
#     neg_matrix = X[len(positive_texts):]

#     pos_mean = np.asarray(pos_matrix.mean(axis=0)).flatten()
#     neg_mean = np.asarray(neg_matrix.mean(axis=0)).flatten()

#     diff = pos_mean - neg_mean

#     feature_names = np.array(vectorizer.get_feature_names_out())

#     top_indices = diff.argsort()[-top_n:][::-1]
#     top_terms = feature_names[top_indices]

#     cleaned_terms = clean_terms(top_terms)

#     if len(cleaned_terms) < 2:
#         fallback = [term.title() for term in top_terms[:3]]
#         return fallback
#     return cleaned_terms[:3]



#FINAL
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re


def clean_terms(terms):

    cleaned = []

    for term in terms:
        term = term.strip()

        if len(term) < 4:
            continue

        if re.search(r"\d", term):
            continue

        if not re.search(r"[a-zA-Z]", term):
            continue

        words = term.split()
        if len(words) != len(set(words)):
            continue

        cleaned.append(term.title())

    return cleaned


def extract_top_factors_from_texts(positive_texts, negative_texts, top_n=20):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000,
        ngram_range=(1, 2)
    )

    all_texts = positive_texts + negative_texts
    X = vectorizer.fit_transform(all_texts)

    pos_matrix = X[:len(positive_texts)]
    neg_matrix = X[len(positive_texts):]

    pos_mean = np.asarray(pos_matrix.mean(axis=0)).flatten()
    neg_mean = np.asarray(neg_matrix.mean(axis=0)).flatten()

    diff = pos_mean - neg_mean

    feature_names = np.array(vectorizer.get_feature_names_out())
    top_indices = diff.argsort()[-top_n:][::-1]
    top_terms = feature_names[top_indices]

    cleaned_terms = clean_terms(top_terms)

    return cleaned_terms[:4]  # Max 4 clean factors
