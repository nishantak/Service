import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp_ = spacy.load("en_core_web_md")

def nlp(text):
    return nlp_(text)

def match(pattern, text):
    doc = nlp_(text)
    matcher = Matcher(nlp_.vocab)
    matcher.add("pattern", [pattern])
    matches = matcher(doc)
    matcher.remove("pattern")
    indexes = []
    for _, s, e in matches:
        indexes.append([s,e])
    return indexes

def phrase_match(terms,text):
    matcher = PhraseMatcher(nlp_.vocab)
    patterns = [nlp_.make_doc(term) for term in terms]
    matcher.add("pattern", patterns)
    doc = nlp_(text)
    matches = matcher(doc)
    if matches:
        return True
    else:
        return False
    
