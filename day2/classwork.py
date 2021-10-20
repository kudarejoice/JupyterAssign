# Write a funciton to check if a given string is a palindrome.  
# Your function should return True if the string is a palindrome
# or False if it is not

# A palindrome is a string that # reads the same from back to front or from front to back.

test_one = "bob"
# result = True

test_two = "flower"
# result = False

test_three = "racecar"
# result = True

def is_palandrome(test_string):
    return test_string == test_string[::-1]
print(is_palandrome(test_three))
