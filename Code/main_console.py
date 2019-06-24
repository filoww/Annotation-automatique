#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:15:48 2019
@author: oni
"""

import glob
import os
import time
from treatment_file import treat_file


def treat_all_files():
    temp = os.getcwd()
    path = temp.replace('/Code','/Corpus')
    liste_file = glob.glob(path+'/Compte_rendu/*')
    i = 1
    compteur = 0
    print('CONSTITUTION DES DONNÉES DE L ONTOLOGY.......')
    start_time2 = time.time()
    for file in liste_file: # on traite chaque fichier du répertoire compte rendu 
        start_time = time.time()
        file_result = path + '/result' + str(i) + '.txt'
        treat_file(file, file_result)
        ex = time.time() - start_time 
        print('DONE.........'+file.replace('Corpus/Compte_rendu/','') +  ' en '+ str(round(ex,2)) + ' secondes')
        i = i+1
        compteur = compteur +1 
    ex2 = time.time() - start_time2 
    print(str(compteur)+' fichiés traités avec succés en moyenne  ' + str(round(ex2,2)/compteur) + ' secondes')

if __name__ == "__main__":
    treat_all_files()
#MODULE RELATION.PY PAS UTILISÉ