# -*- coding: utf-8 -*-
"""
@author: filori quentin 
@Date: 09/05/2019
"""
import re
from nltk import RegexpTokenizer
from nltk.stem.snowball import FrenchStemmer
from nltk.tag.stanford import StanfordPOSTagger

def racinisation(words):   
    words_racine = [stemmer.stem(word) for word in words]
    return words_racine
        
def tagger(words):   #tagging syntaxique utilisé dans relation
    words_tags = [pos_tagger.tag(words)]
    return words_tags
 
    
def generate_ngrams(s, n): # genere les multimots de taille n, sert de tokeniser
    s = s.lower()
    s = (s.replace('é', 'e')).replace('è','e')
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    tokens = [token for token in s.split(" ") if token != ""]
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]    


def filtrage_solution(liste): #permet de garder seulement les solutions les plus précises (termes les plus longs)
    temp = liste.copy()
    for word in liste:
        for elem in temp:
            if elem in word and len(elem) != len(word) :
                liste.remove(elem)
    liste = list(set(liste))
    return liste

toknizer = RegexpTokenizer(r'''\w'|\w+|[^\w\s]''')
stemmer = FrenchStemmer()
root_path ='/home/oni/SESSTIM/stanford-postagger/'
pos_tagger = StanfordPOSTagger(root_path + "models/french.tagger", root_path + "stanford-postagger.jar",encoding='utf8')