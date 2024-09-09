from typing import Sequence, Optional, Type
from math import log2, ceil

type rt = Optional[Type]

def dec_to_bin(number: int, return_type: rt = list) -> Sequence[int]:
    if number == 0:
        return return_type([0])
    else:
        bit_array = []
        for i in range(ceil(log2(number + 1))):
            bit_array.append(1 if (number & pow(2, i)) > 0 else 0)
        return return_type(bit_array[::-1])
