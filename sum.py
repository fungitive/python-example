#/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Wangj
#求和
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))