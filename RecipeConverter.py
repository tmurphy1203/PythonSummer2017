# Recipe Converter
# A program to calculate a recipe for bread
# By Tim Murphy 12/7/17

print ">> Original Recipe <<"
print "Enter the amount of Flour (cups): ",
flour = float(raw_input())
print "Enter the amount of Water (cups): ",
water = float(raw_input())
print "Enter the amount of Salt (teaspoons): ",
salt = float(raw_input())
print "Enter the amount of Yeast (teaspoons): ",
yeast = float(raw_input())
print "Enter the loaf adjustment factor (e.g. 2.0 double the size): ",
factor = float(raw_input())

print ""
print "<< Modified Recipe >>"
print "Flour: %.2f cups." % (flour*factor)
print "Water: %.2f cups." % (water*factor)
print "Salt: %.2f teaspoons." % (salt*factor)
print "Yeast: %.2f teaspoons" % (yeast*factor)
print "Merry Baking!"

gPerCupFlour = 120.0
gPerCupWater = 237.0
gPerTspSalt = 5.0
gPerTspYeast = 3.0

print ""
print "<><> Modified Recipe in Grams <><>"
print "Flour: %.2f g." % (flour*factor*gPerCupFlour)
print "Water: %.2f g." % (water*factor*gPerCupWater)
print "Salt: %.2f g." % (salt*factor*gPerTspSalt)
print "Yeast: %.2f g" % (yeast*factor*gPerTspYeast)
print "Great Baking!"