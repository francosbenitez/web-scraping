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

# function for each column
def extraer_datos(columna):
    equipos = []
    lista = []
    for equipo in eq:
        equipo = equipo.find_all("td")
        equipos.append(equipo)
        for equipo in equipos:
            lista.append(equipo[columna].text)
    lista = pd.unique(pd.Series(lista))
    return lista

equipos = extraer_datos(1)
T20 = extraer_datos(2)
T21 = extraer_datos(3)
Pts = extraer_datos(4)
PJ = extraer_datos(5)
Prom = extraer_datos(6)    

df = pd.DataFrame({'Equipos': pd.Series(equipos),
              'T20': pd.Series(T20),
              'T21': pd.Series(T21),
              'Pts': pd.Series(Pts),
              'PJ': pd.Series(PJ),
              'Prom': pd.Series(Prom),
              })

df.to_csv("Promiedos.csv")