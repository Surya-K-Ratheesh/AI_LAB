def main():
    print("\t\t********DEPTH FIRST SEARCH********\n\n")
    
    goal = input("ENTER THE GOAL NODE: ")
    dfs(visited, graph, 'a', goal)
    

def dfs(visited, graph, node, goalnode):
    if node not in visited:
        visited.append(node)
        print(f"VISITED: {visited}")

        if node == goalnode:
            print("GOAL REACHED")
            print(f"THE PATH TAKEN IS {visited}")
            return True
        
        for neighbour in graph[node]:
            if dfs(visited, graph, neighbour, goalnode):
                return True
    
    return False

visited = []

graph = {  
    'a' : ['b','c'],
    'b' : ['a','c','d'],
    'c' : ['a','b','d'],
    'd' : ['b','c']
}    

if __name__ == '__main__':
    main()
