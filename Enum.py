#from enum import Enum
characters = ["Kaleb", "Getu", "Veronica", "Goytom", "Paulos"]
print("\n------------------------------------\n")

print(list(enumerate(characters)))
print("\n------------------------------------\n")

for index, character in enumerate(characters):
    print(index, character)

print("\n------------------------------------\n")

characters = ["Kaleb", "Getu", "Getu", "Goytom", "Paulos",
              "Kaleb", "Getu", "Veronica", "Goytom","Paulos",
              "Paulos", "Getu", "Veronica", "Getu", "Paulos"]

character_map = {character:[] for character in set(characters)}

print(character_map)
print("\n------------------------------------\n")
print(list(enumerate(characters)))
print("\n------------------------------------\n")


for index, character in enumerate(characters):
    character_map[character].append(index)

print(character_map)
print("\n------------------------------------\n")

