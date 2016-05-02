# the comma "," at the end of each line allows u  finish the line without a new line
print "how old are you?",
age=raw_input()
print "how tall are you?",
height=raw_input()
print "how much do you weight?",
weight=raw_input()

# function int(value) allows u to convert the value a int type
print "so, u're %r old, %r tall, %r heavy" % (age,height,weight)
print "the sum of all values entered are : %r" % (int(age)+int(height)+int(weight))
