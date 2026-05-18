def sumaMayoresIguales(valor, lista):
    ultima_posicion = len(lista) - 1
    return calcular_suma_recursiva(valor, lista, ultima_posicion)

def calcular_suma_recursiva(valor, lista, pos):
    if len(lista) == 0:
        return 0
      
    if pos == 0:
        if lista[pos] >= valor:
            return lista[pos]
        else:
            return 0
        
    else:
        if lista[pos] >= valor:
            actual = lista[pos]
        else:
            actual = 0

        return actual + calcular_suma_recursiva(valor, lista, pos - 1)
    
mi_lista = [3, 8, 5, 9, 7]
valor_limite = 6

resultado = sumaMayoresIguales(valor_limite, mi_lista)
print(f"La suma es: {resultado}")
