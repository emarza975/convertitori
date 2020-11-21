"""
Conversion from Dec to HEX, OCT and Binary
Second Version with only one function
----
for educational purposes
----
"""


def Dec2Basis(start_num, basis) -> str:
    """
    Conversion Engine

    Keyword arguments:
    start_num -- decimal number for conversion
    basis -- integer (2, 8, 16) for conversion
    Return: Result of conversion
    """

    stringa = ''
    hexs = ['A', 'B', 'C', 'D', 'E', 'F']

    while True:
        if start_num > 0:
            resto = int(start_num % basis)
            if resto > 9:
                resto = hexs[resto-10]

            stringa += str(resto)
            start_num //= basis
        else:
            break
    return stringa[::-1]


def main():
    start_num = int(input('Insert the number in Decimal mode: '))

    print('From Decimal {} to Binary: {}'.format(
        start_num, Dec2Basis(start_num, 2)))
    print('From Decimal {} to Octal: {}'.format(
        start_num, Dec2Basis(start_num, 8)))
    print('From Decimal {} to Hexadecimal: {}'.format(
        start_num, Dec2Basis(start_num, 16)))


main()
