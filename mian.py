from bs4 import BeautifulSoup
import pandas as pd

file_path = '/Users/rishabhbhartiya/Desktop/The Jungle Book/index.html'

with open(file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

data = soup.find("table",class_ = "wikitable plainrowheaders")

table_data = data.findAll("tr", class_="expand-child")

description =[]

for text in table_data:
    summary = text.text
    description.append(summary)
    
df = pd.DataFrame(description)
df.to_csv("Summary.csv")

