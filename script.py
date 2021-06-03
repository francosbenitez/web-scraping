from bs4 import BeautifulSoup  # identify dif html elements
import requests                # load html
import pandas as pd            # data manipulation

# function to extract different tables
def extract_table(table_type, class_type=None):
    url = "https://www.promiedos.com.ar/primera"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    if class_type:
        pos = soup.find(id = table_type, class_= class_type)
    else:
        pos = soup.find(id = table_type)
    teams = [list(map(lambda data: data.text, row.find_all("td"))) for row in pos.find_all("tr")]
    headers = next(iter([list(map(lambda data: data.text, row.find_all("th"))) for row in pos.find_all("tr")]))
    df = pd.DataFrame(teams)
    df.columns = headers
    return df

# create dataframe tables
posiciones_zona_1 = extract_table("posiciones", class_type="tablesorter1")
posiciones_zona_2 = extract_table("posiciones", class_type="tablesorter2")
promedios = extract_table("promedios")
tabla_anual_2021 = extract_table("posiciones", class_type="tablesorter3")
goleadores = extract_table("goleadorest")

# save dataframe tables
posiciones_zona_1.to_csv("posiciones_zona_1.csv")
posiciones_zona_2.to_csv("posiciones_zona_2.csv")
promedios.to_csv("promedios.csv")
tabla_anual_2021.to_csv("tabla_anual_2021.csv")
goleadores.to_csv("goleadores.csv")

    
  