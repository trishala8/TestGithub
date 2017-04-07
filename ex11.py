print "how old are you?",
#age = raw_input() - output will be as a string
age = raw_input()
#age = int(raw_input())  #other way to write
print "how tall are you?",
height = raw_input()
#height = int(raw_input())
print "how much do you weigh?",
weight = raw_input()  #output is in '' whereas for other its simple value
#weight = int(raw_input())
print "what is your name?",
name = raw_input()

print "So, you're %r old. %r tall and %r heavy.%r name" % (age, height, weight, name)
#So, you're '25' old. '5' tall and '74' heavy.'trishala' name
