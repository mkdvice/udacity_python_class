# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest_numb(a,b,c):
    return biggest_numb(biggest_numb(a,b),c)



#print biggest(3, 6, 9)
#>>> 9
print(biggest_numb(3,6,9))

#print biggest(6, 9, 3)
#>>> 9

#print biggest(9, 3, 6)
#>>> 9

#print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9