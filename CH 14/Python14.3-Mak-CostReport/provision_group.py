class ProvisionGroup:
    def __init__(self, name):
        self._name = name
        self._provisions = []
        
    @property
    def name(self):
        return self._name

    @property
    def provisions(self):
        return self._provisions
    
    def add(self, item):
        self._provisions.append(item)
        
    def remove(self, item):
        self._provisions.remove(item)

class EquipmentGroup(ProvisionGroup):
    def __init__(self):
        super().__init__('EQUIPMENT')

class UniformGroup(ProvisionGroup):
    def __init__(self):
        super().__init__('UNIFORM')

class FootwearGroup(ProvisionGroup):
    def __init__(self):
        super().__init__('FOOTWEAR')
