module;

import a;
import "../yesImports";

export struct struct_2 {
    // Uses b because own module shadows imported a
    global_1;
};
int global_1;

int function_1(struct struct_3 foo /* Uses b */) {
    // Uses b because own module shadows imported a
    global_1;
}

export struct struct_3 {
    // Uses yesImports
    type struct_4;
};
export int global_2;
export struct struct_6 {
    // Uses a
    type struct_7;
};
export struct struct_8 {
    // uses b
    function_1;
};
