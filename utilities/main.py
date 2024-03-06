from graph import Graph

operations = ['CC', 'CM', 'MM', 'ML', 'CL']

'''
function to turn '33L' into 'A' so it'll work with the graph class
'''

indexes = []

def name_to_letter(name):
    if name not in indexes:
        indexes.append(name)
    return indexes.index(name)

def render_name(name):
    return ''.join(['L' if n == 1 and i == 2 else 'R' if n == -1 and i == 2 else str(n) for i, n in enumerate(name)])

def get_neigh(state, amount=3):
    neigh = []
    # CC
    if state[1]>=2:
        neigh.append([1, amount-state[0], amount-(state[1]-2)])
    # CM
    if sum(state[:-1])>=2:
        neigh.append([2, amount-(state[0]-1), amount-(state[1]-1)])
    # MM
    if state[0]>=2:
        neigh.append([3, amount-(state[0]-2), amount-state[1]])
    
    # Handle individual (round-trip)
    if state[2]==-1:
        # ML
        if state[0]>=1:
            neigh.append([4, amount-(state[0]-1), amount-(state[1])])

        # CL
        if state[1]>=1:
            neigh.append([5, amount-(state[0]), amount-(state[1]-1)])

    return [n+[state[2]*-1] for n in neigh if n[1]>=n[2]]


def encode(state):
    return name_to_letter(render_name(state))

graph = Graph()

def generate_graph(init):
    # print(init)
    if init==(3,3,-1) or init[1]>init[0]:
        print(init)
        return
    neigh = get_neigh(init)
    for n in neigh:
        if encode(n) not in indexes:
            graph.add_edge(encode(init), encode(n[1:]), n[0])
            generate_graph(n[1:])


generate_graph([3,3,1])