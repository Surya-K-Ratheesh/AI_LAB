from sys import maxsize
from itertools import permutations

V = 4
graph = [[0, 10, 15, 20], 
         [10, 0, 35, 25],
         [15, 35, 0, 30], 
         [20, 25, 30, 0]]
s = 0

def travellingSalesmanProblem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    best_tour = None

    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_pathweight = 0
        k = s
        
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        
        current_pathweight += graph[k][s]
        
        if current_pathweight < min_path:
            min_path = current_pathweight
            best_tour = [s] + list(i) + [s]

    return min_path, best_tour


min_path, best_tour = travellingSalesmanProblem(graph, s)
print('min_path =', min_path)
print('best_tour =', best_tour)
