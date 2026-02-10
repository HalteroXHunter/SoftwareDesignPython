class Sparkplug:
    def __init__(self, name):
        self._name = name
    
    def replace(self):
        print(f'Replaced sparkplug {self._name}')
    
class Engine:
    def __init__(self, sparkplug):
        self._sparkplug = sparkplug
        
    @property
    def sparkplug(self): return self._sparkplug
        
    def replace_sparkplug(self):
        self._sparkplug.replace()
        
class DemeterAuto:
    def __init__(self, engine):
        self._engine = engine
        
    def service_sparkplug(self, plug):
        plug.replace()
        
    def maintain_auto(self):
        self._engine.replace_sparkplug()
        
        plug1 = self._engine.sparkplug
        plug1.replace()
        
        plug2 = Sparkplug('plug2')
        plug2.replace()
