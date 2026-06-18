from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck):
        freq = Counter(deck).values()
        
        g = reduce(gcd, freq)
        
        return g > 1