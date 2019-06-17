#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:07:37 2019

@author: oni
"""
from data import generate_data, qualifieurs, racinize_all_concept, racinize_all_qualifieurs
from lemmat import generate_ngrams
from lemmat import racinisation

onto_file = '/home/oni/SESSTIM/ontology/root-ontology.owl'
concepts = racinize_all_concept(generate_data(onto_file))
qualif = racinize_all_qualifieurs(qualifieurs)
mots_reconu = []
 
def reco_concept(concepts,phrase_test): # fait ressortir les troubles reconnus 
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


def reco_qualifieurs(qualif, phrase_test): # fait ressortir les qualifieurs reconnus
    qualif_reco = []
    for j in range(1,5):
        words = generate_ngrams(phrase_test, j)
        words = racinisation(words)
        for word in words:
            for i in range(0,len(qualif)):
                if word == qualif[i].replace('é','e'):
                    qualif_reco.append(qualifieurs[i])
                    mots_reconu.append(word)
    qualif_reco = filtrage_solution(qualif_reco)
    return qualif_reco


def filtrage_solution(liste): #permet de garder seulement les solutions les plus précises (termes les plus longs)
    temp = liste.copy()
    for word in liste:
        for elem in temp:
            if elem in word and len(elem) != len(word) :
                liste.remove(elem)
    liste = list(set(liste))
    return liste
# ex : tachycardie et tachycardie atrial on garde que tachycardie atrial