import requests
from bs4 import BeautifulSoup
import json

class OpenFactFood:


    def category(self):

        
        self.liste = []

        path = "https://fr.openfoodfacts.org/categories"
        
        requete = requests.get(path)
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")
        for tag in soup.find_all("td"):
            self.liste.append(tag.text)

        print(self.liste)

        c = 0
        for i in range(3):
            print(self.liste[c])

            c+=3


































































yo = OpenFactFood()
yo.category()
