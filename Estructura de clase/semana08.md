### 📋 Ficha Técnica de la Sesión

* **Curso:** Estadística y Probabilidad (CBAS-E01A).
* **Tema:** Regresión Lineal Simple (El Salto a la Matemática).
* **Competencia:** Formular modelos matemáticos preliminares a partir de datos bivariados empíricos para realizar predicciones.
* **Objetivo de Aprendizaje:** Comprender la diferencia entre correlación (fuerza) y regresión (ecuación matemática), y utilizar la regresión lineal para estimar valores futuros.
* **Duración:** 50 minutos.
* **Modalidad:** Presencial.
* **Software y Recursos:** Proyector, Excel o Python (Google Colab), y un dataset sencillo de 20 registros.

---

### ⏱️ Estructura Detallada de la Sesión (50 Minutos)

#### a) Información General

Esta sesión marca un punto de inflexión cognitivo para el estudiante: pasamos de simplemente "describir" un fenómeno (estadística descriptiva) a "predecir" el futuro (modelado estadístico). El enfoque abandona el cálculo manual tedioso para centrarse en la interpretación visual y lógica de la línea recta.

#### b) Apertura (8 min) - *El Reto de la Predicción*

* **Dinámica:** Proyecta un diagrama de dispersión que muestre la relación entre el número de flexiones y el número de abdominales que puede hacer un grupo de estudiantes. Informa que el coeficiente de correlación es alto ($r = 0.84$).


* **Preguntas motivadoras (Para debate relámpago):**
1. *"Sabemos que la relación es fuerte, pero si ingresa un estudiante nuevo y sabemos que puede hacer exactamente 28 flexiones, ¿cuántas abdominales predecimos que hará?"*.


2. *"¿Nos sirve el coeficiente 0.84 para calcular ese número exacto?"*.


3. *"¿Qué necesitamos trazar en este gráfico para poder 'adivinar' valores que no están en nuestra muestra?"*



#### c) Exploración (7 min) - *Dibujando el Futuro*

* **Dinámica:** Entrega a los estudiantes (en parejas) el diagrama de dispersión impreso o proyéctalo para que lo abran en Paint/herramientas de recorte.
* **Misión:** Pídeles que tracen a mano alzada la línea recta que, según su intuición, cruce mejor por el centro de la nube de datos, y que la utilicen visualmente para adivinar el número de abdominales para el estudiante de las 28 flexiones. Pide a 3 parejas que compartan su predicción.

#### d) Desarrollo Conceptual (10 min) - *Teoría Mínima*

* **Facilitación ágil (Basado en el texto):**
* **Correlación vs. Regresión:** El coeficiente de correlación solo mide la *fuerza* de la relación, pero no nos habla de la relación matemática (ecuación) entre las dos variables. El **análisis de regresión** es el que encuentra la ecuación de la recta que mejor describe esa relación para realizar predicciones.


* **El Modelo Lineal:** Presentar la ecuación de predicción para la línea recta: $\hat{y} = b_0 + b_1x$.


* **Alternativas No Lineales:** Mostrar visualmente que si los datos tienen forma de curva (como en la figura 3.19), no forzamos una línea recta; existen modelos cuadráticos ($\hat{y} = a + bx + cx^2$) o exponenciales ($\hat{y} = a(b^x)$).




* **Pregunta de verificación rápida:** *"En la ecuación $\hat{y} = b_0 + b_1x$, ¿cuál variable representa el dato que ya conocemos (ej. las flexiones) y cuál representa el futuro que queremos predecir (las abdominales)?"*

#### e) Actividad Guiada y Colaborativa (15 min) - *Hackeando la Recta*

* **Dinámica:** En parejas, los estudiantes abren un pequeño dataset en Excel o Google Colab.
* **Misión Práctica:**
1. Generar el gráfico de dispersión.
2. Activar la opción "Agregar línea de tendencia" (Trendline) en Excel o usar `seaborn.regplot` en Python.
3. Habilitar la opción "Presentar ecuación en el gráfico".
4. Sustituir un valor de $x$ inventado por ellos en la ecuación arrojada por el software para predecir un valor $\hat{y}$.



#### f) Aplicación (5 min) - *El Riesgo en el Mundo Real*

* **Planteamiento del escenario:** *"Un ingeniero de tránsito está diseñando un nuevo sistema de frenado automático. Utiliza la regresión para predecir la distancia requerida para frenar un automóvil con base en su rapidez"*.


* **Pregunta analítica:** *"Si un auto va a 150 km/h y usamos la ecuación para predecir su distancia de frenado, ¿deberíamos programar los sensores esperando que el valor exacto predicho de $\hat{y}$ ocurra con precisión milimétrica?"* (Discusión orientada a entender que por lo general, el valor exacto de $y$ no es predecible, sino una estimación razonablemente cercana).



#### g) Cierre y Reflexión (3 min) - *Metacognición*

* **Pregunta Metacognitiva de Cierre:** *"Si nuestra nube de datos inicial tiene una correlación muy débil ($r = 0.10$), ¿qué tan confiables serán las predicciones que hagamos usando la ecuación de la recta de regresión?"*

#### h) Actividad Final de Consolidación (2 min) - *Ticket de Salida*

* **Evaluación formativa:** Los estudiantes ingresan a Teams/Forms y asocian 3 imágenes de dispersión con su modelo de predicción lógico (Una línea recta ascendente para $\hat{y} = b_0 + b_1x$, una curva en 'U' para el modelo cuadrático, y una nube dispersa sin relación).



Como **Academic Class Designer AI**, he estructurado las sesiones 2 y 3 de esta octava semana. Ambas clases mantienen el factor crítico de **50 minutos** y se centran en el aprendizaje activo, llevando a los estudiantes a "descubrir" la matemática detrás de la regresión y a desarrollar un pensamiento crítico profundo sobre sus límites predictivos.

---

### 📉 Clase N°2: El Método de Mínimos Cuadrados (La Búsqueda del Ajuste Perfecto)

#### a) Información General

* **Curso:** Estadística y Probabilidad (CBAS-E01A).
* **Objetivo de Aprendizaje:** Comprender geométricamente el criterio de mínimos cuadrados y calcular matemáticamente la pendiente ($b_1$) y la ordenada al origen ($b_0$) de la recta de mejor ajuste.


* **Duración:** 50 minutos.
* **Modalidad:** Presencial (Uso de Calculadoras o Excel).

#### b) Apertura (8 min) - *El Reto de las Mil Rectas*

* **Dinámica:** Proyecta la Figura 3.23 (donde hay una recta claramente desajustada y las distancias verticales marcadas).


* **Preguntas motivadoras:**
1. *"Si le pido a 30 de ustedes que dibujen una línea recta a través de una nube de puntos, tendré 30 rectas diferentes. ¿Cómo sabe Excel cuál es la 'ganadora' matemática?"*
2. "Observen las líneas verticales entre los puntos y la recta. Si sumamos todas las distancias positivas (puntos arriba) y las negativas (puntos abajo), ¿qué número creen que obtendremos?"


3. *"¿Por qué la recta de la figura no es la de 'mejor ajuste'?"*.





#### c) Exploración (7 min) - *El Problema del Cero*

* **Dinámica:** Dibuja 3 puntos en la pizarra y traza una recta que pase justo por el medio. Muestra que la distancia del punto superior es $+5$ y la del inferior es $-5$.
* **Reto:** *"Si la suma de los errores es cero, parece un ajuste perfecto. Pero si dibujo una recta completamente horizontal que esté lejísimos pero simétrica, el error también sumará cero. ¿Qué truco matemático usamos para que los signos negativos no cancelen a los positivos?"* (Esperado: Elevar al cuadrado).

#### d) Desarrollo Conceptual (10 min) - *Teoría Mínima*

* **Facilitación ágil:**
* **Criterio de Mínimos Cuadrados:** La recta de mejor ajuste es aquella que hace que la suma de los cuadrados de las distancias $\Sigma(y - \hat{y})^2$ sea tan pequeña como sea posible.


* **Fórmulas de Cálculo:** Conectar con lo aprendido en semanas previas. La pendiente $b_1$ se halla reciclando las sumas de cuadrados de la correlación: $b_1 = \frac{SS(xy)}{SS(x)}$.


* Luego, hallar el punto de anclaje (ordenada al origen $b_0$): $b_0 = \frac{\Sigma y - (b_1 \cdot \Sigma x)}{n}$.




* **Pregunta de verificación:** *"Si la correlación ($r$) es negativa, ¿qué signo obligatorio debe tener la pendiente $b_1$?"*

#### e) Actividad Guiada y Colaborativa (15 min) - *El Motor de Excel al Descubierto*

* **Dinámica:** En parejas. Entrégales los valores pre-calculados de las sumas de cuadrados de un ejercicio anterior de clase (para no perder tiempo sumando a mano).
* **Misión:** Aplicar las ecuaciones 3.6 y 3.7 para calcular $b_1$ y $b_0$ manualmente. Luego, abrir Excel, graficar los mismos 5 puntos de datos, insertar la línea de tendencia y verificar si la ecuación que arroja el software coincide exactamente con su cálculo manual.



#### f) Aplicación (5 min) - *El Costo del Error*

* **Contexto de Ingeniería:** *"En la predicción de demanda de inventarios, la distancia $(y - \hat{y})$ no es solo un trazo en un papel; representa millones de pesos en productos que sobraron o faltaron en bodega. Minimizar ese cuadrado es minimizar pérdidas financieras."*

#### g) Cierre y Reflexión (3 min) - *Metacognición*

* **Pregunta Metacognitiva:** *"¿Por qué castigamos más a un error grande (ej. fallar por 10 unidades) que a dos errores pequeños (fallar por 5 y 5) al usar el criterio de elevar al cuadrado?"*

#### h) Actividad Final de Consolidación (2 min) - *Ticket de Salida*

* Formulario digital de 1 pregunta: Escribir la interpretación práctica del valor de la pendiente $b_1$ (ej. "Por cada unidad que aumenta X, Y aumenta en $b_1$").

---

### 🔮 Clase N°3: Predicciones y el Peligro de la Extrapolación

#### a) Información General

* **Curso:** Estadística y Probabilidad (CBAS-E01A).
* **Objetivo de Aprendizaje:** Realizar predicciones a partir del modelo lineal y evaluar críticamente sus restricciones (dominio muestral, población y tiempo).


* **Duración:** 50 minutos.
* **Modalidad:** Presencial.

#### b) Apertura (8 min) - *El Reto del Absurdo Matemático*

* **Dinámica:** Proyecta la ecuación real de las universitarias: $\hat{y} = -186.5 + 4.71x$ (donde $x$ es estatura en pulgadas y $\hat{y}$ es peso predicho en libras).


* **Preguntas motivadoras:**
1. "Si una estudiante mide 66 pulgadas, predecimos un peso de 124 libras. Pero, ¿qué pasa si analizamos a un bebé recién nacido cuya estatura es 0 pulgadas?"


2. "La matemática dice que el peso sería $-186.5$ libras. ¿Tiene sentido un peso negativo?".


3. *"¿Es la ecuación matemática una ley universal irrompible o tiene fecha de caducidad y límites de uso?"*



#### c) Exploración (7 min) - *Debate de Casos Ciegos*

* **Dinámica:** Divide el salón en 3 sectores. Dales una predicción basada en una recta de mejor ajuste perfecta ($r=0.95$).
* Sector A usa datos de mujeres universitarias para predecir el peso de jugadoras profesionales de baloncesto de la WNBA.


* Sector B usa datos recolectados en 1929 para predecir comportamientos de estudiantes en 2026.


* Pídeles que discutan durante 3 minutos por qué su predicción, aunque matemáticamente perfecta, es un fracaso en la vida real.



#### d) Desarrollo Conceptual (10 min) - *Teoría Mínima: Las 3 Reglas de Oro*

* **Facilitación ágil:** Explicar las restricciones al realizar predicciones:
1. **Límite Poblacional:** La ecuación solo sirve para la población de la que se tomó la muestra.


2. **Límite del Dominio (Peligro de Extrapolación):** Solo es seguro predecir dentro del rango de los datos recolectados (ej. estaturas entre 61 y 69 pulgadas). Predecir el futuro lejano o valores extremos puede ser muy peligroso.


3. **Límite Temporal:** Las poblaciones cambian. Una recta de mejor ajuste de 1929 no se sostiene en la actualidad.




* **Pregunta de verificación:** *"Si mi recta predice ventas de paraguas basada en datos de meses de invierno (diciembre a marzo), ¿por qué es un error usarla para predecir ventas en agosto?"*

#### e) Actividad Guiada y Colaborativa (15 min) - *El Tribunal de los Datos*

* **Dinámica:** En grupos de 4. Se les entregan 3 "Reportes de Consultoría" que utilizan modelos de regresión lineal para justificar inversiones millonarias.
* **Misión:** Actuar como auditores de datos. Cada reporte viola una de las tres restricciones clave (ej. predecir el precio de una casa de 1000 $m^2$ usando datos de apartamentos de 40 a 90 $m^2$). Los grupos deben emitir un veredicto de "Aprobado" o "Rechazado", justificando técnica y lógicamente la restricción violada.

Actividad Guiada y Colaborativa (15 min)
El Tribunal de los Datos

Dinámica: Equipos de 4 estudiantes.

Misión: Actúen como auditores de datos. Cada grupo recibe un reporte de consultoría que utiliza un modelo de regresión lineal para justificar una decisión importante. Analicen el caso y emitan un veredicto de:

✅ Aprobado (el uso del modelo es válido)

❌ Rechazado (el uso del modelo es incorrecto)

Además, deben identificar cuál restricción se viola:

Límite poblacional
Límite del dominio (extrapolación)
Límite temporal

y justificar técnicamente su decisión.

Caso 1. El Centro Comercial Fantasma

Una empresa analizó la relación entre el número de visitantes y las ventas en un centro comercial ubicado en Cartagena.

Los datos utilizados provienen únicamente de sábados y domingos del primer semestre de 2026.

La empresa desarrolló una recta de regresión y concluyó:

"Podemos utilizar este modelo para predecir las ventas de cualquier día de la semana durante todo el año."

Preguntas
¿Aprueba o rechaza el reporte?
¿Qué restricción se está violando?
¿Por qué el modelo podría producir predicciones erróneas?
¿Qué información adicional debería recolectarse?
Caso 2. La Mega Mansión

Una inmobiliaria construyó un modelo para predecir el precio de viviendas.

Los datos utilizados corresponden a apartamentos entre 45 m² y 90 m².

Posteriormente, la empresa utilizó la ecuación para estimar el precio de una mansión de 1.200 m².

La estimación fue presentada a un inversionista como una predicción confiable.

Preguntas
¿Aprueba o rechaza el reporte?
¿Qué restricción se está incumpliendo?
¿Qué significa extrapolar en este contexto?
¿Por qué la predicción puede ser poco confiable?
Caso 3. El Negocio del Helado

Una empresa estudió las ventas de helados durante los meses de diciembre, enero y febrero.

A partir de esos datos creó una ecuación lineal entre temperatura y ventas.

Posteriormente utilizó la ecuación para estimar las ventas de julio, agosto y septiembre.

Preguntas
¿Aprueba o rechaza el reporte?
¿Qué restricción está siendo violada?
¿Qué factores podrían cambiar entre temporadas?
¿Qué datos adicionales serían necesarios para mejorar el modelo?
Caso 4. El Gimnasio Universitario

Un gimnasio construyó una regresión entre horas de entrenamiento y fuerza muscular utilizando únicamente estudiantes universitarios entre 18 y 25 años.

El administrador decidió usar el modelo para predecir el desempeño de adultos mayores entre 60 y 75 años.

Preguntas
¿Aprueba o rechaza el reporte?
¿Qué restricción se incumple?
¿Por qué la población utilizada es diferente?
¿Qué problemas puede generar esta decisión?
Caso 5. La Empresa de Paraguas

Una empresa analizó las ventas de paraguas utilizando datos recolectados entre octubre y marzo.

Después utilizó la recta de regresión para proyectar las ventas en agosto y justificar una inversión millonaria en inventario.

Preguntas
¿Aprueba o rechaza el reporte?
¿Qué restricción se está violando?
¿Por qué las condiciones del mercado pueden ser distintas en agosto?
¿Qué recomendación haría como auditor de datos?
Entregable del grupo

Cada equipo deberá presentar:

Veredicto (Aprobado o Rechazado).
Restricción identificada.
Justificación técnica (máximo 3 argumentos).
Recomendación para corregir el estudio.

Puntaje adicional: si el equipo identifica más de una limitación potencial en el mismo caso y la argumenta correctamente.

#### f) Aplicación (5 min) - *Desastres Reales por Extrapolación*

* **Relato de caso real:** Mencionar brevemente cómo la extrapolación fuera del dominio en modelos de riesgo financiero contribuyó a crisis económicas (asumir que la tendencia de los precios de las viviendas crecería linealmente para siempre sin importar los límites del dominio).

#### g) Cierre y Reflexión (3 min) - *Metacognición*

* **Pregunta Metacognitiva:** *"Las computadoras y los lenguajes de programación siempre nos darán un número al meter un dato en la fórmula de regresión. Como ingenieros y analistas, ¿qué habilidad es más importante: saber programar el cálculo de la recta, o saber cuándo NO usarla?"*

#### h) Actividad Final de Consolidación (2 min) - *Ticket de Salida*

* Mini-quiz rápido (3 preguntas de V/F) evaluando la comprensión sobre extrapolación, dominio de la muestra y vigencia temporal.



---

### 🖥️ Estructura Sugerida de Diapositivas para Ambas Clases

**Para la Clase N°2 (Mínimos Cuadrados):**

1. **El Torneo de las Rectas:** Visual de múltiples rectas cruzando los mismos puntos.
2. **El Problema del Cero:** Visual de distancias positivas y negativas cancelándose.


3. **Mínimos Cuadrados:** Fórmulas de $b_1$ y $b_0$.


4. **Laboratorio Analítico:** Instrucciones del taller manual vs. Excel.
5. **El Impacto Financiero:** Slide sin texto, solo una imagen de una bodega sobre-stockeada.
6. **Metacognición:** Pregunta de cierre visible y Ticket de salida.

**Para la Clase N°3 (Restricciones de Predicción):**

1. **El Bebé de -186 Libras:** La ecuación $\hat{y} = -186.5 + 4.71x$ grande en pantalla.


2. **Las 3 Reglas de Oro:** Iconografía sobre Población, Dominio Muestral y Tiempo.


3. **El Precipicio de la Extrapolación:** Gráfico que muestra datos agrupados en el centro y una línea proyectada hacia un precipicio (valores extremos).
4. **El Tribunal de los Datos:** Cronómetro de 15 minutos e instrucciones del estudio de caso.
5. **Aprobado o Rechazado:** Veredictos de la actividad anterior.
6. **Metacognición Final:** Reflexión sobre la responsabilidad del analista frente a la máquina.