

def cheese_and_crackers(cheese_count,boxes_of_crackers):
        print "You have %d chesses " % cheese_count
        print "You have %d boxes of crackers " % boxes_of_crackers
        print "Man that's enough for the party " 
        print "Get a blanket. \n"



##ncheese= int(raw_input("insert first value:"))
#ncracks= int(raw_input("insert second value:"))

print "insert first value:"
ncheese=int(raw_input())
print "insert second value:"
ncracks=int(raw_input())

print "We can just give the function numbers directly"
cheese_and_crackers(20,50)


print "OR, we can use variables from our script"
#ncheese=20
#ncracks=50
cheese_and_crackers(ncheese,ncracks)

print "We can even do maths combine variables with numbers"
cheese_and_crackers(ncheese+69,ncracks+20)

print "And finally we can do maths without variables, just numbers"

cheese_and_crackers(20+50,100+140)





