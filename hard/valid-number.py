import re


''' 
Problem 65: Valid Number
A trivial problem which I'm sure has some other clever solutions.
My solution just uses regex but you could implement as a DFA yourself.
Besides '3.' and '.3', the examples alone are enough to figure out the regex.
'''

def isNumber(s: str) -> bool:
    pattern = re.compile('(\\s*)([+-]?)(\\.\\d+|\\d+\\.?\\d*)(e[+-]?\\d+)?(\\s*)')
        
    return pattern.fullmatch(s) is not None


testvals = {'0': True,
        '0.1': True,
        'abc': False,
        '1 a': False,
        '2e10': True,
        ' -90e3   ': True,
        ' 1e': False,
        'e3': False,
        '6e-1': True,
        ' 99e2.5': False,
        '53.5e93': True,
        ' --6': False,
        '-+3': False,
        '95a54e53': False,
        '.1': True,
        '3.': True,
        }

for val, ans in testvals.items():
    result = isNumber(val)
    if ans != result:
        print('Error: isNumber(\''+val+'\') returned', result)
