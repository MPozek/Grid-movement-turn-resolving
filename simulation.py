# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 20:58:09 2018

@author: Mislav
"""

import sys

def run_system(start, intent):
    # start: dict actor_id(string)->coordinate(tuple(int,int))
    # intent: dict actor_id(string)->coordinate(tuple(int,int))
    
    # TODO:: turn resolution code here
    
    # return: dict actor_id(string)->coordinate(tuple(int,int))
    return None # return the end state

###################################
###################################
###################################
###################################

assert len(sys.argv) > 1, "usage:\nsimulation.py input_file_path"

start = dict()
end = dict()
intent = dict()

file_contents = None

path = sys.argv[1]
file = open(path, 'r')
file_contents = file.read().splitlines()
file.close()

lines = list(filter(lambda a: a != "", file_contents))

# parse the file
assert len(lines) == 3

def parse(d, line):
    for actor_position in line.split(' '):
        s = actor_position.split('(')
        actor_id = s[0]
        
        # position
        s = s[1][:-1]
        
        d[actor_id] = (int(s[0]), int(s[-1]))

parse(start, lines[0])
parse(intent, lines[1])
parse(end, lines[2])

proposed = run_system(start, intent)

if end == proposed:
    print("pass!")
else:
    print("fail!")
    
print("expected end state:")
print(end)
print("recieved end state:")
print(proposed)