from queue import Queue


class Noeud:
    def __init__(self, *args):
        if len(args) == 0:
            self.contenu = None
        else:
            self.contenu = (args[0], args[1], args[2])

        
    def etiquette (self):
        return(self.contenu[0])

    def gauche(self):
        return(self.contenu[1])
        
    def droit(self):
        return(self.contenu[2])
    
    def est_vide(self):
        return self.contenu == None
    
    def est_feuille(self):
        return self.gauche().est_vide() and self.droit().est_vide()
    
    def __repr__(self):
        return "()" if self.est_vide() else '(' + str(self.etiquette()) + str(self.gauche()) + str(self.droit()) + ')'

    
def hauteur(arbre):
    if arbre.est_vide():
        return 0
    else:
        return 1+max(hauteur(arbre.gauche()),hauteur(arbre.droit()))
    

arbol=Noeud('F',Noeud('B',Noeud('A',Noeud(),Noeud()),Noeud('D',Noeud('C',Noeud(),Noeud()),Noeud('E',Noeud(),Noeud()))),Noeud('G',Noeud(),Noeud('I',Noeud('H',Noeud(),Noeud()),Noeud())))

def afficher_A(a): #infixe
    if not a.est_vide():
        afficher_A(a.gauche())
        print(a.etiquette())
        afficher_A(a.droit())

def afficher_B(a): #postfixe
    if not a.est_vide():
        afficher_B(a.gauche())
        afficher_B(a.droit())
        print(a.etiquette())

def afficher_C(a): #prefixe
    if not a.est_vide():
        print(a.etiquette())
        afficher_C(a.gauche())
        afficher_C(a.droit())


def BFS(a):
    res = []
    s = Queue()
    s.enqueue(a)
    while not s.is_empty():
        x = s.dequeue()
        res.append(x.etiquette())
        if not x.est_feuille():
            if not x.gauche().est_vide():
                s.enqueue(x.gauche())
            if not x.droit().est_vide():
                s.enqueue(x.droit())
    return res
            


print(BFS(arbol))