#!/usr/bin/env python3
# https://connect.ed-diamond.com/GNU-Linux-Magazine/glmfhs-111/le-point-sur-le-debogage-en-python

import logging

LOG_LEVELS = ('critical', 'error', 'warning', 'info', 'debug')

def log(level : str):
    getattr(logging, level)(f'Message de log de niveau {level.upper()}')


if __name__ == '__main__':
    
    #logging.basicConfig(level = logging.INFO)

    logging.basicConfig(
        filename = 'mon_app.log',
        level = logging.WARNING,
        format = '[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt = '%H:%M:%S'
    )

    for level in LOG_LEVELS:
        log(level)

# $ cat mon_app.log 
# [09:53:22] {main.py:8} CRITICAL - Message de log de niveau CRITICAL
# [09:53:22] {main.py:8} ERROR - Message de log de niveau ERROR
# [09:53:22] {main.py:8} WARNING - Message de log de niveau WARNING
