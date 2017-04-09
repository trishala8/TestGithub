from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could dp these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()

indata = open(from_file).read()

print "The input file is %d bytes long" % len (indata)

print "Does the output file exists? %r" % exists (to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input(">")

#This command can be used instead oflines 22 -23
with open(from_file) as in_file, open(to_file, "w") as out_file:
    out_file.write(in_file.read())

#out_file = open(to_file, 'w')
#out_file.write(indata)

print "Alright, all done."

#out_file.close()
#in_file.close()
