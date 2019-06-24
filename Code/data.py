#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:32:49 2019
@author: oni
"""
from nltk.stem.snowball import FrenchStemmer
from onto import recup_onto, constit_dico

quali = [ 'en salves' , 'isolées', 'bigéminées', 'avec aberration', 
               'lambeaux', 'Soutenue', 'non soutenue', 'Brèves', 'salves', 'lambeaux', 'en salves' , 
               'bigéminées', 'une ou plusieurs morphologie',  'pic',
               'répétitives', 'complexes', 'doublets', 'triplets','couplets', 'à couplage précoce', 'à couplage tardif',
               'à couplage variable','Monomorphe', 'polymorphe', 'Soutenue', 'non soutenue', 'Brèves', 'salves', 'lambeaux', 
               'Droit', 'gauche', 'intermittent', 'chrono-dépendant','Diurne', 'nocturne', 'inappropriée', 
               'sur tout le nychémère', 'de haut degré', 'complet', 'intermittent', 'avec échappement', 
               'sans échappement', 'bénigne']

#quelques pas traité car pouvant se rapporter à un qualifieurs 

negationeur = ['ne', 'ni', 'aucun', 'pas', 'absence']


class Concept :
    
    def __init__(self, nom, quanti, qualif, status):
        self.libele = nom #mot unique (ne peut pas étre vide)
        self.quantifieurs  = quanti #liste de qualifieur quantifieur (peut étre vide)
        self.qualifieurs = qualif  #liste de qualifieur qualitatifs  (peut étre vide)
        self.stat = status #Observé ou non(ne peut pas étre vide)

# rare et trés rare defini comme une negation ici ? utile dans l'étiquetage ?
def generate_data(onto_file ):
    quanti = generate_quanti()
    result = recup_onto(onto_file)
    concept = constit_dico(result)  
    concept.append(('rythme sinusal','rythme sinusal'))
    concept.remove(('Sinusale', 'Sinusale'))
    return concept, quanti

def racinize_all_negationeur(concept): #toutes les racinisation servent à gérer les variations pour la détection
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


