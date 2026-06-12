import json 

with open("players.json", "r") as f:
    players = json.load(f)

def get_active_players_by_team(players):
# Return a dict grouping active player names by team
# {"Storm": ["Marcus Reid", "Priya Nair", "Nadia Flores"], ...}
    active_players = {}
    for player in players: 
        team = player["team"]
        season = player["season"]
        if season == "active":
            if team not in active_players:
                active_players[team] = []
            active_players[team].append(player["player"])

    return active_players

def get_player_with_highest_points(players):
# Return the name of the active player 
# with the highest points_per_game
    highest_points = 0
    active_player = ""
    for player in players: 
        if player["season"] == "active":
            if player["points_per_game"] > highest_points:
                active_player = player["player"]
                highest_points = player["points_per_game"]
    return active_player

def get_assists_per_position(players):
# Return average assists per position
# across ALL players regardless of season status
# rounded to 2 decimal places
    total_assists = {}
    total_players = {}
    for player in players: 
        position = player["position"]
        if  position not in total_assists:
            total_assists[position] = 0 
            total_players[position] = 0
        total_assists[position] += player["assists"]
        total_players[position] += 1
        
    result = {}
    for position in total_assists: 
        result[position] = round(total_assists[position] / total_players[position] , 2)
    return result
print(get_assists_per_position(players))

def get_pro_player(players):
# Return a list of names of players with 
# 7 or more years_pro regardless of season status
    pro_player = []
    for player in players: 
        if player["years_pro"] >= 7: 
            pro_player.append(player["player"])
    return pro_player

print(get_pro_player(players))