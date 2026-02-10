import matplotlib.pyplot as plt
from baseball_data import BaseballData

class BaseballReport:
    def __init__(self):
        self._title = 'BASEBALL GAME REPORT'
        self._hits = None
        
        self._singles = 0
        self._doubles = 0
        self._triples = 0
        self._homers  = 0
        
    def _print_header(self):
        print(self._title)
        print()
        
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

        
    def _print_footer(self):
        print()
        print('End of report')
        
    def generate_report(self):
        self._print_header()
        self._acquire_data()
        self._analyze_data()
        self._print_report()
        self._print_footer()