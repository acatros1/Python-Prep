import math

class Misherramientas:
    def __init__(self, lista_numeros):
        if not isinstance(lista_numeros, list):
            self.lista = [lista_numeros]
        else:
            self.lista = lista_numeros

    def primo(self, numero):
        if numero < 2:
            return False
        for i in range(2, int(math.sqrt(numero)) + 1):
            if numero % i == 0:
                return False
        return True

    def numeros_primos(self):
        return [self.primo(i) for i in self.lista] 

    def numero_repetido(self):
        frecuencias = {}
        for num in self.lista:
            frecuencias[num] = frecuencias.get(num, 0) + 1
        max_frecuencia = max(frecuencias.values())
        return [num for num, freq in frecuencias.items() if freq == max_frecuencia][0], max_frecuencia

    def mas_repetido(self):
        frecuencias = {}
        for num in self.lista:
            frecuencias[num] = frecuencias.get(num, 0) + 1
        return max(frecuencias, key=lambda x: frecuencias[x]), max(frecuencias.values())

    def convertir_temperatura(self, valor, origen, destino):
        if not isinstance(valor, (int, float)):
            raise ValueError("El valor debe ser un número")
        if origen not in ["C", "F", "K"]:
            raise ValueError("Origen no válido. Debe ser 'C', 'F' o 'K'")
        if destino not in ["C", "F", "K"]:
            raise ValueError("Destino no válido. Debe ser 'C', 'F' o 'K'")
        if origen == destino:
            raise ValueError("Origen y destino no pueden ser iguales")

        if origen == "C" and destino == "F":
            return (valor * 9/5) + 32
        elif origen == "C" and destino == "K":
            return valor + 273.15
        elif origen == "F" and destino == "C":
            return (valor - 32) * 5/9
        elif origen == "F" and destino == "K":
            return (valor - 32) * 5/9 + 273.15
        elif origen == "K" and destino == "C":
            return valor - 273.15
        elif origen == "K" and destino == "F":
            return (valor - 273.15) * 9/5 + 32
        else:
            raise ValueError("Origen o destino no válido")

    def c_factorial(self, numero):
        if not isinstance(numero, int):
            return 'Debe ingresar un número entero'
        if numero < 0:
            return 'El número debe ser positivo'
        return math.factorial(numero)