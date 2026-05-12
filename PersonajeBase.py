# Variables del personaje RPG 
nombre = 'Gandalf' 
nivel = 2
vida = 80 
vida_maxima = 100
esta_vivo = True 
clase = 'Guerrero' 
puntos_ataque = 18
puntos_defensa = 8
Mana = 120
 
# Verificar tipos 
"""
print(type(nombre))   # <class 'str'> 

print(type(nivel))    # <class 'int'> 

print(type(vida))     # <class 'float'> 

print(type(esta_vivo)) # <class 'bool'> 



print(f'{nombre}[{clase}] Nivel: {nivel} | Vida: {vida}| Mana: {Mana}') 

ataque = 15 

dano = float(ataque) * 1.5  # cast 

msg = 'Dano: ' + str(dano)  # explicito 

# Leer del usuario (input) 

nom = input('Nombre: ') 

niv = int(input('Nivel: ')) 

print(f'{nom} Nv.{niv}') 

# f-strings (muy utiles) 

vida = 87.5 

print(f'Vida: {vida:.1f}%') 
"""