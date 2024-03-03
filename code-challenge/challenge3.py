import string
import random

def solution(N):
    # letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = string.ascii_lowercase
    count = N // 26
    remainder = N % 26
    result = ''.join([letters * count])
    result += letters[:remainder]

    result_list = list(result)
    random.shuffle(result_list)

    return ''.join(result_list)


print(solution(5))