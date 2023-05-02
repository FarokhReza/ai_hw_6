
import numpy
import pandas as pd
import pygad


def get_data():

    train = pd.read_csv("train.csv")
    test = pd.read_csv("test.csv")

    return train, test


def fitness(ga_instance, solution, solution_idx):
    value = 0
    for i in range(0, 1000):
        row = train_data.iloc[i]
        row_clean=row[1:11]
        res = numpy.sum(solution*row_clean)
        difference = (row['result'] - res)**2
        value += difference

    return 1.0/value


if __name__ == "__main__":
    train_data, test_data = get_data()
    num_generations = 50
    num_parents_mating = 5

    fitness_function = fitness

    sol_per_pop =50
    num_genes = 10
    init_range_low = -10
    init_range_high = 10

    parent_selection_type = "sss"
    keep_parents = 2

    crossover_type = "single_point"

    mutation_type = "random"
    mutation_percent_genes = 15
    ga_instance = pygad.GA(num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           init_range_low=init_range_low,
                           init_range_high=init_range_high,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes)
    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("solution is:")
    print(solution)
    print("solution fitness is:")
    print(solution_fitness)
    print("solution_idx is:")
    print(solution_idx)
    err=0
    for i in range(0, 10):
        row = test_data.iloc[i]
        row_clean=row[1:11]
        res = numpy.sum(solution*row_clean)
        print("guess for test {} is {}".format(i,(row['result'] - res)**2))
        err+= (row['result'] - res)**2
    print("Error is:")
    print(err)


