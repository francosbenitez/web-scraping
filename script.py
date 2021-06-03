from bs4 import BeautifulSoup  # identify dif html elements
import requests                # load html
import pandas as pd            # data manipulation

url = "https://www.promiedos.com.ar/primera"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# specific HTML to extract
pos = soup.find(id = "promedios")
table = pos.find_all("tr", class_ = "ipr")
table += pos.find_all("tr", class_ = "pr")

# create function
def extract_table():
    """Precondition: html previously specified
       Postcondition: table in list format"""
    l = []
    for row in table:
        team = row.find_all("td")
        batch = list(map(lambda data: data.text, team))
        l.append(batch)
    return l

# create dataframe
df = pd.DataFrame(extract_table())
df = pd.DataFrame({'Equipo': pd.Series(df[1]),
              'T20': pd.Series(df[2]),
              'T21': pd.Series(df[3]),
              'Pts': pd.Series(df[4]),
              'PJ': pd.Series(df[5]),
              'Prom': pd.Series(df[6]),
              })
df = df.sort_values(by=["Prom"], ascending = False)
df = df.reset_index(drop = True)

# save df
df.to_csv("promiedos.csv")
