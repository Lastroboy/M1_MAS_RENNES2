###### 22200761
###### Noa DELAPORTE

###### SECTION 1 : IMPORTS
import requests
import json
from pprint import pprint
from datetime import *

###### SECTION 2 : DEFINITION DE FONCTIONS ET DE CLASSES
def api_metros():
    url = "https://data.explore.star.fr/api/explore/v2.1/catalog/datasets/tco-metro-circulation-passages-tr/records?limit=-1&refine=precision%3ATemps%20r%C3%A9el"
    http_headers = {'User-Agent': "Mozilla/5.0"}
    contenu_brut = requests.get(url, headers=http_headers)
    contenu_json = contenu_brut.json()
    return contenu_json

def metro_par_station(nom_station):
    metros = api_metros()
    liste_metros = []

    for metro in metros["results"]:
        d = {}
        if metro["nomarret"] == nom_station and metro["depart"] != None:
            d["depart"] = datetime.fromisoformat(metro["depart"])
            d["destination"] = metro["destination"]
            d["ligne"] = metro["nomcourtligne"]
            liste_metros.append(d)
    return liste_metros

def prochain_metro(passages):
    d = {}
    for metro in passages:
        if (metro["ligne"], metro["destination"]) not in d.keys():
            d[(metro["ligne"], metro["destination"])] = metro["depart"]

        elif d[(metro["ligne"], metro["destination"])] > metro["depart"]:
            d[(metro["ligne"], metro["destination"])] = metro["depart"]
    return d

def affiche_horraires(nom_station):
    horraires = prochain_metro(metro_par_station(nom_station))

    print("********************************************")
    print(f"Bienvenue à la station {nom_station}")
    print("********************************************")

    for cle, val in horraires.items():
        print(f"Ligne {cle[0]}, direction {cle[1]} : prochain métro à {datetime.strftime(val, format="%H:%M:%S")}")
    print("********************************************")

class Calendrier:
    def __init__(self):
        self.liste_rdv = []

    def lire_depuis_fichier(self, nom_fichier_json):
        with open(nom_fichier_json, "r", encoding='utf-8') as fic_in:
            data = json.load(fic_in)

            for rdv in data:
                date_deb = datetime.fromisoformat(rdv["debut"]).date()
                heure_deb = datetime.fromisoformat(rdv["debut"]).time()
                date_fin = datetime.fromisoformat(rdv["fin"]).date()
                heure_fin = datetime.fromisoformat(rdv["fin"]).time()
                titre = rdv["titre"]
                lieu = rdv.get("lieu")

                rendez_vous = RendezVous(date_deb, heure_deb, date_fin, heure_fin, titre, lieu)
                self.liste_rdv.append(rendez_vous)
        
    def __repr__(self):
        return f"<Calendrier contenant {len(self.liste_rdv)} rendez-vous>"
    
    def supprime_doublons(self):
        uniques = []
        for rdv in self.liste_rdv:
            if rdv not in uniques:
                uniques.append(rdv)
        self.liste_rdv = uniques
    
    def ajoute_rdv(self, rdv):
        self.liste_rdv.append(rdv)

    def union(self, other):
        nouveau = Calendrier()

        nouveau.liste_rdv = self.liste_rdv + other.liste_rdv
        nouveau.supprime_doublons()

        return nouveau

class RendezVous:
    def __init__(self, date_deb, heure_deb, date_fin, heure_fin, titre, lieu=None):
        self.date_deb = date_deb
        self.heure_deb = heure_deb
        self.date_fin = date_fin
        self.heure_fin = heure_fin
        self.titre = titre
        self.lieu = lieu

    def __eq__(self, other):
        return (
        self.date_deb == other.date_deb and
        self.heure_deb == other.heure_deb and
        self.date_fin == other.date_fin and
        self.heure_fin == other.heure_fin and
        self.titre == other.titre and
        self.lieu == other.lieu
    )

    def __repr__(self):
        return (f"RDV : {self.titre} à {self.lieu}, le {self.date_deb.strftime('%d/%m/%Y')} à {self.heure_deb.strftime('%H:%M:%S')} et fin le {self.date_fin.strftime('%d/%m/%Y')} à {self.heure_fin.strftime('%H:%M:%S')}.")

###### SECTION 3 : TESTS

# Partie 1 : Les passages de métros

# metros = api_metros()
# print(len(metros["results"]))
# pprint(metros["results"])

# # Question 1
# metros_gares = metro_par_station("Gares")
# pprint(metros_gares)

# print(50 * "#")

# horaires_passages = prochain_metro(metros_gares)
# pprint(horaires_passages)

# affiche_horraires("Gares")

# Partie 2 : La gestion de calendriers

# Question 2
c1 = Calendrier()
c1.lire_depuis_fichier("./data/cal01.json")
print(c1.liste_rdv)
print(50 * "#")

# Question 3
print(c1) # <Calendrier contenant 2 rendez-vous>
print(50 * "#")

# Question 4
r1 = RendezVous(
    date_deb=datetime.fromisoformat("2025-01-15T14:00:00").date(),
    heure_deb=datetime.fromisoformat("2025-01-15T14:00:00").time(),
    date_fin=datetime.fromisoformat("2025-01-15T15:00:00").date(),
    heure_fin=datetime.fromisoformat("2025-01-15T15:00:00").time(),
    titre="Réunion projet 2",
    lieu="Salle 204")

r2 = RendezVous(
    date_deb=datetime.fromisoformat("2025-01-15T14:00:00").date(),
    heure_deb=datetime.fromisoformat("2025-01-15T14:00:00").time(),
    date_fin=datetime.fromisoformat("2025-01-15T15:00:00").date(),
    heure_fin=datetime.fromisoformat("2025-01-15T15:00:00").time(),
    titre="Réunion projet 2",
    lieu="Salle 204")

print(r1 == r2)
print(50 * "#")

# Question 5
c1.ajoute_rdv(r1)
c1.ajoute_rdv(r2)
print(c1)
c1.supprime_doublons()
print(c1)
print(50 * "#")

# Question 7
r3 = RendezVous(
    date_deb=datetime.fromisoformat("2025-02-10T09:30:00").date(),
    heure_deb=datetime.fromisoformat("2025-02-10T09:30:00").time(),
    date_fin=datetime.fromisoformat("2025-02-10T10:30:00").date(),
    heure_fin=datetime.fromisoformat("2025-02-10T10:30:00").time(),
    titre="Entretien de stage",
    lieu="Bureau RH"
)

r4 = RendezVous(
    date_deb=datetime.fromisoformat("2025-03-22T16:00:00").date(),
    heure_deb=datetime.fromisoformat("2025-03-22T16:00:00").time(),
    date_fin=datetime.fromisoformat("2025-03-22T18:00:00").date(),
    heure_fin=datetime.fromisoformat("2025-03-22T18:00:00").time(),
    titre="Anniversaire de Pierre",
    lieu="Restaurant Le Patio"
)

r5 = RendezVous(
    date_deb=datetime.fromisoformat("2025-04-03T08:15:00").date(),
    heure_deb=datetime.fromisoformat("2025-04-03T08:15:00").time(),
    date_fin=datetime.fromisoformat("2025-04-03T09:00:00").date(),
    heure_fin=datetime.fromisoformat("2025-04-03T09:00:00").time(),
    titre="Consultation médicale",
    lieu="Clinique Saint-Michel"
)
c2 = Calendrier()
c2.ajoute_rdv(r2)
c2.ajoute_rdv(r3)
c2.ajoute_rdv(r4)
c2.ajoute_rdv(r5)
print(c2)

c3 = c1.union(c2)
print(c3)
print(50 * "#")

print(c3) # <Calendrier contenant 5 rendez-vous>
print(c3.liste_rdv)
