
inventario = ['Espada de hierro', 'Pocion de vida', 'Escudo de madera', 'Llave dorada']
print('=== INVENTARIO ===')
for i, item in enumerate(inventario, 1):
    print(f'{i}. {item}')

xp = 0
nivel = 1
xp_necesario = 100
batallas = [20, 35, 15, 40, 30]

for xp_ganado in batallas:
    xp += xp_ganado
    if xp >= xp_necesario:
        nivel += 1
        xp -= xp_necesario
        print(f'Subiste al Nivel {nivel}')