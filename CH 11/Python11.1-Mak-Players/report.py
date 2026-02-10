from player import Player

class TeamReport:
    def print_list(self, team):
        print()
        print(team.name)
        
        for t in team.players:
            player = Player(*t)
            print(f'{player.player_id} {player.last_name}, '
                                     f'{player.first_name}')

    def print_generator(self, team):
        print()
        print(team.name)
        
        player_generator = team
        
        for _ in range(len(team.players)):
            player = next(player_generator)
            print(f'{player.player_id} {player.last_name}, '
                                     f'{player.first_name}')

    def print_dictionary(self, team):
        print()
        print(team.name)
        
        for key in team.players.keys():
            name = team.players[key]
            player = Player(key, name.last_name, name.first_name)
            print(f'{player.player_id} {player.last_name}, '
                                     f'{player.first_name}')
