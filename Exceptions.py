#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:01:39 2020

@author: levitannin

Working on better understanding python exceptions and how/where to utilize
the different formats.

This series is made during my srive to create clean, clear, code for use in my
spiders and other projects!

The goal here is to not only anticipate human error, but machine error as well.
"""

def start():
    #   The following is designed to throw an error.  We do not want the user to 
    #       see these errors.
    f = open('testfile.txt')    #   Actual file is test_file.txt

def try_except():
    try:
        f = open('testfile.txt')    #   Actual file is test_file.txt
    except Exception:
        print('Sorry, this file does not exist.')

def try_bada_execpt():
    try:
        f = open('test_file.txt')    #   Actual file is test_file.txt
        var = bad_var
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        #   Deal with this error seporately from above!  It can be general.
        #   Printing 'e' will also let you know the error number if you set multiple.
        print(e)

def try_except_else():
    try:
        f = open('test_file.txt')    #   Actual file is test_file.txt
        var = bad_var
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        #   Deal with this error seporately from above!  It can be general.
        #   Printing 'e' will also let you know the error number if you set multiple.
        print(e)
    else:
        #   Only runs if we don't throw an exception.
        print(f.read())
        f.close()
        
def try_except_else_final():
    try:
        f = open('test_file.txt')    #   Actual file is test_file.txt
        var = bad_var
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        #   Deal with this error seporately from above!  It can be general.
        #   Printing 'e' will also let you know the error number if you set multiple.
        print(e)
    else:
        #   Only runs if we don't throw an exception.
        print(f.read())
        f.close()
    finally:
        #   Will execute regardless of exception.
        pass

def raise_except():
    try:
        f = open('corrupt_file.txt')    #   Actual file is test_file.txt
        
        if f.name == 'corrupt_file.txt':
            raise Exception
    except FileNotFoundError as e:
        print(e)
    except Exception:
        #   Deal with this error seporately from above!  It can be general.
        #   Printing 'e' will also let you know the error number if you set multiple.
        print('ERROR!')
    else:
        #   Only runs if we don't throw an exception.
        print(f.read())
        f.close()
    finally:
        #   Will execute regardless of exception.
        pass
    

if __name__ == "__main__":
    #   This section focuses on the different types of exceptions (At a base lvl)
    #   Each function is to show off a different type of exception.  The files
    #       are just examples; make whatever txt file of the same name you want.
    #start()    #   Commented out to avoid the initial error.  Uncomment to see.
    try_except()
    try_bada_execpt()
    try_except_else()
    raise_except()