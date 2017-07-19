# Song Creator
# A program to asist user in constructing a song
# By Tim Murphy 15/7/17

import Epic

verseNum = ["first", "second", "third", "fourth"]
verseList = []

# Acquiring submissions of each verse from user and adding to list
for verse in verseNum:
    userVerses = Epic.userString("Enter your %s verse:" % verse)
    verseList.append(userVerses)
    
chorus = Epic.userString("Enter your chorus:")
repeat = Epic.userInt("Enter your repeat amount:")

fullChorus = (chorus + "") * repeat
lastChorus = fullChorus + chorus

#changing verses to uppercase
verseList = [element.upper() for element in verseList]

#changing chorus to lowercase
fullChorus = fullChorus.lower()
lastChorus = lastChorus.lower()

# Pairing choruses with each verse
verseList.insert(1,fullChorus)
verseList.insert(3,fullChorus)
verseList.insert(5,fullChorus)
verseList.insert(7,lastChorus)
verseList.insert(8, "One More Time Now!")

song = verseList * 2
del song[17]

print song
print

# Printing out each element in song and replacing "cookies"
for lyrics in song:
    lyrics = lyrics.replace("COOKIES", "_______")
    print lyrics