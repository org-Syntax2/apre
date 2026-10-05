import os

archivo_resultado = "resultado.txt"

# Leer resultado anterior si existe, si no iniciar en 0
if os.path.exists(archivo_resultado):
    with open(archivo_resultado, "r") as f:
        contenido = f.read().strip()
        valor_actual = int(contenido) if contenido.isdigit() else 0
else:
    valor_actual = 0

nuevo_resultado = valor_actual + 10

# Guardar el nuevo valor
with open(archivo_resultado, "w") as f:
    f.write(str(nuevo_resultado))

print(f"Suma completada: {valor_actual} + 10 = {nuevo_resultado}")