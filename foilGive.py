import sys
import random

def makeTables(players, foils):
    b = 0
    indexer = 0
    if(players % 2 <> 0):
        indexer = 1
    tables = []
    while (b < foils):
        table = str(random.randint(1,(players/2)) - indexer)
        if(table == "0"):
            d = "Bye gets promo"
        else:
            d = "table: " + table + " seat: " + str(random.randint(1,2))
        if(d in tables):
           continue
        tables.append(d)
        print d
        b = b + 1

def main():
    #idea for bye: take total number of players.  if odd, halve, round up, zero index. zero table gets promo.
    foils = int(sys.argv[1])
    players = int(sys.argv[2])    
    
    if(foils < players):
        makeTables(players, foils)        
    else:
        print "ERROR: number of randoms cannot be greater than players"
if __name__ == "__main__":
    main()

