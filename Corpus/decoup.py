#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:23:00 2019

@author: oni
"""

file = open("Corpus.txt", "r")
lignes = file.readlines()
j =0
name = 'Compte_rendu/CompteRendu'+str(j)+'.txt'
f=open(name,'w')
for i in range(0, len(lignes)):
    lignes[i] = lignes[i].lower()
    lignes[i] = lignes[i].replace('\n','. \n')
    if lignes[i] == 'new. \n':
        j = j+1
        name = 'Compte_rendu/CompteRendu'+str(j)+'.txt'
        f=open(name,'w')
    else :
        f.write(lignes[i])
