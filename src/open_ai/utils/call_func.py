funcs_ok = {"sum", "python"}


def call_func(c):
    "Call the function in `c` with the arguments in `c`"
    fc = c.choices[0].message.function_call
    print(fc, "FUNCTION TO CALL")
    if fc.name not in funcs_ok:
        return print(f"Not allowed: {fc.name}")
    f = globals()[fc.name]
    return f(**json.loads(fc.arguments))
