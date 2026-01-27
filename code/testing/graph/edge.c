module;

import node;

export struct Edge {
    // struct Node *nodes[2];
    struct Node *nodes;
    struct Other o;
};

struct Other {};

export struct Edge create_edge(struct Node *first, struct Node *second) {
    struct Edge e = {{first, second}};
    return e;
}
