from typing import Optional, Type, Sequence

type rt = Optional[Type]

def dec_to_bin(number: int, return_type: rt = list) -> Sequence[int]:
    if number == 0:
        return return_type([0])
    else:
        bit_array = []
		
        while number > 0:
			
            bit_array.append(number % 2)
            number //= 2
	return return_type(bit_array[::-1])
