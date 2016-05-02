from sys import argv
from os.path import exists

script, file_from, file_to = argv

print "Do u really want to copy this file %s to %s" % (file_from,file_to)
print "If u wanna continue with process, hit ENTER, Ctrl + C to abort"
raw_input()

p_content= open(file_from).read() ; print "Size of file %s is %r" % (file_from,len(p_content))
print "Validating if file %s really exists: %r " % (file_to,exists(file_to))

p_output=open(file_to,'w')
p_output.write(p_content)
p_output.close()

print "Alright, well done."

p_content2= open(file_to).read() 
print "Content of %s is : %s" % (file_to, p_content2)  


