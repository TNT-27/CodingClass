def strip(txt: str) -> str:
    return txt.removeprefix("\n").removesuffix("\n")

chicken = strip("""
[']>
L L
""")

block = strip("""
 ___
|___|
""")

ASSET_MAPPING = {
    'p' : chicken,
    'b' : block,
    'a' : "\n"
}
