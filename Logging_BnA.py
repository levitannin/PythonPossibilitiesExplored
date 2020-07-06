#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:07:48 2020

@author: levitannin

Working on better understanding python logging and how/where to utilize
the different levels.

This series is made during my srive to create clean, clear, code for use in my
spiders and other projects!

The goal here is to not only anticipate human error, but machine error as well.

Logging Level:
    DEBUG:      Detailed information, typically of interest only when 
                    diagnosing problems.
    INFO:       Confirmation that things are working as expected.
    WARNING:    An indication that something unexpected happened, or indicative
                    of some problem in the near future (e.g. 'disk space low')
                    Software is still working as expected.
                    DEFAULT SETTING
    ERROR:      Due to a more serious problem, the software has not been able 
                    to perform some function.
    CRITICAL:   A serious error, indicating that the program itself may be 
                    unable to continue running.
    
    By default, logging will ignore debug and info, but will capture warning, 
    error, and critical.
"""

import logging

#   The following line changes the default setting for logging, showing all levels.
#   If this is not working, logging may need to be updated using 'pip install logging'

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

#   The following are used in the basic logging review.

def math(x, y, method):
    if method == 'add':
        return x + y
    elif method == 'subtract':
        return x - y
    elif method == 'multiply':
        return x * y
    elif method == 'divide':
        return x / y
    else: print('ERROR: Incorrect method')

def printmethod(num_1, num_2):
    add_result = math(num_1, num_2, 'add')
    print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
    
    sub_result = math(num_1, num_2, 'subtract')
    print('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result))
    
    multi_result = math(num_1, num_2, 'multiply')
    print('Multiply: {} * {} = {}'.format(num_1, num_2, multi_result))
    
    div_result = math(num_1, num_2, 'divide')
    print('Divide: {} / {} = {}'.format(num_1, num_2, div_result))

def debugmethod(num_1, num_2):
    #   Nothing expected to happen
    add_result = math(num_1, num_2, 'add')
    logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
    
    sub_result = math(num_1, num_2, 'subtract')
    logging.debug('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result))
    
    multi_result = math(num_1, num_2, 'multiply')
    logging.debug('Multiply: {} * {} = {}'.format(num_1, num_2, multi_result))
    
    div_result = math(num_1, num_2, 'divide')
    logging.debug('Divide: {} / {} = {}'.format(num_1, num_2, div_result))

def infomethod(num_1, num_2):
    add_result = math(num_1, num_2, 'add')
    logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))
    
    sub_result = math(num_1, num_2, 'subtract')
    logging.info('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result))
    
    multi_result = math(num_1, num_2, 'multiply')
    logging.info('Multiply: {} * {} = {}'.format(num_1, num_2, multi_result))
    
    div_result = math(num_1, num_2, 'divide')
    logging.info('Divide: {} / {} = {}'.format(num_1, num_2, div_result))
    
def warningmethod(num_1, num_2):
    add_result = math(num_1, num_2, 'add')
    logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))
    
    sub_result = math(num_1, num_2, 'subtract')
    logging.warning('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result))
    
    multi_result = math(num_1, num_2, 'multiply')
    logging.warning('Multiply: {} * {} = {}'.format(num_1, num_2, multi_result))
    
    div_result = math(num_1, num_2, 'divide')
    logging.warning('Divide: {} / {} = {}'.format(num_1, num_2, div_result))
    
def errormethod(num_1, num_2):
    add_result = math(num_1, num_2, 'add')
    logging.error('Add: {} + {} = {}'.format(num_1, num_2, add_result))
    
    sub_result = math(num_1, num_2, 'subtract')
    logging.error('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result))
    
    multi_result = math(num_1, num_2, 'multiply')
    logging.error('Multiply: {} * {} = {}'.format(num_1, num_2, multi_result))
    
    div_result = math(num_1, num_2, 'divide')
    logging.error('Divide: {} / {} = {}'.format(num_1, num_2, div_result))

def criticalmethod(num_1, num_2):
    add_result = math(num_1, num_2, 'add')
    logging.critical('Add: {} + {} = {}'.format(num_1, num_2, add_result))
    
    sub_result = math(num_1, num_2, 'subtract')
    logging.critical('Subtract: {} - {} = {}'.format(num_1, num_2, sub_result))
    
    multi_result = math(num_1, num_2, 'multiply')
    logging.critical('Multiply: {} * {} = {}'.format(num_1, num_2, multi_result))
    
    div_result = math(num_1, num_2, 'divide')
    logging.critical('Divide: {} / {} = {}'.format(num_1, num_2, div_result))

if __name__ == '__main__':
    #   This section is for basic logging using a mathmatic example.
    num_1 = 20
    num_2 = 10
    
    printmethod(num_1, num_2)
    
    debugmethod(num_1, num_2)
    infomethod(num_1, num_2)
    warningmethod(num_1, num_2)
    errormethod(num_1, num_2)
    criticalmethod(num_1, num_2)
    