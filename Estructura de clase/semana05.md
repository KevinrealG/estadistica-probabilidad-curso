### 📋 Información General del Eje (Semana 5)

* **Curso:** Estadística y Probabilidad (CBAS-E01A).


* **Duración Validada:** 50 minutos por sesión (4 sesiones).
* **Modalidad:** Presencial (Aula tradicional y Aula de Informática para laboratorio).
* **Temática:** Evaluación de Corte 1, Frecuencias Agrupadas (Regla de Sturges), Histogramas, y Autoevaluación.

---

### 📝 Clase N°17: Parcial Corte 1 - Parte I (Fundamentos y Análisis Univariado)

**1. Estructura de la Sesión (50 min)**

* **Apertura (5 min) - *Desbloqueo cognitivo*:** Recepción de los estudiantes. Para reducir la ansiedad matemática, proyecta en pantalla un gráfico real (ej. estadísticas de porcentajes de embasarse y apariciones al plato en la liga de béisbol) con un error garrafal de diseño. Pregunta abierta: *"Antes de empezar, ¿quién me dice por qué este gráfico tomaría una decisión gerencial desastrosa?"*.
* **Exploración y Desarrollo Conceptual (0 min):** Transición directa a la evaluación.
* **Actividad Guiada y Colaborativa (40 min) - *Evaluación Aplicada*:** Desarrollo de la Parte I del parcial. Diseña el examen no como preguntas aisladas, sino como un **estudio de caso continuo**.
* *Contexto sugerido del examen:* Entregar un set de datos sobre rendimiento deportivo o clínico y solicitar la clasificación de variables, construcción de tabla de frecuencias simple y cálculo manual de medidas de tendencia central.


* **Cierre y Reflexión (5 min):** Recolección de exámenes. Pregunta de metacognición proyectada en la puerta antes de salir: *"De los cálculos que acaban de hacer, ¿cuál consideran que fue el dato más engañoso del caso?"*.

---

### 📝 Clase N°18: Parcial Corte 1 - Parte II (Dispersión y Posición)

**1. Estructura de la Sesión (50 min)**

* **Apertura (5 min):** *"Ayer analizamos el centro de los datos. Hoy vamos a evaluar qué tan caótico es el comportamiento de esa muestra"*. Breve recordatorio de las reglas del examen.
* **Actividad Aplicada (40 min) - *Evaluación de Desempeño*:** Continuación del caso de estudio de la clase anterior.
* *Retos del examen:* Calcular la varianza y desviación estándar de la muestra. Construir los cuartiles y armar un esquema de diagrama de caja (Boxplot) para identificar si existen valores atípicos en el rendimiento.


* **Cierre y Reflexión (5 min):** Pregunta de cierre (sin "alguna duda"): *"Si tuvieran que defender el rendimiento de este grupo ante un gerente, ¿usarían la media de ayer o el diagrama de caja de hoy?"*.

---

### 📊 Clase N°19: El Caos Masivo (Sturges, Histogramas y Forma)

**1. Estructura de la Sesión (50 min)**

* **Apertura (8 min) - *El Reto*:** Proyecta una base de datos con 1,000 registros numéricos continuos (ej. salarios exactos con centavos). Pregunta detonante: *"Si hacemos una tabla de frecuencias como las de la semana 2, tendríamos 1,000 filas. ¿Cómo le presentamos esto a una junta directiva sin que se queden dormidos?"*.
* **Exploración (7 min) - *Hipótesis*:** Pide a los estudiantes que sugieran cómo agruparían los datos. Escucha sus propuestas sobre rangos (ej. "de 1000 a 2000"). Pregunta: *"¿Cuántos grupos son muy pocos y cuántos son demasiados?"*.
* **Desarrollo Conceptual (10 min):**
* Diferencia visual y conceptual entre Gráfico de Barras (categorías separadas) e Histograma (datos continuos pegados).
* Formalización de la Regla de Sturges para hallar el número de intervalos: $k = 1 + 3.322 \log_{10}(n)$.
* Cálculo de la amplitud: $A = \frac{Rango}{k}$.


* **Actividad Guiada (15 min):** En grupos de 3, entregas un set de 50 datos. Deben calcular $k$ y $A$, construir los intervalos (Límite Inferior - Límite Superior) y hacer el conteo rápido de la primera clase.
* **Aplicación y Asignación de Investigación (5 min):** Proyecta tres histogramas con distintas formas (simétrico, sesgado a la derecha, muy puntiagudo).
* *Asignación:* "La estadística no solo mide el centro y la dispersión, también mide la *forma*. Para la próxima clase, deben investigar qué significan **Kurtosis** y **Sesgo (Skewness)** y cómo se identifican visualmente en un histograma."


* **Cierre y Consolidación (5 min) - *Autoevaluación*:** Los estudiantes llenan un formulario digital (Forms) de 3 preguntas valorando su propio desempeño, participación y comprensión durante este primer corte.

---

### 💻 Clase N°20: Parcial de Laboratorio (Análisis Computacional)

**1. Estructura de la Sesión (50 min)**

* **Apertura (5 min) - *El Entorno Profesional*:** Ingreso al Aula de Informática. Indicación de que hoy actúan como analistas de datos junior enfrentándose a su primer requerimiento técnico con tiempo límite.
* **Actividad Aplicada (40 min) - *Evaluación Práctica*:**
* **El Reto:** Se disponibiliza un dataset crudo (CSV) en MS Teams.
* **Herramientas:** Los estudiantes deben abrir un notebook en Google Colab, importando librerías como Pandas y NumPy para el procesamiento de los datos, o utilizar las funciones de Análisis de Datos en Excel si es su herramienta de preferencia.


* **Entregables requeridos:**
1. Limpieza rápida y generación de tabla descriptiva (`df.describe()` en Python).
2. Generación de un Histograma agrupado y un Boxplot bivariado.
3. Un bloque de texto (Markdown) con dos conclusiones gerenciales interpretando la dispersión.




* **Cierre y Reflexión (5 min):** Carga obligatoria del `.ipynb` o archivo `.xlsx` a la plataforma. Pregunta de salida: *"¿Qué cálculo les tomó más tiempo hacer a mano en las Clases 17 y 18 que hoy resolvieron en un solo segundo?"*.