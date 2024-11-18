import cv2
import time
import random
import numpy as np
import matplotlib.pyplot as plt



def initialize_pop(POP_SIZE, TARGET):
    population = []
    height, width = TARGET.shape
    for _ in range(POP_SIZE):
        random_binary_array = np.random.randint(0, 256, size=(height, width))
        fitness = np.sum(TARGET != random_binary_array)
        population.append([random_binary_array, fitness])
    return population


def fitness_cal(chromo_from_pop, TARGET):
    differences = np.abs(TARGET - chromo_from_pop)
    num_differences = np.sum(differences)
    return num_differences


def selection(population, POP_SIZE):
    sorted_chromo_pop = sorted(population, key=lambda x: x[1])
    return sorted_chromo_pop[:int(0.5 * POP_SIZE)]


def crossover(selected_chromo, population, POP_SIZE):
    offspring_cross = []
    for _ in range(POP_SIZE):
        parent1 = random.choice(selected_chromo)[0]
        parent2 = random.choice(selected_chromo)[0]
        mask = np.random.rand(*parent1.shape) > 0.5
        child = np.where(mask, parent1, parent2)
        offspring_cross.append(child)
    return offspring_cross


def mutate(offspring, MUT_RATE):
    for arr in offspring:
        mutation_mask = np.random.rand(*arr.shape) < MUT_RATE
        noise = np.random.randint(-15, 16, size=arr.shape)
        arr[mutation_mask] = np.clip(arr[mutation_mask] + noise[mutation_mask], 0, 255)
    return offspring


def adaptive_mutation_rate(stagnation_count, base_rate=0.01):
    if stagnation_count > 10:
        return round(random.uniform(base_rate, 0.001), 3)
    else:
        return base_rate


def replace(new_gen, population, POP_SIZE, TARGET):
    new_population = []
    for new_individual in new_gen:
        new_fitness = fitness_cal(TARGET, new_individual)
        new_population.append([new_individual, new_fitness])
        new_population = sorted(new_population, key=lambda x: x[1])[:POP_SIZE]
    return new_population

def plot_best_individual(best_individual, generation, current_best_fitness):
    plt.imshow(best_individual, cmap='gray')
    plt.suptitle(f'Best individual - Generation {generation}')
    plt.title(f'Fitness: {current_best_fitness}', color="grey", style='italic')
    plt.axis('off')
    plt.draw()
    plt.pause(0.1)


def plot_fitness_progress(fitness_history):
    plt.plot(fitness_history, marker='.')
    plt.title('Best fitness change over time')
    plt.xlabel('Generation')
    plt.ylabel('Best fitness')
    plt.grid(True)
    plt.show()


def clear_line(n=1):
        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'
        for i in range(n):
            print(LINE_UP, end=LINE_CLEAR)


def main():
    fitness_history = []
    POP_SIZE = 100
    MUT_RATE = 0.01
    generation = 0
    max_generation = 1000
    stagnation_count = 0
    percent = 0
    total_time = 0
    space = 20*' '
    loc = 'dog.jpg'
    image = cv2.imread(loc, cv2.IMREAD_GRAYSCALE)
    TARGET = image
    population = initialize_pop(POP_SIZE, TARGET)
    fitness = min(population, key=lambda x: x[1])[1]
  
    plt.ion()
    fig, ax = plt.subplots()
  
    while generation <= max_generation:
        start = time.time()
        selected = selection(population, POP_SIZE)
        offspring = crossover(selected, population, POP_SIZE)
        mutated_offspring = mutate(offspring, MUT_RATE)
        population = replace(mutated_offspring, population, POP_SIZE, TARGET)
        best_individual = min(population, key=lambda x: x[1])
        current_best_fitness = best_individual[1]
        fitness_history.append(current_best_fitness)

        if current_best_fitness < fitness:
            fitness = current_best_fitness
            stagnation_count = 0
        else:
            stagnation_count += 1

        MUT_RATE = adaptive_mutation_rate(stagnation_count)

        if generation % 100 == 0 or current_best_fitness == 0:
            plot_best_individual(best_individual[0], generation, current_best_fitness)

        if current_best_fitness == 0:
            break

        end = time.time() - start
        total_time += end
        current_perecent = percent*100/max_generation
        if current_perecent > 0 and current_perecent % 5 == 0:
            space = space.replace(' ', '❚', 1)
        
        print(f'Generation: {generation}')
        print(f'Fitness: {current_best_fitness}')
        print(f'Total time: {format(round(total_time, 3), '.3f')} [s]')
        print(f'|{space}| {format(current_perecent, '.1f')}%')
        clear_line(4)
        percent += 1
        generation += 1
    
    plt.ioff()
    plt.show()
    plot_fitness_progress(fitness_history)


main()
