# Script de Procesamiento de Archivos CSV de Helium

Este script procesa archivos CSV en una carpeta específica para comprobar si se cumplen 
ciertas condiciones. Está diseñado para ser ejecutado desde la línea de comandos, con el 
nombre de la carpeta como argumento.

### Requerimientos
- Python 3.x
- Módulo csv
- Módulo os
- Módulo sys

### Uso
1. Copias keyword de BlackBox a Amazon
2. Abres X-rays e incrementas los resultados ( Boton Mas Resultados )
3. Descargas CSV y reemplazas el nombre del CSV con el nombre de la palabra clave
4. Coloca CSV dentro de la carpeta data
5. Ejecutas en la terminal: 
```python helium.py data/[folder name]```

### Funcionalidad
- Lee y procesa archivos CSV en la carpeta especificada.
- Filtra filas basadas en valores de recuento de reseñas y de ingresos.
- Calcula los ingresos totales para cada marca y verifica si superan el 30% del ingreso total.
- Calcula los ingresos para los 3 productos principales y verifica si superan el 30% del ingreso total.
- Produce una salida de ÉXITO o FRACASO para cada archivo procesado.

### Funciones
`process_csv_file(csv_filename)`

- Entrada: csv_filename (cadena de caracteres) - la ruta al archivo CSV a procesar.
- Salida: 'ÉXITO' si se cumplen las condiciones o un mensaje de error si no se cumplen.
- Funcionalidad:
  - Lee el archivo CSV y elimina cualquier carácter BOM de la fila del encabezado. 
  - Crea un diccionario para almacenar los ingresos totales para cada marca. 
  - Crea una lista para almacenar los datos filtrados y ordenados. 
  - Filtra filas basadas en valores de recuento de reseñas e ingresos. 
  - Calcula los ingresos totales para cada marca y verifica si superan el BRAND_PERCENTAGE del ingreso total. 
  - Calcula los ingresos para los 3 productos principales y verifica si superan el TOP_THREE_PERCENTAGE del ingreso total. 
  - Produce una salida de ÉXITO o FRACASO según los resultados.

### Variables
BRAND_PERCENTAGE - representa el porcentaje máximo de ingresos totales que puede provenir de una sola marca.
TOP_THREE_PERCENTAGE - representa el porcentaje máximo de ingresos totales que puede provenir de los 3 productos principales.
