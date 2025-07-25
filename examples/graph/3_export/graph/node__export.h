#pragma once

#include "node__tstub.h"

#include "edge__tstub.h"
#include "edge_picker__tstub.h"

#include <stdlib__tstub.h>

// Note: constant max_edges_per_node expanded here
struct graph$node$$Node {
    int num_edges;
    struct graph$edge$$Edge$$stub *edges[100];
    struct graph$node$$Other$$stub o;
};

int graph$node$$add_edge(struct graph$node$$Node$$stub *n, struct graph$edge$$Edge$$stub *e);

int graph$node$$random_search(struct graph$node$$Node$$stub *start, struct graph$node$$Node$$stub *end, int steps_left);
