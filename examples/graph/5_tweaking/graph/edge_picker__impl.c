#include "edge_picker__export.h"

#include "edge__export.h"
#include "node__export.h"

#include <stdlib.h>

struct graph$edge_picker$$Controller {};

struct graph$edge_picker$$Controller$$stub graph$edge_picker$$get_controller() {
    return (*(struct graph$edge_picker$$Controller$$stub*)&(struct graph$edge_picker$$Controller){});
}

struct graph$node$$Node$$stub *graph$edge_picker$$pick_next(struct graph$edge_picker$$Controller$$stub *c, struct graph$node$$Node$$stub *n) {
    if (((struct graph$node$$Node*)n)->num_edges == 0) return NULL;
    struct graph$edge$$Edge$$stub *e = ((struct graph$node$$Node*)n)->edges[rand() % ((struct graph$node$$Node*)n)->num_edges];
    return ((struct graph$node$$Node*)((struct graph$edge$$Edge*)e)->nodes[0]) == ((struct graph$node$$Node*)n) ? ((struct graph$edge$$Edge*)e)->nodes[1] : ((struct graph$edge$$Edge*)e)->nodes[0];
}
