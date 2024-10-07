def main():
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    m = 3  
    colour = [0 for _ in range(4)]  

    if not graphColouring(graph, m, 0, colour):
        print("Solution does not exist")

def isSafe(graph, colour):
    for i in range(4):
        for j in range(i + 1, 4):
            if graph[i][j] and colour[j] == colour[i]:
                return False
    return True

def graphColouring(graph, m, i, colour):
    if i == 4:
        if isSafe(graph, colour):
            printSolution(colour)
            return True
        return False

    for j in range(1, m + 1):
        colour[i] = j

        if graphColouring(graph, m, i + 1, colour):
            return True

        colour[i] = 0

    return False

def printSolution(colour):
    print("Solution exists: Following are the assigned colors")
    for i in range(4):
        print(colour[i], end=" ")
    print()  

if __name__ == "__main__":
    main()
