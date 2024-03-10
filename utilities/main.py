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
    if n<=1:
        return []
    comb = []
    for i in range(n // 2 + 1):
        comb.append((i, n - i))
        if i != n - i:
            comb.append((n - i, i))
    return comb+get_comb(n-1)

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
        if (n[1]>=n[2] or n[1]==0) and n[1]+n[2]>=0 and n[1] <= amount and n[2] <=amount  and (amount-n[1] >= amount-n[2] or amount-n[1]==0):
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
    for n in neigh:
        if render_name(n[1:]) not in indexes:
            graph.add_edge(encode(init), encode(n[1:]), n[0])
            generate_graph(n[1:],amount=amount, capacity=capacity)





def test(n, cap):
    generate_graph([n,n,1],n, cap)
    p = [indexes[n] for n in graph.bfs()]
    print(p, p.index(f"{n}{n}R"))
    try:
        print(graph.dijkstra(name_to_index(f'{n}{n}L'),name_to_index(f'{n}{n}R')))
    except:
        print(f"Error : No solution found (vertice {n}{n}R doesn't exist)")
    return '-'*10

print(test(3,3))
# print([render_name(n[1:]) for n in get_neigh([3,2,1],capacity=3)])
