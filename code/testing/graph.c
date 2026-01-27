module;

import graph/node;
import graph/edge;

import stdlib;

export struct Graph {
    struct Node *nodes;
    struct Edge *edges;
    int num_nodes;
    int num_edges;
};

export struct Graph create_rand_graph(int num_nodes, int num_edges) {
    struct Graph g;
    g.num_nodes = num_nodes;
    g.num_edges = num_edges;
    g.nodes = (struct Node *) calloc(num_nodes, sizeof(struct Node));
    g.edges = (struct Edge *) calloc(num_edges, * sizeof(struct Edge));
    for (int i=0; i<num_edges; ++i) {
        struct Node *first = grab_random_node(&g), *second = grab_random_node(&g);
        g.edges[i] = create_edge(first, second);
        add_edge(first, &g.edges[i]);
        add_edge(second, &g.edges[i]);
    }
    return g;
}

export struct Node *grab_random_node(struct Graph *g) {
    return &g->nodes[rand() % g->num_nodes];
}

// const int max_steps_to_walk = 1000;
int max_steps_to_walk = 1000;
export int path_found(struct Node *first, struct Node *second) {
    return random_search(first, second, max_steps_to_walk);
}

export int destroy_graph(struct Graph *g) {
    free(g->nodes);
    free(g->edges);
    return 0;
}