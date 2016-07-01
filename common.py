from itertools import *
import csv

def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((float(xy[0]), float(xy[1])))
        return cities


def format_solution(solution):
    return 'index\n' + '\n'.join(map(str, solution))


def print_solution(solution):
    print(format_solution(solution))

def powerset(s):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    for r in range(len(s)+1):
        for tpl in combinations(s, r):
            yield list(tpl)

def output_powerset():
    with open("output.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(powerset(range(1, 2048)))


if __name__ == '__main__':
    output_powerset()