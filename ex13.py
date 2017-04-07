from sys import argv

script, first, second, third = argv

print "The script is called: ", script
print "The first variable is : ", first
print "The second variable is : ", second
print "The third variable is : ", third

#python ex13.py gives error in line 3 as not defined

#ValueError: too many values to unpack ---- when 4 variable or more are added
#ValueError: need more than 3 values to unpack--- required the exact number of variables specifies

# python ex13.py raw_input raw_input raw_input
#The script is called:  ex13.py
#The first variable is :  raw_input
#The second variable is :  raw_input
#The third variable is :  raw_input


# python ex13.py argv raw_input argv
#The script is called:  ex13.py
#The first variable is :  argv
#The second variable is :  raw_input
#The third variable is :  argv
