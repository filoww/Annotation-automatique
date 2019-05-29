# -*- coding: utf-8 -*-
"""
@author: filori quentin 
@Date: 09/05/2019
"""
import nltk
import re
from nltk import RegexpTokenizer
from nltk.stem.snowball import FrenchStemmer
from nltk.tag.stanford import StanfordPOSTagger
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer


def racinisation(words):
    words_racine = [stemmer.stem(word) for word in words]
    return words_racine
        
def tagger(words):
    words_tags = [pos_tagger.tag(words)]
    return words_tags

def lemmatisation(words):
    words_lemma = [lemmatizer.lemmatize(word) for word in words]    
    return words_lemma
 
    
def generate_ngrams(s, n):
    s = s.lower()
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    tokens = [token for token in s.split(" ") if token != ""]
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]    
    
content_french = "Extrasystoles supraventriculaires fréquentes mais aucun épisode de tachycardie atriale."
toknizer = RegexpTokenizer(r'''\w'|\w+|[^\w\s]''')
stemmer = FrenchStemmer()
lemmatizer = FrenchLefffLemmatizer(load_only_pos='NC')
root_path ='/home/oni/SESSTIM/stanford-postagger/'
pos_tagger = StanfordPOSTagger(root_path + "models/french.tagger", root_path + "stanford-postagger.jar",encoding='utf8') #instance de la classe StanfordPOSTagger en UTF-8
