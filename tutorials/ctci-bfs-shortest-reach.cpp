// BFS: Shortest Reach in a Graph
// Implement a Breadth First Search (BFS).
//
// https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
//

#include <bits/stdc++.h>

using namespace std;

class Graph
{
    vector<vector<int>> edges;

public:
    Graph(int n)
    {
        edges.resize(n);
    }

    void add_edge(int u, int v)
    {
        // le graphe est non orienté: le noeud u et connecté à v et vice-versa
        edges[u].push_back(v);
        edges[v].push_back(u);
    }

    vector<int> shortest_reach(int start) const
    {
        vector<int> distances(edges.size(), -1);
        set<int> visited;
        queue<int> q;

        // on commence sur le noeud de départ
        distances[start] = 0;
        visited.insert(start);
        q.push(start);

        // tant qu'il y a des noeuds à visiter
        while (! q.empty())
        {
            auto node = q.front();
            q.pop();

            // distance relative avec start
            auto distance = distances[node];

            for (auto connected : edges[node])
            {
                if (visited.count(connected) == 0)
                {
                    // noeud non encore visité
                    visited.insert(connected);
                    distances[connected] = distance + 6;
                    q.push(connected);
                }
            }
        }

        return distances;
    }
};


int main()
{
    int queries;
    cin >> queries;

    for (int t = 0; t < queries; t++)
    {

        int n, m;
        cin >> n;
        // Create a graph of size n where each edge weight is 6:
        Graph graph(n);
        cin >> m;
        // read and set edges
        for (int i = 0; i < m; i++)
        {
            int u, v;
            cin >> u >> v;
            u--, v--;
            // add each edge to the graph
            graph.add_edge(u, v);
        }
        int startId;
        cin >> startId;
        startId--;
        // Find shortest reach from node s
        vector<int> distances = graph.shortest_reach(startId);

        for (int i = 0; i < distances.size(); i++)
        {
            if (i != startId)
            {
                cout << distances[i] << " ";
            }
        }
        cout << endl;
    }

    return 0;
}
