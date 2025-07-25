#include "graph__export.h"

#include "graph/node__export.h"
#include "graph/edge__export.h"

#include <stdlib.h>

// move constants to top
const int graph$$max_steps_to_walk = 1000;

struct graph$$Graph$$stub graph$$create_rand_graph(int num_nodes, int num_edges) {
    struct graph$$Graph$$stub g;
    (*(struct graph$$Graph*)&g).num_nodes = num_nodes;
    (*(struct graph$$Graph*)&g).num_edges = num_edges;
    (*(struct graph$$Graph*)&g).nodes = (struct graph$node$$Node$$stub *) calloc(num_nodes, sizeof(struct graph$node$$Node$$stub));
    (*(struct graph$$Graph*)&g).edges = (struct graph$edge$$Edge$$stub *) calloc(num_edges, sizeof(struct graph$edge$$Edge$$stub));
    for (int i=0; i<num_edges; ++i) {
        struct graph$node$$Node$$stub *first = graph$$grab_random_node(&g), *second = graph$$grab_random_node(&g);
        (*(struct graph$$Graph*)&g).edges[i] = graph$edge$$create_edge(first, second);
        graph$node$$add_edge(first, &(*(struct graph$$Graph*)&g).edges[i]);
        graph$node$$add_edge(second, &(*(struct graph$$Graph*)&g).edges[i]);
    }
    return g;
}

struct graph$node$$Node$$stub *graph$$grab_random_node(struct graph$$Graph$$stub *g) {
    return &((struct graph$$Graph*)g)->nodes[rand() % ((struct graph$$Graph*)g)->num_nodes];
}

int graph$$path_found(struct graph$node$$Node$$stub *first, struct graph$node$$Node$$stub *second) {
    return graph$node$$random_search(first, second, graph$$max_steps_to_walk);
}

int graph$$destroy_graph(struct graph$$Graph$$stub *g) {
    free(((struct graph$$Graph*)g)->nodes);
    free(((struct graph$$Graph*)g)->edges);
    return 0;
}
