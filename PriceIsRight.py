import random
import Epic

def main():
    good_prizes = ["New Car!", "$100", "A Badge in Pyhton Class", "A free A in python!"]
    bad_prizes = ["An Old Sock", "A Smelly Garbage Can", "A Sore Throat", "More Homework"]
    doors = ['', '', '']
#place random bad prizes between all 3 doors    
    random.shuffle(bad_prizes)
    doors[0] = bad_prizes[0]
    doors[1] = bad_prizes[1]
    doors[2] = bad_prizes[2]
#replace random bazd prize with good one    
    random.shuffle(good_prizes)
    iGoodPrize = random.randrange(0,3)
    doors[iGoodPrize] = good_prizes[0]
#let user pick door    
    door = Epic.userInt("Pick a door:")
    print "You win..."
    time.sleep(5)
    print "You win a %s" % doors[door-1]
    
main()