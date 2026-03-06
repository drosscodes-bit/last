from bs4 import BeautifulSoup
import json



# link = "https://www.espn.com/nba/boxscore/_/gameId/401809950"

def format_url(url):
    url = url[0:25] + "boxscore" + url[29:]

    return url

def format_links(played_urls):
    box_score_links = []
    for url in played_urls:
        box_score_link = url[0:25] + "boxscore" + url[29:]
        box_score_links.append(box_score_link)
    return box_score_links

# Read from file instead of requesting
with open('dnp_data.html', 'r', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

def awayteam(url):
    flex = soup.find_all("div", class_="flex")
    player_name = flex[1].find_all("tr", class_="Table__TR Table__TR--sm Table__even")
    dnp = soup.find_all("td", class_="tc td BoxscoreItem__DNP Table__TD")
    for player in dnp:
        print(len(dnp))
        stats = soup.find_all("tbody", class_="Table__TBODY")
    
        players_data = []
    
        for player in range(1, 6):
            data = stats[1].find_all("tr", class_="Table__TR Table__TR--sm Table__even")
            get_name = player_name[player].find_all("span")

            data = data[player].find_all("td")
            name = get_name[0].get_text()
            jersey = get_name[2].get_text()
        
            player_stats = { 
                'name': name,
                'jersey': jersey,
                'minutes': data[0].get_text(),
                'points': data[1].get_text(),
                'field_goal_percentage': data[2].get_text(),
                'three_point_percentage': data[3].get_text(),
                'free_throw_percentage': data[4].get_text(),
                'rebounds': data[5].get_text(),
                'assists': data[6].get_text(),
                'turnovers': data[7].get_text(),
                'steals': data[8].get_text(),
                'blocks': data[9].get_text(),
                'o_rebounds': data[10].get_text(),
                'd_rebounds': data[11].get_text(),
                'fouls': data[12].get_text(),
                'plus_minus': data[13].get_text(),
                'Starter': True
            }
            players_data.append(player_stats)

        for player in range(7, 17):
            data = stats[1].find_all("tr", class_="Table__TR Table__TR--sm Table__even")
            get_name = player_name[player].find_all("span")

            data = data[player].find_all("td")
            name = get_name[0].get_text()
            jersey = get_name[2].get_text()
        
            player_stats = {
                'player': name,
                'jersey': jersey,
                'minutes': data[0].get_text(),
                'points': data[1].get_text(),
                'field_goal_percentage': data[2].get_text(),
                'three_point_percentage': data[3].get_text(),
                'free_throw_percentage': data[4].get_text(),
                'rebounds': data[5].get_text(),
                'assists': data[6].get_text(),
                'turnovers': data[7].get_text(),
                'steals': data[8].get_text(),
                'blocks': data[9].get_text(),
                'o_rebounds': data[10].get_text(),
                'd_rebounds': data[11].get_text(),
                'fouls': data[12].get_text(),
                'plus_minus': data[13].get_text(),
                'Starter': False
            }
            players_data.append(player_stats)
    
        return players_data

# def hometeam(url):
#     flex = soup.find_all("div", class_="Wrapper")
#     player_name = flex[2].find_all("tr", class_="Table__TR Table__TR--sm Table__even")
#     stats = soup.find_all("tbody", class_="Table__TBODY")
    
#     # List to store all player data for database insertion
#     players_data = []
    
#     # Process first set of players (1-6)
#     for player in range(1, 6):
#         data = stats[1].find_all("tr", class_="Table__TR Table__TR--sm Table__even")
#         get_name = player_name[player].find_all("span")

#         data = data[player].find_all("td")
#         name = get_name[0].get_text()
#         jersey = get_name[2].get_text()
        
#         player_stats = { 
#             'name': name,
#             'jersey': jersey,
#             'minutes': data[0].get_text(),
#             'points': data[1].get_text(),
#             'field_goal_percentage': data[2].get_text(),
#             'three_point_percentage': data[3].get_text(),
#             'free_throw_percentage': data[4].get_text(),
#             'rebounds': data[5].get_text(),
#             'assists': data[6].get_text(),
#             'turnovers': data[7].get_text(),
#             'steals': data[8].get_text(),
#             'blocks': data[9].get_text(),
#             'o_rebounds': data[10].get_text(),
#             'd_rebounds': data[11].get_text(),
#             'fouls': data[12].get_text(),
#             'plus_minus': data[13].get_text(),
#             'Starter': True  # Add a flag to indicate this player is a starter
#         }
#         players_data.append(player_stats)

#     # Process second set of players (7-17)
#     for player in range(7, 17):
#         data = stats[1].find_all("tr", class_="Table__TR Table__TR--sm Table__even")
#         get_name = player_name[player].find_all("span")

#         data = data[player].find_all("td")
#         name = get_name[0].get_text()
#         jersey = get_name[2].get_text()
        
#         player_stats = {
#             'player': name,
#             'jersey': jersey,
#             'minutes': data[0].get_text(), 
#             'points': data[1].get_text(),
#             'field_goal_percentage': data[2].get_text(),
#             'three_point_percentage': data[3].get_text(),
#             'free_throw_percentage': data[4].get_text(),
#             'rebounds': data[5].get_text(),
#             'assists': data[6].get_text(),
#             'turnovers': data[7].get_text(),
#             'steals': data[8].get_text(),
#             'blocks': data[9].get_text(),
#             'o_rebounds': data[10].get_text(),
#             'd_rebounds': data[11].get_text(),
#             'fouls': data[12].get_text(),
#             'plus_minus': data[13].get_text(),
#             'Starter': False  # Add a flag to indicate this player is not a starter
#         }
#         players_data.append(player_stats)
    
#     return players_data

# final_data = {}
# home_team_data = final_data['home_team'] = hometeam(format_url(link))
# away_team_data = final_data['away_team'] = awayteam(format_url(link))

print(json.dumps(players_data, indent=2))
