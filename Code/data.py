#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:32:49 2019
@author: oni
"""
from nltk.stem.snowball import FrenchStemmer
from onto import recup_onto, constit_dico

quali = [ 'en salves' , 'isolées', 'bigéminées', 'avec aberration', 
               'lambeaux', 'Brèves', 'salves', 'lambeaux', 'en salves' , 
               'bigéminées', 'une ou plusieurs morphologie',  'pic',
               'répétitives', 'complexes', 'doublets', 'triplets','couplets', 'à couplage précoce', 'à couplage tardif',
               'à couplage variable','Monomorphe', 'polymorphe', 'soutenue', 'non soutenue',
               'Droit', 'gauche', 'intermittent', 'chrono-dépendant','Diurne', 'nocturne', 'inappropriée', 
               'sur tout le nychémère', 'de haut degré', 'complet', 'intermittent', 'avec échappement', 
               'sans échappement', 'bénigne', 'mineure', 'paroxystique', 'normal']

#quelques pas traité car pouvant se rapporter à un qualifieurs 

negationeur = ['ne', 'ni', 'aucun', 'pas', 'absence', 'sans']


class Concept :
    
    def __init__(self, nom, quanti, qualif, status):
        self.libele = nom #unique label (not empty)
        self.quantifieurs  = quanti #list of quantitiv adjectives (empty)
        self.qualifieurs = qualif  #list of qualitativ adjectives  (empty)
        self.stat = status #Observed or not (not empty)
        self.link = False

def generate_data(onto_file ):
    quanti = generate_quanti()
    result = recup_onto(onto_file)
    concept = constit_dico(result)  
    concept.append(('rythme sinusal','rythme sinusal'))
    concept.append(('holter ecg','Holter ECG'))
    concept.append(('RS','rythme sinusal'))
    concept.remove(('Sinusale', 'Sinusale'))
    return concept, quanti

def racinize_all_negationeur(concept): #all racinisation are used to work with variations
    nega_tiers = []
    stemmer = FrenchStemmer()
    for i in range(0,len(negationeur)):
        temp = negationeur[i].lower()
        temp2 = stemmer.stem(temp)
        nega_tiers.append(temp2)
    return nega_tiers

def generate_quanti():
    liste = []
    f = open('adj.txt','r')
    lines = f.readlines()
    for line in lines : 
        line = line.replace(' ','')
        liste.append(line.replace('\n',''))
    liste = list(set(liste)) 
    return liste

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
#iznogoud car il veut étre qualif à la place du qualif


