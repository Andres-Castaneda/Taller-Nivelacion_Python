def calcular_dano(ataque, defensa):
    dano = ataque - defensa
    return dano if dano > 0 else 1

def aplicar_curacion(vida, cur, max_vida):
    nueva = vida + cur
    return min(nueva, max_vida)

def subir_nivel(xp_actual, xp_necesario, nivel_actual):
    if xp_actual >= xp_necesario:
        nivel_actual += 1
        print(f"¡Nivel {nivel_actual} alcanzado!")
        return nivel_actual
    return nivel_actual

print(f"Dano: {calcular_dano(20, 8)}")
mostrar_vida = aplicar_curacion(40, 80, 100)
print(f"Vida tras cura: {mostrar_vida}")