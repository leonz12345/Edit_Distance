"""
Math 560
Project 4
Fall 2021

p4tests.py
"""

# Import random and project4 code.
import random
from project4 import ED

################################################################################

def makeEdits(src, edits):
    # Turn src into a list of chars.
    srcList = list(src)
    
    # Loop over the edits.
    for ed in edits:
        # Check if insert, delete, or sub.
        if ed[0] == 'insert':
            # Perform the insertion.
            srcList.insert(ed[2], ed[1])
        elif ed[0] == 'delete':
            # Perform the deletion.
            del srcList[ed[2]]
        elif ed[0] == 'sub':
            # Perform the substitution.
            srcList[ed[2]] = ed[1]
        elif ed[0] == 'match':
            # Nothing to do.
            continue
        else:
            raise Exception('Edit is not insert, delete, or sub!')

    # Join the srcList back into a string.
    editedSrc = ''.join(srcList)
    return editedSrc

################################################################################

def edTests(verbatim=False):
    # Set up the tests.
    string1 = ['spam', 'libate', '', 'abc', 'aaa']
    string2 = ['pims', 'flub', 'abc', '', 'bbb']
    dists = [3, 5, 3, 3, 3]
    labels = ['Class Ex 1', 'Class Ex 2', 'All Inserts', 'All Deletes', \
              'All Subs']

    # Track the number passed.
    numPassed = 0
    
    # Perform the tests.
    for sInd in range(len(string1)):
        s1 = string1[sInd]
        s2 = string2[sInd]
        print('Performing Test ' + str(sInd+1))
        print('Test Description: ' + labels[sInd])
        if verbatim:
            print('\tString 1: ' + s1 + ',\tString 2: ' + s2)
        dist, edits = ED(s1, s2)
        if verbatim:
            print('\tReported Distance: ' + str(dist))
            print('\tReported Edits:')
            for ed in edits:
                print('\t\t' + str(ed))
        edited = makeEdits(s1, edits)
        passed = (edited == s2) and (dists[sInd] == dist)
        if verbatim:
            print('\tTarget String: ' + s2)
            print('\tEdited String: ' + edited)
        if passed:
            print('Test ' + str(sInd+1) + ' Passed!')
            print()
            numPassed += 1
        else:
            print('Test ' + str(sInd+1) + ' Failed!')
            print()

    # Print number passed.
    print('Passed ' + str(numPassed) + '/' + str(len(string1)) + ' Tests')

################################################################################

def getRandGenomes(n=10, seed=None):
    # Set the rng seed (note: will use system time if no seed was given).
    random.seed(seed)

    # List of genome chars.
    basePairs = ['A', 'G', 'T', 'C']

    # Create random strings for ED.
    s1List = [random.choice(basePairs) for x in range(n)]
    s1 = ''.join(s1List)
    s2List = [random.choice(basePairs) for x in range(n)]
    s2 = ''.join(s2List)

    return s1, s2

################################################################################

def compareGenomes(verbatim=False, trials=30, n=10, prob='ED', seed=None):
    # For each trial, generate 2 genomes, compute ED, track average ED.
    avg = 0
    for t in range(trials):
        s1, s2 = getRandGenomes(n, seed)
        dist, edits = ED(s1, s2, prob)
        avg += dist
        if prob == 'ED':
            edited = makeEdits(s1, edits)
            if edited != s2:
                print('Failed Test!!!')
    avg = avg/trials
    if verbatim:
        print('Performed ' + str(trials) + ' trials.')
        print('Compared genomes of size ' + str(n))
        print(('Average %s: ' + str(avg)) % prob)
        print(('Average %s as Fraction of Genome Length: ' + str(avg/n)) % prob)
    return avg

################################################################################

def getRandStrings(n=10, seed=None):
    # Set the rng seed (note: will use system time if no seed was given).
    random.seed(seed)

    # List of chars.
    letters = list('abcdefghijklmnopqrstuvwxyz')

    # Create random strings for ED.
    s1List = [random.choice(letters) for x in range(n)]
    s1 = ''.join(s1List)
    s2List = [random.choice(letters) for x in range(n)]
    s2 = ''.join(s2List)

    return s1, s2

################################################################################

def compareRandStrings(verbatim=False, trials=30, n=10, prob='ED', seed=None):
    # For each trial, generate 2 strings, compute ED, track average ED.
    avg = 0
    for t in range(trials):
        s1, s2 = getRandStrings(n, seed)
        dist, edits = ED(s1, s2, prob)
        avg += dist
        if prob == 'ED':
            edited = makeEdits(s1, edits)
            if edited != s2:
                print('Failed Test!!!')
    avg = avg/trials
    if verbatim:
        print('Performed ' + str(trials) + ' trials.')
        print('Compared strings of size ' + str(n))
        print(('Average %s: ' + str(avg)) % prob)
        print(('Average %s as Fraction of String Length: ' + str(avg/n)) % prob)
    return avg

################################################################################
