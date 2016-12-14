#!/usr/bin/env python3
import random


def rolleDice(count):
    dice = []
    print( random.randint(1,6) )
    return [ random.randint(1,6) for x in range(count) ]















print( rolleDice(6) )