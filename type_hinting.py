from math import pi as PI
import typing as T

c1: float
c2: str

def circle_area(diameter: int) -> float:
    radius = diameter / 2
    return PI * (radius ** 2)

c1 = circle_area(10)
print(f"{c1 = }")

c2 = circle_area(9.5)
print(f"{c2 = }")

def spam(*, max: float=0.0, min: float=0.0, spam: 'Oobleck') -> None:
    pass

print(f"{circle_area.__annotations__ = }")

class Oobleck:
    pass


def process_files(files_to_process: T.Iterable) -> None:
    for file_path in files_to_process:
        print("processing", file_path)


files = ['a.txt', 'b.txt', 'c.txt']

process_files(files)

more_files = 'wombat.txt', 'penguin.txt'

process_files(files)


def wacky(thing: T.Any) -> tuple[int, ...]:
    return (1,)

def weird() -> list[str]:
    return ['abc', 'def']


def spam(foo: T.Union[str, int, bool]) -> None:
    pass

def ham(bar: T.Optional[T.Iterable]) -> None:
    pass

ham(None)
ham([1,2,3])





