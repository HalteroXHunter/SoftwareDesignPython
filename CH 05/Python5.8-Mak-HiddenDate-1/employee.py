class Employee:
    def __init__(self, employee_id, name, birthdate):
        self._employee_id = employee_id
        self._name = name
        self._birthdate = birthdate
    
    @property
    def employee_id(self): return self._employee_id
    
    @property
    def name(self): return self._name
    
    @property
    def birthdate(self):  return self._birthdate
        
    def __str__(self):
        return (
            f'Employee #{self._employee_id}\n'
            f'  Name: {self._name}\n'
            f'  Birthdate: {self._birthdate}\n'
        )
