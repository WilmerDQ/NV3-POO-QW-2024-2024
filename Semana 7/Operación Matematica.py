def es_balanceada(expresion):
    pila = []

    for c in expresion:
        if c in "({[":
            pila.append(c)
        elif c in ")}]":
            if not pila:
                return False
            top = pila.pop()
            if not coinciden(top, c):
                return False

    return len(pila) == 0


def coinciden(apertura, cierre):
    return (apertura == '(' and cierre == ')') or \
           (apertura == '{' and cierre == '}') or \
           (apertura == '[' and cierre == ']')


if __name__ == "__main__":
    expresion = input("Ingrese la expresión a verificar: ")
    if es_balanceada(expresion):
        print("La expresión está balanceada.")
    else:
        print("La expresión NO está balanceada.")
