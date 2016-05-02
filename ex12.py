from sys import argv
# define how many parameters your file will receive, the first parameter [0] always is the filename
script,first,second,third = argv

print "First parameter is ",script
print "Second parameter is ",first
print "Third parameter is ",second
print "Fouth parameter is ",third

last_question= raw_input("are u there? ")
print "your last answer: %s" % last_question
