# calculo.py
x = 10
y = 0
resultado = 0
def SumaNumeros(a, b):
return a+b
def promedio(lista):
suma = 0
for i in range(0, len(lista)):
suma = suma + lista[i]
prom = suma / len(lista) # posible división entre cero
return prom
def imprimirResultados():
datos = [15, 10, 8, 20, 5, 30]
print("Promedio es: ", promedio(datos))
print("Suma total: ", SumaNumeros(5, 10))
z = 100 # variable no usada
def Calcular():
print("Iniciando cálculo...")
imprimirResultados()
print("Fin del cálculo")
if __name__ == "__main__":
Calcular()
