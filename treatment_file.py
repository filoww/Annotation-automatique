#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:18:12 2019

@author: oni
"""
from tagging import reco_concept, reco_qualifieurs
from tagging import concepts, qualif
from lemmat import generate_ngrams, tagger
from negation import neg, status_neg

def recup_text(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    return lines

def treat_line_simple(line): #traitement d'une ligne simple, 80% des cas
    line = line.replace('é','e')
    concept_reco = reco_concept(concepts, line)
    qualif_reco = reco_qualifieurs(qualif, line)
    status = status_neg(neg, line)
    return concept_reco, qualif_reco, status

def treat_line_cplx(line,tag): #phrase en 2 partie obligatoire pour relation
    temp = ''
    temp2 = ''
    i = 0
    cible = ('mais', 'CC')
    while tag[i]!= cible:
        temp +=  tag[i][0] + ' '
        i += 1
    for j in range(i, len(tag)):
        temp2 = temp2 + tag[j][0] + ' '
    concept_reco_t1, qualif_reco_t1, status_t1 = treat_line_simple(temp)   
    concept_reco_t2, qualif_reco_t2, status_t2 = treat_line_simple(temp2)
    concept_reco = str(concept_reco_t1) + '    ' + str(concept_reco_t2)
    qualif_reco =  str(qualif_reco_t1) + '    '  + str(qualif_reco_t2)
    status = status_t1 + '   ' + status_t2
    return concept_reco, qualif_reco, status


def sup_treat(line): #determine quel traitement utiliser 
    words = generate_ngrams(line,1)
    tag = tagger(words)
    taggeur = tag[0]
    if 'mais' in words: 
        concept_reco, qualif_reco, status = treat_line_cplx(line, taggeur)
    else :
        concept_reco, qualif_reco, status = treat_line_simple(line)
    return concept_reco, qualif_reco, status

def treat_file(filename, file_result): #traite un fichier ligne par ligne et affiche le resultat pour chaque ligne du fichier 
    lines = recup_text(filename)
    result = open(file_result, 'w')
    result.write(filename + '\n')
    sol = ' '
    for line in lines: 
        concept_reco, qualif_reco, status = sup_treat(line)
        result.write('\n' + line )
        if qualif_reco and concept_reco:
            sol = 'reconnu :'+  str(concept_reco) +  ' qualifié par :' + str(qualif_reco) +  ' observé : '+ status + '\n'
        elif not concept_reco:
            sol = 'pas de concepts reconnus.\n'
        elif not qualif_reco:
            sol = 'reconnu :'+  str(concept_reco) +  ' observé : '+ status + '\n'
        result.write(sol)
 
