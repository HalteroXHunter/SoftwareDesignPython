from enum import Enum

class SportType(Enum):
    BASEBALL   = 1
    FOOTBALL   = 2
    VOLLEYBALL = 3
    
    def __str__(self): 
        return self.name.lower()

class Sport:
    def __init__(self, sport_type):
        self._type = sport_type
        self._games = []
        
    def add_game(self, game):
        self._games.append(game)
        
    def print_game_scores(self):
        print()
        print(' ', self._type)
        
        for game in self._games:
            game.print_game_score()
            
    def print_game_count(self):
        print(f'{self._type:>12s}: '
              f'{len(self._games)} game(s)')
