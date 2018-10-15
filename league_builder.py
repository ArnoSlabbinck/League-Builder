import csv

dict_team = dict()
team = None
non_experienced = []
experienced = []

def merge_dicts(*dict_args):

    # Takes to two dictionaries and combines them to one
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result 

def make_dict(ex_players, non_players): 
    # Make a dictionary from 6 players; 3 experienced and 3 non experienced players
    first_dict = {ex_players[0]: ", ".join(ex_players) for ex_players in ex_players[:3]}
    second_dict = {non_players[0]: ", ".join(non_players) for non_players in non_players[:3]}

    # Deletes every player from list when added to dictionary
    del ex_players[:3]
    del non_players[:3]

    return first_dict, second_dict

def write_to_file(team, teams, team_name):

    # Takes the name of the right team and write it to the file
    print(list(teams.keys())[team_name], file = f)

    # Write  guardian(s) name(s), player's name, team name to file
    for player in team.values(): 
        print(player, file = f)




if __name__ == "__main__":

    #Open CSV file and read it 
    with open("soccer_players.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for players in csv_reader:

            #Seperate experienced from non_experienced players
            if players[2].lower() == "yes": 
                experienced.append(players)
            else: 
                non_experienced.append(players)

        #Takes out the list of name, height,... out of the list
        team_order = non_experienced.pop(0)


        sharks, sharks2 = make_dict(experienced,non_experienced)
        team_sharks = merge_dicts(sharks, sharks2)

        raptors, raptors2 = make_dict(experienced, non_experienced)
        team_raptors =  merge_dicts(raptors, raptors2)

        dragons, dragons2 = make_dict(experienced, non_experienced)
        team_dragons =  merge_dicts(dragons, dragons2)

        all_teams = {"Sharks": team_sharks,
        "Raptors": team_raptors,
        "Dragons": team_dragons}

        with open('teams.txt', 'w') as f:

            #Open text file and write to the text file the  team name and players
            for i,team in enumerate(all_teams.values()): 
                f.write(str(write_to_file(team, all_teams, i)))
                f.write(str("\n"))
             
     
           


