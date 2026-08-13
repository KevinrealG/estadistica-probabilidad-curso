# Laboratorio 7: Muestreo de medias y varianzas con Python en Colab
---

---

## **Competencias por Desarrollar**

1. **Recolección y sistematización de datos**
    - Importar, organizar y preparar bases de datos para su análisis utilizando Python en Google Colab.
    - Aplicar técnicas de muestreo aleatorio para construir muestras representativas.
2. **Cálculo e interpretación de medidas estadísticas**
    - Calcular medidas descriptivas (media, mediana, varianza, desviación estándar) tanto para la población como para muestras generadas con Python.
    - Analizar la distribución de las medias y varianzas muestrales mediante histogramas.
3. **Uso de herramientas digitales y lenguaje Python para análisis estadístico**
    - Utilizar librerías como **Pandas, NumPy y Matplotlib** para realizar muestreos repetidos y visualizar distribuciones.
    - Comunicar los resultados en reportes claros y fundamentados.

---

## **Resultados de Aprendizaje**

- Recolecto y organizo información cuantitativa en Google Colab, aplicando buenas prácticas de importación y limpieza.
- Analizo e interpreto datos mediante medidas descriptivas, muestreos aleatorios y visualizaciones estadísticas.
- Utilizo Python en Colab para resolver problemas de muestreo, generar histogramas y presentar informes en formato profesional.

---

# **Temáticas desarrolladas en la práctica**

- **Carga y organización de datos en Python (Google Colab)**
- **Selección de una muestra aleatoria utilizando NumPy / Pandas**
- **Generación de múltiples muestras para estudiar la distribución de medias y varianzas**
- **Construcción de histogramas del muestreo con Matplotlib / Seaborn**
- **Interpretación del comportamiento del muestreo (Ley de los Grandes Números y TLC)**

---

# **Problema de aplicación**

Los estudiantes usarán los datos disponibles en la plataforma SAVIO.

Utilizando **Python en Google Colab**, deberán realizar un muestreo aleatorio repetido con el objetivo de estudiar la distribución de las **medias** y **varianzas** muestrales.

La actividad debe realizarse siguiendo **exactamente** el procedimiento mostrado en el video de la Semana 7.

---

# **Instrucciones del Laboratorio**

## **Paso 1. Revisión del video guía**

En el aula de informática:

1. Ingresar a SAVIO → Semana 7
2. Abrir el video titulado:**LABORATORIO 7 – Muestreo de Varianzas en Python**
3. 

https://www.youtube.com/watch?v=8AWwIAU8Kx0

🔗 Enlace alternativo:

https://www.youtube.com/watch?v=8AWwIAU8Kx0

El video muestra paso a paso:

### **1. Organización de los datos para trabajar en Colab**

### **2. Ejemplos de código para el muestreo**

### **3. Realización del muestreo**

- Selección de tamaño muestral
- Generación automática de *k* muestras
- Registro de:
    - media muestral
    - varianza muestral

### **4. Construcción del histograma del muestreo**

- Análisis visual de la distribución
- Identificación de patrones estadísticos

---

# **Paso 2. Compromisos de entrega**

### **📌 Entregable 1 – Evidencia del laboratorio guiado**

Debe incluir:

- Carga y visualización inicial de los datos
- Código utilizado para el muestreo
- Histogramas de medias y varianzas(con sus nombre en los titulos) Seleccionando bien el número de barras.
- PDF exportado desde Colab

---

### **📌 Entregable 2 – Repetición autónoma del laboratorio**

Ahora el estudiante deberá:

- Cambia los parametros iniciales, para simular una nueva variable, diferente a la inicial(**EDAD**).
- Repetir todo el proceso en Colab
- Generar nuevos histogramas
- Concluir si las distribuciones muestrales cambian respecto al primer ejercicio. (**Añadir una celda de Texto**)
- Exportar un segundo **PDF**

---

### **📤 Subida en SAVIO**

Entregar:

- PDF del laboratorio guiado
- PDF del laboratorio repetido con nuevas variables

---

# **Rúbrica de Evaluación – Laboratorio 7 (**

| **Criterio** | **Nivel 1 – Insuficiente** | **Nivel 2 – Aceptable** | **Nivel 3 – Bueno** | **Nivel 4 – Excelente** |
| --- | --- | --- | --- | --- |
| **1. Entregable 1: Carga y visualización de los datos** | No carga correctamente los datos o no los visualiza. | Importa los datos pero con fallas, sin visualización clara o con información incompleta. | Importa y visualiza los datos de forma adecuada con mínimos errores o pasos omitidos. | Importa los datos correctamente, muestra las primeras filas, verifica tipos y evidencia una organización clara. La presentación es limpia y completa. |
| **2. Entregable 1: Código del muestreo + histogramas (titulos correctos)** | No incluye el código de muestreo o los histogramas no existen o son incorrectos. | El código tiene errores importantes o incompletos. Los histogramas están mal rotulados o faltan. | El código funciona con pequeños errores o desorden. Los histogramas aparecen con títulos adecuados aunque con detalles menores. | El código funciona perfectamente, está organizado y comentado. Genera histogramas claros, con títulos correctos (“Histograma de Medias”, “Histograma de Varianzas”). |
| **3. Entregable 2: Repetición autónoma con una variable distinta** | No repite el laboratorio o no utiliza una variable distinta. | Repite parcialmente el procedimiento o no justifica bien la selección de la nueva variable. | Repite el proceso con una variable distinta, pero con omisiones menores o errores no críticos. | Selecciona correctamente **una variable distinta**, repite todo el proceso de forma completa (carga, muestreo, histogramas). El trabajo es claro, organizado y técnicamente correcto. |
| **4. Entregable 2: Histogramas + conclusión comparativa** | No presenta histogramas o no entrega ninguna conclusión. | Histogramas incompletos o mal titulados; conclusión muy superficial o poco clara. | Histogramas correctos, pero con una conclusión breve o poco profunda. | Genera histogramas completos, con títulos correctos, y presenta una conclusión clara sobre si cambia la distribución muestral frente al ejercicio guiado. |
| **5. Entrega final en SAVIO (PDF guiado + PDF autónomo)** | No entrega los archivos o la evidencia es insuficiente. | Entrega solo uno de los PDFs, o los archivos tienen problemas importantes de formato. | Entrega ambos PDFs, pero con errores menores de formato o nomenclatura. | Entrega **los dos PDFs** correctamente nombrados, completos, legibles y en el espacio asignado. Evidencia orden y cumplimiento total. |