// Graph searching algorithm testing script

import graph;

import stdio;
import stdlib;
import unistd;

void print_usage() {
    printf("Usage: program_name [-n num_iter] [-s seed] [-N num_nodes] [-E num_edges] [-c num_checks] [-h]\n");
    printf("Options:\n");
    printf("  -n num_iter   Number of graphs to run on\n");
    printf("  -s seed       Seed for random number generator\n");
    printf("  -N num_nodes  Number of nodes in generated graph\n");
    printf("  -E num_edges  Number of edges in generated graph\n");
    printf("  -c num_checks Number of times to check graph for paths\n");
    printf("  -h            Display this help message\n");
}

struct Arg {
    int num_iter, seed, num_nodes, num_edges, num_checks;
};

struct Arg process_args(int argc, char *argv[]) {
    int opt;
    struct Arg args;
    args.num_iter = 10;
    args.seed = 0;
    args.num_nodes = 100;
    args.num_edges = 100;
    args.num_checks = 10;

    // Parse command line options
    while ((opt = getopt(argc, argv, "n:s:N:E:c:h")) != -1) {
        switch (opt) {
            case 'n':
                args.num_iter = atoi(optarg);
                break;
            case 's':
                args.seed = atoi(optarg);
                break;
            case 'N':
                args.num_nodes = atoi(optarg);
                break;
            case 'E':
                args.num_edges = atoi(optarg);
                break;
            case 'c':
                args.num_checks = atoi(optarg);
                break;
            case 'h':
                print_usage(); // Print usage information
                exit(0);
            case '?':
                // Handle unknown options
                fprintf(stderr, "Unknown option: -%c\n", optopt);
                print_usage();
                exit(1);
            default:
                print_usage();
                exit(1);
        }
    }
    return args;
}

int main(int argc, char *argv[]) {
    struct Arg args = process_args(argc, argv);
    int total_paths = 0;
    srand(args.seed);
    for (int i=0; i<args.num_iter; ++i) {
        struct Graph g = create_rand_graph(args.num_nodes, args.num_edges);
        int paths_found = 0;
        for (int j=0; j<args.num_checks; ++j) {
            struct Node *n1 = grab_random_node(&g);
            struct Node *n2 = grab_random_node(&g);
            paths_found += path_found(n1, n2);  // it's technically returning a bool
        }
        destroy_graph(&g);
        total_paths += paths_found;
        printf("Graph %d: %d paths found over %d checks.\n", i, paths_found, args.num_checks);
    }
    printf("Summary: %d graphs * %d checks = %d total checks performed, %d paths found.\n", args.num_iter, args.num_checks, args.num_iter * args.num_checks, total_paths);
}
