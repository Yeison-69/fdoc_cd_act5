import pandas as pd
import numpy as np

print("--- INICIO DE LA ACTIVIDAD 5 ---")

# Dataset base
datos = {
    'Nombre':  ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'Edad':    [25, 30, 22, None, 28],
    'Ciudad':  ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'Ingreso': [3000, 4500, 2800, 5000, None]
}

df = pd.DataFrame(datos)
# Guarda el dataset base
df.to_csv('actividad_semana5.csv', index=False)
print("\nDataset base creado y guardado como 'actividad_semana5.csv':")
print(df)

# ---------------------------------------------------------
# 1) Series — crear y operar
print("\n--- 1) Series ---")
lista_nums = [10, 20, 30, 40]
serie_lista = pd.Series(lista_nums)
print("Serie desde lista:\n", serie_lista)

dict_datos = {'a': 100, 'b': 200, 'c': 300}
serie_dict = pd.Series(dict_datos)
print("Serie desde diccionario:\n", serie_dict)

print("Acceso por índice (serie_lista[0]):", serie_lista[0])
print("Acceso por clave (serie_dict['b']):", serie_dict['b'])

serie_lista[0] = 999
print("Serie modificada (índice 0 a 999):\n", serie_lista)

serie_multiplicada = serie_lista * 2
print("Serie multiplicada por 2:\n", serie_multiplicada)


# ---------------------------------------------------------
# 2) DataFrame — crear y explorar
print("\n--- 2) DataFrame ---")
datos_pequeno = {'A': [1, 2], 'B': [3, 4]}
df_pequeno = pd.DataFrame(datos_pequeno)
print("DataFrame pequeño:\n", df_pequeno)
print("Tipos de columnas:\n", df_pequeno.dtypes)


# ---------------------------------------------------------
# 3) Inspeccionar y explorar
print("\n--- 3) Inspeccionar ---")
print("Head (2):\n", df.head(2))
print("Tail (2):\n", df.tail(2))
print("\nInfo:")
df.info()
print("\nShape:", df.shape)
print("\nDescribe:\n", df.describe())


# ---------------------------------------------------------
# 4) Acceder a columnas y filas
print("\n--- 4) Acceder ---")
col_nombre = df['Nombre']
print("Columna Nombre (Series):\n", col_nombre)

fila_1_loc = df.loc[1]
print("Fila índice 1 (loc):\n", fila_1_loc)

fila_1_iloc = df.iloc[1]
print("Fila índice 1 (iloc):\n", fila_1_iloc)

valor_especifico = df.at[1, 'Edad'] # O df.loc[1, 'Edad']
print("Valor fila 1, columna Edad:", valor_especifico)


# ---------------------------------------------------------
# 5) Operaciones básicas
print("\n--- 5) Operaciones ---")
df['Edad'] = df['Edad'] + 5
print("Edad incrementada en 5:\n", df)

# Manejar nulos con 0 para la multiplicación, aunque el ejercicio dice "maneja nulos con 0"
# Si Ingreso es NaN, * 12 sigue siendo NaN. Si queremos 0, hay que rellenar antes o después.
# Asumiré rellenar con 0 para el cálculo, o dejar NaN si no se especifica rellenar el original.
# La instrucción dice "maneja nulos con 0", interpretaré fillna(0) para el cálculo.
df['Ingreso_anual'] = df['Ingreso'].fillna(0) * 12
print("Columna Ingreso_anual creada:\n", df)


# ---------------------------------------------------------
# 6) Filtrar datos
print("\n--- 6) Filtrar ---")
filtro_edad = df[df['Edad'] > 30]
print("Filas con Edad > 30:\n", filtro_edad)

filtro_ciudad = df[df['Ciudad'].isin(['Madrid', 'Lima'])]
print("Filas Ciudad Madrid o Lima:\n", filtro_ciudad)


# ---------------------------------------------------------
# 7) Manejo de valores faltantes
print("\n--- 7) Valores Faltantes ---")
print("Nulos por columna:\n", df.isna().sum())

# Rellenar nulos
# Nota: Edad ya fue modificada (+5), así que el nulo original (None) ahora es NaN.
# Ingreso ya fue usado para Ingreso_anual, pero la columna Ingreso original sigue teniendo NaN.
df_relleno = df.copy()
df_relleno['Edad'] = df_relleno['Edad'].fillna(0)
df_relleno['Ciudad'] = df_relleno['Ciudad'].fillna('Desconocido')
mediana_ingreso = df_relleno['Ingreso'].median()
df_relleno['Ingreso'] = df_relleno['Ingreso'].fillna(mediana_ingreso)

print("DataFrame con nulos rellenos:\n", df_relleno)


# ---------------------------------------------------------
# 8) Leer y guardar datos
print("\n--- 8) Leer y Guardar ---")
df_leido = pd.read_csv('actividad_semana5.csv')
print("Leído de 'actividad_semana5.csv' (primeras filas):\n", df_leido.head())

df_seleccion = df[['Nombre', 'Edad', 'Ciudad']]
df_seleccion.to_csv('seleccion_columnas.csv', index=False)
print("Guardado 'seleccion_columnas.csv'")


# ---------------------------------------------------------
# 9) Ejercicio integrado
print("\n--- 9) Ejercicio Integrado ---")
# Reiniciamos con el df original (o usamos el actual modificado según se entienda "incrementa edad en 5")
# El ejercicio 5 YA incrementó la edad en 5. El ejercicio 9 dice "Incrementa Edad en 5" DE NUEVO?
# Asumiré que es un flujo sobre el dataset original o acumulativo.
# Para ser seguro y seguir la instrucción "Ejercicio integrado" como un todo:
# Voy a tomar el df actual (que ya tiene edad + 5 del paso 5) y NO incrementaré otra vez si se asume continuidad.
# PERO, a menudo estos ejercicios son "haz esto todo junto".
# Voy a hacerlo sobre el df actual que ya tiene las modificaciones previas, 
# O mejor, para cumplir "Incrementa Edad en 5" explícitamente aquí, lo haré.
# Si la edad ya es 30 (25+5), sumar 5 más da 35.
# Vamos a asumir que se refiere a realizar las operaciones en cadena sobre el estado actual.

df_final = df.copy()
# Ya se sumó 5 en el paso 5. Si el paso 9 pide "Incrementa Edad en 5", ¿es redundante o adicional?
# Lo haré adicional para cumplir la instrucción literal del paso 9.
df_final['Edad'] = df_final['Edad'] + 5 

# Filtra personas con Ingreso_anual > 36000
# Aseguramos que Ingreso_anual exista (creado en paso 5)
filtro_final = df_final[df_final['Ingreso_anual'] > 36000]

# Ordena por Ingreso_anual descendente
filtro_final_ordenado = filtro_final.sort_values(by='Ingreso_anual', ascending=False)

print("Resultado final (filtrado y ordenado):\n", filtro_final_ordenado)

filtro_final_ordenado.to_csv('personas_filtradas.csv', index=False)
print("Guardado 'personas_filtradas.csv'")

print("\n--- FIN ---")
