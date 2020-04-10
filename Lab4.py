import random
from Chromosome import Chromosome
import itertools

class GA:

    def __init__(self, populationSize, problParam):
        self.__populationSize = populationSize
        self.__problParam = problParam
        self.__population = []

    def initialize(self):
        for _ in itertools.repeat(None, self.__populationSize):
            self.__population.append(Chromosome(self.__problParam, self.__problParam['start']))
        self.computeFitness()

    def getAll(self):
        return self.__population

    def computeFitness(self):
        matrix = self.__problParam['matrix']

        for chromosome in self.__population:
            chromosome.fitness = 0.0

        for chromosome in self.__population:
            chromosome.fitness += matrix[chromosome.repres[-1]][chromosome.repres[0]]
            for i in range(len(chromosome) - 1):
                chromosome.fitness += matrix[chromosome.repres[i]][chromosome.repres[i+1]]

    def bestChromosome(self):
        return min(self.__population)

    def selectRandom(self):
        c1 = random.choice(self.__population)
        c2 = random.choice(self.__population)
        return min(c1, c2)


    def createNewGeneration(self):
        newGeneration = [self.bestChromosome()]
        for _ in itertools.repeat(None, self.__populationSize):
            parent1 = self.selectRandom()
            parent2 = self.selectRandom()
            child = parent1.crossover(parent2)
            child.mutation()
            newGeneration.append(child)
        self.__population = newGeneration

def loadFile(filename):
    graph = {}
    with open(filename, 'r') as f:
        lista = [[int(num) for num in line.split(',')] for line in f]

    n = lista[0][0]
    graph['noNodes'] = n
    matrix = []
    for line in lista[1:n + 1]:
        matrix.append(line)
    graph['matrix'] = matrix
    return graph


filename = '100p_fricker26'

graph = loadFile(filename + ".txt")
populationSize = graph['noNodes'] * 10
noGenerations = 1000
graph['start'] = 0
ga = GA(populationSize, graph)
ga.initialize()

with open (filename + "_solution.txt", 'w') as f:
    f.write(str(populationSize) + '\n')
    for i in range(noGenerations-1):
        ga.createNewGeneration()
        ga.computeFitness()
        f.write(str(ga.bestChromosome()))
        print(i, ga.bestChromosome())
