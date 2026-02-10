class LogReport:
    def __init__(self):
        self._count = 0
        
        print('GAME HITS LOG')
        print()
        
    def log_event(self, event):
        if event is not None:
            player_name = event.player_name
            hit = event.hit
            
            if hit == 0:
                what = 'an out'
            elif hit == 1:
                what = 'a single'
            elif hit == 2:
                what = 'a double'
            elif hit == 3:
                what = 'a triple'
            else:
                what = 'a homer'
            
            self._count += 1
            print(f'{self._count:2d} {player_name:7s}'
                  f' hit {what}')
