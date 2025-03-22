import os
from bs4 import BeautifulSoup
import re


def clean_text(text):
    if text:
        return re.sub(r'\s+', ' ', text).strip()
    return "N/A"

# to count stars


def extract_stars(cell):
    return str(len(cell.find_all('i', class_='fas fa-star')))


html_folder = 'FM24/FM24_WK/'

player_data = []

for filename in os.listdir(html_folder):
    if filename.endswith('.html'):
        filepath = os.path.join(html_folder, filename)

        # load the HTML content
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # parse HTML with BeautifulSoup
        soup = BeautifulSoup(content, 'lxml')

        # iterate through player rows
        for row in soup.select('tr'):
            player = {
                'Name': 'N/A',
                'Club': 'N/A',
                'Position': 'N/A',
                'Wage': 'N/A',
                'Cost': 'N/A',
                'Expiry': 'N/A',
                'Potential': 'N/A'
            }

            # extract player name
            name_tag = row.select_one('td.row-title a.item-title')
            if name_tag:
                player['Name'] = clean_text(name_tag.get_text())

            # extract club name
            club_tag = row.select('td.row-title div.small a.item-title')
            if len(club_tag) > 1:
                player['Club'] = clean_text(club_tag[1].get_text())

            # extract position
            position_tag = row.select_one('td:nth-of-type(4)')
            if position_tag:
                player['Position'] = clean_text(position_tag.get_text())

            # extract wage
            wage_tag = row.select_one('td:nth-of-type(5)')
            if wage_tag:
                player['Wage'] = clean_text(wage_tag.get_text())

            # extract cost
            cost_tag = row.select_one('td:nth-of-type(6)')
            if cost_tag:
                player['Cost'] = clean_text(cost_tag.get_text())

            # extract expiry date
            expiry_tag = row.select_one('td:nth-of-type(8)')
            if expiry_tag:
                player['Expiry'] = clean_text(expiry_tag.get_text())

            # extract potential (star rating)
            potential_tag = row.select_one('td:nth-of-type(10)')
            if potential_tag:
                player['Potential'] = extract_stars(potential_tag)

            # store valid player data
            if player['Name'] != 'N/A' and player['Club'] != 'N/A':
                player_data.append(player)

# display the extracted player information
for index, player in enumerate(player_data, start=1):
    print(f"{index}. {player['Name']} - {player['Club']} - {player['Position']} - {player['Wage']} - {player['Cost']} - {player['Expiry']} - {player['Potential']} Stars")
