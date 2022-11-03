# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:56:19 2022
@author: ayser
"""

import random

def uniform_crossover(individualLength, parent1, parent2):
    
    # Defining mask list
    mask=list()

    bit_list = [0,1]
    
    # Generating mask list as random.
    mask=random.choices(bit_list, weights=[1,1], k=individualLength)
    
    offspring1=parent1
    offspring2=parent2
    
    # Masking
    offspring1=list(map(lambda m, o1, p2: p2 if m==0 else o1, mask, offspring1, parent2))
    offspring2=list(map(lambda m, o2, p1: p1 if m==0 else o2, mask, offspring2, parent1))
    
    return offspring1, offspring2
