#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:02:14 2019

@author: oni
"""

import tkinter
import tkinter.ttk as ttk
import glob
from tagging import onto_file
from treatment_file import treat_file

anno= ''

liste_fichiers = glob.glob('/home/oni/SESSTIM/Corpus/Compte_rendu/*')
ontology = glob.glob('/home/oni/SESSTIM/ontology/*')
file_state = 0
onto_state = 0

def affichage_propre(sol):
    annot = ''
    for concept in sol :
        if len(concept) > 1 :
            for i in range(0, len(concept)):
                annot = afficher_concept(concept[i], annot)
        else :
            annot = afficher_concept(concept[0], annot)
    return annot


def afficher_concept(concept, annot):
    if concept.libele != []  and concept.qualifieur != []:
        annot +=('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
        annot +=((str(concept.qualifieur).replace('[','')).replace(']','') + '\n')
        annot +=('présent : ' + concept.stat+ '\n')
    elif concept.libele != [] and concept.qualifieur == []:
        annot +=('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
        annot +=('aucun qualifieurs \n')
        annot +=('présent : ' +concept.stat+ '\n')
    return annot



root = tkinter.Tk()
root.title("Annotation Automatique de Compte Rendu")
root.geometry("900x900")
root.configure(bg = "#5b9ffe")
               


# s'occupe du fichier 
f = ttk.Combobox(root, values=liste_fichiers, width = 50)
f.grid(row = 2 , padx = 10, pady = 10)

def recup_file () :                     # récupére le fichier que l'on veut annoter
    filename =  f.get()
    file_state = 1
    return filename, file_state

b = tkinter.Button (root, text="select file")
b.config (command = recup_file)         
b.grid(row = 2, column = 1, padx = 10, pady = 10)

# s'occupe de l'onto 
o =ttk.Combobox(root, values=ontology, width = 50)
o.grid(row = 3 , padx = 10, pady = 10)
def recup_onto () :                     # récupére le fichier xml de l'ontologie 
    onto_file = o.get()
    onto_state =  1
    return onto_state
b2 = tkinter.Button (root, text="select onto")
b2.config (command = recup_onto)         
b2.grid(row = 3, column = 1, padx = 10, pady = 10)

# s'occupe de l'annot
def annotation():        # affiche la solution de l'annotation
    filename, file_state = recup_file()
    onto_state = recup_onto()
    if onto_state == 1 and file_state == 1:
        text_widget.delete('1.0', tkinter.END)
        text_widget.insert('1.0', 'Analyse en cours....')
        temp = treat_file(filename, '/home/oni/Bureau/result.txt')
        anno = affichage_propre(temp)
        text_widget.delete('1.0', tkinter.END)
        text_widget.insert('1.0', anno)
    elif onto_state == 0  and file_state == 1: 
        text_widget.delete('1.0', tkinter.END)
        text_widget.insert('1.0', "Veuillez spécifier l'ontology")
    elif onto_state == 1 and  file_state== 0 :  
        text_widget.delete('1.0', tkinter.END)
        text_widget.insert('1.0', "Veuillez spécifier le fichier ")
    else : 
        text_widget.delete('1.0', tkinter.END)
        text_widget.insert('1.0', "Tout les champs sont vides")

a = tkinter.Button(root, text ="Annoter")
a.config(command = annotation)
a.grid(row = 1, column = 1, padx = 10, pady = 10)
text_widget = tkinter.Text(root)
text_widget.config(state = 'normal')
text_widget.grid(row = 1, padx = 40, pady = 40)

root.mainloop()





      