# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 16:29:33 2020

@author: bshaw
"""


n = int(input("input number n: "))
threshold = 0.001      # use more precision if needed

approximation = n/2    # Start with some or other guess at the answer

while True:
    better = (approximation + n/approximation)/2
    print(better)
    if abs(approximation - better) < threshold:
        print("approx root: ", better)
        break
    approximation = better