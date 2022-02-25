def n_factorial(n):
    ret_val = 1
    for i in range(n):
        ret_val *= (i+1)
    return ret_val


def sum_digit_n_factorial(n):
    total = 0
    fproduct = str(n_factorial(n))
    for i in fproduct:
        total += int(i)
    return total


if __name__ == '__main__':
    assert n_factorial(10) == 3628800
    assert sum_digit_n_factorial(10) == 27

    n = 100
    print(f'Sum of the digits in {n}! == {sum_digit_n_factorial(n)}')
