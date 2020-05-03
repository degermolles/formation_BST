#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


class BST():
    
    # constructreur
    def __init__(self,l):
        self.L = l # l est une liste, c'est notre tas

    
    @property 
    def n(self):
        ''' Nombre de noeud dans notre arbre
        '''
        return len(self.L)

    def hauteur(self):
        ''' Hauteur du tas
        '''
        return(int(math.floor(math.log(self.n,2))))
    
    def G(self, i):
        ''' G renvoie l'indice du noeud fils gauche étant donné l'indice du noeud
        '''
        return(2*i+1)
    
    def D(self, i):
        ''' D renvoie l'indice du noeud fils Droit étant donné l'indice du noeud
        A définir, voir wikipédia https://fr.wikipedia.org/wiki/Arbre_binaire
        '''
        pass
    
    def P(self, i):
        ''' P renvoie l'indice du noeud Père étant donné l'indice du noeud
        A définir, voir wikipédia https://fr.wikipedia.org/wiki/Arbre_binaire
        '''
        pass





# Fonction principale, Les fonctions que l'on va appeler ici dévront être définie avant.
# J'ai obté pour l'approche Class comme tu semblais le préférer
if __name__ == '__main__':
    print("Début!")

    # Example d'arbre
    arbre = BST([1,23,45,35,56])
    print("Nombre de noeud: ", arbre.n)
    # Point 1.
    print("Hauteur maximum et minimal d'un arbre: ", arbre.hauteur())


    print("Fin!")
