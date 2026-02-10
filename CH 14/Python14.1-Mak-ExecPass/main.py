from copy import copy
from executive_pass import ExecutivePass

global_pass = ExecutivePass()
    
def run_app():
    global global_pass
    
    ron_pass = global_pass.obtain("Ron")
    print("Ron takes hold of the global pass")
    print(f"  Ron's pass: {ron_pass}")
    
    print()
    
    sal_pass = ron_pass.obtain("Sal")
    print("Sal takes the global pass from Ron")
    print(f"  Sal's pass: {sal_pass}")
    
    print()

    copy_pass = copy(sal_pass)
    bob_pass = copy_pass.obtain("Bob")
    print("Bob makes a copy of Sal's global pass")
    print(f"  Bob's pass: {bob_pass}")
    print("But Sal still holds the original global pass")
    print(f"  Sal's pass: {sal_pass}")
    
    print()
    
    another_pass = ExecutivePass()
    tim_pass = another_pass.obtain("Tim")
    print("Create another executive pass for Tim")
    print(f"  Tim's pass: {tim_pass}")
    print("But Sal still holds the original global pass")
    print(f"  Sal's pass: {sal_pass}")
    print("And Bob still holds his copy")
    print(f"  Bob's pass: {bob_pass}")

if __name__ == '__main__':
    run_app()
    