#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:15:48 2019
@author: oni
"""

import glob
import time
from treatment_file import treat_file

if __name__ == "__main__":
    liste_file = glob.glob('/home/oni/SESSTIM/Corpus/Compte_rendu/*')
    i = 1
    compteur = 0
    print('CONSTITUTION DES DONNÉES DE L ONTOLOGY.......')
    start_time2 = time.time()
    for file in liste_file:
        start_time = time.time()
        file_result = '/home/oni/SESSTIM/Corpus/result' + str(i) + '.txt'
        treat_file(file, file_result)
        ex = time.time() - start_time 
        print('DONE.........'+file +  ' en '+ str(round(ex,2)) + ' secondes')
        i = i+1
        compteur = compteur +1 
    ex2 = time.time() - start_time2 
    print(str(compteur)+' fichiés traités avec succés en moyenne  ' + str(round(ex2,2)/compteur) + ' secondes')
    
    
#MODULE RELATION.PY PAS UTILISÉ