import Epic
def main():
    keepGoing = True
    while keepGoing:
        msg = Epic.userString("Enter a message (enter 'quit' to exit):")
        if msg == "quit":
            keepGoing = False
        else:
            print msg
            
main()