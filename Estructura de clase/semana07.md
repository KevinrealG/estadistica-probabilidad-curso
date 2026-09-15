Como **Academic Class Designer AI**, y asumiendo la duración estándar de **50 minutos por sesión** para el curso de Estadística y Probabilidad (UTB), he estructurado esta semana bajo los principios de aprendizaje activo, pensamiento crítico y análisis visual.

---

### 📋 Información General del Eje (Semana - Correlación y Asociación)

* **Curso:** Estadística y Probabilidad (CBAS-E01A).


* **Modalidad:** Presencial con apoyo digital (Excel / Google Colab).
* **Competencia:** Analizar la relación bivariada entre variables cuantitativas mediante descriptores de asociación para la toma de decisiones informadas.



---

### 📊 Clase N°1: Introducción a la Correlación Lineal

#### a) Información General

* **Objetivo:** Distinguir conceptualmente entre asociación, dependencia y correlación lineal a través del análisis visual de nubes de puntos.
* **Recursos:** Diapositivas, plataforma MS Teams, applet visual de dispersión.

#### b) Apertura (8 min) - *El Reto*

* Proyecta un gráfico real de "Venta de helados vs. Incendios forestales" o "Consumo de chocolate vs. Premios Nobel por país".
* **Preguntas motivadoras (3):**
1. *"Si los datos suben juntos en el gráfico, ¿significa obligatoriamente que uno causa al otro?"*
2. *"¿Cómo definirían con sus propias palabras la 'fuerza' de una relación entre dos variables?"*



#### c) Exploración (7 min)

* Pide a los estudiantes que dibujen en un papel dos variables imaginarias que crean que están correlacionadas negativamente (ej. Horas de fiesta vs. Nota del parcial). Comparten su hipótesis en parejas.

#### d) Desarrollo Conceptual (10 min)

* **Teoría mínima:** Definición de correlación lineal (fuerza, dirección y forma). Diferencia entre dependencia determinista y asociación estadística.
* **Pregunta de verificación:** *"Si los puntos forman un círculo perfecto sin inclinación, ¿la correlación es cero o es alta?"*.

#### e) Actividad Guiada y Colaborativa (15 min)

* En grupos de 3, los estudiantes analizan 4 tarjetas (ir a colab) con diagramas de dispersión diferentes (proyectadas en pantalla) y deben clasificar cualitativamente la fuerza de la correlación (Fuerte, Moderada, Débil, Nula).

#### f) Aplicación (5 min)

* Plantear un escenario de ingeniería o negocios: *"En un proceso de manufactura, si la temperatura del horno sube y la resistencia del material baja de forma alineada, ¿cómo describirían esta correlación para el control de calidad?"*.

#### g) Cierre y Reflexión (5 min)

* **Pregunta metacognitiva:** *"¿Por qué una correlación lineal puede fallar si la verdadera relación entre los datos es una curva?"*. (Prohibido el "¿Alguna pregunta?").

#### h) Actividad Final de Consolidación (3 min)

* Mini-quiz digital de 3 preguntas de opción múltiple (vía Forms/Teams) sobre identificación visual de correlaciones.

---

### 📈 Clase N°2: Covarianza y Coeficiente de Correlación Lineal ($r$ de Pearson)

#### a) Información General

* **Objetivo:** Calcular e interpretar el coeficiente de correlación lineal de Pearson ($r$) conectándolo con la covarianza y su representación en diagramas de dispersión.
* **Recursos:** Calculadoras, Excel / Google Colab con bases de datos UTB.

#### b) Apertura (8 min) - *El Reto*

* Muestra dos diagramas de dispersión con la misma tendencia positiva, pero uno medido en metros/kilogramos y otro en centímetros/gramos.
* **Preguntas motivadoras (3):**
1. *"Si cambiamos las unidades de medida, ¿cambia la realidad de la relación entre las variables?"*
2. *"¿Por qué la covarianza por sí sola no nos sirve para comparar qué tan fuerte es una relación?"*
3. *"¿Cómo logramos estandarizar esa medida para que siempre esté entre -1 y 1?"*



#### c) Exploración (7 min)

* Debate relámpago: Discutir intuitivamente qué valor numérico le darían a una correlación perfecta y a una ausencia total de correlación basándose en una escala de -1 a 1.

#### d) Desarrollo Conceptual (10 min)

* **Teoría mínima:** Relación matemática entre Covarianza y Desviaciones Estándar. Fórmula conceptual del Coeficiente de Correlación de Pearson ($r$). Propiedades clave: acotación entre -1 y 1, adimensionalidad.
* **Pregunta de verificación:** *"Si $r = -0.95$, ¿la relación es débil o fuerte? ¿Hacia dónde se inclina?"*.

#### e) Actividad Guiada y Colaborativa (15 min)

* En parejas, utilizando Excel o la herramienta *Bachué Data Toolbox*, calculan el coeficiente $r$ de Pearson para un subconjunto de 15 datos de la base institucional (ej. Estatura vs. Peso) y visualizan el gráfico generado automáticamente.

#### f) Aplicación (5 min)

* Análisis de un reporte financiero con $r = 0.12$: *"Un analista afirma que hay una fuerte relación porque el software dio un número positivo. ¿Qué le responderían técnicamente?"*.

#### g) Cierre y Reflexión (5 min)

* **Pregunta metacognitiva:** *"¿Qué nos dice el signo de $r$ que no nos dice el gráfico de dispersión por sí solo?"*.

#### h) Actividad Final de Consolidación (3 min)

* Subida de una captura del gráfico con su respectivo valor de $r$ calculado al canal de MS Teams.

---

### 📉 Clase N°3: Más Allá del Número: Causación y Variables Ocultas

#### a) Información General

* **Objetivo:** Desarrollar pensamiento crítico frente a la interpretación de coeficientes de correlación altos, identificando falacias de causación y variables confusoras u ocultas.
* **Recursos:** Casos de estudio reales (ej. "Spurious Correlations").

#### b) Apertura (8 min) - *El Reto*

* Proyecta un caso real divertido y verídico: *"Existe una correlación de $r = 0.94$ entre las ventas anuales de piscinas en una ciudad y el número de ataques de tiburón reportados"*.
* **Preguntas motivadoras (3):**
1. *"¿Comprar una piscina atrae a los tiburones a la orilla?"*
2. *"Si $r$ es altísimo y cercano a 1, ¿por qué decimos que esto es un absurdo lógico?"*
3. *"¿Qué variable oculta no estamos viendo en esta ecuación?"*



#### c) Exploración (7 min)

* Plenaria rápida: Los estudiantes discuten qué factor común (variable oculta) explicaría el caso de las piscinas y los tiburones (Pista: El clima/verano y el turismo).

#### d) Desarrollo Conceptual (10 min)

* **Teoría mínima:** La máxima estadística: *"La correlación no implica causación"*. Definición de variables confusoras, variables ocultas (lurking variables) y correlaciones espurias.
* **Pregunta de verificación:** *"Si encuentro que el número de bomberos en un incendio se correlaciona fuertemente con la magnitud de los daños, ¿debemos despedir a los bomberos para reducir los daños?"*.

#### e) Actividad Guiada y Colaborativa (15 min)

* Trabajo en grupos. Se entrega a cada equipo una correlación falsa o curiosa del mundo real. Deben debatir e inventar la **variable oculta** que explica el fenómeno y redactar un contraargumento analítico.

#### f) Aplicación (5 min)

* Simulación de un comité directivo: Un gerente quiere tomar una decisión estratégica millonaria basándose únicamente en una correlación estadística simple. El grupo debe redactar una advertencia basada en riesgos de variables ocultas.

#### g) Cierre y Reflexión (5 min)

* **Pregunta metacognitiva:** *"¿Cómo puede un buen analista de datos comprobar si una relación es causal y no una simple coincidencia numérica?"*.

#### h) Actividad Final de Consolidación (3 min)

* Evaluación formativa final del eje: Redacción individual de un párrafo de viñeta crítica sobre un gráfico de correlación falaz expuesto en el aula.