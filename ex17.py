
def print_two(*args):
        arg1, arg2 = args
        print "Arg1: %s, Arg2: %s" % (arg1,arg2)


def print_two_again(arg1,arg2):
        print "Arg1: %s, Arg2: %s" % (arg1,arg2)

def print_one(arg1):
        print "Arg1: %s" % (arg1)

def print_nothing():
        print "This function is gonna print nothing because is a test"

print_two("Manuel","lazo")
print_two_again("Manuel 2","lazo 2")
print_one("lazo")
print_nothing()
