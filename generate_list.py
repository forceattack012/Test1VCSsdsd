import random
def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    return alist
    
"""
print a generate_list
"""

def printIt()
    print( generate_list() )


def main() :
    printIt()
    
"""
if this script flie is called, it will run main() directly
"""

if _name__ == '_main_' :
    print("Test printIt() :")
    main()