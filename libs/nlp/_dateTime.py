import speech_recognition as sr
from spacy.matcher import Matcher
import re
import datetime
import spacy

nlp = spacy.load("en_core_web_md")
doc = nlp(u'20th august 2014 on 1213 pm')

def date_obj(day, month, year):
    day = int(re.findall("\d\d|\d", day)[0])
    year = int(year)
    if 'jan' in month:
        m = 1

    elif 'feb' in month:
        m = 2

    elif 'mar' in month:
        m = 3

    elif 'apr' in month:
        m = 4

    elif 'may' in month:
        m = 5

    elif 'june' in month:
        m = 6

    elif 'july' in month:
        m = 7

    elif 'aug' in month:
        m
    elif 'sep' in month:
        m = 9

    elif 'oct' in month:
        m = 10

    elif 'nov' in month:
        m = 11

    elif 'dec' in month:
        m = 12
    try:
        return datetime.date(year, m, day)
    except:
        return 'invalid date'


def date(doc):
    dates = []
    for ent in doc.ents:
       if ent.label_ == "DATE":
           dates.append(ent.text)

    print(dates)

print(date(doc))