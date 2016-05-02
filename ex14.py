from sys import argv
path,filename = argv
# open a filename
txt= open(filename)
print  "The content of the file introduced is :"
# use the function read to get all content of the file.
print txt.read()
# to close the open file in the right way.
txt.close()

print "Enter the filename one more time please..",
second_file=raw_input("> ")
txt2=open(second_file)
content_second= txt2.read()
txt2.close()
print  content_second

