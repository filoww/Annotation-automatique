#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:23:52 2019

@author: oni
"""

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import os 

def create_uniq_id(name, liste):
    if name in liste:
        return str(liste.index(name))
    else :
        liste.append(name)
        return str(liste.index(name))

def recup_text(file_source, file_cible):
    tree = ET.parse(file_source)
    root = tree.getroot()
    f = open(file_cible, 'w')
    for child in list(root):
        if child.tag == 'TestInfo':
            for child2 in list(child):
                if child2.tag  == 'TechnicalComment':
                    f.write(child2.text)
            
liste_file = os.listdir('/home/oni/SESSTIM/code/anonymisation/compte_rendu')
i = 0
for file in liste_file: 
    file_source= 'compte_rendu/'+file
    file_cible = 'compte_rendu_anno/anno_teste' +str(i) +'.txt'
    recup_text(file_source, file_cible)
    i = i +1