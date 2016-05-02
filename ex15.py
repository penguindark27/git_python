from sys import argv
path,filename=argv

print "This is the content before remove everything into the file.."
print "If you wanna continue, hit ENTER. If not press Cntrl+C (^C)."
raw_input("? ")

print "Opening file %s" % filename
# open file in write mode
txt=open(filename,'w')
print "Removing all the content of the file..."
# remove all the content
txt.truncate()

print "Would you like to add new content into the file?"
first=raw_input("> ")
second=raw_input("> ")
third=raw_input("> ")
# write into the file 
txt.write(first+"\n"+second+"\n"+third)
print "Information was save successfuly"
# close the file in the right way
txt.close()
