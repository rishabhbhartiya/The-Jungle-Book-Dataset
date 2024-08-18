from bs4 import BeautifulSoup
import pandas as pd

file_path = '/Users/rishabhbhartiya/Desktop/The Jungle Book/index.html'

with open(file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

data = soup.find("table",class_ = "wikitable plainrowheaders")

table_data = data.findAll("tr", class_="vevent module-episode-list-row")

rows =[]

for row in table_data:
    cells = row.find_all(['th','td'])
    cells_text = [cell.get_text(strip=True) for cell in cells]
    if cells_text:  # avoid empty rows
        rows.append(cells_text)

df = pd.DataFrame(rows)

df.to_csv("The Jungle Book.csv")