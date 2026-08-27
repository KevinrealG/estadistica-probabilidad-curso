Como tu **Academic Class Designer AI**, y bajo los parámetros estrictos de diseño instruccional, aprendizaje activo y gestión de tiempo, aquí tienes la planificación completa de la **Semana 4** del curso de Estadística y Probabilidad (UTB). Cada sesión está diseñada rigurosamente para **50 minutos**, modalidad presencial, evitando el modelo magistral tradicional.

---

### 📋 Información General del Eje (Semana 4)

* **Curso:** Estadística y Probabilidad (CBAS-E01A).


* **Temática:** Medidas de dispersión (Rango, Varianza, Desviación Estándar), Diagramas de Caja y Análisis Descriptivo Completo.
* **Competencia:** Calcular e interpretar medidas estadísticas (de tendencia central, dispersión y posición) para describir y analizar conjuntos de datos univariados, empleando herramientas digitales.



---

### 📊 Clase N°13: Medidas de Dispersión (¿Por qué el promedio engaña?)

**1. Información General y Recursos**

* **Objetivo:** Diferenciar grupos con igual promedio pero distinta variabilidad mediante el cálculo conceptual de la varianza y la desviación estándar.
* **Recursos Previos:** Video corto recomendado para HTI: *“¿Qué es la Desviación Estándar y por qué importa?”* (Ej. StatQuest o Khan Academy). Calculadoras científicas.

**2. Estructura de la Sesión (50 min)**

* **Apertura (8 min) - *El Reto*:** Proyecta los dos cursos con promedio 3.5 (Curso A: 3.4, 3.5, 3.6, 3.5, 3.4 vs. Curso B: 1.0, 5.0, 2.0, 4.8, 3.7). Lanza el reto: *"Si ambos tienen exactamente el mismo promedio, ¿son iguales para un profesor? ¿Cuál elegirían si fueran el director de carrera?"*.
* **Exploración (7 min) - *Hipótesis*:** Pide a los estudiantes que intenten medir numéricamente "qué tan lejos" está cada número del promedio en ambos cursos antes de dar la fórmula oficial.
* **Desarrollo Conceptual (10 min) - *Teoría mínima*:** Explicación ágil de Rango, Varianza muestral ($s^2$) y Desviación Estándar ($s$). Enfatiza el significado conceptual: *"La desviación estándar es el promedio (aproximado) de cuánto se desvían los datos de la media"*.
* **Actividad Guiada y Colaborativa (15 min):** En parejas, calculan a mano la desviación estándar del Curso A y del Curso B utilizando una tabla guiada en la pizarra. Contrastan el resultado matemático con su intuición inicial.
* **Aplicación (5 min):** Discusión rápida: *"En gestión de riesgos o ingeniería, ¿por qué un proceso con menor desviación estándar es más valioso aunque su promedio sea ligeramente inferior?"*.
Estudiar la variabilidad es crucial porque **el promedio por sí solo puede ser engañoso**. Dos grupos pueden tener la misma media, pero comportamientos completamente distintos en su interior.

Entender la dispersión de los datos permite:

* **Comprender la estabilidad real:** Muestra si un grupo es homogéneo o si su promedio está distorsionado por valores extremos.
* **Medir el riesgo y la incertidumbre:** En finanzas, la variabilidad revela la volatilidad de una inversión; en la ciencia, indica el margen de error y la confiabilidad de las mediciones. En finanzas, evalúa la volatilidad de una inversión (el rendimiento no importa si el riesgo es altísimo). En ciencia, determina qué tan preciso y confiable es un experimento.
* **Controlar la calidad y el servicio:** En la industria, una alta desviación significa inconsistencia (piezas defectuosas). En servicios, como un hospital, ayuda a garantizar tiempos de espera predecibles.
* **Revelar desigualdades ocultas:** En economía o educación, un promedio alto puede esconder una enorme brecha entre quienes tienen mucho y quienes tienen poco, o entre estudiantes que aprenden rápido y los que se rezagan.
* **Detectar valores atípicos:** Facilita la identificación de anomalías, errores o fenómenos especiales que requieren atención.
Detectar brechas y evaluar consistencia: En educación, visibiliza si un grupo de estudiantes avanza a la par o si hay alumnos muy rezagados. En servicios (como hospitales), ayuda a saber qué tan estables son los tiempos de espera.
Identificar anomalías: Permite detectar valores atípicos que podrían ser errores de medición o fenómenos especiales que alteran el análisis.

**🧠 Mensaje clave para tus estudiantes:**

> La media te dice dónde está el centro de los datos, pero la variabilidad te muestra qué tan dispersos están a su alrededor. Sin variabilidad, el promedio es solo un número vacío.
- 
* **Cierre y Reflexión (5 min):** Pregunta de salida obligatoria (en papel o digital): *"¿Por qué elevamos al cuadrado las diferencias al calcular la varianza?"*. Prohibido usar "¿Alguna pregunta?".

**3. Estructura de las Diapositivas (3 slides)**

* **Slide 1:** El Engaño del Promedio (Los datos de los Cursos A y B).
* **Slide 2:** Midiendo el Caos (Fórmulas conceptuales de Varianza y Desviación Estándar).
* **Slide 3:** Reflexión de Cierre (La pregunta sobre el cuadrado de las diferencias).

---

### 📦 Clase N°14: Diagramas de Caja y Valores Atípicos (Boxplots)

**1. Información General y Recursos**

* **Objetivo:** Interpretar la dispersión visual y la asimetría de los datos mediante la construcción y lectura de diagramas de caja (Boxplots).
* **Recursos Previos:** IntroStat App o calculadoras.

**2. Estructura de la Sesión (50 min)**

* **Apertura (8 min) - *El Reto*:** Proyecta un gráfico de sueldos o notas donde hay un punto aislado muy lejos de la caja. Lanza la pregunta: *"¿Es un error de digitación o un genio/afortunado que rompe la regla? ¿Cómo decide la estadística si un dato es un atípico (outlier)?"*.
* **Exploración (7 min) - *Hipótesis*:** Pide al salón que definan qué porcentaje de datos vive dentro de una "caja" en un gráfico si dividimos los datos en 4 partes iguales (Cuartiles).
* **Desarrollo Conceptual (10 min) - *Teoría mínima*:** Anatomía del Boxplot: Mínimo, $Q_1$, Mediana ($Q_2$), $Q_3$, Máximo, Rango Intercuartílico ($RIC = Q_3 - Q_1$) y los límites de control para detectar atípicos ($1.5 \times RIC$).
* **Actividad Guiada y Colaborativa (15 min):** Entrega un mini-conjunto de 12 datos a cada grupo. Deben calcular los cuartiles a mano, trazar el esquema básico de un diagrama de caja en su cuaderno e identificar si hay valores atípicos.
* **Aplicación (5 min):** Verificación rápida de la simetría: *"Si la línea de la mediana está exactamente en el centro de la caja y los bigotes son iguales, ¿qué podemos decir de la distribución?"*.
* **Cierre y Reflexión (5 min):** Pregunta de salida: *"¿Por qué el diagrama de caja es más resistente a los valores extremos que la media y la desviación estándar?"*.

**3. Estructura de las Diapositivas (3 slides)**

* **Slide 1:** El Misterio del Punto Aislado (Introducción visual al outlier).
* **Slide 2:** La Anatomía de la Caja (Esquema claro del Boxplot y los límites de 1.5 RIC).
* **Slide 3:** Cierre Crítico (Ventajas del Boxplot frente a los descriptores tradicionales).

---

### 🧪 Clase N°15: Evaluación - Actividad de Análisis Descriptivo de Datos

**1. Información General y Recursos**

* **Objetivo:** Evaluar la competencia de recolección, tabulación y cálculo de descriptores univariados (tendencia, posición y dispersión) aplicados a los datos reales de los estudiantes.
* **Recursos Previos:** Formularios creados en la Semana 2 y bases de datos tabuladas en MS Teams.

**2. Estructura de la Sesión (50 min)**

* **Apertura (5 min) - *Instrucciones de la Evaluación*:** Explicación del taller práctico integrador. No es un examen de memoria, es una **actividad de desempeño** basada en sus propios datos recolectados.
* **Exploración y Desarrollo (0 min):** (Transición directa al trabajo autónomo/colaborativo guiado).
* **Actividad Guiada y Colaborativa (30 min):** En grupos, los estudiantes abren su base de datos de la encuesta de la UTB. Deben entregar un reporte corto que incluya:
1. Tabla de frecuencias completa de su variable numérica (con notación $f_i, F_i, f_{ri}, F_{ri}$).
2. Cálculo de Media, Mediana, Desviación Estándar y Cuartiles.
3. Generación e interpretación del Diagrama de Caja.


* **Aplicación (10 min):** Cada grupo redacta 2 conclusiones gerenciales basadas en los hallazgos de dispersión de su variable (Ej: *"El 50% central de los estudiantes gasta entre X y Y dinero, encontrándose un comportamiento altamente disperso..."*).
* **Cierre y Reflexión (5 min):** Subida obligatoria del entregable en MS Teams. Cierre motivacional sobre el poder de convertir datos crudos en conocimiento útil.

**3. Estructura de las Diapositivas (2 slides)**

* **Slide 1:** Rúbrica y Requisitos de la Actividad Descriptiva.
* **Slide 2:** Cronómetro en pantalla (30 min para desarrollo y subida a Teams).

---

### 💻 Clase N°16: Laboratorio 4 - Análisis de Datos con Python (Google Colab)

**1. Información General y Recursos**

* **Objetivo:** Emplear Python en Google Colab para automatizar el cálculo de medidas de dispersión, tendencia y gráficos avanzados (Boxplots e Histogramas) sobre bases de datos institucionales.
* **Recursos Previos:** Cuentas de Google activas, entorno de **Google Colab**, dataset unificado de la UTB en formato CSV cargado en Teams.

**2. Estructura de la Sesión (50 min)**

* **Apertura (5 min) - *El Gancho*:** *"Hoy dejamos las calculadoras y la mano alzada. Vamos a programar nuestro primer script estadístico en la nube como científicos de datos"*.
* **Exploración (5 min):** Demostración en vivo de cómo abrir Google Colab y cargar una librería básica de análisis (`import pandas as pd`, `import matplotlib.pyplot as plt`).
* **Desarrollo Conceptual (5 min):** Breve explicación de las funciones clave en Python para estadística descriptiva (`df.describe()`, `df['variable'].mean()`, `df['variable'].std()`).
* **Actividad Guiada y Colaborativa (25 min):** Los estudiantes abren el Notebook precargado por el docente en Google Colab. En parejas, ejecutan los bloques de código para importar el dataset de la UTB, calcular la desviación estándar, generar histogramas y un `boxplot()` automático de la variable numérica del grupo. El docente circula resolviendo errores de sintaxis.
* **Aplicación (5 min):** Interpretar los gráficos generados por la consola de Python frente a los cálculos manuales hechos en la clase anterior.
* **Cierre y Reflexión (5 min):** Pregunta de salida: *"¿Qué ventaja y qué riesgo encuentran al delegar todo el análisis estadístico a una línea de código en Python?"*. Envío del link de su Colab a Teams.

**3. Estructura de las Diapositivas (2 slides)**

* **Slide 1:** Bienvenidos a Google Colab (Enlace al notebook base y reglas del laboratorio).
* **Slide 2:** Sintaxis Esencial (Comandos clave proyectados en pantalla para consulta rápida).
- Presentaciones de Análisis
    - Rubricas de evaluación
    - Link para informe
        
        Evaluación de Presentación de Análisis estadístico descriptivo.docx
        

    

### Ejercicios EN Casa
    
🔵 Ejercicio 3 — Rango, Varianza y Desviación Estándar
    
    ### “¿Qué grupo es más homogéneo?”
    
    Se comparan dos grupos en un examen. Grupo A: 65, 68, 70, 72, 74, 76, 78 y Grupo B: 50, 60, 70, 80, 90, 100, 110.
    
    ### 🔎 Actividades
    
    1. Calcular rango en ambos grupos. 2. Calcular varianza y desviación estándar. 3. Comparar dispersión. 4. Determinar cuál grupo es más homogéneo.
    
    ---
    
    ### 💬 Discusión
    
    - Ambos grupos tienen la misma media (70).
    - ¿Significa eso que son iguales?
    - ¿Qué información adicional da la desviación estándar?
    
    ---
    
    ---
    
🔵 Ejercicio 4 — Rango intercuartílico y valores atípicos
    
    ### “¿Hay estudiantes con desempeño extremo?”
Notas: 40, 55, 60, 62, 65, 67, 70, 72, 75, 78, 80, 82, 85, 90, 150.
Calcular Q1, Q3, RIC, límites, valores atípicos y analizar el efecto del 150 en la media frente a la mediana.
- ¿Eliminarías el valor 150?
    - ¿Es error o caso excepcional?
    - ¿Cómo afecta la media vs la mediana?
    
    ---
    
    # 🎯 Competencias que desarrollan estos ejercicios
    
    - Interpretación de cuartiles y percentiles.
    - Comparación de dispersión y homogeneidad.
    - Identificación de valores atípicos.