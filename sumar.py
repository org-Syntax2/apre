import sys
import os

archivo_resultado = "resultado.txt"

# 1. Obtener los números ingresados por parámetro (ej: python sumar.py 50 60)
if len(sys.argv) > 1:
    numeros = [int(arg) for arg in sys.argv[1:] if arg.lstrip('-').isdigit()]
else:
    # Si no se pasan parámetros por defecto
    numeros = [0]

# 2. Calcular la suma exacta de los números actuales (sin acumular)
suma_total = sum(numeros)

# 3. Guardar el resultado exacto en el archivo
with open(archivo_resultado, "w", encoding='utf-8') as f:
    f.write(str(suma_total))

print("====================================")
print(f"Números a sumar     : {numeros}")
print(f"Suma total          : {suma_total}")
print("====================================")