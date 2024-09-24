from typing import Optional, Type, Sequence, Union

type rt = Optional[Type]
type b = Union[2, 8, 10, 16]


# Comments are for pussies
def conv(num: int, return_type: rt = list, base: b = 2) -> Sequence[bytes]:
    try:
        match num:
            case 0:
                return return_type([0])
            case _:
                array = []
                while num > 1:
                    array.append(num % base)
                    num //= base
                return return_type(array[::-1])
    except ValueError | TypeError as e:
        raise e('Invalid input. Try again with different arguments.')


print(conv(num=279, return_type=tuple, base=16))


# Should I even comment a goddamn one-liner? No. Did I still do it? Yeah.
def byte_name(name: str, return_type: rt = list) -> Sequence[int]:
    return return_type([ord(i) for i in name])


print(byte_name(name=input(), return_type=tuple))
