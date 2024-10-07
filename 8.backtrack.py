domain_colors = ['Red', 'Blue', 'Green']

# wa-west australia, nt-northern territory, sa-south australia, q-queensland, nsw-new south wales, v-victoria, t-tasmania
variable_states = ['wa', 'nt', 'sa', 'q', 'nsw', 'v', 't']
neighbors = {
    'wa': ['nt', 'sa'],
    'nt': ['wa', 'sa', 'q'],
    'sa': ['wa', 'nt', 'q', 'nsw', 'v'],
    'q': ['nt', 'sa', 'nsw'],
    'nsw': ['q', 'sa', 'v'],
    'v': ['sa', 'nsw'],
    't': []
}

finalstateswithcolor = {}

def getthecolor(state):
    for color in domain_colors:  # Corrected variable name
        if assigncolor(state, color):
            return color

def assigncolor(state, color):
    for neighbor in neighbors.get(state, []):  # Handles states with no neighbors
        color_of_neighbor = finalstateswithcolor.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True

def main():
    # Use degree heuristics to find the state with the largest number of neighbors first
    sorted_states = sorted(neighbors.keys(), key=lambda state: len(neighbors[state]), reverse=True)

    for state in sorted_states:
        finalstateswithcolor[state] = getthecolor(state)
    print("The states with colors are", finalstateswithcolor)

main()
