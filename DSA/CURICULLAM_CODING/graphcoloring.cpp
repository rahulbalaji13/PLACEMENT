#include <iostream>
#include <list>
using namespace std;
class Graph
{
    int V;
    list<int> *adj;
public:
    Graph(int V)   { this->V = V; adj = new list<int>[V]; }
    ~Graph()       { delete [] adj; }
 
    void addEdge(int v, int w);
 
    void greedyColoring();
};
 
void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w);
    adj[w].push_back(v);  
}
 

void Graph::greedyColoring()
{
    int result[V];
 
    result[0]  = 0;

    for (int u = 1; u < V; u++)
        result[u] = -1; 
 
    bool available[V];
    for (int cr = 0; cr < V; cr++)
        available[cr] = false;
 

    for (int u = 1; u < V; u++)
    {

        list<int>::iterator i;
        for (i = adj[u].begin(); i != adj[u].end(); ++i)
            if (result[*i] != -1)
                available[result[*i]] = true;
 
        int cr;
        for (cr = 0; cr < V; cr++)
            if (available[cr] == false)
                break;
 
        result[u] = cr; 
 
        for (i = adj[u].begin(); i != adj[u].end(); ++i)
            if (result[*i] != -1)
                available[result[*i]] = false;
    }
 

    for (int u = 0; u < V; u++)
        cout << "Vertex " << u << " --->  Color "
             << result[u] << endl;
}
 

int main()
{
    //Biology = 0, Chemistry = 1, CS = 2, Physics = 3, Mathematics = 4
    Graph g(5);
    g.addEdge(0, 1); //there exists a common student between bio and chem
    g.addEdge(0, 2); //there exists a common student between bio and CS
    g.addEdge(1, 2); //there exists a common student between chem and CS
    g.addEdge(1, 4); //there exists a common student between chem and mathematics
    g.addEdge(2, 4); //there exists a common student between CS and mathematics
    g.addEdge(4, 3); //there exists a common student between physics and mathematics
    cout << "Coloring of graph \n";
    g.greedyColoring();
 
    return 0;
}
