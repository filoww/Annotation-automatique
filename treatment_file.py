#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:18:12 2019

@author: oni
"""
from tagg_concepts import reco_concept, reco_qualifieurs
from tagg_concepts import concepts, qualif


def recup_text(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    return lines

def treat_line(line):
    line = line.replace('é','e')
    concept_reco = reco_concept(concepts, line)
    qualif_reco = reco_qualifieurs(qualif, line)
    return concept_reco, qualif_reco

def treat_file(filename, file_result):
    lines = recup_text(filename)
    result = open(file_result, 'w')
    for line in lines: 
        concept_reco, qualif_reco = treat_line(line)
        result.write(filename + '\n     ' + line)
        sol = '\n'+  str(concept_reco) +  '\n' + str(qualif_reco)
        result.write(sol)
        
filename ='/home/oni/SESSTIM/Corpus/Compte_rendu/CompteRendu20.txt'
filecible = '/home/oni/SESSTIM/Corpus/EXTRA.txt'
treat_file(filename,filecible)