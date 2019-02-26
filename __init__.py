from Parent import *
from Child import *

def main():
    c = Child()  # instance of child
    c.myMethod()  # child calls overridden method
    p = Parent()
    p.myMethod()

if __name__ == '__main__':
    main()