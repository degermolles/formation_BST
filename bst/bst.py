#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################################################
#################################### Zone import modules ##################################
import math
###########################################################################################
#################################### Création d'une classe ################################
class BST():
    
    # constructreur
    def __init__(self,l):
        self.L = self.tas(l) # l est un tas.
############################################################################################
	@property 
    def n(self): 
        if self.root is None:    # Nombre de noeud dans notre arbre
			return 0
		stack = Stack()
		stack.push(self.root) 
		
		size = 1
		while stack:
		node = stack.pop
		if node.left:
			n += 1
			stack.push(node.left)
		if node.right:
			n += 1
			stack.push(node.right)
		return len(self.L)

    @property 
    def hauteur(self, node):
        if node is None:  # Hauteur du tas
			return - 1
		g_hauteur = hauteur(node.left)
        d_hauteur = hauteur(node.right)
        return(int(math.floor(math.log(self.n,2))))
    
    def G(self, i):
        if G < self.i:  # G renvoie l'indice du noeud fils gauche étant donné l'indice du noeud
       
        return(2*i+1)
    
    def D(self, i):
        if D > self.i:  # D renvoie l'indice du noeud fils Droit étant donné l'indice du noeud
						# A définir, voir wikipédia https://fr.wikipedia.org/wiki/Arbre_binaire
        
        return(2*i+2)
    
    def P(self, i):
        if P(0) // i = 0:  # P renvoie l'indice du noeud Père étant donné l'indice du noeud
							# A définir, voir wikipédia https://fr.wikipedia.org/wiki/Arbre_binaire
        
        return (int(math.floor(i-1)/2))
		
	def ajout(self, l): # On ajoute un élément dans un tas
		nouveau = self.l
		file = []
		file.append(self)
		while (len(file) > 0):
			node = file.pop(o)   # On retire l'élément en tête de la file
			
			if node.gauche is None:  # si l'enfant gauche est vide
				none.gauche = nouveau
				break
				
			elif node.droit is None:  # si l'enfant droit est vide
				none.droit = nouveau
				break
				
			else:
				file.append(node.gauche)
				file.append(node.droit)
				

    def tas(self, l):
        '''tas converti une list en un tas
        Pour l'instant, elle ne fait rien (voir question 6b), elle retourne juste la liste
        que nous considérerons comme un tas (pour l'instant...)
        '''
        return(l)


# Fonction principale, Les fonctions que l'on va appeler ici devront être définie avant.
# J'ai obté pour l'approche Class comme tu semblais le préférer
if __name__ == '__main__':
    print("Début!")

    # Example d'un
    notreTas = [1,23,45,35,56]
    print(notreTas)
    arbre = BST(notreTas)
    print("Nombre de noeud: ", arbre.n)
    # Point 1.
    print("Hauteur d'un tas: ", arbre.hauteur)

    print("Fin!")
