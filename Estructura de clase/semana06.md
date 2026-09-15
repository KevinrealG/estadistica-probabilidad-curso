### 📋 Información General del Eje (Bivariado: Relaciones y Dependencia)

* **Curso:** Estadística y Probabilidad (CBAS-E01A).


* **Duración:** 4 sesiones de 50 minutos cada una, modalidad presencial.
* **Temática:** Análisis bivariado preliminar (Cualitativa vs. Cuantitativa), Diagramas de dispersión y Covarianza.

---

### 📊 Clase N°1: Análisis Bivariado (Cualitativa vs. Cuantitativa)
```python
import pandas as pd
import io

data = """CURSO	EXAMEN1
ESTADÍSTICA Y PROBABILIDAD	3.4
ESTADÍSTICA Y PROBABILIDAD	4.3
ESTADÍSTICA Y PROBABILIDAD	1.5
ESTADÍSTICA Y PROBABILIDAD	2.3
ESTADÍSTICA Y PROBABILIDAD	3.5
ESTADÍSTICA Y PROBABILIDAD	4.3
ESTADÍSTICA Y PROBABILIDAD	3.6
ESTADÍSTICA Y PROBABILIDAD	3.5
ESTADÍSTICA Y PROBABILIDAD	3.2
ESTADÍSTICA Y PROBABILIDAD	3.3
ESTADÍSTICA Y PROBABILIDAD	2.9
ESTADÍSTICA Y PROBABILIDAD	4.1
ESTADÍSTICA Y PROBABILIDAD	3.0
ESTADÍSTICA Y PROBABILIDAD	4.1
ESTADÍSTICA Y PROBABILIDAD	3.3
ESTADÍSTICA Y PROBABILIDAD	4.2
ESTADÍSTICA Y PROBABILIDAD	3.8
ESTADÍSTICA Y PROBABILIDAD	2.5
ESTADÍSTICA Y PROBABILIDAD	4.1
ESTADÍSTICA Y PROBABILIDAD	4.1
ESTADÍSTICA Y PROBABILIDAD	1.8
ESTADÍSTICA Y PROBABILIDAD	5.0
ESTADÍSTICA Y PROBABILIDAD	3.2
ESTADÍSTICA Y PROBABILIDAD	3.9
ESTADÍSTICA Y PROBABILIDAD	2.4
ESTADÍSTICA Y PROBABILIDAD	2.9
ESTADÍSTICA Y PROBABILIDAD	4.0
ESTADÍSTICA Y PROBABILIDAD	3.7
ESTADÍSTICA Y PROBABILIDAD	3.7
ESTADÍSTICA Y PROBABILIDAD	3.7
ESTADÍSTICA Y PROBABILIDAD	3.8
ESTADÍSTICA Y PROBABILIDAD	2.6
ESTADÍSTICA Y PROBABILIDAD	2.7
ESTADÍSTICA Y PROBABILIDAD	2.0
ESTADÍSTICA Y PROBABILIDAD	3.5
ESTADÍSTICA Y PROBABILIDAD	3.1
ESTADÍSTICA Y PROBABILIDAD	4.7
ESTADÍSTICA Y PROBABILIDAD	2.7
ESTADÍSTICA Y PROBABILIDAD	4.3
ESTADÍSTICA Y PROBABILIDAD	4.3
ESTADÍSTICA INFERENCIAL	1.5
ESTADÍSTICA INFERENCIAL	3.7
ESTADÍSTICA INFERENCIAL	5.0
ESTADÍSTICA INFERENCIAL	5.0
ESTADÍSTICA INFERENCIAL	2.0
ESTADÍSTICA INFERENCIAL	3.8
ESTADÍSTICA INFERENCIAL	4.7
ESTADÍSTICA INFERENCIAL	3.6
ESTADÍSTICA INFERENCIAL	2.1
ESTADÍSTICA INFERENCIAL	5.0
ESTADÍSTICA INFERENCIAL	2.3
ESTADÍSTICA INFERENCIAL	5.0
ESTADÍSTICA INFERENCIAL	2.6
ESTADÍSTICA INFERENCIAL	3.6
ESTADÍSTICA INFERENCIAL	4.0
ESTADÍSTICA INFERENCIAL	4.2
ESTADÍSTICA INFERENCIAL	2.5
ESTADÍSTICA INFERENCIAL	4.3
ESTADÍSTICA INFERENCIAL	2.5
ESTADISTICA II	2.4
ESTADISTICA II	2.7
ESTADISTICA II	3.3
ESTADISTICA II	4.4
ESTADISTICA II	2.5
ESTADISTICA II	3.1
ESTADISTICA II	2.9
ESTADISTICA II	1.5
ESTADISTICA II	2.9
ESTADISTICA II	1.5
ESTADÍSTICA I	3.3
ESTADÍSTICA I	1.6
ESTADÍSTICA I	2.3
ESTADÍSTICA I	2.1
ESTADÍSTICA I	3.4
ESTADÍSTICA I	2.0
ESTADÍSTICA I	2.7
ESTADÍSTICA I	3.5
ESTADÍSTICA I	2.3
ESTADÍSTICA I	2.6
ESTADÍSTICA I	2.5
ESTADÍSTICA I	2.3
ESTADÍSTICA I	2.9
ESTADÍSTICA I	2.8
ESTADÍSTICA I	4.3
ESTADÍSTICA I	3.9
ESTADÍSTICA I	2.0
ESTADÍSTICA I	3.8
ESTADÍSTICA I	1.2
ESTADÍSTICA I	3.2"""

df = pd.read_csv(io.StringIO(data), sep='\t')
summary = df.groupby('CURSO')['EXAMEN1'].agg(['count', 'mean', 'median', 'min', 'max', 'std']).round(2)
print(summary)


```

```text
                            count  mean  median  min  max   std
CURSO                                                          
ESTADISTICA II                 10  2.72    2.80  1.5  4.4  0.85
ESTADÍSTICA I                  20  2.74    2.65  1.2  4.3  0.80
ESTADÍSTICA INFERENCIAL        19  3.55    3.70  1.5  5.0  1.16
ESTADÍSTICA Y PROBABILIDAD     40  3.42    3.50  1.5  5.0  0.80


```

Aquí tienes el diseño instruccional detallado para la primera sesión del análisis bivariado, estructurado rigurosamente bajo la metodología de aprendizaje activo.

He procesado previamente tu conjunto de datos para garantizar que los tiempos de la actividad en clase sean exactos. Los resultados reales (que tus estudiantes descubrirán) son:

* **Estadística Inferencial:** Media 3.55 (Alta dispersión, $s = 1.16$)
* **Estadística y Probabilidad:** Media 3.42 (Baja dispersión, $s = 0.80$)
* **Estadística I:** Media 2.74 ($s = 0.80$)
* **Estadística II:** Media 2.72 ($s = 0.85$)

---

### 📋 Información General

* **Tema:** Análisis Bivariado (Variable Cualitativa vs. Variable Cuantitativa).
* **Curso:** Estadística y Probabilidad.
* **Competencia:** Comparar el comportamiento y distribución de una variable cuantitativa segmentada por categorías para identificar diferencias estructurales.
* **Duración:** 50 minutos.
* **Modalidad:** Presencial (Aula tradicional o Aula de Informática).
* **Software sugerido:** Excel o Python (Pandas).

---

### ⏱️ Estructura de la Sesión (50 Minutos)

**1. Apertura (7 min) - *El Marcador del Rendimiento***

* **Reto Inicial:** Inicia la sesión proyectando un tablero de puntuación vacío. Plantea el siguiente escenario gerencial: *"La universidad va a otorgar becas a los mejores estudiantes para un semillero de investigación avanzada. Si tuvieran que elegir un solo curso como 'cantera' de talentos, ¿a cuál de los cuatro cursos de estadística irían a reclutar?"*.
* **Preguntas Detonantes:**
1. ¿Es estadísticamente justo comparar un 3.5 obtenido en 'Estadística I' con un 3.5 en 'Estadística Inferencial'?
2. ¿El éxito en un examen depende netamente de la preparación individual o existe un "efecto de curso"?



**2. Exploración (5 min) - *Hipótesis Estudiantil***

* Muestra brevemente en pantalla la imagen **image_d1aba5.png** para que los estudiantes se enfrenten visualmente a los datos crudos.
* Pide que, a simple vista y sin hacer cálculos, voten a mano alzada cuál curso creen que tuvo el desempeño más alto y cuál el más crítico. Registra la hipótesis ganadora en el tablero.

**3. Desarrollo Conceptual (8 min) - *Teoría Mínima***

* **Concepto Core:** Explica la **Segmentación de Datos** (Data Slicing). Define cómo una variable cualitativa (el nombre del curso) actúa como un filtro o "molde" que nos permite agrupar y analizar una variable cuantitativa (la nota del examen).
* **Pregunta de Verificación:** *"Si en un proyecto de grado queremos evaluar si el salario de los egresados depende de su género, ¿cuál variable es la que segmenta y cuál es la que se mide?"*

**4. Actividad Guiada y Colaborativa (15 min) - *Desmintiendo la Intuición***

* Divide el salón en cuatro grandes grupos. Asigna a cada grupo un curso específico del set de datos.
* **La Misión:** Utilizando Excel (filtros y función `PROMEDIO` / `DESVEST.M`) o un script rápido de Python con la función `groupby()`, cada equipo debe calcular la **Media** y la **Desviación Estándar** de su curso asignado.
* Pide a un representante de cada equipo que pase al frente y anote sus resultados en el "Marcador" vacío de la pizarra.

**5. Aplicación (7 min) - *El Análisis del Cuarto Bate***

* Con los resultados reales revelados, lanza un nuevo reto interpretativo.
* **El dilema:** *"Noten que 'Estadística Inferencial' tiene el promedio más alto (3.55), pero también el rendimiento más errático y caótico de todos ($s = 1.16$, notas desde 1.5 hasta 5.0). Por otro lado, 'Estadística y Probabilidad' es sumamente constante (media 3.42, $s = 0.80$)."*
* **Discusión:** *"Como directores de programa, ¿qué escenario les preocupa más: un curso de promedios altos pero caótico (Inferencial), o un curso de promedios bajos pero donde todos rinden exactamente igual (Estadística I)?"*

**6. Cierre y Reflexión (5 min) - *Metacognición***

* **Pregunta de reflexión proyectada antes de salir:** *"Si un analista perezoso solo hubiera calculado el promedio global de los 89 estudiantes juntos (que es de 3.24), ¿qué patrón crítico de esta universidad nos habría ocultado?"*

**7. Actividad Final de Consolidación (3 min) - *Ticket de Salida***

* Para evaluar el aprendizaje de la sesión, solicita que escriban en un papel (o mediante un formulario corto en Teams) lo siguiente:
* *Redacta una conclusión de máximo 2 líneas explicando si tu intuición inicial al ver los datos crudos coincidió con la realidad matemática descubierta hoy.*

* **1. Información General:**
* **Objetivo:** Comparar el comportamiento de una variable numérica a través de diferentes categorías (ej. Salario vs. Género o Programa Académico).


* **2. Estructura de la Sesión (50 min):**
* **Apertura (8 min):** Proyectar dos grupos de datos de notas de la UTB divididos por facultad. Pregunta: *"¿Tienen el mismo rendimiento académico todas las ingenierías por igual o hay diferencias estructurales?"*.
* **Exploración (7 min):** Discusión en parejas sobre cómo comparar visualmente dos distribuciones numéricas separadas por categorías.
* **Desarrollo Conceptual (10 min):** Introducción al cruce de variables (Cualitativa + Cuantitativa). Uso de estadísticos condicionados por grupo (Media y Mediana por categoría).
* **Actividad Guiada (15 min):** En hojas de cálculo o calculadora, agrupan un subconjunto de datos para hallar la media de una variable numérica filtrada por categoría.
* **Aplicación (5 min):** Plantear una hipótesis de negocio (ej. *"¿El estrato socioeconómico afecta el promedio acumulado?"*).
* **Cierre y Consolidación (5 min):** Pregunta de salida digital (Form): *"¿Por qué comparar solo la media global de la universidad oculta las diferencias reales entre facultades?"*.



---

### 📈 Clase N°2: Diagramas de Dispersión (Dos Variables Cuantitativas)

* **1. Información General:**
* **Objetivo:** Visualizar y determinar gráficamente la relación o tendencia entre dos variables cuantitativas continuas.


* **2. Estructura de la Sesión (50 min):**
* **Apertura (8 min):** Mostrar un gráfico de Estatura vs. Peso sin línea de tendencia. Pregunta: *"Si una persona es más alta, ¿pesa necesariamente más? ¿Cómo podemos ver esa pareja de datos en un plano cartesiano?"*.
* **Exploración (7 min):** Trazar puntos en la pizarra de forma intuitiva a partir de 5 pares de datos dictados por el salón.
* **Desarrollo Conceptual (10 min):** Anatomía del Diagrama de Dispersión (Eje X, Eje Y, pares ordenados $(x_i, y_i)$).
Diagrama de puntos dispersos
Podemos trazar un diagrama de puntos dispersos localizando un punto por cada par de dos
variables que representan una observación del conjunto de datos. El diagrama de puntos dispersos
es una representación de los datos, que comprende lo siguiente:
1) El rango de cada variable.
2) La pauta de valores existente dentro del rango.
3) Una sugerencia sobre la posible relación entre las dos variables.
4) Una indicación de los casos atípicos (puntos extremos).
* **Actividad Guiada (15 min):** Construcción manual rápida de un diagrama de dispersión en papel milimetrado o Excel usando 15 registros de la base de datos UTB (ej. Horas de estudio vs. Calificación).
* **Aplicación (5 min):** Analizar si existe un clúster o patrón atípico visual en el gráfico.
* **Cierre y Consolidación (5 min):** Miniquiz (3 preguntas de opción múltiple en pantalla): Identificar el tipo de correlación visual a partir de imágenes de scatter plots.



---

### 📉 Clase N°3: Covarianza (Midiendo la Variación Conjunta)

* **1. Información General:**
* **Objetivo:** Calcular e interpretar analíticamente la covarianza para determinar si dos variables crecen o decrecen juntas.


* **2. Estructura de la Sesión (50 min):**
* **Apertura (8 min):** Retomar el gráfico de dispersión anterior. *"Vimos que los puntos suben juntos, pero ¿cómo le ponemos un número a esa 'fuerza' de compañía?"*.
* **Exploración (7 min):** Analizar el producto de las desviaciones respecto a la media $(x_i - \bar{x})(y_i - \bar{y})$ en cuadrantes del plano cartesiano.
* **Desarrollo Conceptual (10 min):** Fórmula de la Covarianza muestral ($S_{xy}$). Significado de su signo: Positivo (crecen juntas), Negativo (inversas), Cero (independencia lineal aparente). Limitación de la escala.
* **Actividad Guiada (15 min):** Resolución en parejas de una tabla guiada de 5 pares de datos para calcular paso a paso la covarianza.
* **Aplicación (5 min):** Discutir por qué la covarianza por sí sola es difícil de interpretar sin conocer las unidades de medida originales de las variables.
* **Cierre y Consolidación (5 min):** Pregunta de reflexión escrita: *"Si cambiamos la unidad de medida de los salarios de millones a pesos, ¿qué le ocurre al valor numérico de la covarianza?"*.



---

### 🧪 Clase N°4: Laboratorio 5 - Análisis Bivariado Inicial y Retroalimentación

* **1. Información General:**
* **Objetivo:** Ejecutar la fase de análisis bivariado preliminar (Scatter plots y Covarianza) utilizando software especializado y recibir retroalimentación del proceso formativo previo.


* **2. Estructura de la Sesión (50 min):**
* **Apertura (5 min):** Entrega de notas / retroalimentación general de los aciertos y errores comunes del primer bloque de evaluaciones de corte.
* **Exploración y Configuración (5 min):** Apertura de herramientas digitales (Excel, Google Colab o Statgraphics) con el dataset institucional.
* **Actividad Práctica / Laboratorio (30 min):**
1. Generar diagramas de dispersión cruzando dos variables cuantitativas de la base UTB.
2. Calcular la covarianza mediante funciones de software (`COVARIANCE.S` en Excel o `df.cov()` en Python).
3. Redactar dos conclusiones descriptivas sobre la relación hallada.


* **Cierre y Consolidación (10 min):** Subida del entregable corto a MS Teams y cierre motivacional del inicio del segundo bloque temático.