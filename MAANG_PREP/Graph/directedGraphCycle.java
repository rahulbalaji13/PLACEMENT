class Solution 
{
    public boolean isCyclic(int V, int[][] edges) 
    {
        // Create adjacent list
        List<List<Integer>> adj = new ArrayList<>();
        
        // Add elements into created adjacency list 
        for(int i = 0; i < V; i++)
        {
            adj.add(new ArrayList<>());
        }
        
        // Add edge value into adjacency list 
        for(int[] edge : edges)
        {
            adj.get(edge[0]).add(edge[1]);
        }
        
        // Visited array
        boolean[] visited = new boolean[V];
        
        //Recursion stack array
        boolean[] recStack = new boolean[V];
        
        // Check for cycle in each connected component 
        for(int i = 0; i < V; i++)
        {
            if(!visited[i])
            {
                if(dfs(i, adj, visited, recStack))
                {
                    return true; // Cycle found
                }
            }
        }
        return false; // No cycle found
    }
    
    public static boolean dfs(int node, List<List<Integer>> adj, boolean[] visited, boolean[] recStack)
    {
        visited[node] = true;
        recStack[node] = true;  // add node to recusion stack
        
        // Visit all neighbor
        
        for(int neighbor : adj.get(node))
        {
            if(!visited[neighbor])
            {
                if(dfs(neighbor, adj, visited, recStack))
                {
                    return true;  // If cycle found in the deeper call
                }
            }
            else if(recStack[neighbor])
            {
                return true;  // Back edge found cycle detected 
            }
        }
        recStack[node] = false;
        return false;
    }
}
