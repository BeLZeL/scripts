#!/usr/bin/env python3

Color = {
    'END': '\033[0m',
    'RED': '\033[1;31m',
    'GREEN': '\033[1;32m',
}

print(Color['GREEN'] + '[OK]' + Color['END'])
print('Print without color')
print(Color['RED'] + '[Failed]' + Color['END'])
