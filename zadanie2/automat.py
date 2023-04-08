from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint


def generate_data(data_size):
    seed(111)
    return {"a": [randint(0, 10 ** 6) for _ in range(data_size)]}


def solve_problem(a):
    ret = sorted(a)
    return ret


def run_tests(generator, solver, step_factor=1.3, max_size=10 ** 5):
    size = 10
    sizes = []
    times = []
    while size < max_size:
        print(f'testing solver for {size=:.0f} ...', end=' ')
        data = generator(int(size))
        REPETITIONS = 0
        time_sum = 0
        while True:
            st = datetime.now().timestamp()
            ret = solver(**data)
            en = datetime.now().timestamp()
            time_sum += (en - st)
            REPETITIONS += 1
            if time_sum > 0.1:
                break

        sizes.append(size)
        exec_time = time_sum / REPETITIONS * 10 ** 6
        print(f' execution time: {int(exec_time / 10**3)}ms')
        times.append(exec_time)
        size *= step_factor

    return sizes, times


def visualize(sizes, times):
    x = sizes
    y = times
    linxx = [0.01 * x_ ** 1 for x_ in x]
    alg_n_sqrt_n = [0.01 * x_ ** 1.2 for x_ in x]
    quadx = [0.01 * x_ ** 2 for x_ in x]
    cubex = [0.01 * x_ ** 3 for x_ in x]

    plt.plot(x, linxx, linestyle='dotted')
    plt.plot(x, alg_n_sqrt_n, linestyle='dotted')
    plt.plot(x, quadx, linestyle='dotted')
    plt.plot(x, cubex, linestyle='dotted')
    plt.plot(x, y)
    plt.legend(['O(N)','O(N sqrt N)', 'O(N**2)', 'O(N**3)', 'algorytm'], loc='upper left')

    plt.xlabel("Rozmiar danych")
    plt.ylabel("Czas wykonania (usec)")
    plt.yscale('log')
    plt.xscale('log')
    plt.show()
    # plt.savefig('aa.png')


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve_problem)
    visualize(x, y)