import random
def coinToss():
    x = 0
    y = 0
    print "starting the program..."
    for toss in range(5000):
        toss = random.randint(0, 1)
        if toss == 0:
            x += 1
            print "Tossing a coin... It's heads! You have", x, "head(s) and", y, "tail(s) so far!" 
        if toss == 1:
            y += 1
            print "Tossing a coin... It's tails! You have", y, "tail(s) and", x, "head(s) so far!"
    print "Final outcome:", x, "heads and", y, "tails!"
    print "Ending the program. Thank you."  
coinToss()
