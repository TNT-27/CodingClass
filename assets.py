def strip(txt: str) -> str:
    return txt.removeprefix("\n").removesuffix("\n")

chicken = strip("""
[']>
L L
""")

block = strip("""
 ___
|  |
""")
