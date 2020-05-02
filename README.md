# formation_BST

Introduction : 
Un tas est un arbre binaire ordonné d'entiers, dans le sens où les valeurs sont croissantes le long des branches.
Les tas sont des arbres presque complets: tous les niveaux sont remplis sauf éventuellemnt le dernier qui est rempli en partie et à partir de la gauche.
Les sommets de l'arbre sont numérotés selon un parcours en largeur (c'est à dire niveau par niveau, et sur chaque niveau de gauche à droite).
En particulier, la racine (élément d'indice 0) contient la plus petite valeur de la liste.
On vérifie (admis ici) que les indices des fils du sommet d'indice i sont les noeuds dindices 2i + 1 et 2i + 2.
Autrement dit, untas est codé par une liste L = [a0, ....., an-1]


1) On définit la hauteur p de l'arbre comme la longueur maximale des branches
Un arbre réduit à un unique élément (c'est à dire sa racine) est considérée de hauteur p=0
Exprimer p en fonction de n en utilisant la fonction (logarithme en base 2) et des
fonctions floor et ceil

2) Définir trois fonctions G(i), D(i) et P(i) qui étant donné un entier i renvoie les indices du fils Gauche,
du filq Droit et du Père d'un sommet d'indice i dans un tas, par exemple G(i) renvoie 2i + 1
Pour définir P(i), utiliser l'opérateur de division euclidienne //.
On prend par convention P(0) = 0

3) Ajout d'un élément dans un tas, On utilise le principe de percolation ascendante.
On commence par ajouter le nouvel élément x à la fin de la liste (en position n).
Puis on compare sa valeur à celle de son père et on procède par échange s'il est plus petit que lui.
Et on itère le procédé. Tant qu'il n'est pas à la racine et que sa valeur x est infèrieure à celle 
de spn pèren on procède à un échange en le plaçant à la place de son père.
On admet que le procédé aboutit bien à un tas.
Ecrire une procédure ajout (L, x) qui étant donné un tas représenté par la liste L modifie L 
de sorte à ajouter x au tas L = [0, 2, 4, 6, 8] ajout (L, 3) en [0, 2, 3, 6, 8, 4]


4) Suppression de la racine dans un tas L. On utilise le principe de percolation descendante.
Si le tas est composé d'un unique élément, le tas L devient vide, sinon on commence par remplacer
la racine par le dernier élément x de la liste (la liste perd donc un élément.
Tant que x n'est pas une feuille et que x est supérieur à l'un de ses fils, on échange x avec
le plus petit de ses fils.
Définir une procédure fonction supprimer (L) qui d'une part modifie le tas en supprimant la racine r 
(et en conservant la structure de tas) et d'autre part renvoie r (la valeur suprimée)
Par exemple, si L = [0, 2, 3, 6, 8, 4], supprime (L) modifie L en [2, 4, 3, 6, 8] et renvoie 0

5) Exprimer la complexité de ajout et supprime en fonction du nombre n d'éléments du tas.

6a) En utilisant les fonctions précédentes, définir une fonction triTas(L) qui étant donné un tas renvoie en O(n log n) opérations la liste triée de ses éléments.
6b)  En utilisant les fonctions précédentes, définir une fonction tas(M), qui étant donné une liste d'entiers M renvoie en O(n log n) opérations un tas L comportant les mêmes éléments que que M.
6c) En déduire une fonction triListe(M) qui utilisant étant donnée une liste d'entiers M renvoie la liste triée de ses éléments.
On obtient ainsi une fonction effectuant O(n log n) opérations.

7) On se propose d'améliorer la fonction tas(M) définie au 6b)
Le principe est de construire la structure du tas en procédant par dichotomie.
Pour simplifier la description, on note M(i) le sous arbre issu du sommet i : il s'agit dont d'une partie de la liste M correspondant 
aux descendants du sommet i. De façon analogue au 4)n on peut définir (le code n'est pas demandé ici) une procédure auxiliaire percol(M, i) qui :
Suppose que dans la liste M, les sous arbres M (2i +1) et M(2i + 2) sont des tas (s'ils existent).
Modifie M par percolation descendante de sorte à rtansformer M(i) en un tas (ayant les mêmes éléments). La procédure utilise (log m) opérations, où m est le nomre d'éléments du sous-arbre M(i).
Reùarque : Lorsque le sommet d'indice i est une feuille , percolation (M, i) ne modifie rien.
A) En déduire une prcédure tasPartiel(M, i) qui étant donné une liste M de longueur n et un entier i < n modifie les éléments du sous-arbre M(i) une structure de tas (pour le sous arbre uniquement).
Donner pour conclure la nouvelle fonction tas5m° en utilisant tasPartiel.
B) On note c(n) ke nombre d'opérations effectuées par la nouvelle fonction tas(M). On se limite désormais au cas où np = 2p - i (arbre complet).
A chaque étape, on effectue la construction du tas sur les deux sous-arbres (complets eux aussi), puis on obtient la strucrure de tas de l'arbre complet en utilisant une percolation descendante en O(p) opérations.
On a donc c(O) = 1 c(np) < 2c(np - i) + Kp pour tout entier p€N*, où np ^2p - 1.
Trouver une constante L telle que c(n) < Ln pour tout n de la forme np
