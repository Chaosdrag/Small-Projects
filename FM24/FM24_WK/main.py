import os
import re
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

# initialize Flask app
app = Flask(__name__)

# to clean up whitespace and newlines


def clean_text(text):
    if text:
        return re.sub(r'\s+', ' ', text).strip()
    return "N/A"

# to count stars (potential rating)


def extract_stars(cell):
    return str(len(cell.find_all('i', class_='fas fa-star')))


# directory containing HTML files
html_folder = 'HelloWorld\FM24\FM24_WK'

# to parse HTML files and collect player data


def load_players():
    player_data = []

    # loop through all HTML files in the specified folder
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
                    'Potential': 'N/A',
                    'Age': 'N/A'
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
                cost_tag = row.select_one('td:nth-of-type(7)')
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

                # extract age
                age_tag = row.select_one('td:nth-of-type(3)')
                if age_tag:
                    player['Age'] = clean_text(age_tag.get_text())

                # store valid player data
                if player['Name'] != 'N/A' and player['Club'] != 'N/A':
                    player_data.append(player)

    return player_data


# load players once at startup
players = load_players()

# to handle search and display


@app.route('/', methods=['GET'])
def index():
    # get search parameters from query string
    query = request.args.get('query', '').lower()
    position = request.args.get('position', '').lower()
    potential = request.args.get('potential', '')
    age = request.args.get('age', '')
    sort_by = request.args.get('sort_by', 'Name')

    # filtered player list
    filtered_players = players

    # search by name or club
    if query:
        filtered_players = [p for p in filtered_players if query in p['Name'].lower(
        ) or query in p['Club'].lower()]

    # filter by position
    if position:
        filtered_players = [
            p for p in filtered_players if position in p['Position'].lower()]

    # filter by exact potential (stars)
    if potential.isdigit():
        filtered_players = [
            p for p in filtered_players if p['Potential'] == potential]

    # filter by exact age
    if age.isdigit():
        filtered_players = [p for p in filtered_players if p['Age'] == age]

    # sort results
    filtered_players = sorted(
        filtered_players, key=lambda x: x.get(sort_by, ''))

    # render template with filtered players
    return render_template('index.html', players=filtered_players, query=query, position=position, potential=potential, age=age, sort_by=sort_by)


# to run Flask app
if __name__ == '__main__':
    app.run(debug=True)
