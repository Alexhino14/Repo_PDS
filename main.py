import sys
from src.tarea1 import generar_senales
from src.tarea2 import frec_senal
from src.tarea3 import senal_parametros
from src.tarea4 import convertidor_da

def main(options):
    if options[1] == "act_1":
        generar_senales()
    elif options[1] == "act_2":
        if len(options) > 2:
            frec_senal(options[2])
        else:
            print("Escribe una frecuencia al final: python main.py act_2 2")
    elif options[1] == "act_3":
        if len(options) > 4:
            senal_parametros(options[2], options[3], options[4])
        else:
            print("Escribe una amplitud, frecuencia y fase al final: python main.py act_3 1 2 0.785")
    elif options[1] == "act_4":
        if len(options) > 2:
            convertidor_da(options[2])
        else:
            print("Escribe un numero de bits al final: python main.py tarea4 8")

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example ( run activity 1 ): python main.py act_1")
        print("Example ( run activity 2 ): python main.py act_2 2")
        print("Example ( run activity 3 ): python main.py act_3 1 2 0.785")
        print("Example ( run activity 4 ): python main.py act_4 8")


