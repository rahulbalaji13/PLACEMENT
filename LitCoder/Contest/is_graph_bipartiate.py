from collections import deque

def is_bipartite(graph):
    """
    Check if the given undirected graph is bipartite.

    Args:
    graph (List[List[int]]): The adjacency list representation of the graph.

    Returns:
    bool: True if the graph is bipartite, False otherwise.
    """
    n = len(graph)
    color = [-1] * n  # -1 indicates uncolored

    for start in range(n):
        if color[start] == -1:  # Not colored yet
            queue = deque([start])
            color[start] = 0  # Start coloring with color 0
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # If neighbor is uncolored
                        color[neighbor] = 1 - color[node]  # Color with opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # Same color found
                        return False
    return True

def main():
    """
    Main function to take user input and check if the graph is bipartite.
    """
    n = int(input("Enter the number of nodes: "))
    graph = []
    
    print("Enter the adjacency list for each node (space-separated, one line per node):")
    for _ in range(n):
        neighbors = list(map(int, input().split()))
        graph.append(neighbors)
    
    if is_bipartite(graph):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()
