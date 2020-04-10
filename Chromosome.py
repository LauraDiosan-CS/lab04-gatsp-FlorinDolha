from random import randint, shuffle


def generateARandomPermutation(n, start):
    perm = [i for i in range(n)]
    shuffle(perm)
    posStart = perm.index(start)
    perm[0], perm[posStart] = perm[posStart], perm[0]

    pos1 = randint(1, n - 1)
    pos2 = randint(1, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm


class Chromosome:
    def __init__(self, problParam=None, start=0):
        self.__problParam = problParam
        self.__repres = generateARandomPermutation(self.__problParam['noNodes'], self.__problParam['start'])
        self.__fitness = 0.0
        self.__start = start

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        pos1 = randint(1, len(self.__repres) - 1)
        pos2 = randint(1, len(self.__repres) - 1)
        if pos1 > pos2:
            pos1, pos2 = pos2, pos1

        newrepres = [None] * len(self.__repres)
        newrepres[pos1:pos2+1] = self.__repres[pos1:pos2+1]
        for elem in c.__repres:
            if elem not in newrepres:
                pos = newrepres.index(None)
                newrepres[pos] = elem
        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        pos1 = randint(1, len(self.__repres) - 1)
        pos2 = randint(1, len(self.__repres) - 1)
        self.__repres[pos1], self.__repres[pos2] = self.__repres[pos2], self.__repres[pos1]

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness

    def __lt__(self, other):
        return self.__fitness < other.__fitness

    def __gt__(self, other):
        return self.__fitness > other.__fitness

    def __ge__(self, other):
        return self.__fitness >= other.__fitness

    def __le__(self, other):
        return self.__fitness <= other.__fitness

    def __len__(self):
        return len(self.__repres)