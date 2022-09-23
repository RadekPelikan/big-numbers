MINUS = [
    "        ",
    "        ",
    "        ",
    "████████",
    "        ",
    "        ",
    "        ",
]
ZERO = [
    "████████",
    "██    ██",
    "██    ██",
    "██    ██",
    "██    ██",
    "██    ██",
    "████████",
]
ONE = [
    "      ██",
    "      ██",
    "      ██",
    "      ██",
    "      ██",
    "      ██",
    "      ██",
]
TWO = [
    "████████",
    "      ██",
    "      ██",
    "████████",
    "██      ",
    "██      ",
    "████████",
]
THREE = [
    "████████",
    "      ██",
    "      ██",
    "████████",
    "      ██",
    "      ██",
    "████████",
]
FOUR = [
    "██    ██",
    "██    ██",
    "██    ██",
    "████████",
    "      ██",
    "      ██",
    "      ██",
]
FIVE = [
    "████████",
    "██      ",
    "██      ",
    "████████",
    "      ██",
    "      ██",
    "████████",
]
SIX = [
    "████████",
    "██      ",
    "██      ",
    "████████",
    "██    ██",
    "██    ██",
    "████████",
]
SEVEN = [
    "████████",
    "      ██",
    "      ██",
    "      ██",
    "      ██",
    "      ██",
    "      ██",
]
EIGHT = [
    "████████",
    "██    ██",
    "██    ██",
    "████████",
    "██    ██",
    "██    ██",
    "████████",
]
NINE = [
    "████████",
    "██    ██",
    "██    ██",
    "████████",
    "      ██",
    "      ██",
    "████████",
]
GAP = " "

NUMBERS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]

number_str = input("Enter a number: ")
negative = number_str[0] == "-"
if negative:
    number_str = number_str[1:]

for row_index in range(len(NUMBERS[0])):
    if negative:
        print(MINUS[row_index] + GAP, end="")

    for i, digit_str in enumerate(number_str):
        digit = int(digit_str)
        print(NUMBERS[digit][row_index], end=(
            GAP if (len(number_str) - i - 1) % 3 != 0 else GAP + " " * len(NUMBERS[0]) + GAP)
        )
    print()
