#include "node__export.h"

#include "edge__export.h"
#include "edge_picker__export.h"

#include <stdlib__export.h>

// move constants to top
const int graph$node$$max_edges_per_node = 100;
const int graph$node$$continue_rate = 2;

// also move function declarations (of those not already in `node__export.h`) to top
int graph$node$$random_search$$mangle(struct graph$node$$Node$$stub *start, struct graph$node$$Node$$stub *end, int *steps_left);

int graph$node$$add_edge(struct graph$node$$Node$$stub *n, struct graph$edge$$Edge$$stub *e) {
    if (((struct graph$node$$Node*)n)->num_edges >= graph$node$$max_edges_per_node) exit(2);
    ((struct graph$node$$Node*)n)->edges[((struct graph$node$$Node*)n)->num_edges++] = e;
    return 1;
}

int graph$node$$random_search(struct graph$node$$Node$$stub *start, struct graph$node$$Node$$stub *end, int steps_left) {
    while (steps_left > 0) {
        int result = graph$node$$random_search$$mangle(start, end, &steps_left);
        if (result != 0) return result;
    }
    return 0;
}

int graph$node$$random_search$$mangle(struct graph$node$$Node$$stub *start, struct graph$node$$Node$$stub *end, int *steps_left) {
    if (start == end) return 1;
    (*steps_left)--;
    if (rand() % graph$node$$continue_rate == 0) return 0;
    struct graph$edge_picker$$Controller$$stub c = graph$edge_picker$$get_controller();
    struct graph$node$$Node$$stub *n = graph$edge_picker$$pick_next(&c, start);
    if (n == NULL) return 0;
    return graph$node$$random_search$$mangle(n, end, steps_left);
}
