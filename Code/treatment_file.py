#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:18:12 2019

@author: oni
"""
from tagging import reco_concept, reco_quali, reco_quanti
from lemmat import generate_ngrams, tagger
from negation import neg, status_neg
from data import Concept

def recup_text(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    return lines

def treat_line_simple(line): #treat a simple line 80% of cases 
    line = line.replace('é','e')
    concept_reco = reco_concept(line)
    qualif_reco = reco_quali(line)
    quanti_reco = reco_quanti(line)
    status = status_neg(neg, line)
    return concept_reco, qualif_reco,quanti_reco, status

def treat_line_cplx(line,tag, cible): #treat the two parts sentences 
    temp = ''
    temp2 = ''
    concept_reco = []
    qualif_reco = []
    quanti_reco = []
    status = []
    i = 0
    while tag[i]!= cible:
        temp +=  tag[i][0] + ' '
        i += 1
    for j in range(i, len(tag)):
        temp2 = temp2 + tag[j][0] + ' '
    concept_reco_t1, qualif_reco_t1, quanti_reco_t1, status_t1 = treat_line_simple(temp.replace(cible[0],''))   
    concept_reco_t2, qualif_reco_t2, quanti_reco_t2, status_t2 = treat_line_simple(temp2)
    concept_reco.append(concept_reco_t1)  
    concept_reco.append(concept_reco_t2)
    qualif_reco.append(qualif_reco_t1)
    qualif_reco.append(qualif_reco_t2)
    quanti_reco.append(quanti_reco_t1)
    quanti_reco.append(quanti_reco_t2)
    status.append(status_t1)
    status.append(status_t2)
    return concept_reco, qualif_reco, quanti_reco, status

def sup_treat(line): #determine if its a simple or cplx treatment
    words = generate_ngrams(line,1)
    tag = tagger(words)
    taggeur = tag[0]
    liste_concept = []
    Trigger = False
    if 'mais' in words: 
        concept_reco, qualif_reco, quanti_reco, status = treat_line_cplx(line, taggeur, ('mais', 'CC'))
        for i in range(0,len(concept_reco)):
            if concept_reco[i] is not None:
                concept = Concept(concept_reco[i], quanti_reco[i], qualif_reco[i], status[i])
                liste_concept.append(concept)
            else : 
                concept = None 
                liste_concept.append(concept)
    elif 'sans' in words:
        concept_reco, qualif_reco, quanti_reco, status = treat_line_cplx(line, taggeur, ('sans', 'P'))
        for i in range(0,len(concept_reco)):
            if concept_reco[i] is not None:
                concept = Concept(concept_reco[i], quanti_reco[i], qualif_reco[i], status[i])
                liste_concept.append(concept)
                Trigger = True
            else : 
                concept = None 
                liste_concept.append(concept)
    else :
        concept_reco, qualif_reco, quanti_reco, status = treat_line_simple(line)
        if concept_reco is not None: 
            concept = Concept(concept_reco, quanti_reco, qualif_reco,  status )
            liste_concept.append(concept)
        else : 
            concept = None
            liste_concept.append(concept)
    return  liste_concept

def afficher_concept(concept, result): #print one concept
     if concept.libele != []  and concept.qualifieurs != [] and concept.quantifieurs != []:
         result.write('\n' + ((str(concept.libele).replace("['","")).replace("']","")).replace("'","") + '\n')
         result.write('qualifiers : '+(str(concept.qualifieurs).replace('[','')).replace(']','') + '\n')
         result.write('quantifiers : '+(str(concept.quantifieurs).replace('[','')).replace(']','') + '\n')
         result.write('orbserved : ' + concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs == [] and concept.quantifieurs != []:
         result.write('\n' + ((str(concept.libele).replace("['","")).replace("']","")).replace("'","") + '\n')
         result.write('no qualifiers \n')
         result.write('quantifiers : '+(str(concept.quantifieurs).replace('[','')).replace(']','') + '\n')
         result.write('orbserved : ' +concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs != [] and concept.quantifieurs == []:
         result.write('\n' + ((str(concept.libele).replace("['","")).replace("']","")).replace("'","") + '\n')
         result.write('qualifiers : '+(str(concept.qualifieurs).replace('[','')).replace(']','') + '\n')
         result.write('no quantifiers \n')
         result.write('orbserved : ' +concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs == [] and concept.quantifieurs == []:
         result.write('\n' + ((str(concept.libele).replace("['","")).replace("']","")).replace("'","") + '\n')
         result.write('no qualifiers \n')
         result.write('no quantifiers \n')
         result.write('orbserved : ' +concept.stat+ '\n')
         

def affichage_solution(sol, result): #print a bunch of concepts
    for concept in sol :
        if len(concept) > 1 :
            for i in range(0, len(concept)):
                afficher_concept(concept[i], result)
        else :
            afficher_concept(concept[0], result)
                        
def treat_file(filename, file_result): #treat a file line by line  
    lines = recup_text(filename)
    result = open(file_result, 'w')
    result.write(filename + '\n\n')
    result.write('-'*20+'\n')
    sol = []
    for line in lines: 
        liste_concept = sup_treat(line)
        result.write(line)
        sol.append(liste_concept)
    result.write('-'*20)
    affichage_solution(sol, result) 
    return sol













