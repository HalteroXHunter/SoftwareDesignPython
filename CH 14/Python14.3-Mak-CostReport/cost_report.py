class CostReport:
    def __init__(self, equipment, uniform, 
                       footwear, sunscreen):
        self._equipment = equipment
        self._uniform   = uniform
        self._footwear  = footwear
        self._sunscreen = sunscreen
        
        self._equipment_cost = 0
        self._uniform_cost   = 0
        self._footwear_cost  = 0
        
    def _compute_group_costs(self):
        for item in self._equipment.provisions:
            self._equipment_cost += item.cost
            
        for item in self._uniform.provisions:
            self._uniform_cost += item.cost
            
        for item in self._footwear.provisions:
            self._footwear_cost += item.cost

        self._uniform_cost += self._footwear_cost
    
    def _print_costs(self):
        print('PROVISIONS')
        
        print(f'    {self._equipment.name}')
        for item in self._equipment.provisions:
            print('        ', end='')
            item.print_item()

        print(f'    {self._equipment.name}'
              f' total: ${self._equipment_cost:2d}')
        
        print(f'    {self._uniform.name}')
        for item in self._uniform.provisions:
            print('        ', end='')
            item.print_item()
        
        print(f'        {self._footwear.name}')
        for item in self._footwear.provisions:
            print('            ', end='')
            item.print_item()

        print(f'        {self._footwear.name}'
              f' total: ${self._footwear_cost:2d}')

        print(f'    {self._uniform.name}'
              f' total: ${self._uniform_cost:2d}')

        print('    ', end='')
        self._sunscreen.print_item()
        
        provisions_total = (  self._equipment_cost
                            + self._uniform_cost
                            + self._sunscreen.cost)
        print(f'PROVISIONS total: ${provisions_total}')
    
    def generate_report(self):
        self._compute_group_costs()
        self._print_costs()

        