# Bird Counting
# A program to count multiple bird sightings
# By Tim Murphy 23/7/17

import Epic
# Fetches and reads the specified bird and returns a dictionary value of how many times seen
def countBirds(filename):
    d = {}
    file = open(filename)
    for line in file:
        temp = line.split(",")
        bird = temp[0].strip()
        timesSeen = int(temp[1].strip())
        if bird in d:
            d[bird] = d[bird] + timesSeen
        else:
            d[bird] = timesSeen
    return d

# Asks the user to enter a bird name and then looks up the sighting count if requested bird is in dictionary
def askUser(d):
    count = 0
    b = Epic.userString("Enter a bird name: ")
    if b in d.keys():
        count = d[b]
    return count

def main():
    birds = countBirds("Birds.txt")
    birdCount = askUser(birds)
    print "I have seen that bird %s time(s)." % birdCount
    
main()