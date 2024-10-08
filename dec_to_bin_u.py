from typing import Sequence, Union, Optional, Type
#Deprecated
'''
def dec_to_custom(num: int, out_base: int, return_type: Optional[Type] = list) -> Sequence[int]:
    array = []
    while num > 0:
        array.append(num % out_base)
        num //= out_base
    return return_type(array[::-1])
'''
#Deprecated
'''
def custom_to_dec(in_num: Sequence[int], in_base: int) -> int:
    out_num = 0
    for i in range(len(in_num)):
        out_num += in_num[i] * pow(in_base, len(in_num) - (i + 1))
    return out_num
'''
#Deprecated test
'''
out1 = dec_to_custom(num=317, out_base=8, return_type=tuple)
out2 = custom_to_dec(in_num=(4, 7, 5), in_base=8)

print(f'{out1}\n{out2}')
'''
def base_conv(in_num: Union[Sequence[int], int], in_base: int, out_base: int, return_type: Optional[Type] = list) -> Union[Sequence[int], int]:
    try:
        if isinstance(in_num, int):
            if in_num == 0:
                return in_num
            elif out_base == 10:
                return in_num
            else:
                array = []
                while in_num > 0:
                    array.append(in_num % out_base)
                    in_num //= out_base
                return return_type(array[::-1])
        else:
            if sum(map(int, in_num)) == 0:
                return 0
            out_num = 0
            for i in range(len(in_num)):
                out_num += int(in_num[i]) * pow(in_base, len(in_num) - (i + 1))
            if out_base == 10:
                return out_num
            else:
                array = []
                while out_num > 0:
                    array.append(out_num % out_base)
                    out_num //= out_base
                return return_type(array[::-1])
    except ValueError | TypeError as e:
        raise e('Invalid input. Try again with different arguments.')

'''
Test:
In:         Exp. Out:
    13 bin          13 oct
    13 dec          13 oct
    13 bin          13 dec
    13 dec          13 dec
    0               0
'''
print(f'''
{base_conv(in_num='1101', in_base=2, out_base=8, return_type=tuple)}
{base_conv(in_num=13, in_base=10, out_base=8, return_type=tuple)}
{base_conv(in_num='1101', in_base=2, out_base=10, return_type=tuple)}
{base_conv(in_num=13, in_base=10, out_base=10, return_type=tuple)}
{base_conv(in_num=[0], in_base=8, out_base=8, return_type=list)}
'''
)
