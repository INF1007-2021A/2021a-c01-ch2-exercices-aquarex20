#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    longueur=len(mot)
    liste=[]
    i=0
    for lettre in mot:
        liste.append(chr(ord(lettre)-32))
    mot_maj=str()
    while i<longueur:
        mot_maj+=liste[i]
        i+=1
    return mot_maj



if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
