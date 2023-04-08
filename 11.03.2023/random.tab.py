from random import seed, randint

from zadanie2.automat import run_tests, visualize


def solve(a: list[int]) -> int:
    #your solution comes in here...
    return 10


def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return {"a": data_a}


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve, max_size=10**4)
    visualize(x, y)
    # print(solve([2, 5, 7, 9, 2], [4, 8, 18, 27]))