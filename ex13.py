from sys import argv
# define how many parameters your file will receive, the first parameter [0] always is the filename
file,username=argv
prompt='> '
print "Hello my name is %s" % file
print "Would you mind if ask u some questions dear Mr.%s ?" % username
print "First question: do u like me Mr.%s?" % username
first_answer=raw_input(prompt)
print "Second question: why do learn Python Mr. %s?" % username
second_answer=raw_input(prompt)
print "Last question: are u sure you are going to complete this online course Mr. %s?" % username
last_answer=raw_input(prompt)

print """
Your answera about about the questions were:
* %s\n* %s\n* %s
""" % (first_answer,second_answer,last_answer)


