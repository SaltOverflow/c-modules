#pragma once

#include "edge__tstub.h"

#include "node__tstub.h"

struct graph$edge$$Edge {
    struct graph$node$$Node$$stub *nodes[2];
    struct graph$edge$$Other$$stub o;
};

struct graph$edge$$Edge$$stub graph$edge$$create_edge(struct graph$node$$Node$$stub *first, struct graph$node$$Node$$stub *second);
