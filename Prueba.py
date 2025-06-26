stock_total = 150


def main_menu ():
    print("Bienvenido a CafeConleche")
    print("1- Comprar entradas a Cats.")
    print("2- Cambio de función.")
    print("3- Mostrar stock de funciones.")
    print("4- Salir.")

    def entradas_Cats_dia_viernes():
        if len(entradas_Cats_dia_viernes) >= stock_total:
        print("no hay mas entradas disponibles para Cats dia viernes")
        return
    nombre = input("ingrese nombre del comprador: ").strip()
    if nombre in entradas_Cats_dia_viernes:
        print("este comprador ya tiene una entrada.")
        return
  

    funcion = input("Función (1 ó 2): ")

    if funcion == "1":

      if stock_funcion_1 > 0:

        compradores[nombre] = 1

        stock_funcion_1 -= 1

        print("Entrada registrada en función 1! Stock restantes:")

        print(" Función 1 (Viernes):", stock_funcion_1)

        print(" Función 2 (Sábado):", stock_funcion_2)

      else:

        print("No hay entradas disponibles para función 1.")

      break

    elif funcion == "2":

      if stock_funcion_2 > 0:

        compradores[nombre] = 2

        stock_funcion_2 -= 1

        print("Entrada registrada en función 2! Stock restantes:")

        print(" Función 1 (Viernes):", stock_funcion_1)

        print(" Función 2 (Sábado):", stock_funcion_2)

      else:

        print("No hay entradas disponibles para función 2.")

      break

    else:

      print("Error: opción de función inválida.")





def cambiar_funcion():

  global stock_funcion_1, stock_funcion_2



  print("-- Cambio de función --")

  nombre = input("Nombre del comprador: ").strip()

  if nombre not in compradores:

    print("Error: comprador no encontrado.")

    return



  actual = compradores[nombre]

  nueva = 2 if actual == 1 else 1



  print(f"Cambiar de función {actual} a {nueva}? (S/N): ", end="")

  respuesta = input().strip().lower()

  if respuesta != "s":

    print("Cambio cancelado.")

    return



  if nueva == 1 and stock_funcion_1 > 0:

    compradores[nombre] = 1

    stock_funcion_1 -= 1

    stock_funcion_2 += 1

    print("Cambio exitoso. Ahora está en función 1.")

  elif nueva == 2 and stock_funcion_2 > 0:

    compradores[nombre] = 2

    stock_funcion_2 -= 1

    stock_funcion_1 += 1

    print("Cambio exitoso. Ahora está en función 2.")

  else:

    print("No hay stock disponible para la función deseada.")





def mostrar_stock():

  vendidos1 = 150 - stock_funcion_1

  vendidos2 = 180 - stock_funcion_2

  print("-- Stock de Funciones --")

  print(f"Función 1 (Viernes): Disponibles {stock_funcion_1}, Vendidas {vendidos1}")

  print(f"Función 2 (Sábado): Disponibles {stock_funcion_2}, Vendidas {vendidos2}")





def main():

  while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ").strip()



    if opcion == "1":

      comprar_entrada()

    elif opcion == "2":

      cambiar_funcion()

    elif opcion == "3":

      mostrar_stock()

    elif opcion == "4":

      print("Programa terminado...")

      break

    else:

      print("Debe ingresar una opción válida!!")



main()
    
    
    

