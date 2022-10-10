# Collections: (Tableaux: Array), Listes, Tuples...
# Tuple (): immutable
# Liste []: mutable -> modifiable: rajouter/supprimer des éléments où les modifier
# Plusieurs éléments

# _________TUPLES---------------_____-
# personnes = ("Mélanie", "Jean", "Martin", "Alice")
# print(len(personnes))
# print(personnes[-1]) -1 pour le dernier élément

# for i in range(0, len(personnes)):
#     print(personnes[i])

# for i in personnes:
#     print(i)
#     print(len(i))
#     print((i[-1]))

# (0, 1, 2, 3, 4)
# valeurs = range(0, 5)
# print(valeurs[-1])

# __________ LISTES ----------

# personnes = ["Mélanie", "Yahya", "Martin", "Alice"]
# new_personne = "Daouda"

# # print(personnes)
# personnes.append(new_personne)
# del personnes[1]
# # print(personnes)


# def display_personnes(c):
#     for i in c:
#         print(i)


# def modifier_valeur(a):
#     a[0] = 10


# test = [1, 2, 3, 4]
# print(test)
# modifier_valeur(test)
# print(test)


# display_personnes(personnes)


# ---------Fonctions et TUPLES------------

"""
def obtenir_information():
    return "Mélanie", 37, 1.6


def affichez_informations(nom, age, taille):
    print(f"Information: Nom: {nom}, age: {age}, taille: {taille}")


infos = obtenir_information()
affichez_informations(*infos)

print(infos)
print(*infos) #unpack tuple
# print(f"nom: {infos[0]}")
# print(f"age: {infos[1]}")
# print(f"taille: {infos[2]}")


# nom, age, taille = obtenir_information()
# affichez_informations(nom, age, taille)
"""

# ------------- SLICES --------------

#personnes = ("Mélanie", "Yahya", "Martin", "Alice", "Pierre", "Paul")

# [strart:stop:step]


# for i in personnes[::-2]:
#     print(i)


# nom = "Yahya"
# print(nom[::-1])
