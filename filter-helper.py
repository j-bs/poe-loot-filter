input = """Assembler Wand
Congregator Wand
Accumulator Wand
Hollowpoint Dagger
Pressurised Dagger
Pneumatic Dagger
Flickerflame Blade
Flashfire Blade
Infernal Blade
Shadow Fangs
Malign Fangs
Void Fangs
Maltreatment Axe
Disapprobation Axe
Psychotic Axe
Fickle Spiritblade
Capricious Spiritblade
Anarchic Spiritblade
Flare Hammer
Crack Hammer
Boom Hammer
Oscillating Sceptre
Stabilising Sceptre
Alternating Sceptre
Hedron Bow
Foundry Bow
Solarine Bow
Transformer Staff
Accumulator Staff
Battery Staff
Capacity Rod
Potentiality Rod
Eventuality Rod
Prime Cleaver
Honed Cleaver
Apex Cleaver
Rebuking Blade
Blasting Blade
Banishing Blade
Blunt Force Condenser
Crushing Force Magnifier
Impact Force Propagator
Micro-Distillery Belt
Mechalarm Belt
Astrolabe Amulet
Simplex Amulet
Cogwork Ring
Geodisic Ring
Exhausting Spirit Shield
Subsuming Spirit Shield
Transfer-attuned Spirit Shield
Endothermic Buckler
Polar Buckler
Cold-attuned Buckler
Exothermic Tower Shield
Magmatic Tower Shield
Heat-attuned Tower Shield
"""

all_baseTypes = ""

for baseType in input.split("\n"):
    all_baseTypes += "\"" + baseType + "\" "

print(all_baseTypes)
