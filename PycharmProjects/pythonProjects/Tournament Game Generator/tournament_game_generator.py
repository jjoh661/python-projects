def get_number_of_teams():
    while True:
        num_teams_ = int(input("Enter the number of teams in the tournament: "))

        if num_teams_ >= 2:
            break

        print("The minimum number of teams is 2, try again.")

    return num_teams_


def get_team_names(num_teams_):
    team_names_ = []

    for idx in range(num_teams_):
        while True:
            team_name = input(f"Enter the name for team #{idx + 1}: ")
            num_words = len(team_name.split(" "))

            if num_words > 2:
                print("Team names may have at most 2 words, try again.")
            elif len(team_name) < 2:
                print("Team names must have at least 2 characters, try again.")
            else:
                break

        team_names_.append(team_name)

    return team_names_


def get_number_of_games_played(num_teams_):
    while True:
        games_played_ = int(
            input("Enter the number of games played by each team: "))

        if games_played_ >= num_teams_ - 1:
            break

        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")

    return games_played_


def get_team_wins(team_names_, games_played_):
    team_wins_ = []

    for team in team_names_:
        while True:
            wins = int(input(f"Enter the number of wins Team {team} had: "))

            if wins > games_played_:
                print(
                    f"The maximum number of wins is {games_played_}, try again.")
            elif wins < 0:
                print("The minimum number of wins is 0, try again.")
            else:
                break

        team_wins_.append((team, wins))

    return team_wins_


def get_second_item(item):
    return item[1]


num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")
sorted_teams = sorted(team_wins, key=get_second_item)
game_pairings = []

games_to_make = len(sorted_teams)//2

for game_num in range(games_to_make):
    home_team = sorted_teams[game_num][0]
    away_team = sorted_teams[num_teams - 1 - game_num][0]
    game_pairings.append([home_team, away_team])

for pairing in game_pairings:
    home_team, away_team = pairing
    print(f"Home: {home_team} VS Away: {away_team}")
