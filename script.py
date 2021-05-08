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

# # teams name
# equipos = []
# nombres = []
# for equipo in eq:
#     equipo = equipo.find_all("td")
#     equipos.append(equipo)
#     for equipo in equipos:
#         nombres.append(equipo[1].text)

# nombres = pd.unique(pd.Series(nombres))

# # teams T20
# equipos = []
# T20 = []
# for equipo in eq:
#     equipo = equipo.find_all("td")
#     equipos.append(equipo)
#     for equipo in equipos:
#         T20.append(equipo[2].text)

# T20 = pd.unique(pd.Series(T20))

# # teams T21
# equipos = []
# T21 = []
# for equipo in eq:
#     equipo = equipo.find_all("td")
#     equipos.append(equipo)
#     for equipo in equipos:
#         T21.append(equipo[3].text)

# T21 = pd.unique(pd.Series(T21))

# # teams pts
# equipos = []
# pts = []
# for equipo in eq:
#     equipo = equipo.find_all("td")
#     equipos.append(equipo)
#     for equipo in equipos:
#         pts.append(equipo[4].text)

# pts = pd.unique(pd.Series(pts))

# df = pd.DataFrame({"T20": T20, "PTS": pts})


    

    