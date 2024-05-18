import requests
from bs4 import BeautifulSoup

#URL = "https://www.lddb.com/top100.php?id=11"
URL = "https://www.lddb.com/collection.php?action=list&user=jherioch&max=250"
# https://www.lddb.com/shop/top10.php
# https://www.lddb.com/shop/top10.php?month=2024-04
# https://www.lddb.com/shop/top10.php?month=2024-03
# https://www.lddb.com/shop/top10.php?month=2024-02
# https://www.lddb.com/shop/top10.php?month=2024-01

soup = BeautifulSoup(requests.get(URL).text, 'lxml')
n = 0

tables = soup.findAll("table")

for table_index, table in enumerate(tables):
    if table.findParent("table") is None:
        header = []
        rows = []
        for i, row in enumerate(table.find_all('tr')):
            # Check if the row has the desired class and id
            #if (('contents_0' in row.get('class', []) or 'contents_1' in row.get('class', [])) and row.get('id') == 'tr'):
                if i == 0:
                    header = [el.text.strip() for el in row.find_all('th')]
                else:
                    row_data = [el.text.strip().replace('\xa0', ' ').replace('\n', ' ').rstrip() for el in row.find_all('td')]
                    rows.append((table_index, row_data))

        for table_index, row in rows:
            print(f"Table {table_index}: {' | '.join(row)}")
            print()  # Add an extra newline for separation between rows
