from sys import argv  #argv just imports sys to get the filename

script, filename = argv

txt = open(filename)  #will open the txt file
#open(name[, mode[, buffering]])

print "Here's the file %r:" % filename
print txt.read()    #prints the text in the file

#Lines below this is removed then it prints the details only once
print "Type the file name again:"
file_again = raw_input(">")  #file(name[, mode[, buffering]])

txt_again = open(file_again)   #opens the file ex15_sample.txt to print the txt again

print txt_again.read()
