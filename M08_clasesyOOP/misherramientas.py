import math

class HERRAMIENTAS:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def primo(self, numero):
        if numero < 2:
            return False
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

    def numeros_primos(self):
        Lprimos = []
        for i in self.lista:
            if self.primo(i) == True:
                Lprimos.append(i)
        return Lprimos
    
    def numero_repetido(self, numerosR):
        max_repetidos = 0
        repite = 0
        for i in numerosR:
            contador = numerosR.count(i)
            if contador > max_repetidos:
                max_repetidos = contador
                repite = i
        return  [repite, max_repetidos]
    
    def mas_repetido(self):
        # Crea un diccionario para contar la frecuencia de cada número
        frecuencias = {}
        for num in self.lista:
            if num in frecuencias:
                frecuencias[num] += 1
            else:
                frecuencias[num] = 1

        # Busca el número con la frecuencia más alta
        max_frecuencia = max(frecuencias.values())
        mas_repetido = [num for num, freq in frecuencias.items() if freq == max_frecuencia][0]

        return mas_repetido, max_frecuencia
    
    def convertir_temperatura(self, valor, origen, destino):
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
        factorial = 0
        if type(numero) != int:
            return 'Debe imgresar un numero entero'
        if numero < 0:
            return 'el numero debe ser positivo'
        if numero <= 1:
            return 1
    
        factorial = math.factorial(numero)
        return factorial