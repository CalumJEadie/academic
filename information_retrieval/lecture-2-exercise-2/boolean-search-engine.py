#!/usr/bin/env python

import sys
import argparse

INDEX_FILE = "tmp2/counted-sorted-terms"
AND_QUERY, OR_QUERY = 0,1

def get_index():
    """
    Returns an index of terms, documents and frequencies.

    Implemented niavely as a list of dictionaries.
    """
    index = []
    with open(INDEX_FILE) as index_file:
        for line in index_file:
            line = line.lstrip().rstrip()
            (freq, document, term) = line.split(" ")
            index.append({
                "term" : term,
                "document" : document,
                "freq" : freq
            })
    return index

def get_documents_with_term(index, term):
    """
    Returns the set of documents containing the term.
    """
    documents = set()
    for entry in index:
        if term == entry["term"]:
            documents.add(entry["document"])
    return documents

def get_documents_matching_query(index, query_type, query_terms):

    assert query_type in (AND_QUERY, OR_QUERY)
    assert len(query_terms) > 0

    documents = get_documents_with_term(index, query_terms[0])

    for term in query_terms[1:]:
        term_documents = get_documents_with_term(index, term)

        if query_type == AND_QUERY:
            documents &= term_documents
        else:
            documents |= term_documents

    return documents

def parse_query(query):
    """
    :return: (type, terms)
    """

    query_split = query.split(" ")

    if len(query_split) == 1:
        query_type, query_terms = AND_QUERY, query_split
    else:
        first_operator = query_split[1]
        if first_operator == "AND":
            query_type = AND_QUERY
        elif first_operator == "OR":
            query_type = OR_QUERY
        else:
            raise RuntimeError("query should be AND or OR")

        if query_type == AND_QUERY:
            query_terms = query.split(" AND ")
        else:
            query_terms = query.split(" OR ")

    return (query_type, query_terms)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Either an AND query \"term1 AND term2 AND"
        " ...\" or an OR query \"term1 OR term2 OR ...\"")

    args = parser.parse_args(sys.argv[1:])

    index = get_index()

    query_type, query_terms = parse_query(args.query)

    documents = get_documents_matching_query(index, query_type, query_terms)

    print "\n".join(documents)

if __name__ == "__main__":
    main()