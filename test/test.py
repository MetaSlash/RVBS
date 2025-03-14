
# Deinir les clients

# Definir les refs des produits

# definir les quantitees des clients par refs 

# definir les familles et les correspondances aux refs

# fair les calcules des quantitées par refs et par client 

'''
ex : 
client 1 :
    a 4 de la ref 0

client 2:
    a 2 de la ref 1 et 4

client 3:
    a 12 de la ref 2 
    & 3  de la ref 3

afficher tout ça
'''

class Client:
    def __init__(self, nom):
        self.nom = nom
        self.commandes = {}

    def ajouter_commande(self, produit, quantite):
        # Recherche de la famille du produit dans le dictionnaire references
        famille_trouvee = None
        for famille, produits in references.items():
            if produit in produits:
                famille_trouvee = famille
                break

        if famille_trouvee:
            if famille_trouvee not in self.commandes:
                self.commandes[famille_trouvee] = {}
            self.commandes[famille_trouvee][produit] = quantite
        else:
            print(f"Produit '{produit}' non trouvé dans les références.")

    def __str__(self):
        commandes_str = "\n".join(
            f"    {quantite} {produit} de {famille}"
            for famille, produits in self.commandes.items()
            for produit, quantite in produits.items()
        )
        return f"{self.nom}:\n{commandes_str}"

# Références des produits
references = {
    "audio/video": {"écran": 0, "télé": 0, "enceinte": 0},
    "decorations": {"table": 0, "chaise": 0, "sillon": 0},
    "ordinateurs": {"ordinateur": 0, "clavier": 0, "souris": 0},
}

# Création des clients
client1 = Client("client 1")
client2 = Client("client 2")
client3 = Client("client 3")

# Ajout des commandes des clients
client1.ajouter_commande("écran", 4)
client2.ajouter_commande("chaise", 2)
client2.ajouter_commande("souris", 4)
client3.ajouter_commande("table", 12)
client3.ajouter_commande("ordinateur", 3)

# Affichage des commandes des clients
print("Quantités par référence et par client:")
print(client1)
print(client2)
print(client3)
