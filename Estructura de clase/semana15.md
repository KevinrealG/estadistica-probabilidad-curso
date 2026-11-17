Como **Academic Class Designer AI**, he estructurado la planificación de estas tres sesiones de **1 hora (60 minutos) cada una**, aplicando estrictamente los principios de aprendizaje activo, pedagogía universitaria centrada en competencias y el uso de **Google Colab / Python** como herramienta de simulación computacional.

Cada clase aborda un único concepto central con un enfoque práctico y dinámico, evitando la cátedra pasiva.

---

# 📚 PLAN DE CLASE 1: Distribución Binomial

### 📋 1. Información General

* **Tema:** Distribución Binomial (Ensayos de Bernoulli y probabilidad de $x$ éxitos).
* **Curso:** Estadística y Probabilidad (Pregrado Universitario).
* **Competencia:** Modelar fenómenos de conteo de éxitos independientes en procesos discretos mediante la distribución binomial para la toma de decisiones.
* **Resultados de Aprendizaje:** Identificar experimentos de Bernoulli, calcular probabilidades puntuales y acumuladas, e interpretar su comportamiento gráfico en Python.
* **Nivel de Estudiantes:** Pregrado (Ingeniería / Administración).
* **Duración:** 60 minutos.
* **Modalidad:** Presencial (Aula de informática / Computadores portátiles).
* **Software:** Google Colab (`scipy.stats.binom`, `matplotlib`).

---

### ⏱️ 2. Estructura de la Sesión (60 Minutos)

#### a) Apertura (8 min) — *El Reto de las Llamadas de Ventas*

* **Dinámica:** Se proyecta el escenario de un equipo de telemarketing cuya tasa de cierre de ventas efectiva es del 20% ($p=0.20$). Si un asesor realiza 10 llamadas en el día, se plantean las siguientes **preguntas motivadoras**:
1. *"Si la tasa es del 20%, ¿es seguro que de 10 llamadas venda exactamente 2?"*
2. *"¿Qué es más probable: no vender nada, vender exactamente 2, o vender las 10?"*
3. *"¿Qué condiciones matemáticas deben cumplirse para que cada llamada sea independiente de la anterior?"*
4. *"¿Cómo cambiaría el riesgo para la empresa si el número de llamadas aumentara a 100?"*



#### b) Exploración (7 min) — *La Intuición del Triángulo y las Combinaciones*

* **Dinámica:** En parejas, los estudiantes discuten cómo calcularían las formas posibles en que ocurran 3 ventas específicas en 10 llamadas (ej. ventas en la llamada 1, 2 y 3 vs. otras posiciones). Se introducen de forma intuitiva las combinaciones antes de dar la fórmula formal.

#### c) Desarrollo Conceptual (12 min) — *Teoría Mínima y Estructura Binomial*

* **Facilitación ágil:**
* Definición de un **Ensayo de Bernoulli** (dos resultados posibles: éxito/fracaso).
* Supuestos clave de la Binomial: $n$ ensayos idénticos, independencia, probabilidad de éxito $p$ constante.
* Fórmula de la Función de Masa de Probabilidad (PMF):

$$P(X = x) = \binom{n}{x} p^x (1-p)^{n-x}$$


* *Pregunta de verificación rápida:* *"Si $n = 20$ y $p = 0.50$, ¿la distribución de probabilidad será simétrica o sesgada hacia algún lado? ¿Por qué?"*



#### d) Actividad Guiada y Colaborativa (15 min) — *Laboratorio en Google Colab*

* **Dinámica:** Los estudiantes abren un notebook en Google Colab y ejecutan un script guiado para calcular la probabilidad binomial usando `scipy.stats.binom`.
* **Misión:** Graficar la PMF para $n=20$ y $p=0.30$. Modificar el parámetro $p$ a $0.80$ y observar cómo la distribución cambia de sesgada a la derecha a sesgada a la izquierda en tiempo real.

#### e) Aplicación (8 min) — *Control de Calidad en Lotes*

* **Reto contextualizado:** Una fábrica de componentes electrónicos recibe lotes de microchips donde el 5% presenta defectos de soldadura. Si el departamento de calidad inspecciona una muestra aleatoria de 15 chips, el equipo debe calcular la probabilidad de encontrar a lo sumo 2 chips defectuosos utilizando acumuladas (`cdf`).

#### f) Cierre y Reflexión (5 min) — *Metacognición*

* **Pregunta de reflexión:** *"Si en un problema real los ensayos no fueran independientes (por ejemplo, extraer cartas de una baraja sin reemplazo), ¿por qué fallaría el modelo binomial y qué distribución deberíamos usar en su lugar?"* *(Prohibido cerrar con "¿Alguna pregunta?").*

#### g) Actividad Final de Consolidación (5 min) — *Ticket de Salida*

* Mini-quiz digital de 3 preguntas de opción múltiple en la plataforma SAVIO sobre identificación de parámetros $n$ y $p$ y cálculo conceptual de valor esperado ($E(X) = n \cdot p$).

---

# 📚 PLAN DE CLASE 2: Distribución de Poisson

### 📋 1. Información General

* **Tema:** Distribución de Poisson (Conteo de eventos raros en intervalos de tiempo o espacio).
* **Curso:** Estadística y Probabilidad (Pregrado Universitario).
* **Competencia:** Modelar la tasa de ocurrencia de eventos discretos independientes en un intervalo continuo utilizando la distribución de Poisson para la gestión de riesgos.
* **Resultados de Aprendizaje:** Calcular probabilidades de eventos raros usando el parámetro $\lambda$, interpretar tasas de intensidad y simular el modelo en Python.
* **Nivel de Estudiantes:** Pregrado (Ingeniería / Administración).
* **Duración:** 60 minutos.
* **Modalidad:** Presencial (Aula de informática).
* **Software:** Google Colab (`scipy.stats.poisson`).

---

### ⏱️ 2. Estructura de la Sesión (60 Minutos)

#### a) Apertura (8 min) — *El Reto del Call Center*

* **Dinámica:** Se plantea el caso de una central de atención médica que recibe en promedio 4 llamadas de emergencia cada 15 minutos ($\lambda = 4$). Se lanzan las siguientes **preguntas motivadoras**:
1. *"Si el promedio es 4 llamadas por cuarto de hora, ¿significa que en cada cuarto de hora exacto recibiremos siempre 4 llamadas?"*
2. *"¿Cuál es la probabilidad de que en los próximos 15 minutos no entre ninguna llamada?"*
3. *"¿Qué diferencia fundamental hay entre la distribución Binomial y la de Poisson si ambas manejan datos discretos (conteo)?"*
4. *"¿Por qué decimos que Poisson modela 'eventos raros' o tasas en el tiempo?"*



#### b) Exploración (7 min) — *El Límite de la Binomial*

* **Dinámica:** Discusión breve en pizarra: ¿Qué pasa si intentamos usar una Binomial para modelar cuántos autos pasan por un peaje en una hora? (Aquí $N$ es enorme y desconocido, pero $p$ es muy pequeño). Se introduce a Poisson como el límite matemático de la Binomial.

#### c) Desarrollo Conceptual (12 min) — *Teoría Mínima de Poisson*

* **Facilitación ágil:**
* Definición del parámetro de intensidad o tasa media: $\lambda$ (lambda).
* Supuestos: Los eventos ocurren de manera independiente, la tasa media es constante y dos eventos no pueden ocurrir exactamente en el mismo instante infinitesimal.
* Fórmula de la PMF:

$$P(X = x) = \frac{e^{-\lambda} \lambda^x}{x!}$$


* Propiedad fundamental: En la distribución de Poisson, la media y la varianza son exactamente iguales ($\mu = \sigma^2 = \lambda$).
* *Pregunta de verificación:* *"Si en un servidor web la tasa media de errores es $\lambda = 3$ errores por hora, ¿cuánto vale la varianza de esa variable?"*



#### d) Actividad Guiada y Colaborativa (15 min) — *Simulación de Tasas en Colab*

* **Dinámica:** En Google Colab, los estudiantes parametrizan la función `scipy.stats.poisson(mu=lambda)`.
* **Misión:** Simular el comportamiento de las fallas de un servidor con $\lambda = 2.5$. Calcular la probabilidad exacta de tener 0 fallas, 1 falla y más de 3 fallas, visualizando el gráfico de barras de la distribución.

#### e) Aplicación (8 min) — *Optimización de Servidores y Tráfico*

* **Reto contextualizado:** Una empresa de logística analiza la llegada de camiones a un centro de distribución a razón de 5 camiones por hora. El gerente de operaciones necesita saber cuál es la probabilidad de que lleguen más de 8 camiones en una hora dada para dimensionar el personal de muelle.

#### f) Cierre y Reflexión (5 min) — *Metacognición*

* **Pregunta de reflexión:** *"Si duplicamos el intervalo de observación de 1 hora a 2 horas, ¿qué le ocurre al parámetro $\lambda$ y cómo afecta esto a la probabilidad de ocurrencia de los eventos?"*

#### g) Actividad Final de Consolidación (5 min) — *Ticket de Salida*

* Mini-quiz digital en SAVIO evaluando el cálculo conceptual de Poisson y la propiedad de igualdad entre media y varianza.

---

# 📚 PLAN DE CLASE 3: Distribución de Variables Aleatorias Continuas

### 📋 1. Información General

* **Tema:** Variables Aleatorias Continuas y Función de Densidad de Probabilidad (PDF).
* **Curso:** Estadística y Probabilidad (Pregrado Universitario).
* **Competencia:** Analizar modelos probabilísticos de variables continuas mediante funciones de densidad y cálculo de áreas bajo la curva para resolver problemas de ingeniería y control de procesos.
* **Resultados de Aprendizaje:** Comprender la transición de lo discreto a lo continuo, calcular probabilidades mediante integrales (áreas) y utilizar herramientas computacionales para su visualización.
* **Nivel de Estudiantes:** Pregrado (Ingeniería / Administración).
* **Duración:** 60 minutos.
* **Modalidad:** Presencial (Aula de informática).
* **Software:** Google Colab (`scipy.stats.uniform` o exponencial, `matplotlib`).

---

### ⏱️ 2. Estructura de la Sesión (60 Minutos)

#### a) Apertura (8 min) — *El Reto de la Medición Exacta*

* **Dinámica:** Se proyecta la imagen de una báscula industrial de alta precisión que mide el peso de sacos de cemento (variable continua). Se plantean las **preguntas motivadoras**:
1. *"Si el peso puede tomar infinitos valores decimales, ¿cuál es la probabilidad exacta de que un saco pese exactamente 50.0000000 kg?"*
2. *"Si la probabilidad de un punto exacto es cero, ¿cómo calculamos entonces la probabilidad de que un saco pese **entre** 49.5 y 50.5 kg?"*
3. *"¿Por qué ya no podemos usar sumas (como en las variables discretas) y necesitamos usar áreas bajo una curva?"*
4. *"¿Qué condiciones debe cumplir una función matemática para poder ser considerada una función de densidad de probabilidad (PDF)?"*



#### b) Exploración (7 min) — *Del Histograma a la Curva Suave*

* **Dinámica:** Discusión en pizarra sobre cómo al aumentar el número de datos en un histograma y reducir el ancho de las barras, los escalones se convierten en una curva continua tersa. Se introduce el concepto de la integral como el acumulador de área.

#### c) Desarrollo Conceptual (12 min) — *Teoría Mínima de Variables Continuas*

* **Facilitación ágil:**
* Definición de **Variable Aleatoria Continua** y su Función de Densidad de Probabilidad $f(x)$ (PDF).
* Las dos reglas de oro de toda PDF:
1. $f(x) \ge 0$ para todo $x$ (la curva nunca va por debajo del eje $x$).
2. El área total bajo la curva debe ser exactamente 1 ($\int_{-\infty}^{\infty} f(x) dx = 1$).


* Cálculo de probabilidad como área en un intervalo $[a, b]$:

$$P(a \le X \le b) = \int_a^b f(x) dx$$


* Introducción a la Función de Distribución Acumulada (CDF): $F(x) = P(X \le x)$.
* *Pregunta de verificación:* *"Si el área total bajo una curva de densidad es 1, ¿puede una función de densidad $f(x)$ tomar un valor superior a 1 en un punto específico?"* (Respuesta esperada: Sí, porque la altura es densidad, no probabilidad; lo que no puede superar 1 es el área acumulada).



#### d) Actividad Guiada y Colaborativa (15 min) — *Visualizando Áreas en Google Colab*

* **Dinámica:** Los estudiantes utilizan un notebook en Google Colab para trabajar con una distribución continua sencilla (por ejemplo, una distribución uniforme continua o exponencial).
* **Misión:** Graficar la función de densidad con `matplotlib` y utilizar funciones de integración numérica o la función acumulada (`cdf`) de `scipy.stats` para calcular y sombrear el área exacta de probabilidad entre dos puntos de corte dados.

#### e) Aplicación (8 min) — *Tiempos de Espera en Logística*

* **Reto contextualizado:** El tiempo de entrega (en horas) de un proveedor internacional sigue un modelo de distribución continua uniforme entre 2 y 6 días. El equipo de compras debe calcular la probabilidad de que un pedido llegue en menos de 3.5 días utilizando el cálculo geométrica del área bajo la recta de densidad.

#### f) Cierre y Reflexión (5 min) — *Metacognición*

* **Pregunta de reflexión:** *"¿Por qué conceptualmente es un error grave intentar calcular $P(X = c)$ en una variable continua, a diferencia de lo que hacíamos con las variables discretas?"*

#### g) Actividad Final de Consolidación (5 min) — *Ticket de Salida*

* Mini-quiz digital en SAVIO evaluando las dos propiedades fundamentales de una PDF (no negatividad y área total igual a 1).