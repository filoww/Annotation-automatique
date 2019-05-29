#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:15:48 2019

@author: oni
"""

import glob
from treatment_file import treat_file

if __name__ == "__main__":
    liste_file = glob.glob('/home/oni/SESSTIM/Corpus/Compte_rendu/*')
    i = 0
    for file in liste_file:
        file_result = '/home/oni/SESSTIM/Corpus/result' + str(i) + '.txt'
        treat_file(file, file_result)
        i = i+1