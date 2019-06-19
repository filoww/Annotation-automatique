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

def treat_line_simple(line): #traitement d'une ligne simple, 80% des cas
    line = line.replace('é','e')
    concept_reco = reco_concept(line)
    qualif_reco = reco_quali(line)
    quanti_reco = reco_quanti(line)
    status = status_neg(neg, line)
    return concept_reco, qualif_reco,quanti_reco, status

def treat_line_cplx(line,tag): #phrase en 2 partie obligatoire pour relation
    temp = ''
    temp2 = ''
    concept_reco = []
    qualif_reco = []
    quanti_reco = []
    status = []
    i = 0
    cible = ('mais', 'CC')
    while tag[i]!= cible:
        temp +=  tag[i][0] + ' '
        i += 1
    for j in range(i, len(tag)):
        temp2 = temp2 + tag[j][0] + ' '
    concept_reco_t1, qualif_reco_t1, quanti_reco_t1, status_t1 = treat_line_simple(temp)   
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

def sup_treat(line): #determine quel traitement utiliser 
    words = generate_ngrams(line,1)
    tag = tagger(words)
    taggeur = tag[0]
    liste_concept = []
    if 'mais' in words: 
        concept_reco, qualif_reco, quanti_reco, status = treat_line_cplx(line, taggeur)
        for i in range(0,len(concept_reco)):
            if concept_reco[i] is not None:
                concept = Concept(concept_reco[i], quanti_reco[i], qualif_reco[i], status[i])
                liste_concept.append(concept)
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
    return liste_concept

def afficher_concept(concept, result): #affiche un seul concept
     if concept.libele != []  and concept.qualifieurs != [] and concept.quantifieurs != []:
         result.write('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
         result.write('qualifieurs : '+(str(concept.qualifieurs).replace('[','')).replace(']','') + '\n')
         result.write('quantifieurs : '+(str(concept.quantifieurs).replace('[','')).replace(']','') + '\n')
         result.write('présent : ' + concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs == [] and concept.quantifieurs != []:
         result.write('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
         result.write('aucun qualifieurs \n')
         result.write('quantifieurs : '+(str(concept.quantifieurs).replace('[','')).replace(']','') + '\n')
         result.write('présent : ' +concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs != [] and concept.quantifieurs == []:
         result.write('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
         result.write('qualifieurs : '+(str(concept.qualifieurs).replace('[','')).replace(']','') + '\n')
         result.write('aucun quantifieurs \n')
         result.write('présent : ' +concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs == [] and concept.quantifieurs == []:
         result.write('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
         result.write('aucun qualifieurs \n')
         result.write('aucun quantifieurs \n')
         result.write('présent : ' +concept.stat+ '\n')
         

def affichage_solution(sol, result): #affiche l'ensemble des concepts reconnus
    for concept in sol :
        if len(concept) > 1 :
            for i in range(0, len(concept)):
                afficher_concept(concept[i], result)
        else :
            afficher_concept(concept[0], result)
                        
def treat_file(filename, file_result): #traite un fichier ligne par ligne et affiche le resultat pour chaque ligne du fichier 
    lines = recup_text(filename)
    result = open(file_result, 'w')
    result.write(filename + '\n\n')
    sol = []
    for line in lines: 
        liste_concept = sup_treat(line)
        result.write(line )
        sol.append(liste_concept)
    affichage_solution(sol, result) 
    return sol


treat_file('/home/oni/SESSTIM/Corpus/Compte_rendu/CompteRendu2.txt','result.txt')
















