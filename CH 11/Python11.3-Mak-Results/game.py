class Game:
    def __init__(self, winner, winner_points,
                       loser,  loser_points):
        self._winner = winner
        self._winner_points = winner_points
        self._loser = loser
        self._loser_points = loser_points
        
        winner.increment_win_count()
        
    def print_game_score(self):
        print(f'{self._winner.name:>14s} beat '
              f'{self._loser.name:>10s}'
              f'{self._winner_points:3d} to '
              f'{self._loser_points:2d}')
