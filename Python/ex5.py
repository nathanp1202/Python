my_name = 'Nathan Peyzner'
my_age = 17 #not a lie
my_height = 65 #inches
my_weight = 150 #lbs
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Blonde'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)



Inch = 2.54
centimeters = int(input("Enter a number of centimeters"))
print "Entered number of %s centimeters is equal to %s inches" % (centimeters , centimeters/inch)

inch = 2.54 #centimeters
centimeters = int(input("Enter a number of centimeters"))
print "Entered number of %s centimeters is equal to %s inches" % (centimeters , centimeters / inch)