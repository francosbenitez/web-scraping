from bs4 import BeautifulSoup  # identify dif html elements
import requests                # load html
import pandas as pd            # data manipulation

def extract_promedios_table():
    url = "https://www.promiedos.com.ar/primera"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    pos = soup.find(id = "promedios")
    teams = [list(map(lambda data: data.text, row.find_all("td"))) for row in pos.find_all("tr", class_ = "ipr")]
    teams += [list(map(lambda data: data.text, row.find_all("td"))) for row in pos.find_all("tr", class_ = "pr")]
    headers = next(iter([list(map(lambda data: data.text, row.find_all("th"))) for row in pos.find_all("tr")]))
    df = pd.DataFrame(teams)
    df.columns = headers
    df = df.sort_values(by=["Prom"], ascending = False)
    df = df.reset_index(drop=True)
    return df
        
print(extract_promedios_table())
    
  