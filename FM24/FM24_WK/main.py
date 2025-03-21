from bs4 import BeautifulSoup

with open('FM24\FM24_WK\FM25_CB_WK.html', 'r', encoding='utf-8') as file:
    content = file.read()

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())

    # find player name elements
    player_name_divs = soup.find_all('div', {'col-id': 'name'})

    players_data = []

    for name_div in player_name_divs:
        # extract player name
        player_name = name_div.get_text(strip=True)

        # get row-id of the player
        player_row = name_div.find_parent('div', role='row')
        if not player_row:
            continue

        row_id = player_row.get('row-id')

        # find row with same row-id containing stats
        stats_row = soup.find('div', {'role': 'row', 'row-id': row_id})
        if not stats_row:
            continue

        # extract player stats
        club = stats_row.find('div', {'col-id': 'basedTeam.name'})
        position = stats_row.find(
            'div', {'col-id': 'playerAttributes.position_sort'})
        cost = stats_row.find('div', {'col-id': 'contract.sale_value'})
        expiry = stats_row.find(
            'div', {'col-id': 'contract.team_expires_timestamp'})

        players_data.append({
            "Name": player_name,
            "Club": club.get_text(strip=True) if club else None,
            "Position": position.get_text(strip=True) if position else None,
            "Cost": cost.get_text(strip=True) if cost else None,
            "Expiry": expiry.get_text(strip=True) if expiry else None
        })

for player in players_data[:10]:
    print(player)
