module;

import edge;
import node;

import stdlib;

struct Controller {};

export struct Controller get_controller() {
    return (struct Controller){};
}

export struct Node *pick_next(struct Controller *c, struct Node *n) {
    if (n->num_edges == 0) return NULL;
    struct Edge *e = n->edges[rand() % n->num_edges];
    return e->nodes[0] == n ? e->nodes[1] : e->nodes[0];
}
