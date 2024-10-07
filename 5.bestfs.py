# Define the successor list (graph) and initialize the start and goal nodes
SuccList = {
    'Arad': [['Sibiu', 253], ['Timisoara', 329], ['Zerind', 374]],
    'Sibiu': [['Rimnicu Vilcea', 193], ['Arad', 366], ['Fagarus', 176], ['Oradea', 380]],
    'Rimnicu Vilcea': [['Sibiu', 253], ['Pitesti', 100]],
    'Pitesti': [['Craiova', 160], ['Rimicu Vilcea', 193], ['Bucharest', 0]],
    'Fagarus': [['Sibiu', 253], ['Bucharest', 0]],
    'Timisoara': [['Arad', 366], ['Lugoj', 274]],
    'Zerind': [['Arad', 366], ['Oradea', 380]],
    'Oradea': [['Sibiu', 253]]
}

Start = 'Arad'
Goal = 'Bucharest'
Explored = list()

def GOALTEST(N):
    return N == Goal

def APPEND(L1, L2):
    return list(L1) + list(L2)

def SORT(L):
    L.sort(key=lambda x: x[1])
    return L

def GENCHILD(N):
    New_list = []
    if N in SuccList.keys():
        return SuccList[N]
    else:
        return []

def BestFirstSearch():
    Frontier = [[Start, 366]]
    EXPLORED = []
    global State

    while len(Frontier) != 0:
        print("\nCurrent Frontier:", Frontier)
        N = Frontier[0]
        print("Expanding Node:", N)
        del Frontier[0]  # Remove the first node
        
        # Check if the goal is reached
        if GOALTEST(N[0]):
            State = "SUCCESS"
            EXPLORED = APPEND(EXPLORED, [N])
            print("Goal Found! Path to goal:", EXPLORED)
            return State
        
        State = "FAILURE"
        EXPLORED = APPEND(EXPLORED, [N])
        print("Nodes Explored:", EXPLORED)
        
        # Generate children of the current node
        CHILD = GENCHILD(N[0])
        print("Generated Children:", CHILD)

        # Remove explored nodes from the children
        for val in EXPLORED:
            if val in CHILD:
                CHILD.remove(val)
        
        # Remove frontier nodes from the children
        for val in Frontier:
            if val in CHILD:
                CHILD.remove(val)
        
        # Append children to the frontier
        Frontier = APPEND(CHILD, Frontier)
        print("Unsorted Frontier:", Frontier)
        SORT(Frontier)
        print("Sorted Frontier:", Frontier)
        
        if State == "SUCCESS":
            break

    return State

# Execute the Best First Search algorithm
result = BestFirstSearch()
print("Result:", result)
