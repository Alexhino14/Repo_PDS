import sys
from src import examen_p1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py examen_p1")
    else:
        practica = sys.argv[1]
        if practica == "examen_p1":
            examen_p1.run()
        else:
            print("Práctica no encontrada")
