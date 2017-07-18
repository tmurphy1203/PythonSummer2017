import Epic

sentence = Epic.userString("Please enter a entence")
words = sentence.split(' ')
largeWords = []
medWords = []
smallWords = []

for word in words:
    if len(word) > 5:
        largeWords.append(word)
    elif len(word) > 4:
        sortOfLargeWords.append(word)
    elif len(word) > 3:
        medWords.append(word)
    else:
        smallWords.append(word)

print largeWords
print sortOfLargeWords
print medWords
print smallWords
