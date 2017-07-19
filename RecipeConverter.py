# Recipe Converter
# A program to assist user in baking bread with measurements also in grams
# By Tim Murphy 15/7/17

print '>> Original Recipe <<'
# Acquiring user input
print 'Enter the amount of flour (cups):',
flour = input()
print 'Enter the amount of water (cups):',
water = input()
print 'Enter the amount of salt (teaspoons):',
salt = input()
print 'Enter the amount of yeast (teaspoons):',
yeast = input()
print 'Enter the loaf adjustment factor (e.g. 2.0 double the size):',
adjustment = input()
print ''

# Multiplying original recipe by adjusted input
print '<< Modified Recipe >>'
print 'Flour: %.2f cups.' % (flour * adjustment)
print 'Water: %.2f cups.' % (water * adjustment)
print 'Salt: %.2f teaspoons.' % (salt * adjustment)
print 'Yeast: %.2f teaspoons.' % (yeast * adjustment)
print 'Super Baking!'
print ''

# Converting modified recipe to grams
print '<><> Modified Recipe in Grams <><>'
print 'Flour: %.2f g.' % ((flour * adjustment)*120)
print 'Water: %.2f g.' % ((water * adjustment)*237)
print 'Salt: %.2f g.' % ((salt * adjustment)*5)
print 'Yeast: %.2f g.' % ((yeast * adjustment)*3)
print 'Super Duper Baking!'