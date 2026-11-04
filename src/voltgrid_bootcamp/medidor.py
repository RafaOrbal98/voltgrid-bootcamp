"""Procesamiento básico de lecturas de medidor (intervalos de 15 min)."""

LECTURAS_KWH: list[float] = [
    120.5,
    118.0,
    121.3,
    119.8,  # 00:00 - 01:00
    125.0,
    -3.0,
    126.4,
    124.9,  # 01:00 - 02:00  <- ojo: una lectura negativa
]


def total_kwh(lecturas: list[float]) -> float:
    """Suma solo las lecturas válidas (>= 0)."""
    total = 0.0
    for lectura in lecturas:
        if lectura >= 0:
            total += lectura
    return total


def kwh_a_mwh(kwh: float) -> float:
    """Convierte kWh a MWh."""
    return kwh / 1000


def lecturas_invalidas(lecturas: list[float]) -> list[int]:
    """Regresa las posiciones (índices) de las lecturas negativas."""
    return [i for i, lectura in enumerate(lecturas) if lectura < 0]


def totales_por_hora(lecturas: list[float]) -> list[float]:
    """Agrupa lecturas de 15 min en bloques de 4 y regresa el total de cada hora."""
    # 1. Preparo una lista vacía para los resultados
    totales: list[float] = []

    # 2. Recorro las lecturas de 4 en 4
    for i in range(0, len(lecturas), 4):
        # 3. Tomo el grupo de 4 lecturas
        grupo = lecturas[i + 0 : i + 4]
        # 4. Lo sumo y lo guardo en la lista
        totales.append(sum(grupo))

    # 5. Regreso la lista con las sumas
    return totales
