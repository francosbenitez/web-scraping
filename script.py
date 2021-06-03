from bs4 import BeautifulSoup  # identify dif html elements
import requests                # load html
import pandas as pd            # data manipulation

# function to extract different tables
def extract_table(table_type):
    url = "https://www.promiedos.com.ar/primera"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    pos = soup.find(id = table_type)
    teams = [list(map(lambda data: data.text, row.find_all("td"))) for row in pos.find_all("tr")]
    headers = next(iter([list(map(lambda data: data.text, row.find_all("th"))) for row in pos.find_all("tr")]))
    df = pd.DataFrame(teams)
    df.columns = headers
    return df

# create dataframe tables
promedios = extract_table("promedios")
posiciones = extract_table("tablaseccion")
goleadores = extract_table("goleadorest")

# save dataframe tables
promedios.to_csv("promedios.csv")
posiciones.to_csv("posiciones.csv")
goleadores.to_csv("goleadores.csv")

    
  