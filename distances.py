import numpy as np
import matplotlib.pyplot as plt

def generatePoints(num = 10, dim = 2, bounds = [[-2, 2], [-2, 2]]):
    points = np.empty([num, dim])
    for n in range(num):
        for d in range(dim):
            points[n][d] = round(np.random.uniform(bounds[d][0], bounds[d][1]), 2)
    return points

def showPoints(points):
    plt.scatter(points[:,0], points[:,1])
    plt.show()

def generateDistanceMatrix(points):
    num_distances = len(points[:,0])
    dim = len(points[0])
    distance_matrix = np.empty([num_distances, num_distances])
    for i in range(num_distances):
        for j in range(num_distances):
            d2 = 0
            for p in range(dim):
                d2 += (points[i][p] - points[j][p]) ** 2
            distance_matrix[i][j] = round(np.sqrt(d2), 2)
    return distance_matrix

def shiftCentroidToOrigin(points):
    translation = np.empty([len(points[:,0]), len(points[0])])
    new_points = np.empty([len(points[0])])
    for i in range(len(points[:,0])):
        translation += points[i]
    new_points = points - (translation / len(points[:,0]))
    return new_points

def derivePointsFromDistanceMatrix(distance_matrix, dim):
    return

def computeCrossProduct(distance_matrix, i, j):
    total_distances = 0
    dij = distance_matrix[i][j]
    a = 0
    b = 0
    n = len(distance_matrix[:,0])
    for k in range(n):
        a += distance_matrix[i][k] ** 2
        b += distance_matrix[k][j] ** 2
        for l in range(n):
            total_distances += distance_matrix[l][k] ** 2
    print(a)
    print(b)
    print(total_distances)
    print(dij)
    cross_product = (-1 / 2) * ((dij ** 2) - ((1 / n) * a) - ((1 / n) * b) + ((1 / (n ** 2)) * total_distances))
    return cross_product

points = generatePoints()
new_points = shiftCentroidToOrigin(points)
dm = generateDistanceMatrix(new_points)
print(dm)
print(new_points)
cross_product = computeCrossProduct(dm, 0, 0)
print(cross_product)