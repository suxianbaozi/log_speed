#!/usr/bin/env python
#coding:utf8

import sys
import time


count = 0
time_start = time.time()

while True:
    row = sys.stdin.readline()
    if not row:
        break
    count += 1

    deta_t = time.time()-time_start
    sys.stdout.write('\rtotal:%d,speed: %d/s'% (count,count/deta_t))
    sys.stdout.flush()
