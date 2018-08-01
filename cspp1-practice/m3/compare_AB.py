'''
Author: Rishika Haritha - 20186041
Date: 1-August-2018
Encoding: Utf-8
'''

VARA = "abc"
VARB = "abcd"

if isinstance(VARA, str) or isinstance(VARB, str) is str:
    print("string involved")
elif VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")
