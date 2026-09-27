# Entrada de datos con conversión de tipo (casting)
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en kg : "))
estatura = float(input("Ingresa tu estatura en metros : "))

# Cálculo del Índice de Masa Corporal (IMC)
imc = peso / (estatura ** 2)

# Mostrar el resultado
print(f"\nEdad: {edad} años")
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")