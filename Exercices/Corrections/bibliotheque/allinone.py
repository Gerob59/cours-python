class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self._titre = titre
        self._auteur = auteur
        self._annee_publication = annee_publication
        
    @property
    def titre(self):
        return self._titre
    
    @titre.setter
    def titre(self, valeur):
         self._titre = valeur
    
    @property
    def auteur(self):
        return self._auteur
    
    @auteur.setter
    def auteur(self, valeur):
         self._auteur = valeur
    
    @property
    def annee_publication(self):
        return self._annee_publication
    
    @annee_publication.setter
    def annee_publication(self, valeur):
         self._annee_publication = valeur

    def __str__(self) -> str:
        return f"Titre: {self.titre}\nAuteur: {self.auteur}\nAnnée de publication: {self.annee_publication}"

    def afficher_details(self):
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"Année de publication: {self.annee_publication}")


# livre = Livre("Livre 1", "Auteur 1", 2022)
# print(livre) # str
# livre.afficher_details() 

class Bibliotheque:
    def __init__(self):
        self.livres : [Livre] = []

    def ajouter_livre(self, livre: Livre) -> None:
        self.livres.append(livre)
        

    def retirer_livre(self, livre: Livre) -> None:
        if livre in self.livres:
            flag = self.livres.remove(livre)
        else:
            print(f"Le livre avec le titre '{self.titre}' n'est pas dans la bibliothèque.")
        

    def lister_livres(self):
        for livre in self.livres:
            # livre.afficher_details()
            print(livre)



bibliotheque = Bibliotheque()
mon_objet_livre = Livre("Livre 1", "Auteur 1", 2020)

bibliotheque.ajouter_livre(mon_objet_livre)
bibliotheque.lister_livres()
bibliotheque.retirer_livre(mon_objet_livre)
bibliotheque.lister_livres()