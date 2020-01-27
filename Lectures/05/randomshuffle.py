# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:29:43 2020

@author: bshaw
"""
import random

rng = random.Random()

cards = list()
type(cards)
for i in range(52):
    cards.append(i)
print(cards)

rng.shuffle(cards) # shuffle cannot work directly with a lazy promise
print(cards)