input = """Winter's Embrace
Sambodhi's Wisdom
The Enthusiasts
Broken Promises
Brush, Paint and Palette
Deadly Joy
The Adventuring Spirit
The Eternal War
Prejudice
The Shortcut
The Card Sharp
A Modest Request
Luminous Trove
The Hook"""

all_baseTypes = ""

for baseType in input.split("\n"):
    all_baseTypes += "\"" + baseType + "\" "

print(all_baseTypes)
