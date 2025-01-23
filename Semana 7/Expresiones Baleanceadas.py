def es_balanceada(expresion):
    pila = []

    for c in expresion:
        if c in "({[":
            pila.append(c)
        elif c in ")}]":
            if not pila:
                return False

            tope = pila.pop()
            if (c == ')' and tope != '(') or \
               (c == ']' and tope != '[') or \
               (c == '}' and tope != '{'):
                return False

    return len(pila) == 0


if __name__ == "__main__":
    expresion = "{7+(8*5)-[(9-7)+(4+1)]}"
    if es_balanceada(expresion):
        print("Fórmula balanceada")
    else:
        print("Fórmula no balanceada")
1