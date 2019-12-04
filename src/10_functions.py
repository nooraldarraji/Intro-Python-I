# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even():
    okay = int(input('enter int: '))
    even = (okay % 2) == 0
    if even:
        print('Even')
        return True
    else:
        print('Odd')
        return False
is_even()
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
#is_even()
