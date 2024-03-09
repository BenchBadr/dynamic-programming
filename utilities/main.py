from graph import Graph

'''
function to turn '33L' into digit so it'll work with the graph class
'''

indexes = []

def name_to_index(name):
    if name not in indexes:
        indexes.append(name)
    return indexes.index(name)

def render_name(name):
    return ''.join((str(n) for n in name[:2]))+['R','L'][name[2]]

def get_comb(n):
    comb = []
    for i in range(n):
        if (i,n-i) not in comb:
            comb.append((i,n-i))
        if (n-i,i) not in comb:
            comb.append((n-i,i))
    return comb

def get_neigh(state, amount=3, capacity=2):
    neigh = []
    comb = get_comb(capacity)
    for c in comb:
        if state[0]>=c[0] and state[1]>=c[1]:
            neigh.append([-1, amount-(state[0]-c[0]), amount-(state[1]-c[1])])
    
    # Handle individual (round-trip)
    if state[2]==0:
        # ML
        if state[0]>=1:
            neigh.append([4, amount-(state[0]-1), amount-(state[1])])

        # CL
        if state[1]>=1:
            neigh.append([5, amount-(state[0]), amount-(state[1]-1)])

    result = []
    for n in neigh:
        if (n[1]>=n[2] or n[1]==0) and n[1]+n[2]<=amount*2 and n[1]+n[2]>=0 and n[1] <= amount and n[2] <=amount  and (amount-n[1] >= amount-n[2] or amount-n[1]==0):
            modified_n = n + [int(not(state[2]))]
            result.append(modified_n)
    return result



def encode(state):
    return name_to_index(render_name(state))

graph = Graph()

def generate_graph(init, amount=3, capacity=2):
    if init==(amount,amount,0) or (init[1]>init[0] and init[0]!=0):
        return
    neigh = get_neigh(init, amount=amount, capacity=capacity)
    # print(render_name(init),[render_name(n[1:]) for n in neigh])
    for n in neigh:
        if render_name(n[1:]) not in indexes:
            graph.add_edge(encode(init), encode(n[1:]), n[0])
            generate_graph(n[1:],amount, capacity)




generate_graph([3,3,1],3, 2)

print([indexes[n] for n in graph.dfs()])
print(graph.dijkstra(name_to_index('33L'),name_to_index('33R')))


# print([render_name(n[1:]) for n in get_neigh([3,3,1])])
# print(get_neigh([0,2,0]))