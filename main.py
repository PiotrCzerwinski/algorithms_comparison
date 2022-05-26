# This is a sample Python script.
from mealpy.swarm_based.BFO import OriginalBFO
from mealpy.swarm_based.ABC import BaseABC
import numpy as np


def fitness_function(solution):
    return np.sum(solution ** 2)

def multiplePasses(dict,
                   epoch,
                   pop_size,
                   ):
    return None


if __name__ == '__main__':
    problem_dict1 = {
        "fit_func": fitness_function,
        "lb": [-10, -15, -4, -2, -8],
        "ub": [10, 15, 12, 8, 20],
        "minmax": "min",

    }
    epoch = 100
    pop_size = 50
    # ci = 0.01
    # ped = 0.25
    # nc = 5
    # ns = 5
    # attract_repels = [0.1, 0.2, 0.1, 10]

    model = OriginalBFO(problem_dict1,
                        epoch,
                        pop_size)
    best_position_bfo, best_fitness_bfo = model.solve()
    model.history.save_trajectory_chart("bfo_trajectory")

    print(f"Solution: {best_position_bfo}, Fitness: {best_fitness_bfo}")

    print(sum(model.history.list_epoch_time))

    # bees

    couple_bees = [16, 4]
    patch_variables = [5, 0.98]
    sites = [3, 1]
    abc_model = BaseABC(problem_dict1, epoch, pop_size)

    best_position_abc, best_fitness_abc = abc_model.solve()
    abc_model.history.save_trajectory_chart("abc_trajectory")
    print(f"Solution: {best_position_abc}, Fitness: {best_fitness_abc}")
    print(sum(abc_model.history.list_epoch_time))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
