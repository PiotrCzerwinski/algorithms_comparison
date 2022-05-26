# This is a sample Python script.
from mealpy.swarm_based.BFO import OriginalBFO
from mealpy.swarm_based.ABC import BaseABC
import numpy as np


def fitness_function(solution):
    return np.sum(solution ** 2)


def multiplePasses(dict,
                   epoch,
                   pop_size,
                   repetitions
                   ):
    bfo_solutions = [{} for _ in range(repetitions)]
    abc_solutions = [{} for _ in range(repetitions)]
    bfo = OriginalBFO(dict, epoch, pop_size)
    abc = BaseABC(dict, epoch, pop_size)
    for i in range(repetitions):
        best_position_bfo, best_fitness_bfo = bfo.solve()
        time_bfo = sum(bfo.history.list_epoch_time)
        bfo_solutions[i]['bp'] = best_position_bfo
        bfo_solutions[i]['bf'] = best_fitness_bfo
        bfo_solutions[i]['t'] = time_bfo

        best_position_abc, best_fitness_abc = abc.solve()
        time_abc = sum(abc.history.list_epoch_time)
        abc_solutions[i]['bp'] = best_position_abc
        abc_solutions[i]['bf'] = best_fitness_abc
        abc_solutions[i]['t'] = time_abc

    print(f"BFO {bfo_solutions}")
    print(f"ABC {abc_solutions}")


if __name__ == '__main__':
    problem_dict1 = {
        "fit_func": fitness_function,
        "lb": [-10, -15, -4, -2, -8],
        "ub": [10, 15, 12, 8, 20],
        "minmax": "min",

    }
    epoch = 100
    pop_size = 50
    multiplePasses(problem_dict1, epoch, pop_size, 3)

