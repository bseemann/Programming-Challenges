#!/usr/bin/python
#
#   UVa Judge ID: 861
#   http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=10&page=show_problem&problem=802
#
#   Little Bishops
#

"""Solution to the Little Bishops problem. UVa Judge ID 861."""

__author__ = ('Srivani Narra')

import sys

def backtrack(chessboard, j, size, num_bishops) :
    """The backtrack function

    Args:
        chessboard:      the current state of the chess board
	j:               the index being examined
	size:            the input size of the chessboard
	num_bishops:     the number of bishops to be placed on the chessboard
    """

    if is_solution(chessboard, j, size, num_bishops) :
	process_solution(chessboard, j, size, num_bishops)
	return

    if acceptable_solution(chessboard, j, size, num_bishops) :
        if j == size * size  :
	    return

	chessboard[j] = 1
	backtrack(chessboard, j+1, size, num_bishops)

	chessboard[j] = 0
	backtrack(chessboard, j+1, size, num_bishops)

    else :
	return

def process_solution(chessboard,j,size,num_bishops) :
    """Update the number of arrangements when a solution is found

    Args:
        chessboard:      the current state of the chess board
	j:               the index being examined
	size:            the input size of the chessboard
	num_bishops:     the number of bishops to be placed on the chessboard
    """

    global total_arrangements
    total_arrangements = total_arrangements + 1

def is_solution(chessboard, j, size, num_bishops) :
    """Check if the current state of the chessboard is a complete solution

    Args:
        chessboard:      the current state of the chess board
	j:               the index being examined
	size:            the input size of the chessboard
	num_bishops:     the number of bishops to be placed on the chessboard
    """

    cur_bishops = 0
    for i in range(0, j) :
	if chessboard[i] == True :
	    cur_bishops = cur_bishops + 1

    # if we have placed all the bishops and the state of the chessboard is acceptable
    # then the current chessboard state is an acceptable solution
    if num_bishops==cur_bishops and acceptable_solution(chessboard, j, size, num_bishops) :
	return True
    else :
	return False

    return False

def acceptable_solution(chessboard, j, size, num_bishops) :
    """Check if the current state of the chessboard is a potential solution

    Args:
        chessboard:      the current state of the chess board
	j:               the index being examined
	size:            the input size of the chessboard
	num_bishops:     the number of bishops to be placed on the chessboard
    """

    cur_bishops = 0
    for i in range(0, j) :
	if chessboard[i] == True :
	    cur_bishops = cur_bishops + 1

    bishops = [0]*cur_bishops

    bishop = 0
    for i in range(0, j) :
	if chessboard[i] == True :
	    bishops[bishop] = i
	    bishop = bishop + 1

    for i in range(len(bishops)) :
	for j in range(i) :
	    if attack(bishops[i], bishops[j], size) :
		return False

    return True

def attack(i, j, size) :
    """Check if two bishops on the chessboard attack each other

    Args:
        i:     the position of the 1st bishop.
	j:     the position of the 2nd bishop
	size:  the input size of the chessboard
    """

    i_row = (i - i%size)/size
    i_col = i%size

    j_row = (j - j%size)/size
    j_col = j%size

    if abs(i_row - j_row) == abs(i_col - j_col) :
	return True

    return False

total_arrangements = 0

# loop through the input file
for line in sys.stdin.readlines() :
    line = line.strip()
    values = line.split()

    size = int(values[0]) # length of the chessboard
    num_bishops = int(values[1]) # number of bishops

    if not ( size==0 and num_bishops==0 ) :
	total_arrangements = 0 # reset the output

	total_array_length = size * size
	chessboard = [0]*total_array_length # initialize the chessboard
	                                    # the chessboard is represented as an array of size n^2
			          	    # the ith row of the chessboard starts at (i-1)*n th index in the array
                                            # chessboard[i] = 0 means there is no bishop at the position i
                                            # chessboard[j] = 0 means there is a bishop at position i
	backtrack(chessboard, 0, size, num_bishops)      
        print total_arrangements
