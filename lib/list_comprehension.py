#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [integer for integer in num_list if integer % 2 == 0]
    return even_numbers

def make_exclamation(sentence_list):
    exclamation_added = [string + "!" for string in sentence_list ]
    return exclamation_added