from sys import argv

script, input_file = argv

def print_all(f):   #function print_all is used
    print f.read()

#seek fun--- [0-- refers to begnning of file] [1- current file position] [2- end of file]
def rewind(f):   #function rewind is used
    f.seek(0)  # mainly useful when operating over an open file

def print_a_line(line_count, f):     #function print_a_line is used
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1                 #the first line is printed
print_a_line(current_line, current_file) # hte first line is displayed

current_line = current_line + 1  #line 2 is read
print_a_line(current_line, current_file) # line 2 is then printed

current_line = current_line + 1 #line 3 is read
print_a_line(current_line, current_file)   #line 3 is printed

# [+=]-- refers to x+y
