# Video 1 🎬 Resumen del Video

* **Plataforma:** YouTube Shorts / Reels / TikTok (Vertical 9:16).
* **Duración:** 70-85 segundos.
* **Concepto:** Diferenciar Media, Mediana y Moda con rigor matemático (notación, casos par/impar, tipos de moda) y su sensibilidad a valores atípicos.
* **Audiencia:** Estudiantes universitarios, de secundaria avanzada y aprendices de ciencia de datos.

---

### 🔎 SEO y Metadatos

* **Título Principal:** ¿El "Promedio" te Miente? La Estadística Oculta 📊
* **Títulos Alternativos:** Media, Mediana y Moda: Fórmulas y Trucos | Entiende Medidas de Tendencia Central
* **Tags:** `#Estadistica`, `#Manim`, `#CienciaDeDatos`, `#AprendeEnYouTube`, `#Matematicas`
* **Descripción Corta:** Descubre la diferencia real entre la media, la mediana y la moda. Aprende las fórmulas para datos pares e impares, y cómo los valores atípicos engañan a tu cerebro.
* **Miniatura Sugerida:** Fondo oscuro (estilo 3Blue1Brown). Una distribución de puntos asimétrica en neón. Tres líneas (rojo, verde, azul) etiquetadas con símbolos matemáticos: $\bar{x}$, $\tilde{x}$ y $m_o$.

---

### 📜 Guion y Storyboard Técnico (Manim)

| Tiempo | Narración (Locución) | Visual / Animación (Manim) | Texto en Pantalla / Ecuaciones | Sonidos / Efectos |
| --- | --- | --- | --- | --- |
| **00:00 - 00:03** | **(Hook)** ¿Sabías que el "promedio" casi siempre te está mintiendo? | La cámara hace zoom a un punto que explota en 30 números moviéndose caóticamente. | "¿EL PROMEDIO MIENTE?" en fuente gruesa roja. | *Whoosh* agresivo. Música electrónica estilo synthwave. |
| **00:03 - 00:08** | **(Problema)** Tenemos las edades de 30 gamers. Si buscamos la edad "típica", ¿cuál medida usamos? | Los números se alinean rápidamente en una recta numérica horizontal (`NumberLine`). | $n = 30$ | *Tick-tick-tick* (contador rápido). |
| **00:08 - 00:20** | **(Explicación 1: Moda)** La Moda es el más popular. Aquí es el 18. Un conjunto univariado puede ser unimodal, bimodal, multimodal o amodal. | Los números idénticos se apilan. La torre del "18" brilla en amarillo. Aparecen fantasmas de otras torres brillando brevemente (mostrando casos bimodales/multimodales). | **Moda:** $m_o$ (Muestra)<br>

<br>$M_o$ (Población) | *Campana* (Ding) al iluminarse el 18. |
| **00:20 - 00:32** | **(Explicación 2: Mediana - Par)** La Mediana es el centro exacto. Con 30 datos, que es par, promediamos los dos valores centrales. | Una línea verde cae entre los dos puntos centrales (18 y 19). Se unen y se dividen entre dos. | FÓRMULA PAR:<br>

<br> $\frac{x_{n/2} + x_{n/2+1}}{2} = 18.5$ | *Swoosh* ninja y sonido de cálculo electrónico. |
| **00:32 - 00:45** | **(Explicación 2: Mediana - Impar)** ¿Y si quitamos al mayor y quedan 29 datos? El centro exacto cae justo sobre un dato: el 18. | El punto "30" desaparece (pop). La línea verde se desplaza y corta exactamente al punto número 15 (el 18). | **Mediana:** $\tilde{x}$ o $m_e$<br>

<br>($M_e$ Población)<br>

<br>$n=29 \rightarrow$ Centro: 18 | *Pop* (desaparece el dato). *Click* al encajar la línea. |
| **00:45 - 00:55** | **(Explicación 3: Media)** La Media es el punto de equilibrio. Esta fórmula indica la suma de cada dato individual, dividida por el total. | Vuelve el dato "30". Un triángulo (fulcro) equilibra la línea en 19.4. Los puntos destellan uno a uno rápidamente simulando la sumatoria. | **Media:**<br>

<br>$\bar{x} = \frac{\sum x_i}{n}$ | Sonido mecánico de balanza equilibrándose. |
| **00:55 - 01:05** | **(Aplicación)** Mira esto: unos pocos gamers mayores arrastran la media hacia arriba, pero la mediana y moda ni se inmutan. | Los datos extremos (27, 28, 30) parpadean en rojo. El fulcro ($\bar{x}$) se desliza a la derecha. La línea verde ($\tilde{x}$) se queda quieta. | ¡Los extremos afectan la media! | *Bloop* de alerta. Alarma suave. |
| **01:05 - 01:10** | **(Cierre)** Si analizaras salarios en una empresa donde el jefe es millonario, ¿usarías la media o la mediana? | Barrido rápido de cámara hacia arriba. | ¿Media o Mediana? 👇 ¡Comenta! | *Impacto de bajo* (Boom). Cierre de música. |

---

### 🛠️ Recursos y Prompts IA

**1. Prompt para Manim (IA de Código - Claude 3.5 Sonnet / ChatGPT 4o):**

> "Genera un script en Python usando Manim Community. Configura resolución vertical (1080x1920).
> Escenas secuenciales:
> 1. Crea un histograma de puntos (`Dot`) sobre una `NumberLine` con la lista de 30 datos: `[14, 15... 30]`.
> 2. Destaca la columna del 18 en `YELLOW`. Muestra el texto en LaTeX: 'Moda: $m_o$ (Muestra) / $M_o$ (Población)'.
> 3. Dibuja una línea `GREEN` entre los valores centrales y muestra la fórmula en LaTeX: $\frac{x_{n/2} + x_{n/2+1}}{2}$.
> 4. Anima la eliminación del valor máximo (30), desplaza la línea verde para que cruce el dato central restante y muestra: 'Mediana: $\tilde{x}$ o $m_e$ / $M_e$'.
> 5. Restaura el dato 30, dibuja un fulcro en x=19.4, y muestra la fórmula $\bar{x} = \frac{\sum x_i}{n}$ con notación LaTeX.
> Usa animaciones de `Transform`, `Write` y `Create` para transiciones fluidas."
> 
> 

**2. Prompt para ElevenLabs (Voz):**

> "Voz masculina/femenina, estilo divulgador científico (tipo Kurzgesagt o 3Blue1Brown en español). Tono claro, académico pero ágil e intrigante. Ritmo dinámico. Haz pausas de medio segundo antes de leer las fórmulas para dar tiempo al espectador de asimilarlas visualmente. Énfasis analítico en 'punto de equilibrio'."Cálculo de Medidas de Tendencia Central  Guion, animaciones manim y audio de videos,

# Video 2


---

### 🎬 Resumen del Video

* **Plataforma:** YouTube 
* **Duración:**
* **Concepto:** Cálculo de percentiles usando interpolación lineal para encontrar la posición exacta en un conjunto de datos.
* **Audiencia:** Estudiantes de secundaria, universitarios y curiosos por la estadística y ciencia de datos.

---

### 🔎 SEO y Metadatos

* **Título Principal:** ¿Cómo saber si realmente eres el mejor? (Percentiles) 📈
* **Títulos Alternativos:** El truco matemático para calcular Percentiles | Interpolación Lineal en Estadística | No te dejes engañar por tus notas
* **Tags:** `#Estadistica`, `#CienciaDeDatos`, `#Matematicas`, `#Percentiles`, `#AprendeEnTikTok`, `#Manim`
* **Descripción Corta:** Un estudiante sacó 85/100 y dice estar en el Top 15% de su clase. ¿Es cierto? Descubre cómo la ciencia de datos y la interpolación lineal nos dan la respuesta exacta.
* **Miniatura Sugerida:** Fondo oscuro. Una nota de examen gigante "85/100" con un sello rojo que dice "¡MENTIRA!". A un lado, una flecha de neón apuntando al número 96.15 con el texto "Top 15% Real".

---

### 📜 Guion y Storyboard Técnico (Manim)

| Tiempo | Narración (Locución) | Visual / Animación (Manim) | Texto en Pantalla / Ecuaciones | Sonidos / Efectos |
| --- | --- | --- | --- | --- |
| **00:00 - 00:04** | **(Hook)** Alguien sacó 85 en su examen y jura que está en el "15% superior" de su clase. ¿Le creemos? | Aparece un examen con un "85/100" gigante. El examen se hace a un lado y el personaje/icono del estudiante se pone gafas de sol. | "¡Estoy en el 15% superior!" | *Swoosh* rápido. Sonido de rasgado de papel y un *Record Scratch* (disco rayado). |
| **00:04 - 00:09** | **(Problema)** Vamos a comprobarlo matemáticamente. Aquí están las 20 notas de la clase, ordenadas de menor a mayor. | Caída en cascada de los 20 números formando una matriz o línea vertical/horizontal: 45, 52... hasta 100. El "85" se ilumina. | $N = 20$ (Datos) | *Pop-pop-pop* rápido (aparición de números). |
| **00:09 - 00:18** | **(Explicación 1: Posición)** Estar en el 15% superior significa superar al 85% de la clase. Es decir, buscamos el Percentil 85. Primero, hallamos su posición con esta fórmula. | Se escribe la fórmula de posición en pantalla. Los números 85 (K) y 20 (N) vuelan a la fórmula y se resuelve paso a paso. | $P_{85}$<br>

<br>$i = \left[ \frac{K(N-1)}{100} \right] + 1$<br>

<br>$i = 17.15$ | *Clics* tecnológicos al reemplazar los números. *Campana* al dar "17.15". |
| **00:18 - 00:30** | **(Explicación 2: El dilema)** Nos dio 17.15. La posición 17 es la nota 96, y la 18 es el 97. Como no es un número entero, usamos el estándar de oro de la ciencia de datos: La Interpolación Lineal. | Zoom intenso a las posiciones 17 y 18. Aparecen los números **96** y **97** en grande. Una flecha señala el espacio vacío entre ambos (el 0.15). | Posición 17: **96**<br>

<br>Posición 18: **97** | Sonido de zoom (lente de cámara). |
| **00:30 - 00:48** | **(Explicación 3: Interpolación)** Tomamos el valor entero, el 96... y le sumamos la parte decimal, cero punto quince, multiplicada por la diferencia entre ambos números. ¡La magia ocurre! | Aparece la fórmula de interpolación. Los elementos ($X_{[i]}, d, X_{[i]+1}$) bajan a su lugar: $96 + 0.15(97 - 96)$. Se resuelve visualmente. | $P_k = X_{[i]} + d(X_{[i]+1} - X_{[i]})$<br>

<br>$P_{85} = 96 + 0.15(1)$<br>

<br>**$P_{85} = 96.15$** | *Whoosh* suave para cada elemento que entra a la fórmula. *Ding* de victoria al final. |
| **00:48 - 01:00** | **(Aplicación)** Matemáticamente, el "15% superior" comienza en 96.15 puntos. Nuestro presumido sacó 85... así que ni siquiera está cerca. ¡Está en el percentil 60! | Una línea de meta brillante aparece en el 96.15. El estudiante con el "85" intenta saltarla pero choca contra una pared invisible mucho más atrás. | Corte: 96.15<br>

<br>Su nota: 85 | Sonido de golpe cómico (*bonk*). Alarma de "error" (*buzzer*). |
| **01:00 - 01:10** | **(Cierre)** La estadística no miente. Si tienes 50 datos y buscas el percentil 25, ¿cuál sería el valor de 'i'? | Transición rápida a un fondo limpio con la pregunta. | Calcula $i$ si $N=50$ y $K=25$<br>

<br>¡Comenta tu respuesta! 👇 | *Impacto de bajo profundo*. Fin de la música. |

---

### 🛠️ Recursos y Prompts IA

**1. Prompt para Manim (Para entregar a un modelo de código o programador):**

> "Genera un script en Python usando Manim Community. Configura la resolución para 
> **Escena 1:** Muestra un arreglo de 20 números ordenados: `[45, 52, 60, 63, 67, 70, 72, 75, 78, 80, 82, 85, 87, 90, 92, 94, 96, 97, 98, 100]`. Resalta el '85' en rojo.
> **Escena 2:** Usa `MathTex` para mostrar la fórmula de posición: $i = \frac{K(N-1)}{100} + 1$. Anima la sustitución $K=85$ y $N=20$, calculando hasta mostrar $i = 17.15$.
> **Escena 3:** Haz zoom en los elementos de las posiciones 17 y 18 del arreglo (que son 96 y 97).
> **Escena 4:** Escribe la fórmula de interpolación lineal: $P_k = X_{[i]} + d(X_{[i]+1} - X_{[i]})$. Subraya la parte entera $X_{[17]} = 96$ y la parte decimal $d = 0.15$. Sustituye los valores: $96 + 0.15(97 - 96)$ y resuelve para mostrar el resultado destacado en una caja verde: `P_{85} = 96.15`.
> **Escena 5:** Muestra una recta numérica final comparando el `85` (rojo) frente a la barrera del `96.15` (verde neón)."

**2. Prompt para ElevenLabs (Voz en Off):**

> "Genera una voz masculina joven, estilo youtuber educativo dinámico y sarcástico (estilo 'StatQuest' pero más juvenil). Tono investigador y un poco burlón al principio ('¿le creemos?'). Al explicar las fórmulas, la voz debe volverse clara, pausada y muy didáctica, marcando bien las pausas en las partes matemáticas ('el valor entero... y le sumamos la parte decimal'). Termina con energía retando a la audiencia."

**3. Prompt para Midjourney / IA de Imágenes (Para la Miniatura):**

> "A YouTube thumbnail, ultra-realistic, dramatic lighting. A giant exam paper with the grade '85/100' stamped in red, but a glowing neon green sign overlays it saying 'TOP 15% is 96.15!'. A big red 'X' mark. Educational math style, dark background like a blackboard with subtle math formulas, highly engaging, 8k resolution, vibrant colors --ar 16:9"