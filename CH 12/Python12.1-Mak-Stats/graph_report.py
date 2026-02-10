import matplotlib.pyplot as plt

class GraphReport:
    def __init__(self):
        self._singles = 0
        self._doubles = 0
        self._triples = 0
        self._homers  = 0
    
    def _display_graph(self):
        hits = [self._homers,  self._triples,
                self._doubles, self._singles]
        what = ['Homers',  'Triples',
                'Doubles', 'Singles']
        
        _, ax = plt.subplots(figsize=(6, 2))
        ax.barh(what, hits, height=0.75)
        
        plt.title('GAME HITS GRAPH')
        plt.xticks([5, 10, 15, 20, 25, 30], 
                   ['5', '10', '15', '20', '25', '30'])
        
        for i in range(len(what)):
            ax.text(hits[i] + 1, i, str(hits[i]),
                    fontsize=10, 
                    ha='left', va='center')
            
        plt.show()
    
    def handle_event(self, event):
        if event is not None:
            hit = event.hit
            
            if hit == 1:
                self._singles += 1
            elif hit == 2:
                self._doubles += 1
            elif hit == 3:
                self._triples += 1
            elif hit == 4:
                self._homers += 1
        else:
            self._display_graph()
