from got import *

def test_lee_batalas(batallas):
    print(f"La ultima batalla fue {batallas[-1]}")

def test_reyes_mayor_menor_ejercito(batallas):
    res = reyes_mayor_menor_ejercito(batallas)
    print(f"El rey con mayor y menor ejercito son: {res}")

def main():
    batallas = lee_batallas("data/battles.csv")
    test_lee_batalas(batallas)
    print("\n")
    test_reyes_mayor_menor_ejercito(batallas)
    print(batallas_mas_comandante(batallas, {"The North", "The Riverlands"}, 4))
    print(rey_mas_victorias(batallas, "ambos"))


if __name__=="__main__":
    main() 