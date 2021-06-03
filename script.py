from bs4 import BeautifulSoup  # identify dif html elements
import requests                # load html
import pandas as pd            # data manipulation

def extract_table(table_type):
    url = "https://www.promiedos.com.ar/primera"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    pos = soup.find(id = table_type)
    teams = [list(map(lambda data: data.text, row.find_all("td"))) for row in pos.find_all("tr", class_ = "ipr")]
    teams += [list(map(lambda data: data.text, row.find_all("td"))) for row in pos.find_all("tr", class_ = "pr")]
    headers = next(iter([list(map(lambda data: data.text, row.find_all("th"))) for row in pos.find_all("tr")]))
    df = pd.DataFrame(teams)
    df.columns = headers
    df = df.sort_values(by=["#"], ascending = False)
    df = df.reset_index(drop=True)
    return df
        
posiciones = extract_table("posiciones")
promedios = extract_table("promedios")

    
  