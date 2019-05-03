'''First Challenge of the Second day of the Advent of Code'''

from typing import Tuple
def string_dist(string_one: str, string_two: str) -> Tuple[int, int]:
    '''Returns number of postions where string_one and string_two differ'''
    distance = 0
    last_occurrence = 0
    for idx, _ in enumerate(string_one):
        if string_one[idx] != string_two[idx]:
            distance += 1
            last_occurrence = idx
    return distance, last_occurrence

with open("input.txt", 'r') as inp:
    DIST = 0
    WORDS = []
    for line in inp:
        for word in WORDS:
            DIST, OCCURRENCE = string_dist(line, word)
            if DIST == 1:
                print(line[:OCCURRENCE] + line[OCCURRENCE + 1:])
                break
        WORDS.append(line)
