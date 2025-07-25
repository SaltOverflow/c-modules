// First, have a graph of file import dependencies
// graph/edge_picker.c : graph/node.c graph/edge.c
// graph/node.c : graph/edge_picker.c graph/edge.c
// graph/edge.c : graph/node.c
// graph.c : graph/node.c graph/edge.c
// main.c : graph.c

// Second, collect all symbols related to types in the modules
// // graph/edge_picker.c
// struct Controller {};
// // graph/node.c
// struct Node {
//     int num_edges;
//     struct Edge *edges[max_edges_per_node];
//     struct Other o;
// };
// const int max_edges_per_node = 100;
// struct Other {};
// // graph/edge.c
// struct Edge {
//     struct Node *nodes[2];
//     struct Other o;
// };
// struct Other {};
// // graph.c
// struct Graph {
//     struct Node *nodes;
//     struct Edge *edges;
//     int num_nodes;
//     int num_edges;
// };
// // main.c
// struct Arg {
//     int num_iter, seed, num_nodes, num_edges, num_checks;
// };

// Third, analyze imports to add namespaces and produce an ordering
// graph/edge_picker.c
struct graph$edge_picker$$Controller {};
// graph/node.c
const int graph$node$$max_edges_per_node = 100;
struct graph$node$$Other {};
struct graph$node$$Node {
    int num_edges;
    struct graph$edge$$Edge *edges[graph$node$$max_edges_per_node];
    struct graph$node$$Other o;
};
// graph/edge.c
struct graph$edge$$Other {};
struct graph$edge$$Edge {
    struct graph$node$$Node *nodes[2];
    struct graph$edge$$Other o;
};
// graph.c
struct graph$$Graph {
    struct graph$node$$Node *nodes;
    struct graph$node$$Edge *edges;
    int num_nodes;
    int num_edges;
};
// main.c
struct Arg {
    int num_iter, seed, num_nodes, num_edges, num_checks;
};

// Fourth, print out size/alignment information
#include <stdio.h>
#define PRINT_TYPE_INFO(T) \
    printf("%-40s size = %4zu   align = %4zu\n", \
        #T, (size_t)sizeof(T), (size_t)_Alignof(T))
int main() {
    PRINT_TYPE_INFO(struct graph$edge_picker$$Controller);
    PRINT_TYPE_INFO(struct graph$node$$Other);
    PRINT_TYPE_INFO(struct graph$node$$Node);
    PRINT_TYPE_INFO(struct graph$edge$$Other);
    PRINT_TYPE_INFO(struct graph$edge$$Edge);
    PRINT_TYPE_INFO(struct graph$$Graph);
    PRINT_TYPE_INFO(struct Arg);
}

// Prints:
// struct graph$edge_picker$$Controller     size =    0   align =    1
// struct graph$node$$Other                 size =    0   align =    1
// struct graph$node$$Node                  size =  808   align =    8
// struct graph$edge$$Other                 size =    0   align =    1
// struct graph$edge$$Edge                  size =   16   align =    8
// struct graph$$Graph                      size =   24   align =    8
// struct Arg                               size =   20   align =    4
