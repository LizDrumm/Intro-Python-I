# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if num %2 == 0: 
        return True
    return False
    #return num %2 == 0   - PYTHONIC WAY!

print(is_even(7))
print(is_even(8))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
# print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# def even_odd(num):
#     if num %2 == 0: 
#         # print("Even!")
#         return
#     print("Odd!")

# print(even_odd(5))

# YOUR CODE HERE

if is_even(num):
    print ("Even!")
else:
    print("Odd")