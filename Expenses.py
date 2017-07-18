def userint(prompt):
    print prompt,
    num = int(raw_input())
    return num

kmWeekday = userInt("How many km did you travel on a weekday?")
miWeekday = 0.62 * kmWeekday

print "How many km did you travel on a Weekend?"
kmWeekend = int(raw_input())
miWeekend = 0.62 * kmWeekend

dollarsWeekday = miWeekday * 0.13;
dollarsWeekend = miWeekend * 0.24;

print "Weekday $%.2f" % dollarsWeekday
print "Weekend $%.2f" % dollarsWeekend
print "Total $%.2f" % (dollarsWeekday + dollarsWeekend)
