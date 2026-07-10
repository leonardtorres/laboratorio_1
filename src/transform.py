import pandas as pd


def limpiar_ventas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    df = df.dropna(subset=['producto', 'monto']).drop_duplicates()
    df['monto'] = df['monto'].astype(float)
    
    return df[df['monto'] > 0]


def total_por_producto(df: pd.DataFrame) -> pd.DataFrame:
    
    return (df.groupby('producto', as_index=False)['monto']
              .sum().rename(columns={'monto': 'total'}))
