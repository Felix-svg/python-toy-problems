"""
Write a function:

function solution(A);

that, given an array A of N integers, returns the minimum number of moves needed to end up with exactly 10 bricks in every box. If this is not possible, the function should return −1.
"""

def solution(A):
    total_bricks = sum(A)
    target_sum = 10 * len(A)
    excess = total_bricks - target_sum
    if excess < 0:
        return -1
    moves = 0
    for bricks in A:
        if bricks < 10:
            moves += 10 - bricks
    return moves

A = [7, 15, 10, 8]
print(solution(A))


