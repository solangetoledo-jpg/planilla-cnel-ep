def generar_planilla():
    print("=" * 60)
    print("                 CNEL EP - UNIDAD DE NEGOCIO")
    print("                PLANILLA DE ENERGÍA ELÉCTRICA")
    print("=" * 60)

    nombre = input("Nombre del cliente: ").strip().upper()
    suministro = input("Número de suministro: ").strip()

    while True:
        try:
            consumo = float(input("Cantidad de energía consumida (kWh): "))
            if consumo < 0:
                print("El consumo no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Ingrese un valor numérico válido.")

    precio_kwh = 0.10
    iva_porcentaje = 0.15

    subtotal = consumo * precio_kwh
    iva = subtotal * iva_porcentaje
    total = subtotal + iva

    numero_planilla = "000001"

    print()
    print("=" * 60)
    print("                 CNEL EP - UNIDAD DE NEGOCIO")
    print("                PLANILLA DE ENERGÍA ELÉCTRICA")
    print("=" * 60)
    print(f"Planilla N.º: {numero_planilla}")
    print(f"Cliente:       {nombre}")
    print(f"Suministro:    {suministro}")
    print("-" * 60)
    print("N.º  DESCRIPCIÓN            CONSUMO   V. UNITARIO    TOTAL")
    print("-" * 60)
    print(f"1    Energía eléctrica      {consumo:7.2f} kWh   "
          f"USD {precio_kwh:5.2f}    USD {subtotal:6.2f}")
    print("-" * 60)
    print(f"{'SUBTOTAL:':>48} USD {subtotal:6.2f}")
    print(f"{'IVA 15 %:':>48} USD {iva:6.2f}")
    print(f"{'TOTAL:':>48} USD {total:6.2f}")
    print("=" * 60)
    print("              GRACIAS POR REALIZAR SU PAGO")
    print("=" * 60)


if __name__ == "__main__":
    generar_planilla()
