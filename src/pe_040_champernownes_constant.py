def champernowne_constant_product():
    champernowne = "0" + "".join(str(n) for n in range(1, 500000))[:1000001]
    return (
        int(champernowne[1])
        * int(champernowne[10])
        * int(champernowne[100])
        * int(champernowne[1000])
        * int(champernowne[10000])
        * int(champernowne[100000])
        * int(champernowne[1000000])
    )
