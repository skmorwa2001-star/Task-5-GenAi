# Import math_utils Module

# First way
import math_utils

# Test the add function
print("Addition of a and b is : ",math_utils.add(10,5))

# Test the subtract function
print("Subtraction of a and b is : ", math_utils.subtract(100,5))

# Test the square function
print("Square of n is : ", math_utils.square(5))

# Second way
from math_utils import square

print("Square of n is : ", square(5))


# String module test

import string_utils

text="hello, my name is sunil kumar"

print("Original Text:",text)
print("Capitalized:",string_utils.capitalize_words(text))
print("Reversed:",string_utils.reverse_string(text))
print("Word Count:",string_utils.word_count(text))