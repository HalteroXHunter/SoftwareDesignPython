from human import Human
from cat import Cat

if __name__ == '__main__':
    ron = Human(77.11, 1.85, True)
    print('Human Ron')
    print(f'{ron.weight = } kg, {ron.height = } m')
    ron.eat()
    ron.perform()
    
    print()
    
    buddy = Cat(5.55, 0.30, 1.25)
    print('Cat Buddy')
    print(f'{buddy.weight = } kg, {buddy.height = } m')
    buddy.eat()
    buddy.perform()
