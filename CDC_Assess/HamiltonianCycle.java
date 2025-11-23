import java.util.*;

 class HamiltonianCycle {
    private int V;
    private int[][] graph;
    private int[] path;

    public HamiltonianCycle(int V, int[][] graph) {
        this.V = V;
        this.graph = graph;
        this.path = new int[V + 1];
        
        Arrays.fill(path, -1);
        
        path[0] = 0;
    }

    private boolean isSafe(int v, int pos) {
        if (graph[path[pos - 1]][v] == 0) {
            return false;
        }

        for (int i = 0; i < pos; i++) {
            if (path[i] == v) {
                return false;
            }
        }

        return true;
    }

    private boolean hamiltonianCycleUtil(int pos) {
        if (pos == V) {
            return graph[path[pos - 1]][path[0]] == 1;
        }

        for (int v = 1; v < V; v++) {
            if (isSafe(v, pos)) {
                path[pos] = v;

                if (hamiltonianCycleUtil(pos + 1)) {
                    return true;
                }

                path[pos] = -1;
            }
        }

        return false;
    }

    public boolean findHamiltonianCycle() {
        if (!hamiltonianCycleUtil(1)) {
            return false;
        }
        
        path[V] = 0;
        return true;
    }

    public void printSolution() {
        for (int i = 0; i <= V; i++) {
            System.out.print(path[i] + (i < V ? " " : ""));
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int V = scanner.nextInt();
        
        int[][] graph = new int[V][V];
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                graph[i][j] = scanner.nextInt();
            }
        }
        
        HamiltonianCycle hamCycle = new HamiltonianCycle(V, graph);
        
        if (hamCycle.findHamiltonianCycle()) {
            hamCycle.printSolution();
        } else {
            System.out.println("Hamiltonian path does not exist");
        }
        
        scanner.close();
    }
}
