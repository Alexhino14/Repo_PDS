def main():
    tarea = input("seleccion de tarea (tarea_numero):  ")

    if tarea == "tarea_1":
        from src.tarea1 import generar_senales
        generar_senales()
    else:
        print("no hay")

if __name__ == "__main__":
    main()
