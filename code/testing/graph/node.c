module;

import edge;
import edge_picker;

import stdlib;

export struct Node {
    int num_edges;
    // struct Edge *edges[max_edges_per_node];
    struct Edge *edges;
    struct Other o;
};
// const int max_edges_per_node = 100;  // don't want to set up a dynamic array
int max_edges_per_node = 100;  // don't want to set up a dynamic array

struct Other {};

export int add_edge(struct Node *n, struct Edge *e) {
    if (n->num_edges >= max_edges_per_node) exit(2);
    n->edges[n->num_edges++] = e;
    return 1;
}

export int random_search(struct Node *start, struct Node *end, int steps_left) {
    while (steps_left > 0) {
        int result = random_search$$mangle(start, end, &steps_left);
        if (result != 0) return result;
    }
    return 0;
}

// const int continue_rate = 2;
int continue_rate = 2;
int random_search$$mangle(struct Node *start, struct Node *end, int *steps_left) {
    if (start == end) return 1;
    (*steps_left)--;
    if (rand() % continue_rate == 0) return 0;
    struct Controller c = get_controller();
    struct Node *n = pick_next(&c, start);
    return random_search$$mangle(n, end, steps_left);
}
