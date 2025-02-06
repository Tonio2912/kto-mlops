#Exercice de controle continu : écriture de la fonction names vu précédemment selon les principes du clean code, tout en utilisant le test unitaire 

import unittest
from typing import List

#Améliorations apportées :
# Fusion des fonctions pour éviter la duplication de code.
# Ajout du paramètre `seuil` pour une flexibilité accrue, et également pour éviter les nombres magiques.
# Ajout d’un paramètre `afficher` pour activer/désactiver l'affichage.
# Optimisation avec `sum()` pour compter sans boucle explicite.
# Ajout d'annotations de type pour améliorer la lisibilité et éviter les erreurs.
# Mise à jour des tests unitaires pour vérifier le comportement avec et sans affichage.

def analyser_prenoms(prenoms: List[str], seuil: int = 7, afficher: bool = True) -> int:
    """
    Analyse une liste de prénoms : affiche leur longueur par rapport au seuil et retourne le nombre de prénoms longs.

    :param prenoms: Liste des prénoms à analyser
    :param seuil: Longueur minimale pour qu’un prénom soit considéré comme long
    :param afficher: Indique si les résultats doivent être affichés
    :return: Nombre de prénoms dépassant le seuil
    """
    compteur = sum(1 for prenom in prenoms if len(prenom) > seuil)

    if afficher:
        for prenom in prenoms:
            comparaison = "supérieur" if len(prenom) > seuil else "inférieur ou égal"
            print(f"{prenom} est un prénom avec un nombre de lettres {comparaison} à {seuil}.")

    return compteur

class TestAnalyserPrenoms(unittest.TestCase):
    """
    Classe de tests unitaires pour la fonction analyser_prenoms.
    """

    def test_seuil_par_defaut(self) -> None:
        """
        Vérifie que la fonction compte correctement les prénoms longs avec le seuil par défaut (7).
        """
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        self.assertEqual(analyser_prenoms(prenoms, afficher=False), 4)

    def test_seuil_personnalise(self) -> None:
        """
        Vérifie que la fonction compte correctement avec un seuil personnalisé.
        """
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        self.assertEqual(analyser_prenoms(prenoms, seuil=8, afficher=False), 2)

    def test_aucun_prenom_long(self) -> None:
        """
        Vérifie le comportement lorsque tous les prénoms sont courts.
        """
        prenoms = ["Leo", "Anna", "Paul", "Eve"]
        self.assertEqual(analyser_prenoms(prenoms, afficher=False), 0)

    def test_tous_les_prenoms_longs(self) -> None:
        """
        Vérifie le comportement lorsque tous les prénoms sont longs.
        """
        prenoms = ["Guillaume", "Théophile", "Cassandre", "Frédérique"]
        self.assertEqual(analyser_prenoms(prenoms, afficher=False), len(prenoms))

    def test_liste_vide(self) -> None:
        """
        Vérifie que la fonction retourne 0 avec une liste vide.
        """
        self.assertEqual(analyser_prenoms([], afficher=False), 0)

if __name__ == '__main__':
    unittest.main()

