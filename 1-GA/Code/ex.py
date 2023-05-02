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

def fitness_(solution, pandas_data, idx_solution=0):
    answer = 0
    for i in range(len(pandas_data)):
        temp = 0
        if type(pandas_data) == pd.core.frame.DataFrame:
            for j in range(10):
                temp += abs(pandas_data.iloc[i, j]*solution[j])
            answer += (pandas_data.iloc[i, 10] - temp)
        else:
            for j in range(10):
                temp += abs(pandas_data[i][j]*solution[j])
            answer += (pandas_data[i][10] - temp)
    answer /= 1000
    
    return abs(1.0/answer)



if __name__ =="__main__" :
    train_data , test_data =  get_data()
    
    solution = []
    for i in range(20):
        s = solution_gen()
        solution.append(s)
    
    rankedsolution = []
    for i in range(20):
        x = fitness_(solution[i], train_data)
        rankedsolution.append( (x, solution[i]) )
    rankedsolution.sort(reverse=True)
    best_solutions = [x[1] for x in rankedsolution[:10]]
    initial_population = np.array(best_solutions)
    ga = pygad.GA(
                initial_population=initial_population,
                num_generations=50, 
                num_parents_mating=10, 
                fitness_func=fitness_, 
                # sol_per_pop=50, 
                # num_genes=10, 
                # gene_type=float, 
                # init_range_low=-1.0, 
                # init_range_high=1.0, 
                # gene_space=[-1, 1],
                # args=(train_data,)
                )

    ga.run()

    best_solution, best_fitness = ga.best_solution()
    print("Best solution:", best_solution)
    print("Best fitness:", best_fitness)
