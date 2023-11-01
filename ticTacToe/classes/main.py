# import Tree
import node as node


def main():
    car = {"brand": "Ford", "color": "Mustang", "year": 1964, "mileage": 10000}
    prop = input("Ingrese propiedad: ")
    print(car[prop])

# def crear_arbol(estado, jugador):
#     nodo_raiz = node(estado, jugador)

#     for i in range(3):
#         for j in range(3):
#             if estado[i][j] == " ":
#                 nuevo_estado = estado.copy()
#                 nuevo_estado[i][j] = jugador
#                 nodo_raiz.agregar_hijo(
#                     nuevo_estado, jugador_contrario(jugador))

#     return nodo_raiz

if __name__ == "__main__":
    main()
