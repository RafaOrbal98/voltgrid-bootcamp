from voltgrid_bootcamp.medidor import (
    LECTURAS_KWH,
    kwh_a_mwh,
    lecturas_invalidas,
    total_kwh,
    totales_por_hora,
)


def main() -> None:
    total = total_kwh(LECTURAS_KWH)
    malas = lecturas_invalidas(LECTURAS_KWH)
    por_hora = totales_por_hora(LECTURAS_KWH)

    print(f"Lecturas recibidas: {len(LECTURAS_KWH)}")
    print(f"Total válido: {total:,.2f} kWh ({kwh_a_mwh(total):.4f} MWh)")
    print(f"Lecturas inválidas en posiciones: {malas}")
    print(f"Totales por hora: {por_hora}")
