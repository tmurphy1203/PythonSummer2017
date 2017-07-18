import Epic

verse1 = Epic.userString("Enter your first verse:")
verse2 = Epic.userString("Enter your second verse:")
verse3 = Epic.userString("Enter your third verse:")
verse4 = Epic.userString("Enter your fourth verse:")
chorus = Epic.userString("Enter your chorus:")
print ("Enter your chorus repeat amount:")
num = raw_input()
song = verse1 + (chorus * int(num)) + verse2 + (chorus * int(num)) + verse3 + (chorus * int(num)) + verse4 + (chorus * int(num)) + chorus
print song
print "One More Time"
print song