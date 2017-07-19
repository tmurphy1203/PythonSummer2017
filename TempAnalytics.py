# Temperature Analytics
# A program to assist the user calculating climate change
# By Tim Murphy 18/7/17

import Epic

# Reading in data from temps.txt file
def readTemps():
    file = open("temps.txt", 'r')
    tempList = []
    for temp in file:
        tempFloat = float(temp.strip('\n'))
        tempList.append(tempFloat)
    return tempList

# Calculating average by adding each element in the list and dividing by the total number of items in list
def calculateAvg(tempList, start, stop):
    total = 0
    for index in range(start, stop):
        total += tempList[index]
    return total / (stop - start)
  
# Counting temperatures in the specified range that are greater than 0 
def count(tempList, start, stop):
    counter = 0
    for index in range(start, stop):
        if tempList[index] > 0:
            counter += 1
    return counter

# Calling in all functions to main
def main():
    tempList = readTemps()
    
    percentage = Epic.userFloat("Enter a percentage of how you'd like the data split: ") 
    
# Calculating percentage based on user input
    start = 0
    percentage = percentage / 100
    stop = int(len(tempList) * percentage)
   
    first_average = calculateAvg(tempList, start, stop)
    first_count = count(tempList, start, stop)
   
    print ("\nDuring the first %s years, the average deviation from the temperature anomoly is %s.") % (stop, first_average)
    print ("During the first %s years, %s had a positive temperature anomoly.") % (stop, first_count)
    
# Starting where first list had left off
    start = stop
    stop = len(tempList)

    second_average = calculateAvg(tempList, start, stop)
    second_count = count(tempList, start, stop)    

    print ("During the last %s years, the average deviation from the temperature anomoly is %s.") % ((stop - start), second_average)
    print ("During the last %s years, %s had a positive temperature anomoly.") % ((stop - start), second_count)

main()