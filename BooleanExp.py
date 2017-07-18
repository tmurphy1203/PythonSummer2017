import Epic

 # if height is < 54 or age < 14 cannot ride
 # if height == 54 and age == 14 ask attendant
 # if height > 54 abd age > 14 can ride
 
 height = Epic.userInt("Plese enter your height in inches:")
 age = Epic.userInt("Please enter your age:")
 
 canRide = height > 54 and age > 14 # True or False
 cannotRide = height < 54 or age < 14 # True False
 askAttendant = height == 54 and age == 14 # True False
 
 if canRide:
     print "You can ride!"
    elif cannotRide:
        print "You cannot ride!"
    elif askAttendant:
        print "You must ask!"