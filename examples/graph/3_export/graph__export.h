#pragma once

#include "graph__tstub.h"

#include "graph/node__tstub.h"
#include "graph/edge__tstub.h"

#include <stdlib__tstub.h>

struct graph$$Graph {
    struct graph$node$$Node$$stub *nodes;
    struct graph$edge$$Edge$$stub *edges;
    int num_nodes;
    int num_edges;
};

struct graph$$Graph$$stub graph$$create_rand_graph(int num_nodes, int num_edges);

struct graph$node$$Node$$stub *graph$$grab_random_node(struct graph$$Graph$$stub *g);

int graph$$path_found(struct graph$node$$Node$$stub *first, struct graph$node$$Node$$stub *second);

int graph$$destroy_graph(struct graph$$Graph$$stub *g);
