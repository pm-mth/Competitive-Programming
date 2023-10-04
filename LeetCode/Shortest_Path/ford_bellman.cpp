#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph;
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph.push_back({u, v, w});
    }

    const int inf = INT_MAX;
    vector<int> distances(n + 1, inf);
    distances[1] = 0;

    for (int _ = 0; _ < n - 1; _++) {
        for (const vector<int>& edge : graph) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            if (distances[u] != inf && distances[u] + w < distances[v]) {
                distances[v] = distances[u] + w;
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        if (distances[i] == inf) {
            distances[i] = 30000;
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << distances[i] << " ";
    }

    return 0;
}
