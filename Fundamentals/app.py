import json,_hashlib,hashlib

try:
    with open('bloques.json', 'r') as f:
        bloques = json.load(f)
except FileNotFoundError:
    bloques = {}

def actualizar():
    # for i in bloques:
    if bloques.has_key(1):
        print(bloques[1])

actualizar()




























# import random
# materias = input('ingrese cuantas materias vamos a programar \n')
# materia = []
# materia = materias.split(',')

# profes = [['vacio'],'tatiana','uldarico']

# profesTematicas = [['vacio'],['java','kotlin','proyecto'],['python','proyecto']]

# res=True

# horario = []
# for i in range(len(profes)):
#     print(f"el profesor {profes[i]} puede dictar {profesTematicas[i]}")
#     position = random.randint(1,3)
#     while res==True:
#         if len(profesTematicas) > 0:
#             print(f"{profes[position]} and {profesTematicas[position]}")
#         else : 
#             position = random.randint(1,3)
#             print(f"{profes[position]} and {profesTematicas[position]}")
            


# sede = []
# salon = []

# materia.pop(0)
# print(materia)
