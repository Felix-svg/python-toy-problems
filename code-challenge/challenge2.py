def sum_of_numbers(number):
    return sum(int(digit) for digit in str(number))

def solution(A):
    maximum_sum = -1
    digit_sums = {}

    for num in A:
        sum_digits = sum_of_numbers(num)
        if sum_digits not  in digit_sums:
            digit_sums[sum_digits] = num
        else:
            maximum_sum = max(maximum_sum, digit_sums[sum_digits] + num)
            digit_sums[sum_digits] = max(digit_sums[sum_digits], num)

    return maximum_sum

my_array = [51, 71, 17, 42]
print(solution(my_array))