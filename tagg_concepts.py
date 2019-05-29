#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:07:37 2019

@author: oni
"""
from data import concept, qualifieurs, racinize_all_concept, racinize_all_qualifieurs
from lemmat import generate_ngrams
from lemmat import racinisation

concepts = racinize_all_concept(concept)
qualif = racinize_all_qualifieurs(qualifieurs)

def reco_concept(concepts,phrase_test):
    concept_reco =[]
    for j in range(1,5):
        words = generate_ngrams(phrase_test, j)
        words = racinisation(words)
        for word in words:
            for i in range(0,len(concepts)):
                if word == concepts[i][0]:
                    concept_reco.append(concepts[i][1])
    concept_reco = filtrage_solution(concept_reco)
    concept_reco = set(concept_reco)
    return concept_reco

#isole
def reco_qualifieurs(qualif, phrase_test):
    qualif_reco = []
    print(concepts)
    for j in range(1,5):
        words = generate_ngrams(phrase_test, j)
        words = racinisation(words)
        for word in words:
            print(word)
            for i in range(0,len(qualif)):
                if word == qualif[i]:
                    qualif_reco.append(qualifieurs[i])
    qualif_reco = filtrage_solution(qualif_reco)
    qualif_reco = set(qualif_reco)
    return qualif_reco


def filtrage_solution(liste):
    taille = len(liste)
    i = 0
    
    while i <= taille-1:
        for j in range(0, len(liste)-2):
            if (liste[i].find(liste[j]) != -1 and j!=i):
                del liste[j]
                i = i-1
                taille = taille-1
        i = i+1
    return liste