"""
Math 560
Project 4
Fall 2021

Partner 1: Leon Zhang, lz198
Partner 2: Casper Hsiao, ph139
Date: 17th Nov 2021
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function
"""
def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')
    # Initialize lookup table
    m, n = len(dest), len(src)
    dpTable = [[None for _ in range(m+1)] for _ in range(n+1)]
    # Fill in the base cases (first row and first column).
    for i in range(n+1):
        dpTable[i][0] = i
    for j in range(m+1):
        dpTable[0][j] = j
    # Fill in the rest of the table
    for i in range(1,n+1):
        for j in range(1,m+1):
            if src[i-1] == dest[j-1]: # Characters match
                dpTable[i][j] = dpTable[i-1][j-1]
            else: # Characters doesn't match
                dpTable[i][j] = 1+ min(dpTable[i][j-1], # Insert
                                       dpTable[i-1][j], # Delete
                                       dpTable[i-1][j-1]) # Substitude
    # Distance is the bottom right entry
    dist = dpTable[-1][-1]
    # Recontruct the solution
    i, j = n,m
    edits = []
    while (i != 0) and (j != 0):
        if src[i-1] == dest[j-1]:
            move = ('match', src[i-1], i-1)
            edits.append(move)
            i -= 1
            j -= 1
        else:
            smallest = dpTable[i][j]
            if 0 <= i-1 and 0 <= j-1 and dpTable[i-1][j-1] < smallest:
                smallest = dpTable[i-1][j-1]
                action = 'sub'
            if 0 <= i-1 and 0 <= j and dpTable[i-1][j] < smallest:
                smallest = dpTable[i-1][j]
                action = 'delete'
            if 0 <= i and 0 <= j-1 and dpTable[i][j-1] < smallest:
                smallest = dpTable[i][j-1]
                action = 'insert'
            if action == 'sub':
                move = (action, dest[j-1], i-1)
                i -= 1
                j -= 1
            elif action == 'delete':
                move = (action, src[i-1], i-1)
                i -= 1
            else:
                move = (action, dest[j-1], i)
                j -= 1
            edits.append(move)
    while i > 0:
        move = ('delete', src[i-1], i-1)
        edits.append(move)
        i -= 1
    while j > 0:
        move = ('insert', dest[j-1], i)
        edits.append(move)
        j -= 1
        
            
    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    # compareGenomes(True, 30, 300, 'ASM')
    # print()
    # compareRandStrings(True, 30, 300, 'ASM')
