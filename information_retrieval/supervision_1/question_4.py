"""
Supervision 1 - Question 4
"""

import re
import nltk
from show import show
import collections
import math

import documents

# http://norm.al/2009/04/14/list-of-english-stop-words/
STOPWORDS = ("a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the")

class Document(object):
    """
    Basis data structure to represent a document.
    """

    def __init__(self, text):
        # Original text
        self.text = text
        # List of tokens
        self.tokens = stem(stop_word_removal(tokenise(text)))
        self.term_freqs = Document._get_term_freqs(self.tokens)

    def __repr__(self):
        return self.text[:20] + "..."

    @classmethod
    def from_texts(cls, texts):
        """
        :rtype: Document list
        """
        documents = []
        for text in texts:
            documents.append(cls(text))
        return documents

    @staticmethod
    def _get_term_freqs(tokens):
        term_freqs = collections.Counter()
        term_freqs.update(tokens)
        return term_freqs

class VSM(object):
    """
    Vector space model.
    """

    def __init__(self, documents):

        self._documents = documents
        self._terms = VSM._get_terms(self._documents)
        # self._term_freqs = VSM._get_term_freq(documents)
        # Number of documents in which terms appear
        self._document_freqs = VSM._get_document_freqs(self._documents, self._terms)
        self._calculate_document_vectors()

    @staticmethod
    def _get_terms(documents):
        """
        Return terms from all documents.
        """
        terms = set()
        for document in documents:
            terms |= set(document.tokens)
        return terms

    # @staticmethod
    # def _get_term_freq(documents):
    #     """
    #     Return a dict mapping terms to their frequency in all documents.
    #     """
    #     term_freqs = collections.Counter()
    #     for document in documents:
    #         term_freqs += document.term_freqs
    #     return term_freqs

    @staticmethod
    def _get_document_freqs(documents, terms):
        """
        Returns counts of the number of documents in which a term appears.
        """
        document_freqs = dict.fromkeys(terms, 0)
        for term in document_freqs.keys():
            for document in documents:
                if term in document.term_freqs.keys():
                    document_freqs[term] += 1
        return document_freqs

    def _calculate_document_vectors(self):

        # Calculate vector per document
        for document in self._documents:
            document.vector = self._calculate_document_vector(document)

    def _calculate_document_vector(self, document):
        """
        Use TF x IDF scheme for document term weighting.

        tf_i_j - frequency of ith term in jth document
        N - number of documents in collection
        df_i - number of documents in which ith term appears

        TF_i_j = 1 + log(tf_i_j)

        IDF_i = log( N / df_i )
        """
        N = len(self._documents)

        # Terms are basis vectors for the space.
        vector = {}
        for term in dict.fromkeys(document.term_freqs.keys()):
            tf_i_j = document.term_freqs[term]
            TF_i_j = 1 + math.log(tf_i_j)
            df_i = self._document_freqs[term]
            IDF_i = math.log( float(N) / df_i )
            weight = TF_i_j * IDF_i
            vector[term] = weight
        return Vector(vector)

    def _calculate_query_vector(self, query):
        """
        Use TF x IDF scheme to for query term weighting.

        tf - number of times term appears in query
        max tf - highest number of occurences for any term in the query
        N - total number of documents
        n - number of documents in whch query term appears

        TF x IDF = (0.5 + (0.5*tf / max tf)) log (N/n)

        :type query: string
        """
        N = len(self._documents)

        term_freqs = collections.Counter(stem(stop_word_removal(tokenise(query))))
        terms = term_freqs.keys()

        vector = {}
        for term in terms:
            tf = term_freqs[term]
            max_tf = term_freqs.most_common(1)[0][1]
            n = self._document_freqs.get(term)
            if n > 0:
                weight = (0.5 + (0.5*tf / max_tf)) * math.log(N/n)
            else:
                weight = 0
            vector[term] = weight

        return Vector(vector)

    def query(self, query):
        """
        :type query: string
        """
        query_vector = self._calculate_query_vector(query)

        results = []
        for document in self._documents:
            similarity = document.vector.cosine(query_vector)
            results.append((document, similarity))

        # Sort by similarity
        results = sorted(results, key=lambda (d,s): s)

        return results

class DictWithDefault(dict):
    """
    Similiarly to collections.defaultdict a default is retuend when a key is missing
    however where a value is not inserted.
    """

    def __init__(self, mapping, default):
        super(DictWithDefault, self).__init__(mapping)
        self._default = default

    def get(key):
        super(DictWithDefault, self).get(key, self._default)

class Vector(object):
    """
    Implementation of a vector that supports operations where not all components
    are specified and where basis vectors can be identified by strings rather
    than keeping track of indexes into an array.

    Implemented using a dict.
    """

    def __init__(self, mapping):
        self._vector = DictWithDefault(mapping, 0.0)

    def dot_product(self, other):
        """
        Calculate inner product using dot product. Not length normalised.

        x.y = x_1*y_1 + ... + x_n*y_n
        """
        keys = set(self._vector.keys()) & set(other._vector.keys())
        product = 0.0
        for key in keys:
            product += self._vector[key] * other._vector[key]
        return product

    def cosine(self, other):
        """
        Calculae innner product using cosine. Lenght normalised.
        """
        dot_product = self.dot_product(other)
        if dot_product == 0:
            return 0
        return dot_product / (self.norm() * other.norm())

    def norm(self):
        """
        Calculate norm of vector.

        || x || = sqrt( x.x )
        """
        return math.sqrt( self.dot_product(self) )

def tokenise(document):
    """
    Normalise case
    Remove punctuation
    Split on spaces

    :param document: freeform text
    :return: tokens
    """
    # Remove punctuation
    document = document.lower()
    document = document.translate(None, '.,!?')
    return document.split(" ")

def stop_word_removal(tokens):
    """
    :param tokens: tokens incl. stopwords
    :return: tokens excl. stopwords
    """
    not_stopword = lambda word: not word in STOPWORDS
    return filter(not_stopword, tokens)

def stem(tokens):
    """
    :type tokens: string list
    :rtype: string list
    """
    ps = nltk.PorterStemmer()
    return map(ps.stem, tokens)

def _pprint(obj):
    if isinstance(obj, list):
        print ' '.join(obj)
    else:
        print obj
    print

def boolean_query(documents, query):
    """
    Perform a query using a boolean model.

    Query must contain only one term

    :type documents: Document list
    :type query: string
    :rtype: Document list
    """
    assert ' ' not in query

    term = stem([query.lower()])[0]

    matching_documents = []

    for d in documents:
        if term in d.tokens:
            matching_documents.append(d)

    return matching_documents

def main():

    # Tokenisation, stop word removal and stemming.

    d1 = documents.DOCUMENT_1
    _pprint(d1)
    d1 = tokenise(d1)
    _pprint(d1)
    d1 = stop_word_removal(d1)
    _pprint(d1)
    d1 = stem(d1)
    _pprint(d1)

    # Boolean model

    ds = Document.from_texts([documents.DOCUMENT_1, documents.DOCUMENT_2, documents.DOCUMENT_3])

    q = "nobel"
    mds = boolean_query(ds, q)
    show(q)
    show.items(mds)

    # Vector space model

    vsm = VSM(ds)

    queries = [
        "Physicist",
        "Nobel Prize Genius",
        "President of the United States",
        "US President",
        "Quantum Mechanics",
        "President of Germany",
        "Famous politicians"
    ]

    for query in queries:
        show(query)
        results = vsm.query(query)
        show(results)

if __name__ == "__main__":
    main()