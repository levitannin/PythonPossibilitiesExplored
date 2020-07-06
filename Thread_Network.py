#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 04:21:23 2020

@author: levitannin

Working on threadding module in python.
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

import requests
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')