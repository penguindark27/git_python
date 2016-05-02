def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return (a + b)

def substract(a,b):
	print "SUBSTRACTING %d - %d" % (a,b)
	return (a - b)

def multiply(a,b):
        print "MULTIPLYING %d * %d" % (a,b)
        return (a * b)

def divide(a,b):
        print "DIVIDING %d / %d" % (a,b)
        return (a / b)
def my_own_function(a,b):
        print "My own function is : ((%d + %d)/2) * 5 " % (a,b)
        return  ((a+b)/2) * 5

print "Let's do some math with just functions."

age= add(30,5)
height=substract(89,40)
weight=multiply(3,40)
iq=divide(80,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age,height,weight,iq)

print "Here's a Puzzle."

what= add(age,substract(height,multiply(weight,divide(iq,2))))

print "That becomes: ",what," can u do it"

result= my_own_function(20,30)
print "the last result is %d " % result



