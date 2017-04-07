age = raw_input("how old are you?")
height = raw_input("how tall are you?")
weight = raw_input("how much do you weigh?")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
# %s is used wont give a string output
#python -m pydoc raw_input
#        Help on built-in function raw_input in module __builtin__:
#        raw_input(...)
#            raw_input([prompt]) -> string
