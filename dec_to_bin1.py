from typing import Optional, Type, Sequence
from math import log2, ceil

type rt = Optional[Type]

def dec_to_bin(number: int, return_type: rt = list) -> Sequence[int]:
    if number == 0:
        return return_type([0])
    else:
        dec_num = number
        bit_array = [0 for _ in range(ceil(log2(number + 1)))]

        while dec_num > 0:

            bit_value = 1
            bit_index = 0

            while bit_value <= dec_num / 2:

                bit_value <<= 1
                bit_index += 1

            dec_num -= bit_value
            bit_array[bit_index] = 1
        return return_type(bit_array[::-1])

num = int(input())
print(dec_to_bin(num))
