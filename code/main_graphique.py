#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:02:14 2019

@author: oni
"""
import tkinter
import tkinter.ttk as ttk
from tkinter.ttk import *
import glob
from tagging import onto_file
from treatment_file import treat_file

anno= ''

liste_fichiers = glob.glob('/home/oni/SESSTIM/Corpus/Compte_rendu/*') #repertoire contenant les fichiers à traiter
ontology = glob.glob('/home/oni/SESSTIM/ontology/*')#repertoire contenant l'ontology

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
     if concept.libele != []  and concept.qualifieurs != [] and concept.quantifieurs != []:
         annot+=('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
         annot+=('qualifieurs : '+(str(concept.qualifieurs).replace('[','')).replace(']','') + '\n')
         annot+=('quantifieurs : '+(str(concept.quantifieurs).replace('[','')).replace(']','') + '\n')
         annot+=('présent : ' + concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs == [] and concept.quantifieurs != []:
         annot+=('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
         annot+=('aucun qualitatifs \n')
         annot+=('quantifieurs : '+(str(concept.quantifieurs).replace('[','')).replace(']','') + '\n')
         annot+=('présent : ' +concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs != [] and concept.quantifieurs == []:
         annot+=('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
         annot+=('qualifieurs : '+(str(concept.qualifieurs).replace('[','')).replace(']','') + '\n')
         annot+=('aucun quantitatifs \n')
         annot+=('présent : ' +concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs == [] and concept.quantifieurs == []:
         annot+=('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
         annot+=('aucun qualitatifs \n')
         annot+=('aucun quantitatifs \n')
         annot+=('présent : ' +concept.stat+ '\n')
     return annot

# récupére le fichier que l'on veut annoter
def recup_file () :
    filename =  f.get()
    file_state = 1
    return filename, file_state

#récupére le fichier xml de l'ontologie 
def recup_onto () :
    onto_file = o.get()
    onto_state =  1
    return onto_state

#annoter tout les fichiers
def treat_all_files():
    i = 1
    compteur = 0
    unit = 100/len(liste_fichiers)
    text_widget.insert('1.0','\nCONSTITUTION DES DONNÉES DE L ONTOLOGY.......')
    for file in liste_fichiers: # on traite chaque fichier du répertoire compte rendu 
        file_result = '/home/oni/SESSTIM/Corpus/result' + str(i) + '.txt'
        treat_file(file, file_result)
        text_widget.insert('1.0','\nDONE.........'+file.replace('/home/oni/SESSTIM/Corpus/Compte_rendu/',''))
        progressBar["value"] = (compteur+1)*unit
        progressBar.update()
        progressBar["value"] = 0
        compteur = compteur +1
        i = i+1
    progressBar["value"] = 100
    progressBar.update()
    text_widget.delete('1.0', tkinter.END)
    text_widget.config(fg = '#00fa00')
    text_widget.insert('5.0','TOUT LES TEXTES ONT ÉTÉ TRAITÉS')

# affiche la solution de l'annotation
def annotation():
    file_state = 0
    onto_state = 0
    filename, file_state = recup_file()
    onto_state = recup_onto()
    if onto_state == 1 and file_state == 1:
        text_widget.delete('1.0', tkinter.END)
        text_widget.config(fg = 'black')
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


if __name__ == "__main__": 
    #generation de la fenetre
    root = tkinter.Tk()
    root.title("Annotation Automatique de Compte Rendu")
    root.geometry("900x900")
    root.configure(bg = "#5b9ffe")
    
    #style pour la progressbar
    style = ttk.Style()
    style.theme_use('alt')
    style.configure("green.Horizontal.TProgressbar", foreground='#00fa00', background='#00fa00')
    
    # s'occupe du fichier 
    f = ttk.Combobox(root, values=liste_fichiers, width = 50)
    f.grid(row = 3 , padx = 10, pady = 10)
    
    # s'occupe de l'onto 
    o =ttk.Combobox(root, values=ontology, width = 50)
    o.grid(row = 4 , padx = 10, pady = 10)
    
    #bouton annoter
    a = ttk.Button(root, text ="Annoter")
    a.config(command = annotation)
    a.grid(row = 3, column = 1, padx = 10, pady = 10)
    
    #barre de progression pour annotation compléte
    progressBar = ttk.Progressbar(root, style = "green.Horizontal.TProgressbar", orient="horizontal", length=286,mode="determinate")
    progressBar.grid(row = 2, pady=10)
    
        
    #bouton annoter tout
    a2 = ttk.Button(root, text ="Annoter tout les fichiers")
    a2.config(command = treat_all_files)
    a2.grid(row = 5, column = 0, padx = 10, pady = 10)
    
    #zone d'affichage
    text_widget = tkinter.Text(root)
    text_widget.config(state = 'normal')
    text_widget.grid(row = 1, padx = 40, pady = 40)
    
    root.mainloop()



















      