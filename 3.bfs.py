def main():
    print("\t\t********BREATH FIRST SEARCH********\n\n")
    
    goal = input("ENTER GOAL NODE: ")
    bfs(visited, graph, 'a', goal)
    

def bfs(visited, graph, startnode, goalnode):
    flag = 0
    visited.append(startnode)
    queue.append(startnode)
    
    while queue:
        m = queue.pop()
        for neighbour in graph[m]:
            if flag == 0:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    print(f"VISITED: {visited}")
                    
                    if neighbour == goalnode:
                        print("")
                        print("GOAL REACHED")
                        print(f"THE PATH TAKEN IS {visited}")
                        flag = 1
    
    if flag == 0:
        print("GOAL NOT REACHED")
        
        
visited = []
queue = []

graph = {  
    'a' : ['b','c'],
    'b' : ['a','c','d'],
    'c' : ['a','b','d'],
    'd' : ['b','c']
}

# graph = {
#     5 : [3, 7],
#     3 : [2, 4],
#     7 : [8],
#     2 : [],
#     4 : [8],
#     8 : []
# }

if __name__ == '__main__':
    main()