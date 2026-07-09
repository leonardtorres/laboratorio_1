import argparse, json
import pandas as pd
from src.transform import limpiar_ventas, total_por_producto
 
parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()
 
df = pd.read_csv(args.input)
limpio = limpiar_ventas(df)
total_por_producto(limpio).to_csv(args.output, index=False)
 
resumen = {   # <- S6: el pipeline produce su propio reporte
    'filas_entrada': int(len(df)),
    'filas_validas': int(len(limpio)),
    'filas_descartadas': int(len(df) - len(limpio)),
}
with open('output/resumen.json', 'w') as f:
    json.dump(resumen, f, indent=2)
print('PIPELINE OK'); print(json.dumps(resumen, indent=2))