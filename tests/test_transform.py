import pandas as pd, pytest
from src.transform import limpiar_ventas, total_por_producto
 
def test_quita_nulos_y_negativos():
    df = pd.DataFrame({'Producto': ['A', None, 'B'],
                       'Monto':   [10.0, 5.0, -3.0]})
    out = limpiar_ventas(df)
    assert len(out) == 1 and out['monto'].gt(0).all()
 
def test_agrega_por_producto():
    df = pd.DataFrame({'producto': ['A', 'A'], 'monto': [10.0, 5.0]})
    assert total_por_producto(df).loc[0, 'total'] == pytest.approx(15.0)
 
def test_falla_sin_columna_monto():
    with pytest.raises(KeyError):
        limpiar_ventas(pd.DataFrame({'Producto': ['A']}))
