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


