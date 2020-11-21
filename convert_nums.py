"""
Conversion from Dec to HEX, OCT and Binary

----
for educational purposes
----
"""


def Dec2Bin(start_num):
    stringa = ''

    while True:
        if start_num > 0:
            resto = int(start_num % 2)
            stringa += str(resto)
            start_num //= 2
        else:
            break
    return stringa[::-1]


def Dec2Oct(start_num):
    stringa = ''

    while True:
        if start_num > 0:
            resto = int(start_num % 8)
            stringa += str(resto)
            start_num //= 8
        else:
            break
    return stringa[::-1]


def Dec2Hex(start_num):
    stringa = ''
    hexs = ['A', 'B', 'C', 'D', 'E', 'F']

    while True:
        if start_num > 0:
            resto = int(start_num % 16)
            if resto > 9:
                resto = hexs[resto-10]

            stringa += str(resto)
            start_num //= 16
        else:
            break
    return stringa[::-1]


def main():
    start_num = int(input('Insert the number in Decimal mode: '))
    print('From Decimal {} to Binary: {}'.format(start_num, Dec2Bin(start_num)))
    print('From Decimal {} to Octal: {}'.format(start_num, Dec2Oct(start_num)))
    print('From Decimal {} to Hexadecimal: {}'.format(
        start_num, Dec2Hex(start_num)))


main()
