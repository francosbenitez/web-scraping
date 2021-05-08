from bs4 import BeautifulSoup  # identify dif html elements
import requests                # load html
import pandas as pd            # data manipulation

url = "https://www.promiedos.com.ar/primera"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# teams
pos = soup.find(id = "promedios")
eq = pos.find_all("tr", class_ = "ipr")
eq += pos.find_all("tr", class_ = "pr")

# teams name
equipos = []
nombres = []
for equipo in eq:
    nombre = equipo.find_all("td")
    equipos.append(nombre)
    for i in equipos:
        nombres.append(i[1].text)

nombres = pd.unique(pd.Series(nombres))
    

    