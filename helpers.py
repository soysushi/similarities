from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    # TODO
    lines_a = set(a.split("\n"))
    lines_b = set(b.split("\n"))

    results = lines_a & lines_b
    return results


def sentences(a, b):
    """Return sentences in both a and b"""
    # TODO
    # set a list
    sentences_a = set(sent_tokenize(a))
    sentences_b = set(sent_tokenize(b))

    results = sentences_a & sentences_b
    return results


def helper(string, n):
    sub_strings = []

    for i in range(len(string) - n + 1):
        sub_strings.append(string[i:i + n])

    return sub_strings


def substrings(a, b, n):
    """Return sentences in both a and b"""

    # TODO
    sub_a = set(helper(a, n))
    sub_b = set(helper(b, n))
    results = sub_a & sub_b
    return results