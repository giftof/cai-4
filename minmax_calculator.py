import math

def to_float(number: str) -> float:
    try:
        parsed = number.strip().lower()
        constants = {
            'e': math.e,
            'pi': math.pi,
            'tau': math.tau,
            'inf': float('inf'),
            'infinity': float('inf'),
            '-inf': float('-inf'),
            '-infinity': float('-inf'),
        }
        if parsed in constants:
            return constants[parsed]
        if parsed == 'nan':
            raise ValueError('[NaN is short for Not A Number]')
        return float(number.strip().lower())
    except ValueError as desc:
        raise ValueError(f'Invalid input: {number} {desc}')

def sort_values(values: list[str]) -> list[float]:
    return sorted([to_float(n) for n in values if n.strip()])

# def dup_check(values: list[str]) -> bool:
#     return len(values) != len(set(values))

def main():
    try:
        chuck = input('Enter numbers separated by spaces: ')
        sorted_array = sort_values(chuck.split(' '))
        if len(sorted_array) == 0:
            raise ValueError('Input Some Value')
        print(f'Min: {sorted_array[0]}, Max: {sorted_array[-1]}')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
