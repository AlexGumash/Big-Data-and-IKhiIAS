# coding=utf-8
import matplotlib.pyplot as plt
from numpy import *


def function(x, y):
    return x ** 2 + y ** 2


size_x = 2
size_y = 2
area = [-size_x, size_x, -size_y, size_y]
matrix_x, matrix_y = meshgrid(linspace(area[0], area[1], 10), linspace(area[2], area[3], 10))

initial_plants = 5
plants = []
seed_amount = 10
ttl = 5
for i in range(initial_plants):
    new_plant = [random.uniform(area[0], area[1]), random.uniform(area[2], area[3]), seed_amount, ttl]
    plants.append(new_plant)

fig = plt.figure()
fig.show()

steps = 1000

max_plants = 30
weight = 5
kill_radius = 0.875 * sqrt(function(size_x, size_y))
for step in range(steps):

    fig.clf()
    plt.contourf(matrix_x, matrix_y, function(matrix_x, matrix_y))

    for plant in plants:
        conditions_j = function(plant[0], plant[1])

        for k in plants:
            conditions_k = function(k[0], k[1])
            kill_condition = abs(conditions_k) > kill_radius or (k[3] <= 0)
            if kill_condition:
                plants.remove(k)

        for k in range(int(weight / conditions_j)):
            if (len(plants) < max_plants) and (plant[2] > 0):
                new_x = random.uniform(plant[0] - sqrt(conditions_j), plant[0] + sqrt(conditions_j))
                new_y = random.uniform(plant[1] - sqrt(conditions_j), plant[1] + sqrt(conditions_j))
                new_seeds = int(weight / abs(function(new_x, new_y)))
                new_ttl = int(weight / abs(function(new_x, new_y)))
                new_plant_from_seed = [new_x, new_y, new_seeds, new_ttl]
                plants.append(new_plant_from_seed)
                plant[2] = plant[2] - 1

        plant[3] = plant[3] - 1
        plt.axis(area)
        plt.scatter(plant[0], plant[1])
    fig.canvas.draw()
plt.show()