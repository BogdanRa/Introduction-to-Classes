"""
Check you'r post code
"""
def zipvalidate(postcode):
    return len(postcode) == 6 and postcode.isdigit() and postcode[0] not in "05789"

"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.
"""

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

    
"""
Reverse it
"""

def reverse_it(data):
  if isinstance(data, basestring): return data[::-1]
  if isinstance(data, int): return int(str(data)[::-1]) if not isinstance(data, bool) else data
  if isinstance(data, long): return long(str(data)[::-1])
  if isinstance(data, float): return float(str(data)[::-1])
  if isinstance(data, complex): return complex(str(data)[::-1])
  return data


"""
Return the array/list passed into the function with all duplicates removed
"""
def list_de_dup(list_):
    if not isinstance(list_, list):
        return 'Not an array'
    filtered = filter(lambda x: x is not None, list(set(list_)))
    return sorted(filtered)

""""
If team one is stronger, return the string "Team 1 wins!" If team two is stronger, return the string "Team 2 wins!"
If the two teams are of equal strength, the team with the strongest Anchor (the member furthest from the center of the rope) will win. 
In the above example, the member with strength 5 is team one's Anchor and strength 9 is team two's Anchor. 
If the teams and the Anchors are both of equal strength, return the string "It's a tie!"
""""

def tug_o_war(teams):
    (a, b) = (sum(team) for team in teams)
    if a == b:
        a = teams[0][0]
        b = teams[1][-1]
    return "Team 1 wins!" if a > b else "Team 2 wins!" if a < b else "It's a tie!"

"""
Create a function that takes an input String and returns a String, where all the uppercase words of the input String are in front and all the lowercase words at the end.
"""
def capitals_first(string):
    filtered = [word for word in string.split() if word[0].isalpha()]
    up = ' '.join([word for word in filtered if word[0].isupper()])
    low = ' '.join([word for word in filtered if word[0].islower()])
    return up + ' ' + low


"""
Make a program that will take an int (x) and give you the summation of all numbers from 1 up to x included. If the given input is not an integer, return "Error 404".
"""
def summation(x):
     return x * (x + 1) / 2 if isinstance(x, int) else 'Error 404'


"""
Create a function that returns the lowest product of 4 consecutive numbers in a given string of numbers.
This should only work is the number has 4 digits of more. If not, return "Number is too small".

Example
lowest_product("123456789")--> 24 (1x2x3x4)
lowest_product("35") --> "Number is too small"
"""
def lowest_product(input):
	
    s = map(int, str(input))
    
    if len(s) < 4:
        return "Number is too small"
    return min(map(lambda a,b,c,d : a * b * c * d, s[:-3], s[1:-2], s[2:-1], s[3:]))

print(lowest_product("2345611117899"))




"""
not in array
"""

def find(string_, list_):
  return True if string_ in list_ else False

""""
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

For example an array [2, 3, 9] equals 239, add one would return an array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

The array can't be empty and only positive, single digit integers are allowed. The function should return null if the array is empty or any of the array values are negative or more than 10.

[1, -9] would return null/nil/None (according to the language implemented).

""""

def up_array(arr):
    return None if arr==[] or any([x not in range(10) for x in arr]) else [int(c) for c in str(int("".join([str(x) for x in arr]))+1)]


"""
For the purposes of this kata, here is what makes a valid email:

At least one letter character at the beginning
All characters between the first character and the @ (if any) must be letters, numbers, or underscores
There must be an @ character (after the points listed just now)
After the @ character, there must be at least one word character (letter, number, or underscore) or hyphen
The email must end with at least one set of a dot followed by one or more word characters.
The input must NOT be case-sensitive
"""
import re

def validate(input_):
    return bool(re.match(r'^[A-Za-z]\w*@[\w-]+(\.\w+)+$', input_))

"""
for you'r inf
"""
def greet(name):
    return "Hello, {} how are you doing today?".format(name)

"""
syntax
"""
def fizzbuzz(n):
    if n % 15 == 0:return 'fizz buzz'
    elif n % 5 == 0:return 'buzz'
    elif n % 3 == 0:return 'fizz'
    return n


"""

"for"  in "return" ( only if len == 4 )

"""
def friend(x):
    return [f for f in x if len(f) == 4]



"""
Write a function that removes each 9 that it is in between 7s.

seven_ate9('79712312') => '7712312'
seven_ate9('79797') => '777'
"""
def seven_ate9(str_):
    while str_.find('797') != -1:
       str_ = str_.replace('797','77')
    return str_




"""
open file
"""
with open("text.txt", "w") as textfile:
	textfile.write("Success!")





"""
more if
"""
def cookie(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")















