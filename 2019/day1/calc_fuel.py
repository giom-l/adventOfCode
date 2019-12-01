#!/usr/bin/env python3
# coding: utf-8

import sys
# Append the parent parent dir to syspath to be able to read utils lib
sys.path.append('..')

from utils import read_file

def calc_fuel(mass):
    return mass//3 -2

def calc_fuel_rec(mass):
    fuel = calc_fuel(mass)
    if fuel<=0:
        return 0
    else:
        return fuel+calc_fuel_rec(fuel)

inputs = read_file('../inputs/day1')
masses = [int(mass) for mass in inputs]

total_fuel_part1 = sum([calc_fuel(mass) for mass in masses])
total_fuel_part2= sum([calc_fuel_rec(mass) for mass in masses])

print(f"Total Fuel part 1 : {total_fuel_part1}")
print(f"Total Fuel part 2 : {total_fuel_part2}")
