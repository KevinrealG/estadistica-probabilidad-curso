# Video 1: Probabilidad Clásica (A Priori)

- **Gancho (0:00 - 0:30)**

  - **Visual (Manim):** Un fondo oscuro con partículas que flotan. Se dibujan dos hebras de ADN que se entrelazan y se dividen, dando paso a un cuadro de Punnett 2x2. Los alelos del padre ($A$, $a$) y la madre ($A$, $a$) se deslizan hacia las celdas formando: $AA$, $Aa$, $Aa$ y $aa$.
  - **Audio:** Imagina que cruzamos dos especies con genes híbridos. Tenemos estos dos genes interactuando y, por las leyes de la genética, obtenemos exactamente cuatro resultados posibles. Pero aquí está el misterio: si necesitas aislar una característica específica, ¿cómo calculamos matemáticamente la probabilidad de que en la siguiente generación aparezca exactamente ese gen que buscas?

- **Intro y Promesa (0:30 - 0:55)**

  - **Visual (Manim):** El cuadro de ADN se desplaza a la izquierda. A la derecha, con tipografía dinámica y de colores vivos, aparece el título: "PROBABILIDAD CLÁSICA (A Priori o Teórica)". Se añade el subtítulo: "Cálculo antes de que ocurra el evento".
  - **Audio:** Hoy vamos a dominar la Probabilidad Clásica. Te voy a mostrar cómo calcular las chances de un evento mucho antes de que ocurra, siempre y cuando todos los resultados tengan exactamente la misma oportunidad de ganar.

- **Desarrollo (0:55 - 2:30)**

  - **Visual (Manim):** Aparece en grande y con un recuadro brillante la Regla de Laplace:$$P(A) = \frac{\text{Casos Favorables}}{\text{Casos Totales}}$$
  - **Audio:** La definición es sencilla y directa: la probabilidad de un evento es el número de casos favorables dividido entre el total de casos posibles.
  - **Visual (Manim):** Regresa el Cuadro de Punnett. El número total de celdas (4) se resalta con un borde blanco que parpadea, mientras que el recuadro del gen recesivo específico "$aa$" se tiñe de un color azul brillante, marcándolo como el "Caso Favorables".
  - **Audio:** Volvamos a nuestros genes. Tenemos 4 resultados posibles en total. Si buscamos el gen recesivo específico, "aa", vemos que solo aparece en 1 de esas 4 celdas. Nuestro cálculo es directo: 1 dividido entre 4. Esto nos da un 25% o 0.25.
  - **Visual (Manim/Simulación):** El cuadro se desvanece y en su lugar aparecen de forma animada: un dado girando, una moneda dando vueltas en el aire y una baraja de cartas abriéndose en abanico. Debajo de ellos se escribe la palabra: "EQUIPROBABLES".
  - **Audio:** ¿Cuándo usar la probabilidad clásica? Únicamente cuando los resultados son equiprobables. Es decir, cuando cada opción posible tiene exactamente el mismo peso y la misma probabilidad de salir, como en un dado perfecto, una moneda sin trucar o una baraja de cartas.

- **Cierre y Conexión (2:30 - 3:00)**

  - **Visual (Manim):** La escena se transforma en una cancha de fútbol en 2D (vista cenital o lateral). Se dibuja un punto de penal en color blanco y se coloca un balón sobre él. Al lado, la silueta de un jugador con el dorsal número 7 (Cristiano Ronaldo) se prepara para patear. Aparece un gran signo de interrogación arriba.
  - **Audio:** Todo esto funciona perfecto en la teoría, en un mundo donde todo es igual. Pero, ¿qué pasa en el mundo real donde no todo es equiprobable? Por ejemplo, si te pregunto: ¿Cuál es la probabilidad de que Cristiano Ronaldo anote un penal? Obviamente no es 50/50. Descubre cómo se calcula esto en el siguiente video. ¡Suscríbete para no perdértelo!

# Video 2: Probabilidad Frecuentista (A Posteriori)

- **Gancho (0:00 - 0:35)**

  - **Visual (Manim o simulación de videojuego pixel art 2D):** Un jugador de baloncesto animado lanza tiros libres uno tras otro. A un lado, un marcador digital acumula velozmente los tiros anotados y fallados. Una línea de tendencia en el fondo sube y baja de manera caótica.
  - **Audio:** Si LeBron James se para en la línea de tiros libres, ¿cuál es la probabilidad de que enceste? En el video anterior vimos que lanzar una moneda es 50/50. ¿Aplica lo mismo aquí? ¿O la mete o la falla? ¡Claro que no! En la vida real, los resultados no son equiprobables: el talento, la fatiga y la práctica cambian todo el juego.

- **Intro y Promesa (0:35 - 0:50)**

  - **Visual (Manim):** El título "Probabilidad Frecuentista (Experimental o A Posteriori)" aparece en pantalla, rodeado de gráficos estadísticos en movimiento y bases de datos simuladas.
  - **Audio:** Cuando no todos los resultados tienen la misma oportunidad de ocurrir, la teoría no nos sirve. Hoy descubriremos la Probabilidad Frecuentista, la herramienta que de verdad usan los científicos de datos y los analistas deportivos.

- **Desarrollo (0:50 - 2:40)**

  - **Visual (Manim):** Aparece la fórmula:$$P(A) \approx \frac{\text{Frecuencia del evento }(n_A)}{\text{Número total de experimentos }(N)}$$Se añade con un efecto de animación un gran texto al lado: "¡NO ES EXACTA! Es una aproximación" y luego el símbolo de límite:$$\lim_{N \to \infty}$$.
  - **Audio:** Su definición se basa en el registro de la experiencia: la probabilidad de un evento se estima dividiendo la cantidad de veces que ocurrió entre el total de intentos. Pero ojo: este cálculo no es exacto, es una aproximación. Para que sea realmente confiable, el número de repeticiones ($N$) debe ser gigantesco, buscando el límite matemático cuando las pruebas tienden al infinito.
  - **Visual (Pantalla de código o interfaz de análisis):** Se muestra un fragmento de datos (DataFrame de Pandas) donde se despliegan filas y filas de estadísticas reales de LeBron James, destacando su historial masivo. Se enfoca la cantidad: "11,300 intentos" y "8,300 aciertos".
  - **Audio:** Por ejemplo, miremos los datos históricos de LeBron James. No podemos saber el valor exacto de su probabilidad, pero al tener un número tan grande de repeticiones (más de once mil trescientos intentos), podemos buscar esa aproximación límite. Si dividimos 8,300 anotaciones entre sus 11,300 intentos, obtenemos aproximadamente un 73.4%.
  - **Visual (Manim):** Animación de un embudo donde caen miles de datos y sale la aproximación al límite. Luego, aparecen logos de bases de datos, sensores médicos y archivos de clima para mostrar cuándo usarla.
  - **Audio:** ¿Cuándo usamos la probabilidad frecuentista? Cuando tenemos acceso a datos históricos o cuando podemos repetir un experimento miles de veces. No te dará una probabilidad matemática perfecta, pero al buscar ese límite con un gran número de repeticiones, es lo más preciso que tendremos en el mundo real. ¡Para ponerlo en práctica, te dejo los datos históricos de Cristiano Ronaldo en la descripción para que calcules la aproximación de su probabilidad de penal y la dejes en los comentarios!

- **Cierre y Conexión (2:40 - 3:00)**

  - **Visual (Manim):** En pantalla se compara a la izquierda una moneda con un letrero de "50% Teórico", y a la derecha una gráfica en constante cambio con muchos datos que de a poco se estabiliza. Ambos lados se unen mediante una flecha o puente matemático.
  - **Audio:** Ya conoces la probabilidad matemática teórica y la experimental basada en acumular datos. Pero, ¿cómo se relacionan estas dos ideas? ¿Por qué al repetir y repetir la experimentación nos acercamos a la teoría? La respuesta está en la estadística más poderosa de todas: La Ley de los Grandes Números. ¡Haz clic para el siguiente video!

# Video 3: La Ley de los Grandes Números

- **Gancho (0:00 - 0:35)**

  - **Visual (Código Python o simulación en Manim):** Se simula una consola que lanza una moneda de forma virtual. En pantalla se leen los primeros resultados: "Cara, Cara, Cara". Se dibuja un gráfico donde la tasa de acierto de "Cara" se marca provisionalmente en el 100%.
  - **Audio:** Si lanzas una moneda 3 veces y las 3 veces cae cara, tu experimento (la frecuencia) te dice que la probabilidad de sacar cara es del 100%. Pero tu lógica teórica te dice que debería ser 50/50. ¿Quién tiene la razón, el experimento de hoy o la teoría matemática? La respuesta es: ambos, es solo cuestión de tiempo y volumen.

- **Intro y Promesa (0:35 - 0:50)**

  - **Visual (Manim):** Un título imponente se dibuja en pantalla: "LA LEY DE LOS GRANDES NÚMEROS". Debajo se visualiza el símbolo de un infinito ($\infty$) y miles de monedas cayendo en cascada.
  - **Audio:** Hoy vamos a descubrir la magia que une la teoría con la realidad: La Ley de los Grandes Números. Veremos cómo el caos individual se convierte en un patrón perfectamente predecible cuando el volumen es inmenso.

- **Desarrollo (0:50 - 2:40)**

  - **Visual (Manim / Gráfico dinámico):** Se despliega un gráfico de líneas (matplotlib/seaborn simulado). El eje X (horizontal) es el "Número de Lanzamientos" (de 1 a 1000). El eje Y (vertical) es la "Probabilidad acumulada" (de 0 a 1.0). Una línea roja horizontal y recta se posiciona en el valor 0.5 (la probabilidad teórica). De repente, una línea azul (la experimental) empieza a dibujarse desde la izquierda, saltando salvajemente de 0 a 1.0, 0.7, etc., pero a medida que el eje X avanza a 100, 500 y 1,000 lanzamientos, los saltos de la línea azul se reducen, aplanándose y pegándose casi por completo a la línea roja.
  - **Audio:** Esta ley establece que a medida que repetimos un experimento independiente muchísimas veces (un número grande de repeticiones), la probabilidad frecuentista (la azul) se aproxima, busca el límite y se estabiliza justo en la probabilidad teórica o clásica (la línea roja). Al principio, el azar hace locuras y es impredecible, pero con el tiempo y el gran volumen, la ley de los grandes números toma el control.
  - **Visual (Manim / Gráfico de auditoría o detección):** Se muestra un tablero de casino o un dado. Se simulan 10,000 lanzamientos de dado de forma rápida con números que corren. Una barra de alerta parpadea: "DADO SESGADO DETECTADO - 40% de 6s en lugar del 16.6%".
  - **Audio:** ¿Para qué se usa esto? Es la clave para determinar si un sistema o un juego están sesgados. Si lanzas un dado 10,000 veces y el número 6 aparece un 40% de las veces en lugar del 16.6% que dicta la teoría, la Ley de los Grandes Números te está gritando que el juego está trucado o que el dado tiene un peso extra.

- **Cierre y Conexión (2:40 - 3:00)**

  - **Visual (Manim / Efectos especiales en 2D):** El gráfico de la Ley de los Grandes Números se disuelve en una densa nube de estática digital. Se dibuja una Tierra en rotación y de la esquina superior cae un meteorito llameante. Aparece el texto "Casi 0% histórico".
  - **Audio:** Excelente, esta ley requiere que el experimento se repita miles de veces. Pero, ¿qué pasa cuando no existen datos históricos, el evento ocurre muy raras veces en la historia y no se puede repetir en un laboratorio? Es decir, ¿qué hacemos cuando las matemáticas del infinito no nos pueden salvar? En el próximo video, la intuición toma el control

# Video 4: Probabilidad Subjetiva

- **Gancho (0:00 - 0:35)**

  - **Visual (Simulación / Video generado por IA o animación):**
    En pantalla se muestra un tranquilo barrio residencial de día, con un pequeño auto rojo estacionado junto a la acera. De repente, desde el cielo, un meteorito envuelto en fuego desciende a gran velocidad e impacta directamente en el auto, aplastándolo por completo con un efecto de humo, chispas y escombros (como en image_0.png).
  - **Audio:** ¿Cuál es la probabilidad de que tu carro sea destruido por un meteorito el día de mañana? Piénsalo bien. No puedes usar la probabilidad clásica porque "que caiga o no" no son opciones equiprobables. Tampoco puedes usar la frecuentista porque, por suerte, no tenemos registros de millones de autos aplastados por meteoritos para calcular su límite. Aquí es donde la intuición toma el control.

- **Intro y Promesa (0:35 - 0:50)**

  - **Visual (Manim):** De las ruinas del meteorito se levantan de forma dinámica las palabras: "PROBABILIDAD SUBJETIVA: Cuando la intuición es el único dato disponible".
  - **Audio:** Bienvenidos al territorio donde la experiencia humana llena el vacío de los números. Hoy aprenderemos sobre la Probabilidad Subjetiva, cuando la experticia se convierte en tu mejor aproximación matemática.

- **Desarrollo (0:50 - 2:30)**

  - **Visual (Manim):** Se dibujan tres mentes pensantes (ilustradas con engranajes en movimiento de distintos colores). De cada una brota un número de probabilidad diferente ante el mismo caso del meteorito: "0.000001%", "0.005%" y "0.00000002%". Se visualiza un letrero de advertencia: "Límites: Falta de objetividad".
  - **Audio:** La probabilidad subjetiva es una estimación que hace una persona o un grupo basándose en su propio conocimiento, su experiencia previa y su intuición para eventos únicos o raros. Su principal diferencia y limitación frente a las otras reglas es que aquí no hay una única probabilidad "correcta"; el resultado depende totalmente de la persona que lo calcula.
  - **Visual (Manim):** Pantalla dividida en dos simulaciones científicas: a la izquierda, un astrónomo analizando la trayectoria de asteroides reales en su monitor; a la derecha, una persona común mirando al cielo asustada.
  - **Audio:** Por ejemplo, la probabilidad subjetiva que asigne un astrofísico que lleva años analizando el espacio será muchísimo más cercana a la realidad que la de cualquiera de nosotros, ya que él se apoya en su conocimiento de experimentos relacionados y el contexto del universo. ¿Cuándo se usa? Para valorar riesgos de seguros, predecir el éxito de una innovación tecnológica o en grandes decisiones de negocios donde simplemente no existe un historial.

- **Cierre y Conexión (2:30 - 3:00)**

  - **Visual (Manim):** Los datos se borran y se traza una línea continua de tiempo horizontal que se extiende sin interrupciones. Se resalta en un color brillante un intervalo de tiempo específico (por ejemplo, entre las 2:00 PM y las 2:15 PM). Aparece el texto "¿Resultados Continuos?".
  - **Audio:** Hasta ahora en esta serie, todos nuestros resultados han sido discretos: genes, canastas o caras de una moneda. Pero, ¿qué pasa cuando el mundo se vuelve continuo? Por ejemplo: ¿cuál es la probabilidad de llegar a una cita exactamente en un intervalo de tiempo continuo, como entre las 2:00 y las 2:15? Ahí entra en juego la hermosa Probabilidad Geométrica, y ese es el tema de nuestro próximo video. ¡Suscríbete y descúbrelo!

## 🛠️ Sugerencias Técnicas para Crear las Animaciones (sin mostrar tu rostro)

Como el objetivo es que el video esté compuesto enteramente por gráficos dinámicos y código, aquí tienes herramientas y métodos recomendados para realizar las escenas clave:

- **La animación del meteorito y el auto (Video 4):**
  - **Opción con IA (Recomendada):** Usa herramientas de generación de video (como Luma Dream Machine, Runway Gen-2 o Pika) ingresando el prompt de la secuencia (ej. image_0.png en secuencia de video). Puedes usar imágenes clave de estilo caricatura en 2D (cartoon style flat animation) y pedirle a la IA que cree el movimiento del meteorito cayendo y aplastando el auto rojo.
  - **Opción por código (Manim / Pygame):** Puedes programar un simulador 2D sencillo en Python con la librería pygame o en Manim utilizando físicas básicas: dibuja un rectángulo que simule el auto (o un asset SVG) y haz que un círculo de partículas de fuego (meteorito) descienda rápidamente por el eje Y/X para que al colisionar, el auto cambie de forma (escala y deformación en el eje Y) liberando partículas que simulen el humo y los fragmentos.
- **Gráfico de la Ley de los Grandes Números (Video 3):**
  - Puedes grabarlo ejecutando un script de Python en tiempo real usando librerías como Matplotlib o Seaborn activando el modo animado (matplotlib.animation). Solo necesitas un código que vaya arrojando valores aleatorios entre 0 y 1 (donde si es $>0.5$ es cara) y que calcule la media acumulada para ir graficándola punto por punto hasta llegar a 1000 iteraciones, logrando el efecto en vivo.
- **Cuadro de Punnett y Genética (Video 1):**
  - Esto se resuelve con bastante facilidad y un resultado profesional utilizando Manim (la librería matemática de Python) con animaciones de tipo Transform para mover y duplicar los textos de los alelos ($AA$, $Aa$, $aa$) hacia las celdas de un objeto Table o Mobject matriz en 2x2.