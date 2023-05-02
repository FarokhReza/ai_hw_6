import pandas as pd
import random
import pygad
import numpy as np
import math

def get_data():
    train = pd.read_csv("train.csv")
    test = pd.read_csv("test.csv")
    return train, test

def solution_gen():
    # Generate a random solution with weights between -1 and 1
    solution = [random.uniform(-1, 1) for _ in range(10)]
    return solution

def fitness(solution, *args):
    pandas_data = args[0]
    answer = 0
    for i in range(len(pandas_data)):
        temp = 0
        for j in range(10):
            temp += pandas_data.iloc[i, j] * solution[j]
        answer += (pandas_data.iloc[i, 10] - temp)
    answer /= 1000
    return abs(1.0 / answer)

def callback_generation(ga_instance):
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))

if __name__ == "__main__":
    train_data, test_data = get_data()
    
    # Initialize a new GA instance with the necessary parameters
    num_generations = 50
    num_parents_mating = 100
    ga_instance = pygad.GA(num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness,
                           sol_per_pop=num_parents_mating,
                           num_genes=10,
                           gene_type=float,
                           gene_space=[-1, 1],
                           parent_selection_type="rank",
                           crossover_type="two_point",
                           mutation_type="random",
                           mutation_percent_genes=10,
                        #    callback_generation=callback_generation,
                           args=(train_data,))
    
    # Run the GA
    ga_instance.run()
    
    # Get the best solution from the GA
    best_solution = ga_instance.best_solution
    
    # Evaluate the best solution on the test data
    test_predictions = []
    for i in range(len(test_data)):
        temp = 0
        for j in range(10):
            temp += test_data.iloc[i, j] * best_solution[j]
        test_predictions.append(temp)
    
    print("Predictions on test data:")
    print(test_predictions)
