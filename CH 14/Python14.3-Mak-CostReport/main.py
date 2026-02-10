from provision_group import EquipmentGroup, UniformGroup, \
                            FootwearGroup
from equipment   import Ball, Bat, Glove
from uniform     import Cap, Jersey, Pants
from footwear    import Shoes, Socks
from sunscreen   import Sunscreen
from cost_report import CostReport

def build_provisions_tree():
    equipment = EquipmentGroup()
    uniform   = UniformGroup()
    footwear  = FootwearGroup()
    
    equipment.add(Ball())
    equipment.add(Bat())
    equipment.add(Glove())

    uniform.add(Cap())
    uniform.add(Jersey())
    uniform.add(Pants())

    footwear.add(Shoes())
    footwear.add(Socks())
    
    sunscreen = Sunscreen()

    return equipment, uniform, footwear, sunscreen 

if __name__ == '__main__':
    tree = build_provisions_tree()
    report = CostReport(*tree)
    report.generate_report()
