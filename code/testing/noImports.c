module;

export void fn_1() {}
int fn_2(int a) {}
struct struct_1 fn_3(struct struct_2 a, struct struct_3 *b) {
    global_1;
    type struct_4;
    type *struct_5;
}

struct struct_1 {};
export struct struct_2 {};
struct struct_3 {
    global_2;
    type *struct_6;
};
struct struct_4 {
    type struct_5;
};
export struct struct_5 {
    type *struct_6;
};
struct struct_6 {
    type struct_5;
};

int global_1;
export int global_2 = global_3 + global_4 + global_1;
int global_3 = global_5;
struct struct_4 global_4;
export struct struct_5 *global_5 = global_1;
