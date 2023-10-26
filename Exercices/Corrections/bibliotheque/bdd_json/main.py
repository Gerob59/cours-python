from livre_empruntable import LivreEmpruntable
from bibliotheque import Bibliotheque


if __name__ == "__main__":
    bibliothèque = Bibliotheque()
    bibliothèque.charger_bibliotheque()

    while True:
        print("\nMenu:")
        print("1. Ajouter un livre")
        print("2. Retirer un livre")
        print("3. Afficher la liste des livres")
        print("4. Emprunter un livre")
        print("5. Retourner un livre")
        print("6. Rechercher un livre par titre")
        print("7. Quitter")

        choix = input("Faites votre choix : ")

        if choix == "1":
            titre = input("Titre du livre : ")
            auteur = input("Auteur du livre : ")
            annee_publication = input("Année de publication : ")
            livre = LivreEmpruntable(titre, auteur, annee_publication)
            bibliothèque.ajouter_livre(livre)
            print("Livre ajouté à la bibliothèque.")
            bibliothèque.sauvegarder_bibliotheque()

        elif choix == "2":
            titre = input("Titre du livre à retirer : ")
            bibliothèque.retirer_livre(titre)
            bibliothèque.sauvegarder_bibliotheque()

        elif choix == "3":
            print("Livres disponibles dans la bibliothèque:")
            bibliothèque.lister_livres()

        elif choix == "4":
            titre = input("Titre du livre à emprunter : ")
            bibliothèque.emprunter_livre(titre)
            bibliothèque.sauvegarder_bibliotheque()

        elif choix == "5":
            titre = input("Titre du livre à retourner : ")
            bibliothèque.retourner_livre(titre)
            bibliothèque.sauvegarder_bibliotheque()

        elif choix == "6":
            titre = input("Titre du livre à rechercher : ")
            for livre in bibliothèque.livres:
                if livre.titre == titre:
                    livre.afficher_details()
                    break
            else:
                print(
                    f"Aucun livre avec le titre '{titre}' trouvé dans la bibliothèque."
                )

        elif choix == "7":
            break
