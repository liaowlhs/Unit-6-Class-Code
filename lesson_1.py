'''
Name: Guoming Liao
Date: 12/2/2024
Topic: Indexing, Slicing, Immutability
'''

# Review
name = "Starla" # a string literal
age = 5
# f-strings (formatted strings)
description = f"{name} likes wand toys and is {age}"
print(description)

# same result with concatenation
description = name + " likes wand toys and is " + str(age)
print(description)

# indexing - every character in a string has a location
# starting at 0 from the beginning for -1 from the end

#  0  1  2  4  5  6
#  S  t  a  r  l  a
# -6 -5 -4 -3 -2 -1

first_letter = name[0] # always use 0 if you don't know length
print(first_letter)
first_letter = name[-6]
print(first_letter)
first_letter = name[-1*len(name)] # if you don't know length
print(first_letter)

last_letter = name[-1] # always use if you don't know length
print(last_letter)
last_letter = name[len(name)-1]
print(last_letter)

# use [ ] to access a character not ( ) - gives TypeError
# accessing an index that does not exist gives IndexError

try:
    print(name[20])
except IndexError:
    print("Out of bounds")

# Slicing - usd to aces 1 or more characters in a string
# instead of name[0]+name[1]+name[2] we can do name[0:3]

# first three letters
first_three = name[0]+name[1]+name[2]
print(first_three)
first_three = name[0:3] # start at index 0, go up to but not include 3
print(first_three)

# format
# string_name[start:stop:step] = none are technically required

word_one = "Adventure"
#  0  1  2  3  4  5  6  7  8
#  A  d  v  e  n  t  u  r  e
# -9 -8 -7 -6 -5 -4 -3 -2 -1
print(word_one[3:]) # enture - leave out stop parameter, goes through end
print(word_one[:3]) # Adv - leave out start, default value of 0
print(word_one[:]) # Adventure - leave out start, stop default values of 0,-1
print(word_one[-3:]) # ure - start at -3, go up +1 through end
print(word_one[:-3]) # Advent - start at 0(beginning or -9 in this case), go up to but not including -3 by adding +1 to index
print(word_one[::-1]) # erutnevdA - start at beginnning (end), go to end(beginning), adding -1 to the index
# -step is left
# +step is right
print(word_one[-3:-7:-2]) # un
print(word_one[-7:-3:-2]) # blank
# if step > 0
#   start < step
# if step < 0
#   start > step
word_one = word_one[2:-3]
print(word_one)
