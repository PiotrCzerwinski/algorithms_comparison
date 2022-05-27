# This is a sample Python script.
from mealpy.swarm_based.BFO import OriginalBFO
from mealpy.swarm_based.ABC import BaseABC
import numpy as np
from opfunu.cec_basic.cec2014 import *
from opfunu.type_based.uni_modal import Functions
import csv
import time


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
        bfo_time_start = time.time()
        best_position_bfo, best_fitness_bfo = bfo.solve()
        bfo_time_end = time.time()
        bfo_elapsed = bfo_time_end - bfo_time_start
        bfo_row = ["bfo", best_position_bfo[0], best_position_bfo[1], best_fitness_bfo, int(bfo_elapsed)]
        abc_time_start = time.time()
        best_position_abc, best_fitness_abc = abc.solve()
        abc_time_end = time.time()
        abc_elapsed = abc_time_end - abc_time_start
        abc_row = ["abc", best_position_abc[0], best_position_abc[1], best_fitness_abc, int(abc_elapsed)]
        writer.writerow(bfo_row)
        writer.writerow(abc_row)
    f.close()


if __name__ == '__main__':
    functions = Functions()
    ## Setting parameters
    epoch = 25
    pop_size = 100
    objective_fun = functions._zakharov__
    # problem_dict = {
    #     "fit_func": objective_fun,
    #     "lb": -5,
    #     "ub": 10,
    #     "minmax": "min",
    #     "n_dims": 2
    #
    # }

    multiplePasses(objective_fun, -5, 10, 25, 50, 5)
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
