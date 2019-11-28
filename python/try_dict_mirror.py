#!/usr/bin/python3
# pylint: disable = invalid-name, missing-docstring

numberToStr = {1: 'Account', 2: 'AdvId', 3: 'AdvRefID'}
print(numberToStr)
print(numberToStr[1])
# Will return 'Account'

strToNumber = {numberToStr[key]:key for key in numberToStr}
print(strToNumber)
print(strToNumber['Account'])
# Will return '1'

strToNumber2 = {value:key for key, value in numberToStr.items()}
print(strToNumber2)
print(strToNumber2['Account'])
# Will return '1'
