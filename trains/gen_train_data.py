"""
System "pocigągów" ... de facto połączeń między miastami reprezentowanymi przez liczby

[(4,8), (1,3), (2,2), (3, 1), (1,10)]


"""
from random import randint, seed

N_CITIES = 20
seed(111)


def generate_data(data_size):
    res = []
    for i in range(data_size):
        res.append((randint(0, N_CITIES - 1), randint(0, N_CITIES - 1)))
    return res


if __name__ == '__main__':
    rr = generate_data(10)
    print(rr)