input = """Dreamquest Slippers
Cloudwhisper Boots
Brimstone Treads
Nightwind Slippers
Windbreak Boots
Darksteel Treads
Duskwalk Slippers
Stormrider Boots
Basemetal Treads
Debilitation Gauntlets
Gruelling Gauntlets
Taxing Gauntlets
Sinistral Gloves
Southswing Gloves
Gauche Gloves
Nexus Gloves
Aetherwind Gloves
Leyline Gloves
Blizzard Crown
Winter Crown
Gale Crown
Archdemon Crown
Demon Crown
Imp Crown
Atonement Mask
Penitent Mask
Sorrow Mask"""

all_baseTypes = ""

for baseType in input.split("\n"):
    all_baseTypes += "\"" + baseType + "\" "

print(all_baseTypes)
