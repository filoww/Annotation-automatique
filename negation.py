#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:30:10 2019

@author: oni
"""

from data import negationeur, racinize_all_negationeur
from tagging import filtrage_solution 
from lemmat import generate_ngrams
from lemmat import racinisation


neg = racinize_all_negationeur(negationeur)
mot_neg = []
 
def reco_nega(neg,phrase_test):  #fait ressortir les marqueurs de negations 
    neg_reco =[]
    for j in range(1,5):
        words = generate_ngrams(phrase_test, j)
        words = racinisation(words)
        for word in words:
            for i in range(0,len(neg)):
                if word == neg[i]:
                    neg_reco.append(neg[i])
                    mot_neg.append(word)
    neg_reco = filtrage_solution(neg_reco)
    neg_reco = set(neg_reco)
    return neg_reco


def status_neg(neg, phrase): # si presence de neg_word retourner statut negatif
    statut = ''
    neg_reco = reco_nega(neg,phrase)
    if len(neg_reco) > 0:
        statut = 'NON'
    else :
        statut = 'OUI'
    return statut


#AFFINER AVEC DOUBLE NEGATION ET NEGATION D'UN QUALIFIEUR ?