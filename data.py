#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:32:49 2019
,('','')
@author: oni
"""
from nltk.stem.snowball import FrenchStemmer
from onto import recup_onto, constit_dico,result_final

qualifieurs = ['fréquentes', 'peu fréquentes', 'en salves' , 'isolées', 'bigéminées', 'avec aberration', 
               'lambeaux', 'Soutenue', 'non soutenue', 'Brèves', 'salves', 'lambeaux', 'en salves' , 
               'bigéminées', 'une ou plusieurs morphologie', 'trés rare', 'rare', 'pic',
               'répétitives', 'complexes', 'doublets', 'triplets','couplets', 'à couplage précoce', 'à couplage tardif',
               'à couplage variable','Monomorphe', 'polymorphe', 'Soutenue', 'non soutenue', 'Brèves', 'salves', 'lambeaux', 
               'Droit', 'gauche', 'permanent', 'intermittent', 'chrono-dépendant','Diurne', 'nocturne', 'inappropriée', 
               'sur tout le nychémère', 'de haut degré', 'complet', 'permanent', 'intermittent', 'avec échappement', 
               'sans échappement', 'fréquentes','nombreux', 'peu nombreux', 'trés nombreux','significative', 'quelques']


negationeur = ['ne', 'ni', 'aucun', 'pas', 'absence']


class Concept :
    
    def __init__(self, nom, qualif, status):
        self.libele = nom
        self.qualifieur  = qualif
        self.stat = status


# rare et trés rare defini comme une negation ici ? utile dans l'étiquetage ?
def generate_data(onto_file ):
    recup_onto(onto_file)
    constit_dico()  
    concept = result_final
    concept.append(('Rythme sinusal','Rythme sinusal'))
    concept.append(('rythme de base sinusal', 'Rythme sinusal'))
    return concept

def racinize_all_negationeur(concept):
    nega_tiers = []
    stemmer = FrenchStemmer()
    for i in range(0,len(negationeur)):
        temp = negationeur[i].lower()
        temp2 = stemmer.stem(temp)
        nega_tiers.append(temp2)
    return nega_tiers


def racinize_all_concept(concept):
    concept_tiers = []
    stemmer = FrenchStemmer()
    for i in range(0,len(concept)):
        temp = concept[i][0].lower()
        temp2 = stemmer.stem(temp)
        concept_tiers.append((temp2, concept[i][1]))
    return concept_tiers

def racinize_all_qualifieurs(qualifieurs):
    iznogoud = []
    stemmer = FrenchStemmer()
    for i in range(0,len(qualifieurs)):
        temp = qualifieurs[i].lower()
        if temp == 'isolées':
            temp2 = 'isole'
        else :
            temp2 = stemmer.stem(temp)
        iznogoud.append(temp2)
    return iznogoud

