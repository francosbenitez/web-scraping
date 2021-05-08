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

equipos = list()
for equipo in eq:
    equipos.append(equipo.text)
 
print(equipos)

# create dataframe
# df = pd.DataFrame({"Nombre": equipos, "Puntajes": puntajes},
#               index = list(range(1, 21)))

# print(df)

# df.to_csv("Clasificación.csv", index = False)