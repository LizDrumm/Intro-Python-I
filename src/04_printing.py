"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

#console.log(`x is ${x}, y is ${y}, z is ${"z"}`)

#what data type??? - d for digit 
# s- string
#f- float  - .2- two decimal points -- LEGACY!
print("x is %d, y is %.2f, z is '%s'" % (x,y,z))


# Use the 'format' string method to print the same thing- dont ever use!

print("x is {}, y is {}, z is '{}'" .format(x,"%.2f"%y,z))

# Finally, print the same thing using an f-string- BEST, use this one 
#float syntax is complicated!!!!! just google it

print(f"x is {x}, y is {'%.2f'%y}, z is '{z}'" )