## ------------------------ PROBLEM 01 ------------------------ ##

def possible_ways(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    ways = [0, 1, 2, 4]
    for k in range(4, n+1):
        ways.append( ways[k-1] + ways[k-2] + ways[k-3] )
    return ways[-1]


## ------------------------ PROBLEM 02 ------------------------ ##
## ------------------------ PROBLEM 03 ------------------------ ##
## ------------------------ PROBLEM 04 ------------------------ ##
## ------------------------ PROBLEM 05 ------------------------ ##
## ------------------------ PROBLEM 06 ------------------------ ##
## ------------------------ PROBLEM 07 ------------------------ ##
## ------------------------ PROBLEM 08 ------------------------ ##
## ------------------------ PROBLEM 09 ------------------------ ##



if __name__ == "__main__":
    # ----------------- Problem 03 (v1) ----------------
    print('')
    print('-'*120)
    print('PROBLEM 1, FIRST VERSION\n')
    for n in range(38):
        print('For n={}, ways: {}'.format(str(n).zfill(3), possible_ways(n)))
