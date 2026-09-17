num_modules = 10
num_functions = 100

for i in range(num_modules):
    lines = [f"module stress{i};", ""]
    if i != num_modules-1:
        lines.append(f"import stress{i+1};")
        lines.append("")
    for j in range(num_functions):
        fn_num = i*num_functions + j
        if i != num_modules-1:
            fn_call = fn_num + num_functions
            lines.append(f"export void fn{fn_num}() {{ fn{fn_call}(); }}")
        else:
            lines.append(f"export void fn{fn_num}() {{}}")
    with open(f"stress{i}.cmod", 'w') as f:
        f.write('\n'.join(lines) + '\n')
