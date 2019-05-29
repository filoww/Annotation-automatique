#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:32:49 2019
,('','')
@author: oni
"""
from nltk.stem.snowball import FrenchStemmer

qualifieurs = ['fréquentes' , 'en salves' , 'isolées', 'bigéminées', 'avec aberration', 
               'lambeaux', 'Soutenue', 'non soutenue', 'Brèves', 'salves', 'lambeaux', 'en salves' , 
               'bigéminées', 'une ou plusieurs morphologie', 
               'répétitives', 'complexes', 'doublets', 'triplets','couplets', 'à couplage précoce', 'à couplage tardif',
               'à couplage variable',
               'Monomorphe', 'polymorphe', 'Soutenue', 'non soutenue', 'Brèves', 'salves', 'lambeaux', 'Droit', 'gauche', 'permanent', 
               'intermittent', 'chrono-dépendant','Diurne', 'nocturne', 'inappropriée', 'sur tout le nychémère', 'de haut degré', 
               'complet', 'permanent', 'intermittent', 'avec échappement', 'sans échappement', 'trés rare', 'rare', 'nombreux']
  



concept = [('Trouble du rythme', 'Trouble du rythme')
           ,('Arythmie','Trouble du rythme')
           ,('arythmie cardiaque','Trouble du rythme')
           ,('palpitations', 'Trouble du rythme')
           ,('Dysrythmies','Trouble du rythme')
           ,('dysrythmies cardiaques', 'Trouble du rythme')
           ,('TDR', 'Trouble du rythme')
           ,('rythme sinusal','rythme sinusal')
           ,('Arythmie sinusale','Arythmie sinusale')
           ,('Arret sinusale','Arret sinusale')
           ,('pause sinusale','Arret sinusale')
           ,('affection de loreillette','Maladie du sinus')
           ,('affection du noeud sinusal','Maladie du sinus')
           ,('affection du sinus','Maladie du sinus')
           ,('MRA','Maladie du sinus')
           ,('pathologie du sinus','Maladie du sinus')
           ,('bloc cardiaque','Bloc cardiaque')
           ,('dissociation isorythmique','Bloc cardiaque')
           ,('Dissociation atrio-ventriculaire','Bloc cardiaque')
           ,('Dissociation atrioventriculaire','Bloc cardiaque')
           ,('Dissociation auriculo-ventriculaire','Bloc cardiaque')
           ,('Dissociation auriculoventriculaire','Bloc cardiaque')
           ,('Bloc atrioventriculaire','Bloc atrioventriculaire')
           ,('Bloc de branche','Bloc de branche')
           ,('Bloc de branche droite','Bloc de branche droite')
           ,('Bloc de branche gauche','Bloc de branche gauche')
           ,('Bloc fasciculaire antérieur gauche','Bloc fasciculaire antérieur gauche')
           ,('Bloc fasciculaire postérieur gauche','Bloc fasciculaire postérieur gauche')
           ,('Bloc interauriculaire','Bloc interauriculaire')
           ,('Bloc de sortie sino-atrial','Bloc sinoauriculaire')
           ,('Bloc de sortie sino-auriculaire','Bloc sinoauriculaire')
           ,('Bloc sino-atrial','Bloc sinoauriculaire')
           ,('Bloc sino-auriculaire','Bloc sinoauriculaire')
           ,('Bloc sinoatrial','Bloc sinoauriculaire')
           ,('BSA','Bloc sinoauriculaire')
           ,('Lenègre','Maladie de Lenègre')
           ,('Adam Stokes','Syndrome Adam Stokes')
           ,('Brady-arythmies','Bradycardie')
           ,('Bradyarythmie','Bradycardie')
           ,('Bradycardie','Bradycardie')
           ,('fibrillation ventriculaire idiopathique','Brugada')
           ,('FVI','Brugada')
           ,('Commotio cordis','Commotio cordis')
           ,('Extrasystoles','Extrasystoles')
           ,('Extrasystolies','Extrasystoles')
           ,('Bigeminisme','Bigeminisme')
           ,('Extrasystoles auriculaire','Extrasystoles auriculaire')
           ,('Extrasystoles supraventriculaires','Extrasystoles auriculaire')
           ,('Extrasystolies supraventriculaires','Extrasystoles auriculaire')
           ,('Extrasystole atriale','Extrasystoles auriculaire')
           ,('ESA','Extrasystoles auriculaire')
           ,('Extrasystoles multifocale','Extrasystoles multifocale')
           ,('Extrasystoles ventriculaire','Extrasystoles ventriculaire')
           ,('Extrasystolies ventriculaire','Extrasystoles ventriculaire')
           ,('Extrasystolie ventriculaire','Extrasystoles ventriculaire')
           ,('extra-systolie ventriculaire','Extrasystoles ventriculaire')
           ,('ESV','Extrasystoles ventriculaire')
           ,('Fibrillation atriale','Fibrillation auriculaire')
           ,('arythmie complète','Fibrillation auriculaire')
           ,('FA','Fibrillation auriculaire')
           ,('Fibrillation auriculaire','Fibrillation auriculaire')
           ,('Fibrillation ventriculaire','Fibrillation ventriculaire')
           ,('FV','Fibrillation ventriculaire')
           ,('VF','Fibrillation ventriculaire')
           ,('flutter auriculaire','flutter auriculaire')
           ,('FA','flutter auriculaire')
           ,('Flutter atrial','flutter auriculaire')
           ,('flutter ventriculaire','flutter ventriculaire')
           ,('Parasystole','Parasystole'),('préexcitations ventriculaires','Préexcitation')
           ,('Syndrome de pré-excitation ventriculaire','Préexcitation')
           ,('VPE','Préexcitation')
           ,('PR court avec QRS normal','Lown_Ganong_Levine')
           ,('Syndrome du PR court isolé','Lown_Ganong_Levine')
           ,('Préexcitation ventriculaire type Mahaïm','Type mahaïm')
           ,('Syndrome de WPW','Wolf Parkinson White')
           ,('Syndrome WPW','Wolf Parkinson White')
           ,('WPW','Wolf Parkinson White')
           ,('QT long','QT long')
           ,('Andersen','Andersen')
           ,('QT long type 7','Andersen')
           ,('QT long type 1','Jervell_LangeNielsen')
           ,('QT long type 2','Jervell_LangeNielsen')
           ,('QT long type 3','Jervell_LangeNielsen')
           ,('Jervell','Jervell_LangeNielsen')
           ,('QT long-surdité','Jervell_LangeNielsen')
           ,('Romano Ward','Romano-Ward')
           ,('LQT1','Romano-Ward')
           ,('tachycardie','Tachycardie')
           ,('Tachyarythmie','Tachycardie')
           ,('Rythme réciproque paroxystique','Tachycardie paroxystique')
           ,('Tachycardie réciproque paroxystique','Tachycardie paroxystique')
           ,('Tachycardie paroxystique','Tachycardie paroxystique')
           ,('Tachycardie reciproque','Tachycardie reciproque')
           ,('Tachycardie par rythme réciproque','Tachycardie reciproque')
           ,('Tachycardie par réentrée intra-nodale','Réentrée intranodale')
           ,('TRIN','Réentrée intranodale')
           ,('Réentrée nodale sinoauriculaire','Réentrée nodale sinoauriculaire')
           ,('tachycardie par réentrée nodale SA','Réentrée nodale sinoauriculaire')
           ,('svt','Tachycardie supraventriculaire')
           ,('tachycardie atriale','Tachycardie supraventriculaire')
           ,('tsv','Tachycardie supraventriculaire')
           ,('Tachycardie supraventriculaires','Tachycardie supraventriculaire')
           ,('Tachycardie supra-ventriculaire','Tachycardie supraventriculaire')
           ,('Auriculaire ectopique','Auriculaire ectopique')
           ,('Tachycardie atriale ectopique','Auriculaire ectopique')
           ,('Jonctionelle ectopique','Jonctionelle ectopique')
           ,('Tachycardie ventriculaires','Tachycardie ventriculaire')
           ,('TV','Tachycardie ventriculaire')
           ,('RIVA','Rythme idioventriculaire accéléré')
           ,('rythme idio-ventriculaire accéléré','Rythme idioventriculaire accéléré')
           ,('tachycardie idioventriculaire','Rythme idioventriculaire accéléré')
           ,('Tachycardie ventriculaire gauche fasciculaire','Tachycardie ventriculaire gauche fasciculaire')
           ,('Tachycardie ventriculaire monomorphe','Tachycardie ventriculaire monomorphe')
           ,('Tachycardie ventriculaire paroxystique','Tachycardie ventriculaire paroxystique')
           ,('Tachycardie ventriculaire polymorphe','Tachycardie ventriculaire polymorphe')
           ,('Torsade de pointes','Torsade de pointes')
           ,('TDP','Torsade de pointes')
           ]


def racinize_all_concept(concept):
    concept_tiers = []
    stemmer = FrenchStemmer()
    for i in range(0,len(concept)):
        temp = concept[i][0].lower()
        temp2 = stemmer.stem(temp)
        concept_tiers.append((temp2, concept[i][1]))
    return concept_tiers

def racinize_all_qualifieurs(qualifieurs):
    iznogoud = []
    stemmer = FrenchStemmer()
    for i in range(0,len(qualifieurs)):
        temp = qualifieurs[i].lower()
        if temp == 'isolées':
            temp2 = 'isole'
        else :
            temp2 = stemmer.stem(temp)
        iznogoud.append(temp2)
    return iznogoud

