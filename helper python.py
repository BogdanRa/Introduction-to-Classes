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

