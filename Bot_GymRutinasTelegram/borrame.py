print("file one __name__ is set to: {}" .format(__name__))#ejemplo de como importar archivos
from dos import saluda
def main():
    saluda()

if __name__ == "__main__":
    main()