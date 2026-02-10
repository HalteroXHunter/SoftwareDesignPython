import matplotlib.pyplot as plt
from game_report import GameReport
from baseball_data import BaseballData

class BaseballReport(GameReport):
    def __init__(self):
        super().__init__('BASEBALL GAME REPORT')
        
        self._singles = 0
        self._doubles = 0
        self._triples = 0
        self._homers  = 0
        
    def _acquire_data(self):
        data = BaseballData()
        self._hits = data.hits
        
    def _analyze_data(self):
        for hit in self._hits:
            if hit == 1:
                self._singles += 1    
            elif hit == 2:
                self._doubles += 1
            elif hit == 3:
                self._triples += 1
            elif hit == 4:
                self._homers += 1
        
    def _print_report(self):
        print('   Hit type')
        print(f'{self._singles:2d} singles')
        print(f'{self._doubles:2d} doubles')
        print(f'{self._triples:2d} triples')
        print(f'{self._homers:2d} homers')

        plt.bar(['singles', 'doubles', 'triples', 'homers'],
                [self._singles, self._doubles, 
                 self._triples, self._homers])
        plt.title('Hits During the Game')
        plt.xlabel('Type of hits')
        plt.ylabel('Number of hits')
        plt.show()
