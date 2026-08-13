# Laboratorio 12. Análisis Exploratorio de Datos con RStudio – Parte 1 y Parte 2S
---

---

## **Competencias Por Desarrollar**

- Recolectar y sistematizar datos para construir tablas de frecuencias y representaciones gráficas pertinentes según el tipo de variable.
- Calcular e interpretar medidas estadísticas (tendencia central, dispersión, posición y asociación) para describir y analizar conjuntos de datos univariados y bivariados.
- Emplear herramientas digitales y software estadístico para realizar análisis exploratorios, aplicar modelos probabilísticos y comunicar resultados con argumentos cuantitativos sólidos.

---

## **Resultados de Aprendizaje**

- Recolecto y organizo información cuantitativa y cualitativa de manera sistemática utilizando métodos adecuados.
- Analizo e interpreto datos univariados y bivariados mediante descriptores estadísticos, gráficos y análisis exploratorio para tomar decisiones informadas.
- Utilizo software especializado (RStudio, Excel, Power BI, Statgraphics, Google Colab y R) para resolver problemas estadísticos con claridad y rigor académico.

---

## **Temáticas desarrolladas en esta práctica**

- **Introducción a RStudio – Parte 1**
- **Carga y organización de datos en R**
- **Exploración de variables en RStudio – Parte 2**
- **Generación de gráficas básicas para análisis exploratorio**
- **Práctica guiada: análisis estadístico y gráfico en RStudio**

---

# **Problema de aplicación**

Los estudiantes utilizarán los datos cargados en la plataforma SAVIO y realizarán un **Análisis Exploratorio de Datos en RStudio**, siguiendo *exactamente* las instrucciones mostradas en los videos de la **Semana 12**.

El análisis incluye:

- Importación y organización de los datos.
- Exploración básica con funciones de R (`summary()`, `str()`, `head()`).
- Gráficos univariados y bivariados.
- Interpretación de patrones relevantes.

---

# **Paso 1. Revisión de los videos guía**

Durante la sesión en el Aula de Informática, los estudiantes deben ingresar a la plataforma SAVIO → Semana 12 y revisar los siguientes videos:

---

### **Video 1. Iniciando en RStudio**

**Título:** Iniciando en RStudio 2026

🔗 https://www.youtube.com/watch?v=qcagALM7wEQ

https://www.youtube.com/watch?v=qcagALM7wEQ

Incluye:

- RStudio Cloud
- Scripts, consola, environment y pestañas esenciales
- Primeros comandos en R
- Lectura básica de datos

---

### **Video 2. Laboratorio – Exploración de Datos con RStudio**

**Título:** Laboratorio 12 Nuevo RStudio

🔗 https://www.youtube.com/watch?v=SQZVlyUnreA

https://www.youtube.com/watch?v=SQZVlyUnreA

Incluye:

- Importación de datasets
- Exploración de variables: `summary()`, `levels()`, `table()`
- Visualizaciones básicas:
- 

```r
#1
table_sexo<-table(DATOS2023$SEXO)
table_sexo
#2
pie_1<-pie(table_sexo, col=c("lightblue","pink"),
        main="Estudio de Pastel.\n Distribución por sexos.", labels = table_sexo)
        
#3
barp<-barplot(table_sexo, col = rainbow(5), border = "darkred",main = "Gráfico de Barras",sub = "UTB",xlab = "SEXO", ylab = "Conteo")
text(barp, table_sexo-30, labels = table_sexo)
#4
table_sexo2<-round(table(DATOS2023$SEXO)/121*100)
table_sexo2
#5
barp2<-barplot(table_sexo2, col = rainbow(5), border = "darkred",main = "Gráfico de Barras",sub = "UTB",xlab = "SEXO", ylab = "Porcentaje")
text(barp2, table_sexo2-30, labels = table_sexo2)
```

- Interpretación y conclusiones

---

# **Paso 2. Compromisos de entrega**

## **📌 Entregable 1 – Evidencia del laboratorio guiado**

Debe incluir:

- Carga del dataset en RStudio
- Exploración inicial (gráficos)
- Gráficos generados (con títulos y ejes bien definidos)
- Interpretación básica de las visualizaciones
- PDF exportado desde RStudio

---

## **📌 Entregable 2 –**

Debe incluir:

Agregar los siguientes chunks:

```r

#1
table_3<-table(DATOS2023$SEXO, DATOS2023$CURSO)
table_3

#2

barp3<-barplot(table_3,
        main = "Gráfico de barras CURSO vs SEXO",
        xlab = "CURSO", ylab = "Frecuencia",
        col = c("pink", "blue"),
        legend.text = rownames(table_3),
        beside = TRUE) # Barras agrupadas
text(barp3, table_3-5, labels = table_3)

#3

table_4<-round(table(DATOS2023$SEXO, DATOS2023$CURSO)/121*100)
table_4

#4 

barp4<-barplot(table_4,
        main = "Gráfico de barras CURSO vs SEXO en porcentajes",
        xlab = "CURSO", ylab = "Frecuencia",
        col = c("pink", "blue"),
        legend.text = rownames(table_4),
        beside = TRUE) # Barras agrupadas
text(barp4, table_4-5, labels = table_4)
#5
table_5<-table(DATOS2023$ESTRATO, DATOS2023$CURSO)
table_5
#6 
barp3<-barplot(table_5,
        main = "Gráfico de barras CURSO vs ESTRATO",
        xlab = "CURSO", ylab = "Frecuencia",
        col = rainbow(5),
        legend.text = rownames(table_5),
        beside = TRUE) # Barras agrupadas
text(barp3, table_5-1, labels = table_3)
```

- Interpretación
- Segundo PDF generado

---

## **📤 Subida en SAVIO**

El estudiante debe subir:

- PDF del laboratorio guiado
- PDF del ejercicio autónomo

---

# ✅ **Rúbrica de Evaluación – Laboratorio 12 (4 niveles – 5 criterios)**

| **Criterio** | **Nivel 4 – Excelente** | **Nivel 3 – Bueno** | **Nivel 2 – Aceptable** | **Nivel 1 – Insuficiente** |
| --- | --- | --- | --- | --- |
| **1. Carga y organización de los datos en RStudio** | Importa los datos correctamente, verifica tipos de datos y presenta adecuada organización y limpieza inicial. | Importa los datos y los visualiza con leves omisiones. | Importación incompleta o sin mostrar exploración básica. | No logra importar los datos o no presenta evidencia. |
| **2. Exploración de los datos (summary, estructura, tablas)** | Muestra `summary()`, estructura, tablas y explicaciones claras de cada salida. | Muestra la mayoría de las exploraciones con mínima explicación. | Exploración incompleta o con interpretaciones superficiales. | No presenta exploración de los datos. |
| **3. Gráficos generados** | Gráficos completos, bien titulados, con ejes claros e interpretación adecuada. | Gráficos correctos con pequeños detalles faltantes. | Gráficos incompletos o sin interpretación. | No presenta gráficos o son incorrectos. |
| **5. Presentación y entrega en PDF** | Entrega ambos PDFs completos, ordenados y con conclusiones vinculadas a competencias y temáticas. | Entrega ambos PDFs con problemas menores en organización. | Entrega incompleta o poco organizada. | No entrega los archivos solicitados. |

---