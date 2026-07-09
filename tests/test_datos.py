import pandas as pd
import pytest

pytestmark = pytest.mark.datos
UMBRAL = 0.30   # criterio de aceptación: máx. 30% de filas inválidas


def test_montos_invalidos_bajo_umbral():
    df = pd.read_csv('data/ventas.csv')
    invalidos = df['Monto'].isna() | (df['Monto'] <= 0)
    tasa = invalidos.mean()
    assert tasa <= UMBRAL, (
        f'Montos inválidos: {tasa:.0%} (umbral {UMBRAL:.0%}). '
        f'Filas: {df[invalidos].index.tolist()}')
