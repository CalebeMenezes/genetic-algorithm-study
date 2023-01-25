import tkinter as tk
from deap import base, creator, tools
from scipy.optimize import minimize  #busca gradiente 

def run_ga():
    def fitness_function(individual):
        return sum(individual),

    creator.create("FitnessMax", base.Fitness, weights=(1, 0))
    creator.create("indvidual", list, fitness=creator.FitnessMax)

    toolbox = base.ToolBox()
    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.individual, toolbox.attr_bool, n=100)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", fitness_function)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.25)
    toolbox.register("select", tools.selTournament, tournsize=3)
    
    pop = toolbox.population(n=300)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40

    #Evaluate the entire population    Avalie toda a população
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    def gradient_optimization(individual):
    res = minimize(fitness_function, individual, method='BFGS')
        return res.x


    for g in range(NGEN):
        # Select the next generation individuals     Selecione os indivíduos da próxima geração
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals         Clone os indivíduos selecionados
        offspring = list(map(toolbox.clone, offspring))


        # Apply crossover and mutation on the offspring   Aplicar cruzamento e mutação na prole
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness    Avalie os indivíduos com aptidão inválida
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        
    pass
def stop_ga():
    pass

root = tk.Tk()
root.title("optimization evolutiva")

run_button = tk.Button(root, text="Run", command=run_ga)
run_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_ga)
stop_button.pack()

info_label = tk.Label(root, text="Aguarde...")
info_label.pack()

root.mainloop()

