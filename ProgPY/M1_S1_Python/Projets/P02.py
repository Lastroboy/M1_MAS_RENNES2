# 22200761 Noa DELAPORTE

# Section 1 : Import de module
import requests
import json
from pprint import pprint

# Section 2 : Fonctions
    
def scraping_data(url):
    http_headers = {'User-Agent': "Mozilla/5.0"}
    contenu_brut = requests.get(url, headers=http_headers)
    contenu_json = contenu_brut.json()

    return contenu_json


def ville_amis(adresse_amis):
    liste_ville_amis = []

    for amis in adresse_amis:
        ville = amis["adresse"]["ville"]
        if ville == "Château Gontier":
            ville = "Château-Gontier"
    
        liste_ville_amis.append(ville.upper())

    return liste_ville_amis


def hotels_par_ville(liste_ville_amis):
    hotels = {}

    for ville in liste_ville_amis:

        url = f"https://tabular-api.data.gouv.fr/api/resources/3ce290bf-07ec-4d63-b12b-d0496193a535/data/?page_size=200&COMMUNE__exact={ville}"
        adresse_hotels = scraping_data(url)
        
        for hotel in adresse_hotels["data"]:

            infos_hotel = {}
            infos_hotel["Nom"] = hotel["NOM COMMERCIAL"]
            infos_hotel["Adresse"] = hotel["ADRESSE"]
            infos_hotel["Classement"] = hotel["CLASSEMENT"]

            if ville in hotel["COMMUNE"]:
                if ville not in hotels:
                    hotels[ville] = []
                hotels[ville].append(infos_hotel)

    return hotels


def affiche_hotels(liste_hotels_par_ville):

    for ville, liste_hotels in liste_hotels_par_ville.items():

        print(f"Ville : {ville}")
        print("-" * (8 + len(ville)))
        
        for hotel in liste_hotels:
            nom = hotel.get("Nom", "Nom inconnu")
            adresse = hotel.get("Adresse", "Adresse inconnue")
            classement = hotel.get("Classement", "Classement inconnu")

            print(f"- {nom}")
            print(f"  Adresse : {adresse}")
            print(f"  Classement : {classement}\n")

        print("\n")



# Section 3 : Tests de fonctions définies et manipulations

url = "https://my-json-server.typicode.com/rtavenar/fake_api/adresses_amis"
adresse_amis = scraping_data(url)
# pprint(adresse_amis)

# url = "https://tabular-api.data.gouv.fr/api/resources/3ce290bf-07ec-4d63-b12b-d0496193a535/data/"
url = "https://tabular-api.data.gouv.fr/api/resources/3ce290bf-07ec-4d63-b12b-d0496193a535/data/?page_size=200&COMMUNE__exact=RENNES"
adresse_hotels = scraping_data(url)
# pprint(adresse_hotels)

liste_ville_amis = ville_amis(adresse_amis)
# print(liste_ville_amis)

liste_hotels_par_ville = hotels_par_ville(liste_ville_amis)
# pprint(liste_hotels_par_ville)

affiche_hotels(liste_hotels_par_ville)