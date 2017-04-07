from sys import argv

script, user_name = argv
play = ">"

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."

print "Do you like me %s?" % user_name
likes = raw_input(play)

print "Where do you live %s?" % user_name
lives = raw_input(play)

print "What kind of computer do you have?"
computer = raw_input(play)

print "What is your favourite color ?" #added a new statement
color = raw_input(play)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
Oh! so %r is your favourite color. Awesome
""" % (likes, lives, computer, color)
