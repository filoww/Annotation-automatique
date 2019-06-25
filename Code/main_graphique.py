#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:02:14 2019

@author: oni
"""
import tkinter
import time
import tkinter.ttk as ttk
import os
from tkinter.ttk import *
import glob
from treatment_file import treat_file

anno= ''
temp = os.getcwd()
path = temp.replace('/Code','/Corpus')
liste_fichiers = glob.glob(path+'/Compte_rendu/*') #folder contains file to treat 
liste_fichiers = list(set(liste_fichiers))
ontology = glob.glob(path+'/Ontology/*')#folder contains ontology file

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
         annot+=('\n' + 
                 (str(concept.libele).replace("['","")).replace("']","") + '\n')
         annot+=('qualifiers : '+(str(concept.qualifieurs).replace('[','')).replace(']','') + '\n')
         annot+=('quantifiers : '+(str(concept.quantifieurs).replace('[','')).replace(']','') + '\n')
         annot+=('observed : ' + concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs == [] and concept.quantifieurs != []:
         annot+=('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
         annot+=('no qualifiers \n')
         annot+=('quantifiers : '+(str(concept.quantifieurs).replace('[','')).replace(']','') + '\n')
         annot+=('observed : ' +concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs != [] and concept.quantifieurs == []:
         annot+=('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
         annot+=('qualifiers : '+(str(concept.qualifieurs).replace('[','')).replace(']','') + '\n')
         annot+=('no quantifiers \n')
         annot+=('observed : ' +concept.stat+ '\n')
     elif concept.libele != [] and concept.qualifieurs == [] and concept.quantifieurs == []:
         annot+=('\n' + (str(concept.libele).replace("['","")).replace("']","") + '\n')
         annot+=('no qualifiers \n')
         annot+=('no quantifiers \n')
         annot+=('observed : ' +concept.stat+ '\n')
     return annot

#get the txt we want to annotate
def recup_file () :
    filename =  f.get()
    file_state = 1
    return filename, file_state

#get the xml ontology
def recup_onto () :
    onto_file = o.get()
    onto_state =  1
    return onto_state

#annotate all files
def treat_all_files():
    start_time = time.time()
    i = 1
    compteur = 0
    unit = 100/len(liste_fichiers)
    text_widget.config(fg = 'black')
    text_widget.delete('1.0', tkinter.END)
    text_widget.insert('1.0','\nCREATE ONTOLOGY DATA.......')
    for file in liste_fichiers: # on traite chaque fichier du répertoire compte rendu 
        file_result = path + '/result' + str(i) + '.txt'
        treat_file(file, file_result)
        text_widget.insert('1.0','\nDONE.........'+file.replace((path+'/Compte_rendu/'),''))
        progressBar["value"] = (compteur+1)*unit
        progressBar.update()
        progressBar["value"] = 0
        compteur = compteur +1
        i = i+1
    ex = time.time() - start_time 
    progressBar["value"] = 100
    progressBar.update()
    text_widget.delete('1.0', tkinter.END)
    text_widget.config(fg = '#00fa00')
    temp = 'ALL FILES TREATED IN  ' + str(round(ex,2)) +' SECONDS'
    text_widget.insert('5.0', temp)

#print the solution of ONE annotation
def annotation():
    file_state = 0
    onto_state = 0
    filename, file_state = recup_file()
    onto_state = recup_onto()
    if onto_state == 1 and file_state == 1:
        text_widget.delete('1.0', tkinter.END)
        text_widget.config(fg = 'black')
        text_widget.insert('1.0', 'Running analysis....')
        temp = treat_file(filename, '/home/oni/Bureau/result.txt')
        anno = affichage_propre(temp)
        text_widget.delete('1.0', tkinter.END)
        text_widget.insert('1.0', anno)
    elif onto_state == 0  and file_state == 1: 
        text_widget.delete('1.0', tkinter.END)
        text_widget.insert('1.0', "please specify ontology")
    elif onto_state == 1 and  file_state== 0 :  
        text_widget.delete('1.0', tkinter.END)
        text_widget.insert('1.0', "please specify a file ")
    else : 
        text_widget.delete('1.0', tkinter.END)
        text_widget.insert('1.0', "all fields are empty")


if __name__ == "__main__": 
    #generate window
    root = tkinter.Tk()
    root.title("CRAA")
    root.geometry("900x900")
    root.configure(bg = "#5b9ffe")
    
    #progressbar style's
    style = ttk.Style()
    style.theme_use('alt')
    style.configure("green.Horizontal.TProgressbar", foreground='#00fa00', background='#00fa00')
    
    #file 
    f = ttk.Combobox(root, values=liste_fichiers, width = 50)
    f.grid(row = 3 , padx = 10, pady = 10)
    
    #onto
    o =ttk.Combobox(root, values=ontology, width = 50)
    o.grid(row = 4 , padx = 10, pady = 10)
    
    #annotate button 
    a = ttk.Button(root, text ="Annotate")
    a.config(command = annotation)
    a.grid(row = 3, column = 1, padx = 10, pady = 10)
    
    #progressbar for complete annotation 
    progressBar = ttk.Progressbar(root, style = "green.Horizontal.TProgressbar", orient="horizontal", length=286,mode="determinate")
    progressBar.grid(row = 2, pady=10)
    
        
    #complete annotation button
    a2 = ttk.Button(root, text ="Annotate all files")
    a2.config(command = treat_all_files)
    a2.grid(row = 5, column = 0, padx = 10, pady = 10)
    
    #print zone
    text_widget = tkinter.Text(root)
    text_widget.config(state = 'normal')
    text_widget.grid(row = 1, padx = 40, pady = 40)
    
    root.mainloop()



















      