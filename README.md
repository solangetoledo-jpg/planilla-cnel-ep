# CNEL EP - Planilla de Consumo Eléctrico

Proyecto académico desarrollado en Python para simular la generación de una planilla de consumo eléctrico de CNEL EP.

## Funcionamiento

El programa solicita:

1. Nombre del cliente.
2. Número de suministro.
3. Cantidad de energía consumida en kWh.

Para el ejercicio se utilizan:

- Precio fijo: **USD 0.10 por kWh**
- IVA simulado: **15 %**

Luego calcula:

- Subtotal = consumo × precio por kWh
- IVA = subtotal × 15 %
- Total = subtotal + IVA

## Ejecución

Desde la terminal:

```bash
python planilla_cnel.py
```

## Ejemplo

Si el cliente consume 150 kWh:

- Subtotal: USD 15.00
- IVA: USD 2.25
- Total: USD 17.25
