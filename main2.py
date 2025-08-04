# PrettyTable displays table in an ascii format
from prettytable import PrettyTable
table = PrettyTable()
# print(table)
# add_column is a method of the PrettTable() class
print("Pokemons")
table.add_column("Lvl1", ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Weedle", "Pidgey", "Rattata", "Spearow", "Pikachu", "Magikarp"])
table.add_column("Lvl2", ["Ivysaur", "Charmeleon", "Wartortle", "Metapod", "Kakuna", "Pidgeotto", "Raticate", "Fearow", "Raichu", "Gyarados"])
# table.add_column('Strongest Pokemon', ["Ronit"])
table.align = "l"
print(table)


