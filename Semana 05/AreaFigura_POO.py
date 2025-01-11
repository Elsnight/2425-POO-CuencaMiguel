"""
Programa para calcular el área y el perímetro de un rectángulo.

Descripción:
Este programa permite al usuario ingresar las dimensiones de un rectángulo (base y altura)
y calcula su área y perímetro. El programa utiliza diferentes tipos de datos y sigue
convenciones de nomenclatura en Python.

Autor: [Tu Nombre]
Fecha: [Fecha de desarrollo]
"""

def calcular_area(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo dado su base y altura.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    return base * altura


def calcular_perimetro(base: float, altura: float) -> float:
    """
    Calcula el perímetro de un rectángulo dado su base y altura.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El perímetro del rectángulo.
    """
    return 2 * (base + altura)


# Programa principal
if __name__ == "__main__":
    print("Cálculo de área y perímetro de un rectángulo")

    # Entrada de datos
    try:
        base = float(input("Ingrese la base del rectángulo (en unidades): "))
        altura = float(input("Ingrese la altura del rectángulo (en unidades): "))

        # Cálculos
        area = calcular_area(base, altura)
        perimetro = calcular_perimetro(base, altura)

        # Salida de datos
        print(f"\nResultados:")
        print(f"Área: {area:.2f} unidades cuadradas")
        print(f"Perímetro: {perimetro:.2f} unidades")
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")
