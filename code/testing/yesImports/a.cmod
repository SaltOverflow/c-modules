module;

import b;

struct struct_2 {
    // Uses a because own module shadows imported b
    global_1;
};
export int global_1;

int function_1() {
    // This is not overloaded with b because they are never
    // exported into the same space
}

export struct struct_5 {
    // Uses b
    type struct_6;
    // Uses b
    global_2;
};
export struct struct_7 {
    // Uses b
    type *struct_8;
};
