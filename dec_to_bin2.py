from typing import Optional, Type, Sequence
from math import log2, ceil
from random import randint

type rt = Optional[Type]

# basically bogosort lol
def dec_to_bin(number: int, return_type: rt = list) -> Sequence[int]:
    if number == 0:
        return return_type([0])    
    else:
        def checker(array: Sequence[int]) -> int:
            value = 0
            length = len(array)

            for j in range(length):
                value += array[j] * pow(2, (length - (j + 1)))
            return value
        
        bit_array = [0 for _ in range(ceil(log2(number + 1)))]
        
        while checker(bit_array) != number:
            
            for i in range(len(bit_array)):
                bit_array[i] = randint(0, 1)
        return return_type(bit_array)
    
