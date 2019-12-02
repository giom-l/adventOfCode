#!/usr/bin/env python3
# coding: utf-8
from itertools import islice
import sys
# Append the parent parent dir to syspath to be able to read utils lib
sys.path.append('..')

from utils import read_file

step_forward = 3

def format_input(data):
    return [int(x) for x in data.split(',')]

def restore_state(data):
    copy = data[:]
    index = 0
    while copy[index] != 99:
        if copy[index] == 1:
            copy[copy[index+3]] = copy[copy[index+1]] + copy[copy[index+2]]
        elif copy[index] == 2:
            copy[copy[index+3]] = copy[copy[index+1]] * copy[copy[index+2]]
        index += 4
    return copy


def find_noun_verb(data):
    for noun in range(100):
        for verb in range(100):
            copy = data[:]
            index = 0
            copy[1] = noun
            copy[2] = verb

            while copy[index] != 99:
                if copy[index] == 1:
                    copy[copy[index+3]] = copy[copy[index+1]] + copy[copy[index+2]]
                if copy[index] == 2:
                    copy[copy[index+3]] = copy[copy[index+1]] * copy[copy[index+2]]
                index += 4
                                                                                                                                                                                            
            if copy[0] == 19690720:
                return noun, verb


#replace position 1 with the value 12 and replace position 2 with the value 2
if __name__== "__main__":
    content = read_file('../inputs/day2')
    inputs_part1 = format_input(content[0])
    inputs_part2 = format_input(content[0])
    # replace position 1 with value 12
    inputs_part1[1] = 12
    # replace position 2 with value 2
    inputs_part1[2] = 2
    get_state = restore_state(inputs_part1)
    print(f'Part 1 Corrupted state : {inputs_part1}')
    print('=============================')
    print(f'Part 1 Restored state : {get_state}')
    print('=============================')
    print(f"Part 1 First position state is {get_state[:1][0]}")

    noun, verb=find_noun_verb(inputs_part2)
    print(f"Part 2 Found noun: {noun} and verb: {verb}")
    print(f"Part 2 final answer is {100*noun+verb}")
