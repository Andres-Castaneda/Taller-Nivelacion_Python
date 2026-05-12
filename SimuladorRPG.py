import PersonajeBase as p

def Combatir (vidaEnemigo, ataqueEnemigo):
    ronda = 1

    while p.vida > 0 and vidaEnemigo > 0:
        vidaEnemigo -= p.puntos_ataque
        if vidaEnemigo > 0:
            p.vida -= ataqueEnemigo
        
        print(f"Ronda {ronda}: Hero={p.vida} | Enemigo={vidaEnemigo}")
        if vidaEnemigo <= 0:
            print(f"Enemigo DERROTADO +20 de vida\n")
            p.vida += 20
        elif p.vida <= 0:
            print(f"El personaje fue DERROTADO\n-------GAME OVER-------")
        ronda+=1
    return vidaEnemigo

def Pelea():
    Derrotados = 0
    Enemigos = [
        ["Goblin", 40, 8],
        ["Orco", 70, 14],
        ["Dragon", 120, 25]
    ]

    for Enemigo in Enemigos:
        vida_e = int(Enemigo[1])
        daño_e = int(Enemigo[2])
        batalla = Combatir(vida_e, daño_e)
        if p.vida <= 0:
            break
        if batalla <= 0:
            Derrotados += 1
        print(f"Enemigos derrotados de momento: {Derrotados}")
    return 0

Pelea()