sys.setrecursionlimit(10**7)

def is_safe(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:
        return False 
        
    if v in path[:pos]:
        return False 
    return True 
    
def ham_cycle(graph, path, pos, n):
    if pos == n:
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False
    
    for v in range(1, n):
        if is_safe(v, graph, path, pos):
            path[pos] = v
            if ham_cycle(graph, path, pos + 1, n):
                return True 
            path[pos] = -1
    return False
        
def find_ham_cycle(graph, v):
    path = [-1] * v
    path[0] = 0
    if not ham_cycle(graph, path, 1, v):
        return None 
    path.append(path[0])
    return path
    
    
data = sys.stdin.read().strip().split()
v = int(data[0])
nums = list(map(int, data[1:]))
graph = []
idx = 0
for _ in range(v):
    row = nums[idx:idx + v]
    graph.append(row)
    idx += v
    
cycle = find_ham_cycle(graph, v)
if cycle is None:
    print("Hamiltonian path does not exist", end = "")
else:
    print(" ".join(map(str, cycle)), end = "")
