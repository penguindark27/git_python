x= "there are %d types of people" % 20
binary= "binary"
do_not= "don't"
y= "Those who know %s and those who %s " % (binary,do_not)
print x
print y

print "I said %r." % x
print "And I also said %r." % y

hilarious= False
joke_evaluation=" isn't that joke so funny?!! %r "

print joke_evaluation %  hilarious

left="this is the left side"
right="this is the right side"

print left,right
# %r : print the value of any variable into char statement
# same way: print left +" "+ right - it means concatenate
