# -*- coding: utf-8 -*-
"""
@author: filori quentin 
@Date: 09/05/2019
"""
import re
import os
from nltk import RegexpTokenizer
from nltk.stem.snowball import FrenchStemmer
from nltk.tag.stanford import StanfordPOSTagger


path = os.getcwd()

def racinisation(words):   
    words_racine = [stemmer.stem(word) for word in words]
    return words_racine
        
def tagger(words):   #tagging syntaxique
    words_tags = [pos_tagger.tag(words)]
    return words_tags
 
    
def generate_ngrams(s, n): # generate multiwords of size n, tokeniser
    s = s.lower()
    s = (s.replace('é', 'e')).replace('è','e')
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    tokens = [token for token in s.split(" ") if token != ""]
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]    


def filtrage_solution(liste): #keep only the solution with the longest libele
    temp = liste.copy()
    for word in liste:
        for elem in temp:
            if elem in word and len(elem) != len(word) :
                liste.remove(elem)
    liste = list(set(liste))
    return liste

toknizer = RegexpTokenizer(r'''\w'|\w+|[^\w\s]''')
stemmer = FrenchStemmer()
root_path = path.replace('/Code','') + '/stanford-postagger/'
pos_tagger = StanfordPOSTagger(root_path + "models/french.tagger", root_path + "stanford-postagger.jar",encoding='utf8')