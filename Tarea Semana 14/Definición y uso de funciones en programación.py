def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicado a una compra.

    :param monto_total: Total de la compra en moneda local.
    :param porcentaje_descuento: Porcentaje de descuento a aplicar (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Llamadas a la función
monto1 = 200  # Monto total de la primera compra
monto2 = 500  # Monto total de la segunda compra
porcentaje_personalizado = 15  # Descuento personalizado

descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, porcentaje_personalizado)

# Mostrar resultados
print(f"Compra 1: Monto total = ${monto1}, Descuento = ${descuento1}, Monto final = ${monto1 - descuento1}")
print(f"Compra 2: Monto total = ${monto2}, Descuento = ${descuento2}, Monto final = ${monto2 - descuento2}")
