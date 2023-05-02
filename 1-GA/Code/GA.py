import pandas as pd
import random
import pygad
import numpy as np
def get_data():

    train = pd.read_csv("train.csv")
    test = pd.read_csv("test.csv")
    
    return train , test

def solution_gen():
    # Generate a random solution with weights between -1 and 1
    solution = [random.uniform(-1, 1) for _ in range(10)]
    
    return solution

def fitness_(ga, solution, idx_solution=0):
    answer = 0
    for i in range(len(train_data)):
        temp = 0
        # if type(pandas_data) == pd.core.frame.DataFrame:
        for j in range(10):
            temp += train_data.iloc[i, j]*solution[j]
        answer += abs(train_data.iloc[i, 10] - temp)
        # else:
        #     for j in range(10):
        #         temp += abs(pandas_data[i][j]*solution[j])
        #     answer += (pandas_data[i][10] - temp)
    # answer /= 1000
    
    return 1.0/answer



if __name__ =="__main__" :
    train_data , test_data =  get_data()
    
    ga = pygad.GA(
                num_generations=50, 
                num_parents_mating=10, 
                fitness_func=fitness_, 
                sol_per_pop=50, 
                num_genes=10, 
                init_range_low=-1.0, 
                init_range_high=1.0, 
                parent_selection_type="sss",
                keep_parents=3,
                crossover_type="single_point",
                mutation_type="random",
                mutation_percent_genes=10,
                )

    ga.run()

    best_solution, best_fitness, solution_idx = ga.best_solution()
    print("Best solution:", best_solution)
    print("Best fitness:", best_fitness)
    print("solution_idx:", solution_idx)

    error = 0
    for i in range(len(test_data)):
        temp = 0
        for j in range(10):
            temp += test_data.iloc[i, j]*best_solution[j]
        x = (test_data.iloc[i, 10] - temp)
        print(f"change {i} : {temp}")
        error += abs(x)
    print(f"Error: {error/10}")