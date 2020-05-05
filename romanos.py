romanos = {'M':1000,
           'D':500,
           'C':100,
           'L':50,
           'X':10,
           'V':5,
           'I':1,
            '':0,
}

def romano_a_entero(numero_romano):
    if numero_romano == '':
        return 'Error en formato'
        
    entero = 0
    numRepes = 1
    letraAnt = ''
    for letra in numero_romano:
        if letra == letraAnt and numRepes == 3:
            return 'Error en formato'
        elif letra == letraAnt :
            numRepes += 1
        else:
            numRepes = 1
        
        if letra in romanos and romanos[letra] <= romanos[letraAnt] or letraAnt == 0:
            entero += romanos[letra]
        elif letra in romanos and romanos[letra] >romanos[letraAnt]:
            entero += romanos[letra] -2 * romanos[letraAnt]
        else:
            return 'Error en formato'
        
        letraAnt = letra

    return entero