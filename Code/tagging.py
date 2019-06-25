#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:07:37 2019

@author: oni
"""
from data import generate_data, quali, racinize_all_concept, racinize_all_qualifieurs
from lemmat import generate_ngrams, racinisation, filtrage_solution

onto_file = '/home/oni/SESSTIM/craa/Ontology/root-ontology.owl'
concept, quanti = generate_data(onto_file)
concepts = racinize_all_concept(concept)
qualif = racinize_all_qualifieurs(quali)
quantit = racinize_all_qualifieurs(quanti)
mots_reconu = []
 
def reco_concept(phrase_test): #tagg known troubles
    concept_reco =[]
    for j in range(1,5):
        words = generate_ngrams(phrase_test, j)
        words = racinisation(words)
        for word in words:
            for i in range(0,len(concepts)):
                if word == concepts[i][0]:
                    concept_reco.append(concepts[i][1])
                    mots_reconu.append(word)
    concept_reco = filtrage_solution(concept_reco)
    return concept_reco


def reco_quali(phrase_test): #tagg known qualitativ
    quali_reco = []
    for j in range(1,5):
        words = generate_ngrams(phrase_test, j)
        words = racinisation(words)
        for word in words:
            for i in range(0,len(qualif)):
                if word == qualif[i].replace('é','e'):
                    quali_reco.append(quali[i])
                    mots_reconu.append(word)
    quali_reco = filtrage_solution(quali_reco)
    return quali_reco



def reco_quanti(phrase_test): #tagg known quantitativ
    
    quanti_reco = []
    for j in range(1,5):
        words = generate_ngrams(phrase_test, j)
        words = racinisation(words)
        for word in words:
            for i in range(0,len(quantit)):
                if word == quantit[i].replace('é','e'):
                    quanti_reco.append(quanti[i])
                    mots_reconu.append(word)
    quanti_reco = filtrage_solution(quanti_reco)
    return quanti_reco

# ex : tachycardie et tachycardie atrial on garde que tachycardie atrial







