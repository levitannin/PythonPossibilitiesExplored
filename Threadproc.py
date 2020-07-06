#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:30:48 2020

@author: levitannin


Working on multiprocessing module in python.
Threading vs Multiprocessing

Multiprocessing -- library uses separate memory space, multiple CPU cores,
    bypasses GIL limitations in CPython, child processes are killable (function
    calls in program) and is easier to use.  Caveats of the module are a larger
    memory footprint and IPC's a little more complicated with more overhead


Threading -- multithreading is a lightweight, memory shring library respionsible
    for UI and used well for I/O bound applications.  It is not killable and
    subject to GIL.
    Multiple threads live in the same process in the same space, each thread
    with a specific task and it's own code, stack memory, pointer, and share
    heap memory.  Memory leak can be damaging to other threads.

Concurrent.Futures -- library with new multiprocessing abilities.  Automatically
    joins iterative processes.  ProcessPoolExecutor is for CPU intensive tasks.
    ThreadPoolExecutor is better for network operations or I/O
    In either case, executor.map() which allows multiple calls to a provided 
    function, passing each of the items in an iterable to that function. Here;
    functions are called concurrently.
        for multiprocessing the iterable is broken into chunks, 
        the size of which can be conntroleld using key chunk_size
        
http://masnun.com/2016/03/29/python-a-quick-introduction-to-the-concurrent-futures-module.html
"""


import time
import threading
import concurrent.futures

start = time.perf_counter()

def base_test():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

def base_arg_test(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return(f'Done Sleeping... {seconds}')
    
def old_thread_test():
    t1 = threading.Thread(target = base_test)
    t2 = threading.Thread(target = base_test)
    
    t1.start()
    t2.start()
    
    #Keep's the processes running before sending the complete signal to main
    t1.join()
    t2.join()

def loop_thread_test():
    threads = []
    for _ in range(10):
        t = threading.Thread(target = base_test)
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()

def loop_arg_thread_test(seconds):
    #   Must be able to serialize args using pickle
    threads = []
    for _ in range(10):
        t = threading.Thread(target = base_arg_test, args = [seconds])
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()

def new_thread_test(seconds):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(base_arg_test, seconds)
        print(f1.result())

def new_thread_test_loop(seconds):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(base_arg_test, seconds) for _ in range(10)]
        
        for f in concurrent.futures.as_completed(results):
            print(f.result())

def new_thread_test_loop2(seconds):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(base_arg_test, sec) for sec in seconds]
        
        for f in concurrent.futures.as_completed(results):
            print(f.result())

def new_thread_test_map(seconds):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(base_arg_test, seconds)
        
        for r in results:
            #   Exception handling would happen here.
            print(r)
    
if __name__ == '__main__':
    #-------------------------------------------------------------------------
    #   The first commands are for the base process -- no multiprocessing
    base_test()
    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')

    #-------------------------------------------------------------------------
    #   Here are the commands for the old multiprocessing format.
    #   Time is not reset; anticipate approximate 1 second added time from above
    old_thread_test()
    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
    
    #-------------------------------------------------------------------------
    #   Here are the commands for multiprocessing (old) in a loop format.
    #   Time is not reset; anticipate approximate 1 second added time from above
    loop_thread_test()
    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
    
    #-------------------------------------------------------------------------
    #   Here are the commands for argument passing
    #   Time is not reset; anticipate approximate 1.5 second added time from above
    seconds = 1.5
    loop_arg_thread_test(seconds)
    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
    
    #-------------------------------------------------------------------------
    #   Here are the commands for argument passing using concurrent.futures
    #   Time is not reset; anticipate approximate 1.5 second added time from above
    seconds = 1.5
    new_thread_test(seconds)
    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
    
    #-------------------------------------------------------------------------
    #   Here are the commands for argument passing using concurrent.futures in a
    #       cleaner format.
    #   Time is not reset; anticipate approximate 1.5 second added time from above
    seconds = 1.5
    new_thread_test_loop(seconds)
    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
    
    #-------------------------------------------------------------------------
    #   Here are the commands for argument passing using concurrent.futures and
    #       iterative args
    #   Time is not reset; anticipate approximate 1.5 second added time from above
    seconds = [5, 4, 3, 2, 1]
    new_thread_test_loop2(seconds)
    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
    
    #-------------------------------------------------------------------------
    #   Here are the commands for argument passing using concurrent.futures and
    #       map.  Will return results in the order they were started; even if
    #       not sequential or the order items finished in.
    #   Time is not reset; anticipate approximate 1.5 second added time from above
    seconds = [5, 4, 3, 2, 1]
    new_thread_test_map(seconds)
    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')