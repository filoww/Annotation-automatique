#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:15:28 2019

@author: oni
"""
#NOT USE IN THE PROJECT 

from lemmat import tagger, generate_ngrams,racinisation
from treatment_file import treat_line
from tagg_concepts import mots_reconu, filtrage_solution

s = 'rythme sinusal permanent pas de troubles rythmiques pas d episodes de bradycardie cardiaque significative extrasystolie ventriculaire charge autour de 7.5% pas de pauses cardiaques significatives'
new_s =''

words = generate_ngrams(s,1)
temp = tagger(words)
tag = temp[0]
for i in range(0, len(tag)):
    if tag[i][1] == 'ADJ' or tag[i][1] == 'NC':
        new_s = new_s + tag[i][0] + ' '
        
print(new_s)
treat_line(new_s)

mots = [] 
for i in range(1, 5):
    temp = generate_ngrams(new_s, i)
    mots = mots + racinisation(temp) 
result = []
reco = mots_reconu
for mot in mots :
    for W in reco:
        if mot == W:
            result.append(mot)
result = filtrage_solution(result)
print(result)

trys = ''
for elm in mots:
    if elm in result:
        trys = trys + elm + ' '
print(trys)
        
   


