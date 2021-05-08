from bs4 import BeautifulSoup  # identify dif html elements
import requests                # load html
import pandas as pd            # data manipulation

url = "https://www.promiedos.com.ar/primera"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# specific HTML to extract
pos = soup.find(id = "promedios")
eq = pos.find_all("tr", class_ = "ipr")
eq += pos.find_all("tr", class_ = "pr")

# initialize lists
nameArray = []
statsArray = []
T20 = []
T21 = []
Pts = []
PJ = []
promArray = []

# team name
for equipo in eq:
    equipo = equipo.find_all("td")[1:2]
    lote = list(map(lambda data: str(data.text), equipo))
    nameArray.append(lote)

# t20, t21, pts & pj
for equipo in eq:
    equipo = equipo.find_all("td")[2:6]
    lote = list(map(lambda data: int(data.text), equipo))
    statsArray.append(lote)
    
for stat in statsArray:
    T20.append(stat[0])
    T21.append(stat[1])
    Pts.append(stat[2])
    PJ.append(stat[3])
        
# averages  
for equipo in eq:
    equipo = equipo.find_all("td")[6:]
    lote = list(map(lambda data: float(data.text), equipo))
    promArray.append(lote)
    
# create dataframe
df = pd.DataFrame({'Equipo': pd.Series(nameArray),
              'T20': pd.Series(T20),
              'T21': pd.Series(T21),
              'Pts': pd.Series(Pts),
              'PJ': pd.Series(PJ),
              'Prom': pd.Series(promArray),
              })

df = df.sort_values(by=["Prom"], ascending = False)
    
# save df
df.to_csv("Promiedos.csv")
        
        
        