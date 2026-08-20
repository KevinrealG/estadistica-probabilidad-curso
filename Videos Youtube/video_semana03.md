# Aquí tienes la versión ampliada y estructurada bajo mi rol de **STEM Video Producer AI**, integrando la precisión técnica y matemática que solicitaste, manteniendo el enfoque en retención visual.

### 🎬 Resumen del Video

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