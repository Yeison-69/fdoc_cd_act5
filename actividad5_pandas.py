# ============================================================
# ACTIVIDAD 5: PANDAS BÁSICO (Series y DataFrames)
# ============================================================
# Autor: Yeison Caro Orrego
# Curso: Fundamentos de Ciencia de Datos
# Descripción: Ejercicios prácticos con Pandas (Series, DataFrames,
#              inspección, operaciones, filtrado, manejo de nulos y CSV).
# ============================================================

import pandas as pd

# ============================================================
# Dataset base
# ============================================================

datos = {
    'Nombre':  ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'Edad':    [25, 30, 22, None, 28],
    'Ciudad':  ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'Ingreso': [3000, 4500, 2800, 5000, None]
}

df = pd.DataFrame(datos)
df.to_csv('actividad_semana5.csv', index=False)  # guardar dataset base
print("✅ Dataset base creado correctamente:\n")
print(df.head())

# ============================================================
# 1) SERIES — CREAR Y OPERAR
# ============================================================

print("\n1️⃣ SERIES — CREAR Y OPERAR")

# Crear Series desde una lista
serie_lista = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("\nSeries desde lista:\n", serie_lista)

# Crear Series desde un diccionario
serie_dict = pd.Series({'Ana': 25, 'Bob': 30, 'Clara': 22})
print("\nSeries desde diccionario:\n", serie_dict)

# Acceder por clave e índice
print("\nValor de 'b':", serie_lista['b'])
print("Valor de índice 0:", serie_lista.iloc[0])

# Modificar un valor
serie_lista['a'] = 100
print("\nSeries modificada:\n", serie_lista)

# Aplicar una operación
serie_doble = serie_lista * 2
print("\nSeries multiplicada por 2:\n", serie_doble)

# ============================================================
# 2) DATAFRAME — CREAR Y EXPLORAR
# ============================================================

print("\n2️⃣ DATAFRAME — CREAR Y EXPLORAR")

df2 = pd.DataFrame({
    'Nombre': ['Ana', 'Bob', 'Clara'],
    'Edad': [25, 30, 22],
    'Ciudad': ['Madrid', 'Lima', 'Bogotá']
})
print("\nDataFrame creado:\n", df2)

print("\nTipos de datos:")
print(df2.dtypes)

# ============================================================
# 3) INSPECCIONAR Y EXPLORAR
# ============================================================

print("\n3️⃣ INSPECCIONAR Y EXPLORAR")

print("\nPrimeras filas:")
print(df.head(3))

print("\nÚltimas filas:")
print(df.tail(2))

print("\nInformación general:")
print(df.info())

print("\nDimensiones (filas, columnas):", df.shape)

print("\nDescripción estadística:")
print(df.describe())

# ============================================================
# 4) ACCEDER A COLUMNAS Y FILAS
# ============================================================

print("\n4️⃣ ACCEDER A COLUMNAS Y FILAS")

print("\nColumna 'Nombre' como Series:")
print(df['Nombre'])

print("\nFila con índice 1 usando loc:")
print(df.loc[1])

print("\nFila con índice 1 usando iloc:")
print(df.iloc[1])

print("\nValor específico (fila 1, columna 'Edad'):")
print(df.loc[1, 'Edad'])

# ============================================================
# 5) OPERACIONES BÁSICAS
# ============================================================

print("\n5️⃣ OPERACIONES BÁSICAS")

# Incrementar edad en 5 años
df['Edad'] = df['Edad'].fillna(0) + 5
print("\nEdad incrementada en 5 años:\n", df)

# Crear columna ingreso anual
df['Ingreso_anual'] = df['Ingreso'].fillna(0) * 12
print("\nNueva columna 'Ingreso_anual':\n", df)

# ============================================================
# 6) FILTRAR DATOS
# ============================================================

print("\n6️⃣ FILTRAR DATOS")

print("\nFilas con Edad > 30:")
print(df[df['Edad'] > 30])

print("\nFilas donde Ciudad es 'Madrid' o 'Lima':")
print(df[df['Ciudad'].isin(['Madrid', 'Lima'])])

# ============================================================
# 7) MANEJO DE VALORES FALTANTES
# ============================================================

print("\n7️⃣ MANEJO DE VALORES FALTANTES")

print("\nDetección de nulos:")
print(df.isna())

print("\nConteo de nulos por columna:")
print(df.isna().sum())

# Rellenar nulos con valores específicos
df['Edad'] = df['Edad'].fillna(0)
df['Ciudad'] = df['Ciudad'].fillna('Desconocido')
df['Ingreso'] = df['Ingreso'].fillna(df['Ingreso'].median())
print("\nDataFrame con nulos rellenados:\n", df)

# ============================================================
# 8) LEER Y GUARDAR DATOS
# ============================================================

print("\n8️⃣ LEER Y GUARDAR DATOS")

# Leer CSV creado
df_leido = pd.read_csv('actividad_semana5.csv')
print("\nPrimeras filas del CSV leído:\n", df_leido.head())

# Guardar CSV con columnas seleccionadas
df[['Nombre', 'Edad', 'Ciudad']].to_csv('personas_basico.csv', index=False)
print("\n✅ Archivo 'personas_basico.csv' guardado correctamente.")

# ============================================================
# 9) EJERCICIO INTEGRADO
# ============================================================

print("\n9️⃣ EJERCICIO INTEGRADO")

# Incrementar edad en 5
df['Edad'] = df['Edad'] + 5

# Filtrar personas con ingreso anual > 36000
df_filtrado = df[df['Ingreso_anual'] > 36000]

# Ordenar por ingreso anual descendente
df_filtrado = df_filtrado.sort_values(by='Ingreso_anual', ascending=False)

# Guardar resultado
df_filtrado.to_csv('personas_filtradas.csv', index=False)
print("\n✅ Archivo 'personas_filtradas.csv' guardado correctamente.")
print("\nResultado final:\n", df_filtrado)

print("\n🎯 Actividad 5 completada con éxito.")
