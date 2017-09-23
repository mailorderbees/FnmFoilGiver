import sys
import random

def main():
    a = int(sys.argv[1])
    c = int(sys.argv[2])
    b = 0
    tables = []
    if(a < c*2):
        while (b < a):
            d = "table: " + str(random.randint(1,c)) + " seat: " + str(random.randint(1,2))
            if(d in tables):
               continue
            tables.append(d)
            print d
            b = b + 1
    else:
        print "ERROR: number of randoms cannot be greater than players"
if __name__ == "__main__":
    main()
