# This is a sample Python script.
from mealpy.swarm_based.BFO import OriginalBFO
from mealpy.swarm_based.ABC import BaseABC
import numpy as np
from opfunu.cec_basic.cec2014 import *
from opfunu.type_based.uni_modal import Functions
import csv


def multiplePasses(function,
                   lb,
                   up,
                   epoch,
                   pop_size,
                   repetitions
                   ):
    dict = {
        "fit_func": function,
        "lb": lb,
        "ub": up,
        "minmax": "min",
        "n_dims": 2

    }

    f = open('bfo_abc.csv', 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(["algorithm", "best position x", "best position y", "best fitness", "time"])
    for i in range(repetitions):
        bfo = OriginalBFO(dict, epoch, pop_size)
        abc = BaseABC(dict, epoch, pop_size)
        best_position_bfo, best_fitness_bfo = bfo.solve()
        time_bfo = sum(bfo.history.list_epoch_time)
        bfo_row = ["bfo", best_position_bfo[0], best_position_bfo[1], best_fitness_bfo, int(time_bfo)]
        best_position_abc, best_fitness_abc = abc.solve()
        time_abc = sum(abc.history.list_epoch_time)
        abc_row = ["abc", best_position_abc[0], best_position_abc[1], best_fitness_abc, int(time_abc)]
        writer.writerow(bfo_row)
        writer.writerow(abc_row)
        bfo = None
        abc = None
    f.close()


if __name__ == '__main__':
    functions = Functions()
    ## Setting parameters
    epoch = 25
    pop_size = 100
    objective_fun = functions._rosenbrock__
    problem_dict = {
        "fit_func": objective_fun,
        "lb": -30,
        "ub": 30,
        "minmax": "min",
        "n_dims": 2

    }

    multiplePasses(objective_fun, -30, 30, 100, 10, 10)
    # bfo = OriginalBFO(problem_dict, epoch, pop_size)
    # best_position_bfo, best_fit_bfo = bfo.solve()
    # time_bfo = sum(bfo.history.list_epoch_time)
    # print(f"BFO best position: {best_position_bfo} best fitness: {best_fit_bfo} time: {int(time_bfo)}")
    # abc = BaseABC(problem_dict, epoch, pop_size)
    # best_position_abc, best_fit_abc = abc.solve()
    # time_abc = sum(abc.history.list_epoch_time)
    # print(f"ABC best position: {best_position_abc} best fitness: {best_fit_abc} time: {int(time_abc)}")

    # bfo.history.save_global_objectives_chart()
    # bfo.history.save_local_objectives_chart()
    # bfo.history.save_global_best_fitness_chart()
    # bfo.history.save_local_best_fitness_chart()
    # bfo.history.save_trajectory_chart()
