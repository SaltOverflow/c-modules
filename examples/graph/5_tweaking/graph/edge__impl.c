#include "edge__export.h"

#include "node__export.h"

struct graph$edge$$Other {};

struct graph$edge$$Edge$$stub graph$edge$$create_edge(struct graph$node$$Node$$stub *first, struct graph$node$$Node$$stub *second) {
    struct graph$edge$$Edge$$stub e = (*(struct graph$edge$$Edge$$stub*)&(struct graph$edge$$Edge){{first, second}});
    return e;
}
