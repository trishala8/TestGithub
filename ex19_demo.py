def keyArgFunc(empname, emprole):
   print ("Emp Name: ", empname)
   print ("Emp Role: ", emprole)
   #return;
print("Calling in proper sequence")
keyArgFunc(empname = "Nick",emprole = "Manager" )

print("Calling in opposite sequence")
keyArgFunc(emprole = "Manager",empname = "Nick")

print("Calling the number: ")
number_of_empname = 10
number_of_emprole = 20

keyArgFunc(number_of_empname, number_of_emprole)

print "The number of emp can be added: "
keyArgFunc(10+20, 5+15)
