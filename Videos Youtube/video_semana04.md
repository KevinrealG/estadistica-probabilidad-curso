# Video 1

### 🎬 Resumen del Video

* **Tema:** Medidas de Dispersión (Rango, Desviación Estándar y Coeficiente de Variación).
* **Plataforma:** YouTube Shorts / Reels / TikTok (Vertical 9:16).
* **Duración:** 85 - 95 segundos.
* **Concepto:** Por qué el promedio engaña y cómo el Rango, la Desviación Estándar y el CV nos revelan la verdadera forma de los datos (incluso al comparar cosas absurdas como notas y elefantes).
* **Público Objetivo:** Estudiantes universitarios, profesionales de ciencia de datos y estadística.

---

### 🔎 SEO y Metadatos

* **Título Principal:** El Engaño del Promedio (Y cómo medir el caos real) ⚠️📊
* **Títulos Alternativos:** Rango vs Desviación Estándar vs CV | ¿Cómo comparar Elefantes y Ratones en Estadística? | Medidas de Dispersión
* **Tags:** `#Estadistica`, `#CienciaDeDatos`, `#DesviacionEstandar`, `#Matematicas`, `#AnalisisDeDatos`, `#Manim`
* **Descripción Corta:** Dos grupos tienen el mismo promedio, pero realidades opuestas. Aprende qué es el Rango, por qué la Desviación Estándar es clave, y cómo el Coeficiente de Variación te permite comparar la dispersión de elefantes y ratones.
* **Miniatura Sugerida:** Pantalla dividida en diagonal. Arriba: Un elefante y un ratón en una balanza con un signo de interrogación. Abajo: Una campana de Gauss roja muy ancha etiquetada "$CV > 30\%$ (¡CAOS!)". Texto gigante: "¿EL PROMEDIO MIENTE?".

---

### 📜 Guion y Storyboard Técnico (Manim)

| Tiempo | Narración (Locución) | Visual / Animación (Manim) | Texto en Pantalla / Ecuaciones | Sonidos / Efectos |
| --- | --- | --- | --- | --- |
| **00:00 - 00:05** | **(Hook)** Dos salones tienen exactamente el mismo promedio: 3.5. Pero si fueras el profesor, notarías que uno es un caos total. | Las notas del Curso A (juntas) y Curso B (dispersas) caen en dos rectas numéricas. Aparece una gran línea de "Promedio 3.5" cruzando ambas. | Curso A: Promedio 3.5<br><br>Curso B: Promedio 3.5 | *Whoosh* doble. Impacto metálico. Música dinámica estilo synthwave. |
| **00:05 - 00:15** | **(Explicación 1: Rango)** ¿Cómo medimos ese caos? La forma más simple es el **Rango**. Restas el valor menor al mayor. Si la nota más alta es 95 y la más baja 40, tu rango es 55. | Se hace zoom al Curso B. Se iluminan el dato menor (40) y el mayor (95). Una llave de corchete gigante conecta ambos. | **RANGO**<br><br>$R = X_{max} - X_{min}$<br><br>$95 - 40 = 55$ | Sonido de estiramiento (cuerda elástica) y un *Ding* de caja registradora. |
| **00:15 - 00:25** | **(Problema del Rango)** ¿El problema grave? Ignora por completo el 100% de los datos intermedios. Solo mira los extremos. | Los puntos extremos brillan, pero todos los puntos del medio (las otras notas) se vuelven grises y se caen de la pantalla tristemente. | **Limitación:** Ignora los datos intermedios. | Sonido de desinflado o *glitch* de error. |
| **00:15 - 00:27** | **(Explicación 1: El dilema)** ¿Cómo medimos ese caos matemáticamente? Calculando la distancia de cada nota al promedio. Pero si sumas estas distancias, las positivas y negativas... ¡se cancelan y dan cero! | Se dibujan líneas (vectores) desde cada punto a la media. Las distancias del lado izquierdo parpadean en rojo (negativas), las del derecho en azul (positivas). Ecuación colapsa a 0. | Distancias a la media: $\sum (x_i - \bar{x}) = 0$ | Sonido de rebote fallido o *glitch*. |
| **00:27 - 00:40** | **(Explicación 2: Varianza)** ¿El truco de los matemáticos? Elevar esas distancias al cuadrado. Así eliminamos los negativos. Sumamos todo y promediamos. A esto se le llama **Varianza**. | Cada línea de distancia se transforma en un cuadrado literal de área (`Square`). Los cuadrados rojos se vuelven positivos. Todos los cuadrados se suman visualmente en uno solo. | **Varianza ($s^2$):**<br><br>$s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$ | Sonido mágico y geométrico al aparecer los cuadrados. *Ding* analítico. |
| **00:40 - 00:52** | **(Explicación 3: Desviación Estándar)** Pero la Varianza nos da "notas al cuadrado". Para volver a la realidad, le sacamos la raíz cuadrada. ¡Bum! **Desviación Estándar**. Es básicamente el promedio de qué tanto se alejan los datos. | El gran cuadrado se encoge (raíz cuadrada) volviendo a ser una línea. La fórmula de $s^2$ se mete dentro de una $\sqrt{\ }$. | **Desviación Estándar ($s$):**<br><br>$s = \sqrt{s^2}$ | *Swoosh* inverso (retroceso). |
| **00:52 - 01:00** | **(Aplicación)** En ingeniería o inversiones, un proceso con baja desviación estándar es predecible y seguro, como el Curso A. | Se muestran los resultados finales: Curso A ($s = 0.07$) verde y seguro. Curso B ($s = 1.73$) rojo y tembloroso. | Curso A: $s = 0.07$<br><br>Curso B: $s = 1.73$<br><br>**Baja $s$ = Predictibilidad** | Sonido de "Check" de confirmación vs Alarma suave de riesgo. |
| **00:25 - 00:38** | **(Explicación 2: Desviación Estándar)** Por eso usamos la **Desviación Estándar**. Calcula cuánto se aleja, en promedio, cada nota del centro. Es la medida reina para saber si los datos están agrupados o dispersos. | Los puntos grises regresan. Aparecen líneas desde cada punto hacia el promedio. Las líneas se transforman en una fórmula rápida que da como resultado $s$. | **Desviación Estándar ($s$)** | Sonidos rápidos y tecnológicos (*bloop-bloop-bloop*) al medir distancias. |
| **00:38 - 00:52** | **(El Reto / Hook 2)** Pero espera... ¿qué pasa si quieres comparar la dispersión de las notas de tus alumnos... con el peso de una manada de elefantes y ratones? | La gráfica de notas desaparece. Entra una gráfica con iconos minimalistas de Elefantes (miles de kilos) y Ratones (gramos). Aparecen signos de interrogación gigantes. | ¿Notas vs Kilos?<br><br>¿Elefantes vs Ratones? | Trompetazo de elefante cómico y chillido de ratón. |
| **00:52 - 01:08** | **(Explicación 3: CV)** Tienen unidades distintas, así que usamos el **Coeficiente de Variación**. Tomas la desviación estándar, la divides por el promedio y lo multiplicas por 100. ¡Se vuelve un porcentaje adimensional! | Aparece la fórmula del CV gigante. Los íconos de "kilos" y "puntos" chocan y se destruyen, dejando solo el símbolo de `%`. | **Coeficiente de Variación (CV)**<br><br>$$CV = \left( \frac{s}{\bar{x}} \right) \times 100\%$$

| Sonido de "Level Up" mágico. |
| **01:08 - 01:18** | **(Aplicación)** La regla de oro: Si el CV es menor al 30%, tu conjunto es homogéneo y predecible. Si es mayor... estás lidiando con pura heterogeneidad. | Un medidor estilo velocímetro aparece. La aguja sube a la zona verde ($<30\%$) etiquetada "Homogéneo", luego salta a la zona roja etiquetada "Heterogéneo". | $< 30\%$ = Homogéneo<br><br>$> 30\%$ = Heterogéneo | Revoluciones de motor acelerando. |
| **01:18 - 01:25** | **(Cierre)** Si tu grupo de estudiantes tiene un CV del 50%... ¿Qué crees que significa eso para ti como profesor? ¡Piénsalo y comenta! | Pantalla oscura con la pregunta resaltada. | Si $CV = 50\%$... ¿Qué significa? 👇 | *Boom* de bajo profundo. Corte musical. |

---

### 🛠️ Recursos y Prompts IA

**1. Prompt para Manim (Para IA de código como Claude 3.5 Sonnet / ChatGPT 4o):**

> "Genera un script en Python usando Manim Community. Configura resolución vertical (1080x1920).
> **Escena 1:** Crea dos `NumberLine`. Grafica puntos del Curso A (agrupados cerca del 3.5) y Curso B (dispersos). Traza una línea vertical indicando `Promedio = 3.5`.
> **Escena 2 (Rango):** Elimina el Curso A. En la línea del Curso B, destaca los puntos en x=40 y x=95. Dibuja un `Brace` entre ellos. Muestra el texto en LaTeX: `R = X_{max} - X_{min} = 95 - 40 = 55`.
> **Escena 3:** Haz que todos los puntos entre 40 y 95 cambien a color gris y caigan fuera de la pantalla (usando `FadeOut` con `shift=DOWN`).
> **Escena 4 (Desviación):** Regresa los puntos. Dibuja flechas bidireccionales desde cada punto hacia la línea del promedio. Muestra la letra $s$ brillante.
> **Escena 5 (CV):** Borra todo. Muestra dos SVGs o textos: 'Elefantes (kg)' y 'Ratones (g)'. Muestra la fórmula LaTeX: `CV = \left( \frac{s}{\bar{x}} \right) \times 100\%`. Usa animaciones para cancelar las unidades (kg y g desaparecen, dejando solo %).
> **Escena 6:** Dibuja un semicírculo (`Arc`) estilo velocímetro. La mitad izquierda (0-30%) en `GREEN` con texto 'Homogéneo'. La derecha en `RED` con texto 'Heterogéneo'. Anima una aguja (`Line`) moviéndose."

**2. Prompt para ElevenLabs (Voz en Off):**

> "Voz masculina o femenina, estilo creador de contenido educativo vibrante y ágil (tipo 'Matemáticas Pro' o 'StatQuest'). El tono debe variar: intrigante al hablar del engaño del promedio, crítico al revelar el defecto del Rango ('ignora por completo...'), y muy entusiasta y casi cómico al introducir a los elefantes y ratones. Termina con un tono desafiante para la pregunta final."

**3. Prompt para IA de Imágenes (Miniatura - Midjourney/DALL-E 3):**

> "A highly engaging YouTube thumbnail, vertical split design. Top half: a cute 3D elephant and a tiny mouse standing on a glowing digital scale, giant glowing question mark. Bottom half: A chaotic scatter plot chart with neon red dots spread everywhere. Big bold 3D text floating in the middle reading '¿El Promedio MIENTE?'. Dark background, vibrant neon lighting, 8k resolution, educational science style."

# Video 2
### 🎬 Resumen del Video

* **Tema:** Creación e interpretación de un Diagrama de Caja y Bigotes (Boxplot).
* **Plataforma:** Reels / Shorts / TikTok (Vertical 9:16).
* **Duración:** 60 segundos.
* **Público Objetivo:** Estudiantes y profesionales de análisis de datos.

---

### 🔎 SEO y Metadatos

* **Título Principal:** El Gráfico que los Analistas de Datos Aman 📦 (Boxplot Explicado)
* **Títulos Alternativos:** Cómo leer un Diagrama de Caja y Bigotes | Adiós al Promedio: Usa Boxplots
* **Tags:** `#CienciaDeDatos`, `#Estadistica`, `#Boxplot`, `#AnalisisDeDatos`, `#Manim`
* **Descripción Corta:** Descubre cómo resumir miles de datos en 5 simples números usando un Boxplot. Identifica valores atípicos al instante.
* **Miniatura Sugerida:** Fondo oscuro. Un Boxplot en color neón vibrante (cyan y magenta). Una flecha roja apuntando a un punto solitario fuera del bigote con el texto: "¡ANOMALÍA!".

---

### 📜 Guion y Storyboard Técnico

| Tiempo | Narración (Locución) | Visual / Animación (Pantalla) | Texto en Pantalla / Ecuaciones | Sonidos / Efectos |
| --- | --- | --- | --- | --- |
| **00:00 - 00:04** | **(Hook)** ¿Quieres descubrir los secretos que el promedio te está ocultando? Necesitas un Boxplot. | Un gráfico de barras aburrido se colapsa y explota, revelando un Boxplot brillante y moderno. | ¡No confíes en el promedio! | *Whoosh* metálico. Música dinámica y rítmica. |
| **00:04 - 00:12** | **(Problema)** Analicemos la asistencia a 50 eventos musicales de champeta. Si solo miras el promedio, no sabrás si la asistencia fue constante o un sube y baja. | Puntos de datos caen aleatoriamente sobre una recta numérica horizontal, representando la asistencia (ej. 100 a 1000 personas). | Asistencia a Eventos | *Pop-pop-pop* rápido (caída de datos). |
| **00:12 - 00:28** | **(Explicación 1: La Caja)** Un Boxplot resume todo en 5 números. El 50% de todos tus eventos están atrapados dentro de esta caja central. Va desde el cuartil 1 hasta el cuartil 3. | Una caja azul neón se dibuja envolviendo la mitad central de los puntos. Aparecen las etiquetas $Q_1$ y $Q_3$. | **Caja:** Contiene el 50% central.<br>

<br>$IQR = Q_3 - Q_1$ | Sonido de trazado láser. |
| **00:28 - 00:36** | **(Explicación 2: La Mediana)** Esa línea gruesa en medio de la caja es la Mediana. El centro absoluto de tu éxito. | Una línea brillante amarilla corta la caja. | **Mediana** ($\tilde{x}$) | *Swoosh* limpio (corte ninja). |
| **00:36 - 00:48** | **(Explicación 3: Los Bigotes)** De la caja salen dos "bigotes" hasta los valores mínimos y máximos normales. Muestran todo el rango esperado de asistencia. | Dos líneas se extienden desde la caja hacia los extremos izquierdo y derecho. | **Bigotes:** Rango esperado. | Sonido de estiramiento (cuerda de arco). |
| **00:48 - 00:54** | **(Aplicación: Outliers)** ¿Y ese punto solitario allá lejos? Es un valor atípico. Ese picó que rompió récord total de asistencia. | Un punto rojo parpadea mucho más allá del bigote derecho. La cámara hace zoom. | **Outlier:** ¡Anomalía! | *Bloop* de alerta. Alarma de victoria. |
| **00:54 - 01:00** | **(Cierre)** Si ves que la caja es muy pequeña, pero los bigotes son larguísimos, ¿qué significa? 👇 | El gráfico se desvanece. Queda la pregunta en pantalla. | Caja pequeña, bigotes largos = ¿Qué significa?<br>

<br>¡Comenta! | *Impacto de bajo*. Fin brusco de música. |

---

### 🛠️ Recursos y Prompts IA

**1. Prompt para Manim (Python):**

> "Genera un script en Python con Manim Community (1080x1920).
> 1. Crea una `NumberLine`.
> 2. Anima la aparición de 50 `Dot`s simulando una distribución asimétrica positiva.
> 3. Dibuja un `Rectangle` (la caja) desde $Q_1$ hasta $Q_3$ con transparencia.
> 4. Añade una `Line` vertical para la Mediana.
> 5. Dibuja dos `Line` horizontales (bigotes) desde la caja hasta los límites calculados por $1.5 \times IQR$.
> 6. Destaca un punto en color `RED` más allá del bigote derecho (Outlier)."
> 
> 

**2. Prompt para ElevenLabs (Voz):**

> "Voz masculina o femenina ágil y analítica, estilo creador de ciencia de datos. Tono de intriga al principio, explicaciones muy articuladas marcando bien las palabras 'caja', 'mediana' y 'bigotes'. Sorpresa y energía al mencionar el 'valor atípico'."
¡Hola! Aquí está tu **STEM Video Producer AI** en acción.

Has traído un concepto brillante: la transición de entender el "centro" al "esparcimiento". El contraste entre el Curso A y el Curso B es un *hook* (gancho) narrativo perfecto porque genera una disonancia cognitiva: **los números dicen que son iguales, pero los ojos dicen que son completamente distintos.**

Vamos a transformar esa clase en un video corto explosivo y muy visual.

---

### 🎬 Resumen del Video

* **Plataforma:** YouTube Shorts / Reels / TikTok (Vertical 9:16).
* **Duración:** 60 - 70 segundos.
* **Concepto:** Varianza y Desviación Estándar. Por qué el promedio no basta para entender los datos y por qué elevamos al cuadrado las diferencias.
* **Audiencia:** Estudiantes universitarios, profesionales de ciencia de datos, ingeniería y administración.

---

### 🔎 SEO y Metadatos

* **Título Principal:** El Peligro Oculto del Promedio ⚠️ (Varianza Explicada)
* **Títulos Alternativos:** ¿Qué es la Desviación Estándar? | El Promedio te Engaña: Medidas de Dispersión | Matemáticas para Ciencia de Datos
* **Tags:** `#Estadistica`, `#CienciaDeDatos`, `#Ingenieria`, `#Matematicas`, `#DesviacionEstandar`, `#Manim`
* **Descripción Corta:** Dos salones tienen exactamente el mismo promedio, pero uno es un caos y el otro es perfecto. Descubre qué es la Varianza y la Desviación Estándar de forma 100% visual.
* **Miniatura Sugerida:** Pantalla dividida. Arriba, puntos muy agrupados con la etiqueta "Aprobados". Abajo, puntos dispersos al extremo con la etiqueta "Caos". En el centro, un enorme "Promedio = 3.5" en ambos, con un signo de interrogación brillante.

---

### 📜 Guion y Storyboard Técnico (Manim)

| Tiempo | Narración (Locución) | Visual / Animación (Manim) | Texto en Pantalla / Ecuaciones | Sonidos / Efectos |
| --- | --- | --- | --- | --- |
| **00:00 - 00:05** | **(Hook)** Estos dos salones tienen exactamente el mismo promedio: 3.5. Pero uno es un sueño y el otro es un caos total. | Aparecen las notas del Curso A (3.4, 3.5...) y del Curso B (1.0, 5.0...). Ambas colapsan en un gran "Promedio: 3.5". | Curso A: 3.5<br><br>Curso B: 3.5 | *Whoosh* doble y sonido de choque eléctrico. Música intrigante y rítmica. |
| **00:05 - 00:15** | **(Problema)** Míralos en una gráfica. El salón A es súper constante. El B tiene genios y estudiantes a punto de reprobar. ¡El promedio oculta este desastre! | Dos rectas numéricas (`NumberLine`) una sobre otra. Los puntos del Curso A se agrupan al centro. Los del B se esparcen por los extremos. Aparece la línea central de la media ($\bar{x}$). | ¡El promedio oculta el caos! | Sonido de "pop" rápido para cada punto. |
| **00:15 - 00:27** | **(Explicación 1: El dilema)** ¿Cómo medimos ese caos matemáticamente? Calculando la distancia de cada nota al promedio. Pero si sumas estas distancias, las positivas y negativas... ¡se cancelan y dan cero! | Se dibujan líneas (vectores) desde cada punto a la media. Las distancias del lado izquierdo parpadean en rojo (negativas), las del derecho en azul (positivas). Ecuación colapsa a 0. | Distancias a la media: $\sum (x_i - \bar{x}) = 0$ | Sonido de rebote fallido o *glitch*. |
| **00:27 - 00:40** | **(Explicación 2: Varianza)** ¿El truco de los matemáticos? Elevar esas distancias al cuadrado. Así eliminamos los negativos. Sumamos todo y promediamos. A esto se le llama **Varianza**. | Cada línea de distancia se transforma en un cuadrado literal de área (`Square`). Los cuadrados rojos se vuelven positivos. Todos los cuadrados se suman visualmente en uno solo. | **Varianza ($s^2$):**<br><br>$s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$ | Sonido mágico y geométrico al aparecer los cuadrados. *Ding* analítico. |
| **00:40 - 00:52** | **(Explicación 3: Desviación Estándar)** Pero la Varianza nos da "notas al cuadrado". Para volver a la realidad, le sacamos la raíz cuadrada. ¡Bum! **Desviación Estándar**. Es básicamente el promedio de qué tanto se alejan los datos. | El gran cuadrado se encoge (raíz cuadrada) volviendo a ser una línea. La fórmula de $s^2$ se mete dentro de una $\sqrt{\ }$. | **Desviación Estándar ($s$):**<br><br>$s = \sqrt{s^2}$ | *Swoosh* inverso (retroceso). |
| **00:52 - 01:00** | **(Aplicación)** En ingeniería o inversiones, un proceso con baja desviación estándar es predecible y seguro, como el Curso A. | Se muestran los resultados finales: Curso A ($s = 0.07$) verde y seguro. Curso B ($s = 1.73$) rojo y tembloroso. | Curso A: $s = 0.07$<br><br>Curso B: $s = 1.73$<br><br>**Baja $s$ = Predictibilidad** | Sonido de "Check" de confirmación vs Alarma suave de riesgo. |
| **01:00 - 01:10** | **(Cierre)** Aquí te va un reto de nivel pro: Para quitar los números negativos, pudimos haber usado el Valor Absoluto. ¿Por qué crees que los estadísticos prefieren elevar al cuadrado? | Pantalla oscura limpia. Texto de la pregunta grande en pantalla. Flecha apuntando a los comentarios. | ¿Por qué al cuadrado ($x^2$) y no Valor Absoluto (|$$$|)? 👇 | *Impacto profundo*. Fin brusco de la música. |

---

### 🛠️ Recursos y Prompts IA

**1. Prompt para Manim (Para el código Python):**

> "Genera un script en Python con Manim Community (formato 1080x1920).
> **Escena 1:** Dibuja dos `NumberLine` apiladas verticalmente (rango de 0 a 6).
> **Escena 2:** Grafica como `Dot`s el Curso A `[3.4, 3.5, 3.6, 3.5, 3.4]` en la línea de arriba y el Curso B `[1.0, 5.0, 2.0, 4.8, 3.7]` en la de abajo. Traza una línea vertical discontinua amarilla que cruce ambas rectas en x=3.5 (Media).
> **Escena 3:** Para el Curso B, dibuja vectores horizontales desde cada punto hasta la media. Los de la izquierda en ROJO, la derecha en AZUL.
> **Escena 4 (Crucial):** Anima cuadrados (`Square`) cuyos lados sean iguales a la longitud de cada vector de distancia. Colócalos debajo de la recta. Muestra la fórmula LaTeX de la varianza muestral $s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$.
> **Escena 5:** Envuelve la fórmula en una raíz cuadrada $\sqrt{\cdot}$ para transformarla en $s$. Encoje los cuadrados de vuelta a líneas. Muestra un texto final: Curso A: $s=0.07$, Curso B: $s=1.73$."

**2. Prompt para ElevenLabs (Voz en Off):**

> "Voz masculina o femenina, estilo 'Veritasium' o 'Dot CSV'. El tono inicial debe ser de incredulidad y contraste ('uno es un sueño y el otro un caos'). Cuando expliques la Varianza (elevar al cuadrado), sube la energía y suena como si revelaras un gran secreto o un 'truco' matemático genial. Termina con un tono de desafío intelectual para la pregunta final."

**3. Nota de Diseño Instruccional (Para el cierre):**
La pregunta de cierre que incluí en el guion (*¿Por qué al cuadrado y no valor absoluto?*) es uno de los debates más ricos en estadística (Desviación Media Absoluta vs. Desviación Estándar). Esto garantiza que profesores, estudiantes aventajados y matemáticos llenen tu sección de comentarios discutiendo sobre derivadas, funciones suaves y el error cuadrático medio. **¡Es una mina de oro para el algoritmo de retención y engagement!**


# Video 3

### 🎬 Resumen del Video

* **Tema:** Interpretación experta de un Diagrama de Caja (Boxplot): IQR, mediana, sesgo, bigotes, valores atípicos y comparación.
* **Público Objetivo:** Analistas de datos, estudiantes y organizadores de eventos.
* **Duración:** 60 - 75 segundos.
* **Plataforma:** YouTube Shorts / Reels / TikTok (Vertical 9:16).
* **Concepto:** Aprender a leer un Boxplot paso a paso utilizando un caso práctico (comparar la asistencia a eventos de dos sistemas de sonido).

---

### 🔎 SEO y Metadatos

* **Título Principal:** Cómo Leer un Boxplot como un Experto 📦📊
* **Títulos Alternativos:** Deja de usar el Promedio | Qué significa el Rango Intercuartílico | Analiza Datos Visualmente
* **Tags:** `#CienciaDeDatos`, `#Estadistica`, `#Boxplot`, `#AnalisisDeDatos`, `#DataScience`
* **Descripción Corta:** Aprende a interpretar la caja, los bigotes, la mediana y los valores atípicos (outliers) en 1 minuto. Descubre cómo identificar el sesgo y comparar grupos fácilmente.
* **Miniatura Sugerida:** Fondo oscuro. Dos Boxplots enfrentados (uno verde muy compacto, uno rojo muy estirado). El verde dice "SEGURO", el rojo dice "RIESGO". Una lupa gigante enfoca un punto atípico.

---

### 📜 Guion y Storyboard Técnico

| Tiempo | Narración (Locución) | Visual / Animación | Texto en Pantalla | Sonidos / Efectos |
| --- | --- | --- | --- | --- |
| **00:00 - 00:03** | **(Hook)** ¿Aún mides el éxito solo con el promedio? Este gráfico revela la verdad completa en segundos. | Un gráfico de barras tradicional se rompe en pedazos y se transforma mágicamente en un Boxplot vertical de neón. | ¡El promedio oculta la verdad! | *Cristal roto* + *Whoosh* electrónico. |
| **00:03 - 00:10** | **(Problema)** Imagina que comparas la asistencia de público de dos Picós distintos. ¿Cuál te asegura el éxito en tu próximo evento de champeta? | Aparecen dos siluetas de sistemas de sonido. Debajo de cada uno, se dibujan cientos de puntos (datos de asistencia) flotando. | ¿Cuál Picó elegirías? | *Beats* rápidos de champeta de fondo. |
| **00:10 - 00:22** | **(Explicación 1: La Caja)** Primero, mira la caja. Contiene el 50% central de tus datos. Es tu IQR. Entre más angosta sea la caja, más constante y predecible es la asistencia. | Los puntos se agrupan y se encierran en una caja brillante. Un calibrador mide su altura. La caja se contrae (verde) y se expande (roja). | **Caja (50% central)**<br>

<br>Angosta = Consistente | Sonido de escáner tecnológico. |
| **00:22 - 00:32** | **(Explicación 2 & 5: Mediana y Asimetría)** La línea del centro es la Mediana. Si no está en el medio de la caja, hay asimetría. ¡Eso indica que los datos están sesgados hacia los extremos! | Hacemos zoom a la línea central. Se desplaza hacia abajo (sesgo positivo), tiñendo el área superior de un color distinto para mostrar el desbalance. | **Mediana descentrada = Asimetría (Sesgo)** | *Corte ninja* (Swoosh). |
| **00:32 - 00:45** | **(Explicación 3: Bigotes y Outliers)** Los "bigotes" muestran el límite de lo esperado. Si ves un punto fuera de ellos... ¡Es un Outlier! Ese evento que inexplicablemente se llenó a reventar. | Se trazan las líneas superior e inferior. Un punto solitario aparece muy arriba de los bigotes, parpadeando. | **Bigotes:** Rango esperado<br>

<br>**Outlier:** ¡Anomalía! | Trazado láser + *Bloop* de alerta. |
| **00:45 - 00:55** | **(Aplicación: Comparar)** Pon dos grupos lado a lado. El Picó "A" tiene una caja ancha: es inestable. El Picó "B" tiene caja angosta: es una apuesta segura. | Pantalla dividida. Boxplot "A" ancho y tembloroso. Boxplot "B" compacto y estable. Se marca un "Check" verde en el B. | "A" = Variable<br>

<br>"B" = Predecible | Sonido de balanza equilibrándose + *Ding* de éxito. |
| **00:55 - 01:05** | **(Cierre)** Si en tu gráfico la mediana toca el fondo de la caja, ¿hacia dónde crees que está el sesgo? 👇 | El gráfico desaparece, dejando solo la caja con la mediana abajo y signos de interrogación. | Mediana al fondo = ¿Qué sesgo es?<br>

<br>¡Comenta! | *Drop de bajo profundo*. Fin brusco. |

---

### 🛠️ Recursos y Prompts IA

**1. Prompt para Python / Manim (Generación de las animaciones visuales):**

> "Genera un script de Python usando Manim. Formato vertical (1080x1920). Escenas secuenciales:
> 1. Dibuja un Boxplot básico.
> 2. Resalta el rectángulo central con un `Brace` etiquetado 'IQR: 50% central'.
> 3. Anima la línea de la mediana desplazándose hacia la parte inferior del rectángulo mostrando texto: 'Asimetría/Sesgo'.
> 4. Dibuja líneas (`whiskers`) extendiéndose a 1.5 * IQR.
> 5. Dibuja un `Dot` en color rojo por encima del bigote superior con la etiqueta 'Outlier'.
> 6. Muestra dos Boxplots lado a lado; uno con un IQR grande (etiqueta: 'Alta Variabilidad') y otro con un IQR pequeño (etiqueta: 'Consistente')."
> 
> 

**2. Prompt para ElevenLabs (Voz en Off):**

> "Voz masculina joven, estilo 'director de arte' o creador de contenido dinámico (tipo Vox o Kurzgesagt en español). Ritmo ágil, sin pausas largas. El tono debe ser explicativo pero contundente. Énfasis especial de sorpresa al decir '¡Es un Outlier!' y tono analítico y seguro en 'es una apuesta segura'."

**3. Prompt para Midjourney / IA de Imágenes (Miniatura y Assets B-Roll):**

> "A YouTube thumbnail for a data science video, vertical split screen. Left side: a highly fluctuating, chaotic neon red bar chart. Right side: a perfectly symmetrical, compact neon green Boxplot on a dark grid background. In the center, a glowing magnifying glass focuses on a single red dot (outlier). Text overlay 'VERDAD' in bold typography, cinematic lighting, 8k --ar 16:9"