class TeamReport:
    def print(self, team):
        print()
        print(team.name)
        
        it = team.iterator
        
        while it.has_next():
            player = it.next()
            print(f'{player.player_id} {player.last_name}, '
                                     f'{player.first_name}')
