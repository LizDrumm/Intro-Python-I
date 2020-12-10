# For the exercise, look up the methods and functions that are available for use
# with Python lists.

# a list in python is very close to a JS array!

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

x.extend(y)
#x = x + y
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
#.pop()- remove last item, but if you put the index it will remove from that index

x.pop(4)
#x.pop(-3)
#x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5,99)
print(x)

# Print the length of list x
# YOUR CODE HERE

print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE


#LIST COMPREHENSION!!!- to create a list, a for loop but with different syntax! 
y = [(num + 5) for num in x]
print(y)

a = [(num * 1000) for num in x]
print(a)
# for num in x:
#     print(num*1000)