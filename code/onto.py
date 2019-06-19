#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:32:33 2019

@author: oni
"""

from lxml import etree
import re 




def recup_onto(onto_file): #récupére les champs de l'ontologie dont on a besoin 
    result = []
    tree = etree.parse(onto_file)
    root = tree.getroot()
    for children in root.getchildren():
        for child2 in children.getchildren():
            if child2.tag == '{http://webprotege.stanford.edu/}RmpWmpzHL6dPyxWm6EyfUY':
                frere = child2.getnext()
                name = frere.text
                re.sub('_',' ', name)
                syn = child2.text
                tup = (name, syn)
                result.append(tup)
            if child2.tag == '{http://www.w3.org/2000/01/rdf-schema#}label' : 
                name = child2.text
                re.sub('_',' ', name)
                tup = (name,name)
                result.append(tup)
    del result[0:5]
    return result

def constit_dico(result): #constitut notre dico sous la forme (forme, libélé)
    result_final = []
    for tup in result:
        if tup[0] != tup[1]:
            string  = tup[1]
            string = string.replace('\n','')
            liste = string.split(', ')
            for elm in liste:          
                new = (elm.replace('_',' '), tup[0].replace('_',' '))
                result_final.append(new)
        else : 
            t1 = tup[0].replace('_',' ')
            t2 = tup[1].replace('_',' ')
            t =(t2,t1)
            result_final.append(t)
    return result_final
#ex : (esv, extrasystoles ventriculaire)
