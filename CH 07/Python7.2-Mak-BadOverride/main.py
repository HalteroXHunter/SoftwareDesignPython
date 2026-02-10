from superclass import Superclass, Subclass

if __name__ == '__main__':
    supe = Superclass()
    sub  = Subclass()
    
    print(f"{supe.operate('Hi, ', 'Ron') = }")
    print(f"{sub.operate(2, 3) = }")
    print(f"{sub.operate('Hi, ', 'Ron') = }")
