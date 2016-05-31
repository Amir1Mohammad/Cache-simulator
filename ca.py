#! /usr/bin/python
from copy import copy
import time
import math
time.sleep(1)

__author__ = 'Amir Mohammad'

# https://github.com/The-WUUSTER/Cache-Simulator


def create_list(number):
	listme=[]
	return map(copy,[[]]*number)

 
def simulation(sequence, (block_size, cache_size, sets_num)):	
    cache_size = cache_size / block_size
    
    for cc in sequence:

        b = cc / block_size
        llll = b % sets_num
        line = create_list(llll)
        hit = 0
        hit = float(hit)
        if b in line:
            hit +=1
        elif len(line) == cache_size/sets_num:
    	    line.pop(0)
        line.append(b)
    ttt = hit / float(len(sequence))
    return ttt

def spl():
    pass


def load_input():

    seq = []
    addd = str(raw_input("name input is : "))
    how = str(raw_input("how : "))
    with open(addd,how) as amir :
        for line in amir :
            seq.append(map(int, line.split(" ")))
    return seq




def load_answer(mmm,bl_sizes,cash_sizes,set_numbers):
    print '***************SIMULATION********************'
    print '# sequence: <%s>' % (', '.join(map(str, seq)))
    print '# ram size: %s' % ram_size
    print '# cache size: %s' % cash_sizes
    print '# mapping: %s' % ('direct' if mmm == 1 else ('fully asso' if mmm == cash_sizes else ('%s-way' % str(mmm))))
    print '# block size: %s' % bl_sizes
    print '# HIT RATE =', simulation(seq, (bl_sizes, cash_sizes, set_numbers))
    print "**********************************************"



esh = pow(2,20)
ram_size = 64 * esh
all_sequences = load_input()
all_block_sizes = [1, 8]
all_cache_sizes = [ram_size / esh, ram_size / pow(2,10)]


for seq in all_sequences:
    for cash_sizes in all_cache_sizes:
        all_mapping_ways = [1, 2, 8, cash_sizes]
        for mmm in all_mapping_ways:
            for bl_sizes in all_block_sizes:
                set_numbers = (cash_sizes / bl_sizes) / mmm if cash_sizes != mmm else 1
                load_answer(mmm,bl_sizes,cash_sizes,set_numbers)

