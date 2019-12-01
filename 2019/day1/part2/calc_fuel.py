#!/usr/bin/env python3
# coding: utf-8

import sys
# Append the parent parent dir to syspath to be able to read utils lib
sys.path.append('../..')

from utils import read_file


def calc_fuel(mass):
    fuel = int(mass/3)-2
    if fuel <= 0:
        return 0
    else:
        return fuel+calc_fuel(fuel)


inputs = read_file('../../inputs/day1')
masses = [int(mass) for mass in inputs]
total_fuel = sum([calc_fuel(mass) for mass in masses])
print("Total Fuel : {}".format(total_fuel))

