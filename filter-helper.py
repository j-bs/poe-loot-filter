input = """Desperate Crusade
A Stone Perfected
Treasures of the Vaal
The Rabbit's Foot
Chasing Risk
The Prince of Darkness
The Catch
Eternal Bonds
Disdain
The Scout
Guardian's Challenge
The Forgotten Treasure
The Fox in the Brambles
The Aspirant"""

all_baseTypes = ""

for baseType in input.split("\n"):
    all_baseTypes += "\"" + baseType + "\" "

print(all_baseTypes)
