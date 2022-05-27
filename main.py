# This is a sample Python script.
from mealpy.swarm_based.BFO import OriginalBFO
from mealpy.swarm_based.ABC import BaseABC
import numpy as np
from opfunu.cec_basic.cec2014 import *
from opfunu.type_based.uni_modal import Functions


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
    functions = Functions()
    ## Setting parameters
    epoch = 50
    pop_size = 150
    objective_fun = functions._rosenbrock__
    problem_dict = {
        "fit_func": objective_fun,
        "lb": -30,
        "ub": 30,
        "minmax": "min",
        "n_dims": 2

    }

    # multiplePasses(problem_dict, epoch, pop_size, 1)

    bfo = OriginalBFO(problem_dict, epoch, pop_size)
    best_position_bfo, best_fit_bfo = bfo.solve()
    time_bfo = sum(bfo.history.list_epoch_time)
    print(f"BFO best position: {best_position_bfo} best fitness: {best_fit_bfo} time: {int(time_bfo)}")
    abc = OriginalBFO(problem_dict, epoch, pop_size)
    best_position_abc, best_fit_abc = abc.solve()
    time_abc = sum(abc.history.list_epoch_time)
    print(f"ABC best position: {best_position_abc} best fitness: {best_fit_abc} time: {int(time_abc)}")
    # bfo.history.save_global_objectives_chart()
    # bfo.history.save_local_objectives_chart()
    # bfo.history.save_global_best_fitness_chart()
    # bfo.history.save_local_best_fitness_chart()
    # bfo.history.save_trajectory_chart()

