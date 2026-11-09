1. # Tecnicas de Conteo Fundamento, combinaciones, permutaciones, orden
**Gancho (0:00 - 0:40)**

* **Visual (Manim / Animación 2D):** Un fondo de colores pastel. Unas manos animadas (representando a un bebé) juegan con seis coloridos bloques de madera. Las letras en los bloques son claras: dos 'A', dos 'P' y dos 'M' ($A, A, P, P, M, M$). Las manitos empujan cuatro bloques al azar, formando una fila en el centro de la pantalla. Aparece un gran signo de interrogación brillante.
> **Audio:** Imagina que tu bebé está jugando con estos seis bloques de letras: tiene dos 'A', dos 'P' y dos 'M'. Si empuja cuatro bloques y los alinea al azar, ¿cuál es la probabilidad exacta de que mágicamente forme la palabra "MAMA" o la palabra "PAPA"? Tu primer instinto matemático podría ser intentar escribir todas las combinaciones posibles en un papel para contar cuántas son correctas. Pero te advierto: si intentas contar los escenarios uno por uno, tu bebé aprenderá a hablar antes de que termines.

**Intro y Promesa (0:40 - 0:55)**

* **Visual (Manim):** Los bloques de madera estallan en una nube de polvo mágico y se reorganizan formando ecuaciones. En el centro aparece el título: *"TÉCNICAS DE CONTEO"*, y debajo flotan las palabras: *"Permutaciones"*, *"Combinaciones"* y *"Orden"*.
> **Audio:** Hoy descubriremos qué son exactamente las Técnicas de Conteo y cómo nos permiten descubrir el tamaño de un universo ra´pidamente

**Desarrollo: ¿Qué son las técnicas de conteo? (0:55 - 1:40)**

* **Visual (Manim):** Se dibuja el símbolo matemático del Espacio Muestral ($\Omega$). Se hace un zoom dentro del símbolo y empiezan a multiplicarse miles de pequeños puntos de datos hasta saturar la pantalla. Un cursor intenta hacer clic en cada uno (contando $1, 2, 3...$) pero aparece un letrero rojo de *"ERROR: Demasiados datos"*.
> **Audio:** ¿Qué son las técnicas de conteo? En probabilidad clásica, para usar la regla de Laplace, necesitas conocer el tamaño total de tu espacio muestral; es decir, todos los resultados posibles. Pero en el mundo real los escenarios son masivos y contar uno por uno es logísticamente tedioso. Las técnicas de conteo son operaciones matemáticas basadas en multiplicaciones y factoriales que nos dan el total exacto. Literalmente, son estrategias  para "contar sin contar".

**Desarrollo: Estrategias, el Orden y el Cálculo (1:40 - 2:50)**

* **Visual (Manim):** La pantalla se divide en dos con una línea brillante.
* **Izquierda ("EL ORDEN IMPORTA"):** Se escribe *"Permutación"*. Aparecen los bloques $M-A-M-A$. Luego cambian a $A-M-A-M$. Se marca con una $X$ roja gigante, demostrando que aunque son las mismas letras, no son la misma palabra.
* **Derecha ("EL ORDEN NO IMPORTA"):** Se escribe *"Combinación"*. Aparece un pequeño saco o bolsa de tela. Entran los bloques $M, M, A, A$. Se agitan y salen. El resultado se marca con un check verde $\checkmark$.


> **Audio:** Estas técnicas son la base fundamental para calcular probabilidades en cualquier espacio muestral finito. Dominarlas te permite resolver problemas extremadamente complejos de forma eficiente. Y todo el secreto se reduce a una sola pregunta: ¿Importa el orden?
* **Visual (Manim):** En el lado de la Permutación, los bloques comienzan a multiplicarse usando la regla de variación/permutación (cálculos factoriales flotando: $n!, (n-r)!$). Las cifras crecen rápidamente.
> **Audio:** Si el orden importa, usamos una Permutación. Para formar la palabra "MAMA", la posición de cada bloque es vital; si cambias una 'M' por una 'A', destruyes la palabra. En cambio, si el orden no importa—digamos que solo quieres saber cuántos grupos diferentes de 4 letras puedes meter en una bolsa para dárselos al bebé—usas una Combinación. Con estas fórmulas, pasas de estar horas sumando con los dedos, a estructurar el universo del azar en un solo paso.

**Cierre y Conexión (2:50 - 3:20)**

* **Visual (Manim):** Los bloques de letras regresan al centro de la pantalla. A través de un rápido cálculo matemático visual ($P(MAMA) = \text{Fórmula}$), los bloques se acomodan perfectamente formando la palabra $MAMA$ en letras doradas. El número resultante de la probabilidad destella en pantalla.
> **Audio:** Con las técnicas de conteo, ya tienes el control matemático absoluto sobre los espacios finitos. Tienes la llave para saber exactamente qué tan probable es un evento raro. Pero, ¿qué pasa si las reglas del juego cambian y los datos sí se pueden repetir? ¿Cómo se transforma nuestro universo si un mismo elemento puede reaparecer una y otra vez? Para ver la diferencia matemática entre repetir y no repetir, vamos a descifrar el misterio de los códigos numéricos. Y ese, será nuestro próximo video. ¡Suscríbete, deja un buen like y nos vemos allá!
2. # ¿Cuántos números de 3 dígitos se pueden formar utilizando los dígitos {1, 2, 3, 4, 5} 
  ## Video: Técnicas de Conteo (Con y Sin Repetición)

**Gancho (0:00 - 0:35)**

* **Visual (Manim / Simulación 2D):** Un maletín de alta seguridad aparece en pantalla. Su cerradura es digital y requiere un código exacto de 3 dígitos. Sin embargo, el teclado numérico está roto y solo funcionan cinco botones: el 1, el 2, el 3, el 4 y el 5. Aparece una lupa sobre la cerradura.
* **Audio:** Eres un analista de seguridad intentando abrir este maletín. El código tiene exactamente 3 dígitos, y sabes que el dueño solo configuró el sistema usando los números del 1 al 5. Pero aquí está el verdadero dilema del hacker: ¿el sistema permite repetir números como "3-3-3", o cada dígito debe ser único, como "1-4-2"? Esa simple regla dicta si tienes el tiempo suficiente para adivinar el código o si estás perdiendo el tiempo.

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** El maletín se abre, liberando números que flotan formando ecuaciones. Aparece el título en pantalla: "CONTEO: Con y Sin Repetición".
* **Audio:** Bienvenidos de nuevo.  Usaremos el principio multiplicativo para calcular exactamente cuántas combinaciones existen cuando las reglas permiten repetir datos, y cómo se desploma ese número cuando la repetición está prohibida.

**Desarrollo: Con Repetición (0:50 - 1:45)**

* **Visual (Manim):** Se dibujan tres casillas vacías en el centro de la pantalla: `[ ] [ ] [ ]`. Arriba, flotan los cinco números disponibles envueltos en esferas de luz: `{1, 2, 3, 4, 5}`. Para la primera casilla, una llave inglesa (representando el algoritmo) cuenta las esferas y aparece un 5 debajo de la primera casilla. Para la segunda casilla, las esferas no desaparecen, siguen siendo cinco y aparece otro 5 debajo. Para la tercera, ocurre lo mismo y aparece un tercer 5, formando finalmente la ecuación: $5 \times 5 \times 5 = 5^3 = 125$.
* **Audio:** Empecemos con el escenario donde sí hay repetición. Imagina tus tres espacios vacíos. Para el primer dígito del código, tienes 5 opciones posibles. Como el sistema te permite usar el mismo número varias veces, para el segundo dígito sigues teniendo las mismas 5 opciones. Y para el tercero, adivinaste, otras 5 opciones. Por el principio fundamental del conteo, simplemente multiplicamos 5 por 5 por 5. Esto nos da 125 números distintos posibles.

**Desarrollo: Sin Repetición (1:45 - 2:35)**

* **Visual (Manim):** La pantalla se reinicia. Vuelven las tres casillas vacías y las cinco esferas numéricas. Para la primera casilla, hay 5 opciones, el número "2" baja a la casilla y desaparece del grupo de arriba. Para la segunda casilla, la llave inglesa cuenta las esferas restantes, ¡solo quedan 4!, aparece un 4 debajo de la segunda casilla y el número "5" baja y desaparece. Para la tercera casilla, solo quedan 3 esferas, aparece un 3 y la ecuación se traza matemáticamente: $5 \times 4 \times 3 = 60$.
* **Audio:** Ahora, ¿qué pasa si el sistema de seguridad es estricto y no permite repetición? Esto es una permutación sin reemplazo. Para tu primer espacio, sigues teniendo 5 opciones. Pero cuidado: el número que elijas se agota, ya no puedes volver a usarlo. Así que, para tu segundo espacio, tu piscina de opciones se reduce a 4. Y para tu último espacio, solo te quedan 3 números disponibles. Multiplicamos 5 por 4 por 3, y el resultado es 60.

**Cierre y Conexión (2:35 - 3:00)**

* **Visual (Manim):** Los dos resultados se enfrentan en pantalla como en un ring de boxeo: 125 (Con Repetición) vs 60 (Sin Repetición). El número 125 es más del doble de grande, destacando visualmente la inmensa diferencia. Luego, ambos números se disuelven y empiezan a formar puntos de datos que trazan una campana de Gauss.
* **Audio:** Con solo bloquear la capacidad de repetir elementos, tus opciones se redujeron a menos de la mitad, pasando de 125 a solo 60. Las reglas de reemplazo cambian la realidad entera de tus probabilidades. 
3. # Principio de Multiplicación (Regla del "y")
Aquí tienes el guion para el video del Principio de la Multiplicación, respetando el formato de viñetas con párrafos únicos, utilizando animaciones puras (sin aparecer en cámara) y con un tema fresco y distinto.

## Video: Principio de la Multiplicación (La Regla del "Y")

**Gancho (0:00 - 0:35)**

* **Visual (Manim / Simulación 2D):** Una escena en estilo *pixel art* de un videojuego retro de atracos. Un personaje (un ladrón) está dentro de la bóveda de un banco con el botín. La interfaz del juego muestra en pantalla: *"PLAN DE ESCAPE"*. Paso 1: Elegir Salida (aparecen 3 íconos: Ventilación, Puerta Principal, Alcantarillas). Paso 2: Elegir Vehículo (aparecen 4 íconos: Moto, Furgoneta, Helicóptero, Patineta). Un reloj hace una cuenta regresiva rápida.
* **Audio:** Imagina que estás jugando un videojuego de escapes y acabas de vaciar la bóveda. Ahora debes planear tu escape perfecto. El juego te obliga a elegir una ruta de salida entre 3 opciones: la ventilación, la puerta principal o las alcantarillas. Pero eso no es todo, también debes elegir un vehículo de escape entre 4 opciones: una moto, una furgoneta, un helicóptero o una patineta. Si obligatoriamente necesitas elegir una salida "Y" un vehículo para ganar, ¿cuántos planes de escape únicos puedes formar en total antes de que se acabe el tiempo?

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** El videojuego se pausa. Las palabras *"PRINCIPIO MULTIPLICATIVO"* aparecen en letras de *pixel art*, y luego se transforman en un elegante y brillante texto matemático en LaTeX. Debajo, se enciende un letrero de neón que dice: *"LA REGLA DEL 'Y'"*.
* **Audio:**  Hoy vamos a dominar el Principio de la Multiplicación. Vas a aprender cómo calcular el tamaño de tus opciones totales de forma instantánea cuando necesitas que ocurra un evento y luego otro evento de forma consecutiva.

**Desarrollo: Construyendo el árbol (0:50 - 1:45)**

* **Visual (Manim):** Se dibuja un diagrama de árbol clásico. Desde un nodo inicial salen 3 ramas gruesas (las 3 salidas). Luego, desde el final de *cada una* de esas 3 ramas, brotan 4 nuevas ramas más pequeñas (los 4 vehículos). Los 12 puntos finales se iluminan uno por uno contando del 1 al 12. Finalmente, el árbol se encoge y da paso a una enorme ecuación central en una caja brillante: $3 \times 4 = 12$.
* **Audio:** Si intentáramos dibujar cada plan de escape uno por uno usando un diagrama de árbol, veríamos que por cada una de las 3 salidas posibles, se abren 4 nuevos caminos correspondientes a los vehículos. Si contamos los puntos finales, tenemos 12 rutas. Pero en la vida real, con datos masivos, los árboles se vuelven gigantescos e imposibles de dibujar. Aquí es donde el principio multiplicativo nos salva la vida: si tienes una cantidad de opciones para una primera etapa, y otra cantidad para una segunda, simplemente multiplicas ambos números. Tres salidas multiplicadas por cuatro vehículos, nos da exactamente los mismos 12 planes de escape, pero en un segundo.

**Desarrollo: La palabra clave "Y" (1:45 - 2:30)**

* **Visual (Manim):** La pantalla se divide. A la izquierda, la letra *"Y"* se resalta en verde brillante junto a un símbolo de multiplicación ($\times$). A la derecha, la letra *"O"* se resalta en rojo junto a un símbolo de suma ($+$). Luego, la pantalla se centra en un candado numérico cilíndrico de 4 ruedas (dígitos del 0 al 9). Las ruedas giran velozmente mientras se forma la ecuación: $10 \times 10 \times 10 \times 10 = 10,000$.
* **Audio:** El secreto definitivo para saber cuándo usar este principio está en el lenguaje: la letra "Y". Siempre que tu problema exija que ocurra la etapa A, "Y" la etapa B, "Y" la etapa C para completar un proceso, debes multiplicar. Piensa en un candado numérico de 4 ruedas. Necesitas configurar el primer número, "Y" el segundo, "Y" el tercero, "Y" el cuarto. Como cada rueda es independiente y tiene 10 opciones, multiplicamos 10 por 10 por 10 por 10, lo que nos da 10,000 combinaciones posibles al instante, sin dibujar ni un solo diagrama.

**Cierre y Conexión (2:30 - 3:00)**

* **Visual (Manim):** El candado numérico se abre de golpe, liberando esferas de luz que se agrupan en el centro para formar el enorme símbolo matemático del Factorial ($!$). Las esferas comienzan a alinearse en fila, intercambiando posiciones rápidamente de todas las formas posibles como si compitieran por el primer lugar.
* **Audio:** La regla de la multiplicación es la base que hace funcionar a todas las fórmulas avanzadas de probabilidad. Pero, ¿qué pasaría si en lugar de elegir entre opciones separadas, tuvieras un grupo cerrado de elementos y simplemente quisieras saber de cuántas formas puedes ordenarlos absolutamente todos en una sola fila? Ahí es donde la multiplicación consecutiva evoluciona hacia una de las operaciones más hermosas de la matemática: El Factorial. Y ese, será nuestro próximo video. 


# Video 1: El Factorial

**Gancho (0:00 - 0:35)**

* **Visual (Manim / Simulación 2D):** Una interfaz de una aplicación de música. Se muestra una lista de reproducción con exactamente 5 canciones. Un cursor animado hace clic en el icono de "Modo Aleatorio" (Shuffle). Inmediatamente, las canciones comienzan a cambiar de lugar a gran velocidad. Aparece un texto brillante parpadeando en la pantalla: *"¿Probabilidad de que suenen en tu orden perfecto?"*.
* **Audio:** Imagina que tienes una lista de reproducción con tus 5 canciones favoritas y le das al botón de modo aleatorio. ¿Cuál es la probabilidad de que la aplicación decida reproducirlas mágicamente en tu orden perfecto, desde la mejor hasta la menos buena? Para calcularlo, primero necesitas descubrir de cuántas formas diferentes se pueden llegar a ordenar esas 5 canciones. Si intentas adivinar, puede que tu mente diga 10 o 20 formas, pero la matemática detrás de esto te va a sorprender.

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** La interfaz de música se desintegra y sus píxeles forman un gigantesco signo de exclamación ($!$) que brilla con luces de neón. Aparece el título: *"EL FACTORIAL"*. Debajo, se escribe el subtítulo: *"La matemática del orden total"*.
* **Audio:** Bienvenidos al símbolo más efusivo de las matemáticas. Hoy vamos a conocer el Factorial, la operación maestra que nos permite calcular instantáneamente de cuántas formas distintas podemos ordenar un grupo completo de elementos en una sola fila.

**Desarrollo: Construyendo el Orden (0:50 - 1:45)**

* **Visual (Manim):** Aparecen 5 espacios vacíos en pantalla: `[ ] [ ] [ ] [ ] [ ]`. Sobre ellos flotan 5 notas musicales de distintos colores. Para la primera casilla, el número "5" aparece debajo y una nota cae dentro. Para la segunda, aparece un "4" y cae otra nota. Luego un "3", un "2" y un "1". Debajo de las casillas se forma y se resuelve la ecuación: $5 \times 4 \times 3 \times 2 \times 1 = 120$.
* **Audio:** Para resolver el problema, usemos el principio multiplicativo. Tienes 5 espacios vacíos. Para elegir la primera canción, la aplicación tiene 5 opciones posibles. Una vez que elige una, le quedan 4 opciones para el segundo lugar. Luego le quedan 3, luego 2 y finalmente 1 sola canción obligatoria para el último lugar. Al multiplicar todas estas opciones de forma descendente, el resultado es 120. ¡Existen 120 formas distintas de ordenar solo 5 canciones! Tu probabilidad de obtener tu orden perfecto es de 1 en 120.

**Desarrollo: El Símbolo y la Regla (1:45 - 2:40)**

* **Visual (Manim):** La larga ecuación multiplicativa se comprime matemáticamente hasta convertirse simplemente en $5!$. El símbolo pulsa. Luego, una nota dorada aparece con el texto: *"Regla de oro: $0! = 1$"*. Finalmente, se dibuja una baraja de 52 cartas. Se aplica el factorial ($52!$) y el resultado estalla llenando la pantalla con el número $8.06 \times 10^{67}$ mientras aparece una galaxia de fondo.
* **Audio:** En probabilidad, esta acción de multiplicar un número entero por todos sus enteros anteriores hasta llegar al uno es tan recurrente que los matemáticos le inventaron su propio símbolo: el signo de exclamación. Esto se lee como "Cinco Factorial". Como regla de oro para que las ecuaciones avanzadas no se rompan, debes saber que el cero factorial siempre es igual a uno. Y ten cuidado, porque los factoriales crecen de forma monstruosa: si intentas ordenar una baraja de 52 cartas, el resultado de "52 factorial" es un número tan masivo que supera a la cantidad de átomos en todo el universo observable.

**Cierre y Conexión (2:40 - 3:10)**

* **Visual (Manim):** Regresan las 5 notas musicales a la pantalla. Un brazo robótico desciende, agarra aleatoriamente solo 3 notas y las guarda en una carpeta que dice *"Mini-Playlist"*. El símbolo de factorial ($!$) mira la acción con un enorme signo de interrogación arriba.
* **Audio:** Ordenar absolutamente todo el grupo de datos es fascinante. Pero, ¿qué pasaría si no queremos escuchar las 5 canciones? ¿Qué pasa si solo queremos seleccionar 3 de ellas al azar para hacer una mini-lista y no nos importa en lo absoluto en qué orden suenen? El factorial directo ya no nos sirve porque nos daría datos duplicados. Para resolver esto, necesitamos una nueva herramienta: Los Números Combinatorios. Y ese, será nuestro próximo video. ¡Suscríbete y acompáñame!

---

# Video 2: Los Números Combinatorios

**Gancho (0:00 - 0:35)**

* **Visual (Manim / Simulación 2D):** Una vista esquemática de la sala de control de una agencia espacial. Un holograma en el centro muestra el planeta Marte. En la base de la pantalla, hay 8 avatares distintos de astronautas. Una interfaz parpadea: *"MISIÓN MARTE: Seleccionar 3 tripulantes"*.
* **Audio:** Imagina que eres el director de una agencia espacial. Tienes a tu disposición un grupo de 8 astronautas de élite, pero la cápsula que viajará a Marte solo tiene 3 asientos. Los roles en la nave son cooperativos y exactamente iguales. Eso significa que enviar a los astronautas Alice, Bob y Charlie, es exactamente el mismo equipo que enviar a Charlie, Bob y Alice. Si necesitas calcular cuántos equipos diferentes puedes formar en total, usar un factorial normal arruinará tus cálculos porque estarías contando el mismo equipo múltiples veces.

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** Los avatares se desvanecen. En el centro de la pantalla se dibujan unos paréntesis grandes, con el número 8 en la parte superior y el número 3 en la inferior: $\binom{8}{3}$. Aparece el título: *"NÚMEROS COMBINATORIOS"*. Subtítulo: *"Elegir sin importar el orden"*.
* **Audio:** Bienvenidos al arte abstracto de seleccionar grupos. Hoy descubriremos los Números Combinatorios, la estructura matemática que nos permite calcular con precisión quirúrgica cuántos subgrupos únicos podemos extraer de un conjunto más grande cuando el orden no importa en lo absoluto.

**Desarrollo: La Estructura y la Fórmula (0:50 - 1:45)**

* **Visual (Manim):** El símbolo $\binom{8}{3}$ se desplaza a la izquierda y se expande en su fórmula general: $\frac{n!}{k!(n-k)!}$. El $n$ (grupo total) se reemplaza por el 8. El $k$ (asientos) se reemplaza por el 3. La ecuación se transforma paso a paso hasta quedar como: $\frac{8!}{3! \times 5!}$.
* **Audio:** Un número combinatorio se escribe como dos números apilados entre paréntesis, y se lee como "8 sobre 3". Para calcular su valor real, usamos la fórmula matemática de las combinaciones. En la parte de arriba del fraccionario, ponemos el factorial de nuestro grupo total, es decir, el 8. En la parte de abajo, ponemos el factorial de los espacios que vamos a llenar, que es el 3, multiplicado por la diferencia entre los dos, que es 8 menos 3, dándonos 5 factorial.

**Desarrollo: El Truco de la Cancelación (1:45 - 2:35)**

* **Visual (Manim):** La ecuación se desarrolla. El numerador pasa de $8!$ a escribirse como $8 \times 7 \times 6 \times 5!$. El denominador se mantiene como $3 \times 2 \times 1 \times 5!$. Una línea roja tipo "slash" tacha el $5!$ de arriba y el $5!$ de abajo, eliminándolos. Nos queda la fracción $\frac{8 \times 7 \times 6}{6}$, que se simplifica y estalla revelando el número **56**. Se dibujan 56 mini-cohetes en el fondo.
* **Audio:** Antes de que busques una calculadora para resolver esos factoriales gigantes, te voy a enseñar el mejor truco de los estadísticos: la cancelación. En lugar de desarrollar todo el 8 factorial hasta el número uno, lo escribimos solo como 8 por 7 por 6... por 5 factorial. ¿Para qué? Para poder cancelar directamente ese 5 factorial de arriba con el 5 factorial de abajo. El problema se reduce a 8 por 7 por 6, dividido entre 3 por 2 por 1. Al resolver esa simple fracción, el resultado es 56. ¡Tienes exactamente 56 formas únicas de armar tu tripulación a Marte!

**Cierre y Conexión (2:35 - 3:00)**

* **Visual (Manim):** Los 56 mini-cohetes se agrupan, apilándose uno sobre otro para formar las barras de un histograma. Una línea curva y suave atraviesa las puntas de las barras formando la gráfica de una Distribución Binomial. En una esquina, la fórmula de la Binomial aparece resaltando su componente combinatorio: $\binom{n}{k} p^k q^{n-k}$.
* **Audio:** Estos números combinatorios son la pieza fundamental que nos faltaba en nuestro arsenal estadístico. Ahora que sabemos cómo empaquetar y calcular estos subgrupos de forma limpia, estamos listos para insertarlos dentro de fórmulas predictivas reales. En el próximo video, usaremos este mismo número combinatorio como el motor para construir una de las gráficas de probabilidad más importantes del mundo: La Distribución Binomial. ¡Suscríbete, deja un buen like y prepárate para el siguiente nivel matemático!

Aquí tienes el guion para el video de Permutación Básica, cumpliendo con la estructura de viñetas, párrafos únicos por sección, y el formato 100% de animación (Manim/código) sin apariciones a cámara. He utilizado un tema de logística y algoritmos de enrutamiento para mantener el enfoque analítico.

# Video: Permutación Básica

**Gancho (0:00 - 0:35)**

* **Visual (Manim / Simulación 2D):** Un mapa digital oscuro estilo radar aparece en pantalla con 5 nodos brillantes etiquetados del $A$ al $E$ (representando ciudades o servidores). Un dron de entregas (o paquete de datos) se sitúa en el centro. Se traza rápidamente una ruta: $A \to B \to C$, marcando un tiempo de "15 ms". Luego la ruta se borra y se traza a la inversa: $C \to B \to A$, marcando un tiempo de "45 ms" debido a la resistencia de la red. Un reloj de batería parpadea en rojo.
* **Audio:** Eres el ingeniero de datos a cargo de trazar la ruta de un dron de entregas urgentes. Tienes 5 destinos críticos en el mapa, pero la batería solo alcanza para visitar exactamente 3 antes de volver a la base. ¿El orden importa? Por supuesto. Volar de la ciudad A a la B y luego a la C toma un tiempo y energía completamente distintos que hacer la ruta a la inversa debido al viento y la distancia. Si necesitas programar un algoritmo para encontrar la ruta más rápida, primero debes saber exactamente cuántas rutas posibles existen. Y calcular eso a mano te tomará más tiempo del que le queda a la batería.

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** El mapa digital se desintegra en partículas geométricas que se reagrupan en el centro para formar el título brillante: *"PERMUTACIÓN BÁSICA"*. Debajo, un subtítulo dinámico se escribe como si fuera código: `orden == True`.
* **Audio:** Bienvenidos a la matemática de la logística y la precisión. Hoy vamos a dominar la Permutación Básica, la herramienta estadística que te permite calcular al instante de cuántas formas puedes elegir y ordenar un grupo específico de elementos cuando la posición de cada uno cambia por completo el resultado final.

**Desarrollo: La Lógica del Espacio (0:50 - 1:45)**

* **Visual (Manim):** Se dibujan tres ranuras vacías en pantalla: `[ ] [ ] [ ]`. Sobre ellas flotan los cinco nodos del mapa: $\{A, B, C, D, E\}$. Para la primera ranura, el número $5$ aparece debajo y el nodo $C$ cae dentro. Para la segunda ranura, aparece un $4$ y el nodo $A$ ocupa el lugar. Para la tercera ranura, aparece un $3$ y el nodo $E$ se inserta. Debajo de las ranuras, la ecuación se escribe sola: $5 \times 4 \times 3 = 60$.
* **Audio:** A diferencia del factorial puro donde estábamos obligados a ordenar absolutamente todos los elementos de un conjunto, en una permutación básica solo tomamos una fracción del grupo total. Si aplicamos el principio multiplicativo a nuestra ruta: para la primera parada, el dron tiene 5 opciones posibles. Una vez que hace esa entrega, le quedan 4 destinos disponibles para la segunda parada. Y para la tercera y última parada, su universo se reduce a solo 3 opciones. Si multiplicamos 5 por 4 por 3, obtenemos 60. Existen exactamente 60 rutas únicas.

**Desarrollo: La Fórmula Matemática (1:45 - 2:35)**

* **Visual (Manim):** Las ranuras desaparecen y la fórmula oficial de la permutación se escribe en elegante formato LaTeX: 
$$P(n,r) = \frac{n!}{(n-r)!}$$


. La variable $n$ se ilumina y se transforma en un $5$ (Destinos Totales). La variable $r$ se transforma en un $3$ (Paradas). La ecuación se actualiza a: 
$$\frac{5!}{(5-3)!} = \frac{5!}{2!}$$


. El numerador se expande como $5 \times 4 \times 3 \times 2!$, y una animación de corte de espada ("slash" rojo) cancela el $2!$ de arriba con el $2!$ de abajo. El resultado brillante $60$ ocupa la pantalla.
* **Audio:** Para no tener que hacer multiplicaciones manuales cuando trabajes con bases de datos de miles de registros, usamos la fórmula general de la permutación. "$n$" es tu número total de elementos disponibles (tus 5 destinos), y "$r$" es el número de espacios que vas a llenar (tus 3 paradas). Arriba colocamos 5 factorial, y abajo la resta de 5 menos 3, es decir, 2 factorial. Aquí aplicamos nuestro viejo truco de cancelación: desarrollamos el 5 factorial solo hasta el 2 factorial para cancelarlo directamente con el de abajo, dejándonos exactamente la misma operación: 5 por 4 por 3. ¡60 rutas calculadas con código en milisegundos!

**Cierre y Conexión (2:35 - 3:00)**

* **Visual (Manim):** El número $60$ se transforma en un bloque de código y se guarda en un candado cerrado marcado como *"Permutación"*. A su lado, aparece un candado abierto marcado como *"Combinación"*. El número $60$ salta al candado abierto, se divide por $3!$, y se transforma en un número $10$. Aparece un signo de interrogación.
* **Audio:** La permutación básica es el motor de los algoritmos de enrutamiento y las contraseñas, porque asume que cada ligero cambio de posición crea un universo nuevo. Pero, ¿y si las reglas del juego cambian de repente? ¿Qué pasaría si tu director te dice que ya no le importa el orden en que entregues, sino que solo quiere saber cuáles 3 paquetes específicos vas a subir al dron del grupo de 5? Ese simple cambio destruye la permutación y nos devuelve al mundo de las combinaciones. ¿Cómo se conectan y se dividen estas dos fórmulas? Ese será nuestro próximo desafío. ¡Suscríbete, deja un buen like y nos vemos en el siguiente algoritmo!

6. #  Permutaciones con Repetición

## Video: Permutaciones con Repetición

**Gancho (0:00 - 0:40)**

* **Visual (Manim / Simulación 2D):** Una pantalla de terminal estilo *hacker* o ciencia ficción. Una barra de progreso llega al 100%. El sistema debe mostrar el mensaje de confirmación "SUCCESS" (Éxito). Sin embargo, un efecto de *glitch* rojo distorsiona la pantalla y las letras se mezclan, arrojando el texto: *"C S U C S S E"*. Un cartel parpadea: *"ERROR DE COMPILACIÓN: Analizando combinaciones"*.
* **Audio:** Imagina que estás programando un sistema y esperas el mensaje de confirmación "SUCCESS" de siete letras. Pero un error en la memoria mezcla los caracteres y te arroja algo como "CSUCSSE". Si intentas calcular de cuántas formas distintas la computadora pudo haber mezclado estas siete letras usando una permutación tradicional de 7 factorial, la matemática te dirá que existen más de 5,000 formas posibles. ¡Pero detente! Ese cálculo está totalmente equivocado. Estás asumiendo que las siete letras son diferentes, ignorando que hay letras repetidas que son clones exactos.

**Intro y Promesa (0:40 - 0:55)**

* **Visual (Manim):** Las letras corruptas en la terminal estallan en fragmentos de código. Esos fragmentos se reagrupan en el centro para formar el título brillante: *"PERMUTACIONES CON REPETICIÓN"*. Debajo, un subtítulo en fuente de código se despliega: *"Cuando los clones engañan a las matemáticas"*.
* **Audio:** Bienvenidos al mundo de los elementos idénticos. Hoy descubriremos las Permutaciones con Repetición, la técnica maestra que nos permite calcular el número real de arreglos posibles cuando en nuestro universo existen objetos repetidos que nuestro cerebro no puede distinguir.

**Desarrollo: La Trampa de los Clones Invisibles (0:55 - 1:45)**

* **Visual (Manim):** Se dibuja la palabra correcta *"S U C C E S S"*. Para que el espectador lo note, a cada letra idéntica se le asigna un pequeño subíndice de color: $S_1, S_2, S_3$ y $C_1, C_2$. Una animación rápida intercambia la posición de la $S_1$ (al inicio) con la $S_3$ (al final). Los subíndices desaparecen un segundo, revelando que la palabra se ve exactamente igual. Aparece una alerta en rojo: *"DUPLICADO FANTASMA DETECTADO"*.
* **Audio:** Volvamos a la palabra "SUCCESS". Tiene siete letras en total. Si calculas un 7 factorial clásico, estás tratando a las tres letras "S" como si fueran completamente distintas entre sí, y a las dos letras "C" como si fueran diferentes. El problema es que, si la computadora simplemente intercambia la primera "S" con la última "S", el resultado visual es exactamente la misma palabra. Si no ajustamos nuestro cálculo estadístico, estaremos contando miles de palabras fantasma que son copias visualmente idénticas, inflando nuestro espacio muestral artificialmente.

**Desarrollo: La Fórmula del Ajuste (1:45 - 2:40)**

* **Visual (Manim):** La palabra desaparece y da paso a la poderosa fórmula en formato LaTeX: 
$$P = \frac{n!}{n_1! \cdot n_2! \cdot \dots \cdot n_k!}$$



Las variables se iluminan. El numerador $n!$ se transforma en el total de letras: $7!$. El denominador se construye destacando las repeticiones: $3!$ (por las tres S) multiplicado por $2!$ (por las dos C). La ecuación queda: 
$$\frac{7!}{3! \times 2!}$$



El cálculo se desarrolla fluidamente: el $7!$ de arriba ($5,040$) se divide por el producto de abajo ($6 \times 2 = 12$). El resultado final de $5,040 / 12$ salta a la pantalla y brilla en dorado: **$420$**.
* **Audio:** Para eliminar a estos clones invisibles, usamos la fórmula de la permutación con repetición. En el numerador, ponemos el factorial de nuestro total absoluto de elementos, es decir, 7 factorial. Pero la magia purificadora ocurre en el denominador: aquí vamos a dividir por el factorial de las repeticiones de cada elemento idéntico. Como tenemos tres letras "S", dividimos entre 3 factorial. Y como tenemos dos letras "C", multiplicamos ese fondo por 2 factorial. Al dividir, matemáticamente estamos "borrando" de nuestro conteo todas las veces que los clones cambiaron de lugar entre ellos. Tu espacio muestral real cae de 5,040 a tan solo 420 formas únicas.

**Cierre y Conexión (2:40 - 3:10)**

* **Visual (Manim):** El número $420$ se descompone en 420 pequeños bloques de texto que forman una matriz perfecta en el fondo. Todos esos bloques se comprimen en un solo cubo de datos brillante. Este cubo se deja caer dentro de una "máquina" abstracta que tiene un plano cartesiano (ejes X y Y) en su interior, lista para graficar.
* **Audio:** Ahora ya sabes cómo corregir tus cálculos cuando la realidad te lanza objetos idénticos. Con esta última técnica, nuestro cinturón negro en estrategias de conteo está oficialmente completo y a prueba de errores. Pero, ¿qué pasa cuando ya no queremos solo contar, sino tomar todos estos universos de datos, extraer muestras al azar y graficar sus probabilidades reales en el tiempo? Ha llegado la hora de aplicar todo esto en los grandes modelos matemáticos. En el próximo video, entraremos oficialmente al fascinante mundo de las Distribuciones de Probabilidad. ¡Suscríbete, deja un buen like y prepárate para graficar el futuro!
4. #  Principio de Adición (Regla del "o")

Aquí tienes el guion para el Principio de Adición (Regla del "o"), manteniendo la estructura de viñetas con párrafos únicos, sin apariciones a cámara y utilizando animaciones visuales inmersivas basadas en un entorno de videojuegos RPG.

## Video: Principio de Adición (La Regla del "O")

**Gancho (0:00 - 0:35)**

* **Visual (Manim / Simulación 2D):** Una interfaz clásica de un videojuego RPG (Role-Playing Game). El inventario de un jugador muestra exactamente 1,000 monedas de oro brillantes. El jugador llega a una encrucijada en la ciudad principal con dos tiendas distintas. A la izquierda, la "Tienda de Bestias", que ofrece 3 caballos acorazados y 2 lobos gigantes. A la derecha, el "Taller Mecánico", que ofrece 4 motos a vapor. Un letrero parpadea indicando: *"Fondos insuficientes para comprar en ambas tiendas. Elige SOLO UNA montura"*.
* **Audio:** Imagina que llevas semanas jugando un RPG y por fin reuniste mil monedas de oro para comprar tu primera montura épica. Llegas a la ciudad y tienes dos opciones: ir a la Tienda de Bestias, que tiene 5 animales distintos, o ir al Taller Mecánico, que ofrece 4 motos a vapor. Tu oro solo alcanza para comprar un único vehículo, así que debes elegir una bestia "O" una moto. ¿Cuántas opciones totales tienes disponibles para gastar tu oro? Si tu mente matemática rápida pensó en multiplicar los números, acabas de desperdiciar todo tu oro en una fórmula equivocada.

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** La interfaz del RPG se congela y las tiendas se transforman en bloques abstractos de datos. En el centro, una gran letra *"O"* se dibuja con fuego mágico, seguida del título: *"PRINCIPIO DE ADICIÓN"*. Abajo, el subtítulo: *"La Regla de los Caminos Separados"*.
* **Audio:** Bienvenidos a la regla más intuitiva pero más incomprendida del conteo. Hoy vamos a dominar el Principio de Adición, conocido como la regla del "O". Vas a descubrir cómo calcular el tamaño de tus opciones cuando los caminos de tus decisiones jamás pueden cruzarse.

**Desarrollo: La Lógica y la Suma (0:50 - 1:45)**

* **Visual (Manim):** La pantalla se divide en dos bloques separados por una barrera de energía láser que impide que se toquen. En el bloque izquierdo (Bestias), flotan 5 íconos circulares. En el bloque derecho (Mecánicos), flotan 4 íconos cuadrados. Un cursor virtual debe hacer un solo clic. Si selecciona un ícono izquierdo, el lado derecho se apaga por completo, y viceversa. Aparece la ecuación matemática: $5 + 4 = 9$.
* **Audio:** La clave de este principio es un concepto que ya vimos: eventos mutuamente excluyentes. Esto significa que si eliges una opción, es físicamente imposible elegir la otra al mismo tiempo; tus decisiones no se mezclan. Como solo tienes dinero para comprar una única montura, si compras una bestia, el taller mecánico se bloquea para ti. Como los caminos no pueden ocurrir de forma consecutiva ni mezclarse, simplemente sumas tus alternativas. Tienes 5 opciones de un lado más 4 del otro, lo que te da un total de 9 monturas posibles para elegir.

**Desarrollo: La Diferencia entre el "O" y el "Y" (1:45 - 2:30)**

* **Visual (Manim):** Se muestran dos cajas de texto enfrentadas.
A la izquierda: *"Bestia O Moto"*. La letra "O" baja y se convierte en un signo gigante de suma ($+$). El resultado $5 + 4 = 9$ brilla en azul.
A la derecha: *"Bestia Y Moto"*. La letra "Y" baja y se convierte en un signo de multiplicación ($\times$). El resultado $5 \times 4 = 20$ brilla en rojo.
* **Audio:** ¿Cómo saber cuándo sumar y cuándo multiplicar en un examen o en un código? Todo se esconde en el lenguaje. Si tu problema dice que debes elegir una opción "O" la otra, significa que son excluyentes, por lo tanto, sumas (+). Pero si el juego te diera oro infinito y te exigiera comprar una bestia "Y" también una moto, los eventos ocurrirían en cadena. En ese caso aplicarías el principio multiplicativo de nuestro video anterior, multiplicando 5 por 4 para obtener 20 combinaciones distintas de garaje. El "O" divide los caminos y suma; el "Y" los encadena y multiplica.

**Cierre y Conexión (2:30 - 3:00)**

* **Visual (Manim):** Los números 9 y 20 se fusionan en un vórtice matemático y se transforman en una gran caja fuerte cerrada con múltiples cerraduras, algunas exigiendo sumas y otras multiplicaciones. Un texto flotante dice: *"Problemas Combinados"*.
* **Audio:** Ahora ya conoces los dos pilares del conteo numérico: el principio multiplicativo y el principio de adición. Pero en la vida real, como en el desarrollo de software o la criptografía, los problemas no son tan amables como para pedirte solo uno u otro. ¿Qué pasa cuando te enfrentas a un sistema que tiene reglas del "Y" mezcladas en la misma ecuación con reglas del "O"? Para resolver esos acertijos de alto nivel, necesitamos combinar nuestras reglas.

8. # combinaciones con y sin repe
Aquí tienes el guion para el video de Combinaciones (Con y Sin Repetición). He utilizado una analogía orientada a la tecnología y el hardware (muy cercana al mundo del *Machine Learning*) para mantener el nivel analítico, respetando el formato visual 100% de animaciones y código en Manim.

## Video: Combinaciones (Con y Sin Repetición)

**Gancho (0:00 - 0:40)**

* **Visual (Manim / Simulación 2D):** Una interfaz estilo tienda de tecnología. Tienes un chasis de servidor vacío con exactamente 4 ranuras (slots) para tarjetas gráficas (GPUs). En el inventario de la tienda hay 3 marcas con un símbolo de infinito ($\infty$) sobre ellas: *"Nvidia"*, *"AMD"*, y *"Intel"*. Un brazo robótico toma 2 Nvidias, 1 AMD y 1 Intel, arrojándolas en un carrito de compras. Al caer en el carrito, las cajas rebotan y se mezclan, dejando claro que su orden final no importa en lo absoluto. Aparece un cartel rojo: *"Error de fórmula clásica"*.
* **Audio:** Imagina que estás construyendo un servidor para entrenar modelos de Inteligencia Artificial y tienes espacio para instalar exactamente 4 tarjetas gráficas. La tienda ofrece 3 marcas distintas, pero tienen un inventario infinito, por lo que puedes comprar varias de la misma marca. Además, como van en el mismo servidor, no importa en qué orden las saques de la caja, el rendimiento final será idéntico. Sabes que si el orden no importa es una combinación, pero ¿cómo la calculas matemáticamente si estás repitiendo marcas? Nuestra fórmula clásica acaba de quedarse corta.

**Intro y Promesa (0:40 - 0:55)**

* **Visual (Manim):** El carrito de compras se transforma en un cubo de datos luminoso. Aparece el título en la pantalla: *"COMBINACIONES: Con y Sin Repetición"*. Las letras del título se duplican rápidamente, simulando el efecto de repetición.
* **Audio:** Bienvenidos a la última frontera de las técnicas de conteo. Hoy dominaremos las combinaciones en sus dos facetas. Repasaremos la regla clásica donde todo es único, y descubriremos la elegante fórmula oculta para calcular nuestro universo cuando sí podemos clonar nuestras opciones.

**Desarrollo: Sin Repetición (El Mundo Único) (0:55 - 1:40)**

* **Visual (Manim):** La pantalla se divide. Del lado izquierdo aparece el texto: *"Sin Repetición"*. Se dibujan 5 avatares de ingenieros distintos. Se abre un recuadro de "Comité" con 3 espacios. Se seleccionan 3 ingenieros, y los avatares originales desaparecen del grupo de origen. La fórmula clásica se ejecuta: $C(5,3) = \frac{5!}{3!(5-3)!} = 10$.
* **Audio:** Para que el contraste sea evidente, recordemos rápido la combinación sin repetición de nuestro video anterior. Digamos que tienes 5 ingenieros y debes elegir un comité de 3. El orden no importa, pero como son seres humanos, no puedes clonarlos; una vez que eliges a uno, se agota y desaparece de tus opciones. Al aplicar nuestra fórmula tradicional del factorial, sabemos que existen 10 equipos posibles. Es un universo cerrado, estricto y sin reemplazo.

**Desarrollo: Con Repetición (El Mundo Infinito) (1:40 - 2:35)**

* **Visual (Manim):** Del lado derecho aparece el texto: *"Con Repetición"*. Regresamos a las 3 marcas de GPU ($n=3$) y las 4 ranuras a llenar ($k=4$). La nueva y poderosa fórmula de Combinación con Repetición aparece en formato LaTeX: 
$$CR(n,k) = \binom{n+k-1}{k} = \frac{(n+k-1)!}{k!(n-1)!}$$


. Las variables se iluminan. El numerador se vuelve $(3+4-1)! = 6!$. El denominador se vuelve $4!(3-1)! = 4!2!$. La ecuación $\frac{6!}{4! \times 2!}$ se resuelve rápidamente cancelando factoriales, dando un resultado brillante: **$15$**.
* **Audio:** Pero volvamos a tu servidor. Tienes 3 marcas disponibles, que es tu variable "$n$", y debes hacer 4 selecciones, tu variable "$k$", con permiso total para repetir. Para esto usamos la fórmula de Combinaciones con Repetición. En el numerador del fraccionario, sumamos nuestras opciones "$n$", más nuestras selecciones "$k$", le restamos 1, y a todo eso le sacamos el factorial. En el denominador, multiplicamos "$k$" factorial por "$n$" menos 1 factorial. Si reemplazamos con nuestros datos, nos queda 6 factorial dividido entre 4 factorial por 2 factorial. Al resolverlo, descubrimos que tienes exactamente 15 formas únicas de armar tu servidor de Inteligencia Artificial.

**Cierre y Conexión al Siguiente Gran Tema (2:35 - 3:00)**

* **Visual (Manim):** El número 15 se eleva en la pantalla. Las 15 configuraciones posibles de servidores caen desde arriba apilándose en forma de barras. Una curva brillante, similar a una Distribución Normal, se dibuja abrazando las barras desde abajo hacia arriba, transformando los bloques rígidos en una gráfica estadística fluida.
* **Audio:** Con esta última fórmula, dominas por completo las reglas de los elementos idénticos. Las permutaciones, las combinaciones y las reglas del "Y" y el "O" ya no tienen secretos para ti. Oficialmente, tienes todas las herramientas matemáticas para medir cualquier azar. Ya estamos listos para tomar estos conteos y dar el salto hacia las gráficas predictivas masivas. En nuestro próximo video, estrenamos temporada y entramos al poderoso mundo de las Variables Aleatorias. ¡Suscríbete, deja un buen like y prepárate para la verdadera estadística!
8. # Aplicación: Conteo de Rutas en una Cuadrícula 
    # cuantos caminos tiene una Torre en un tablero de ajedrez para llegar a la casilla de la torre diagonalmente contraria.
9. # Permutaciones y combinaciones con restricciones (bloques, puestos fijos, elementos fijos)



1. 📹 Video 4: Distribuciones de probabilidad discretas
3. Variable aleatoria discreta
4. funsion de masa de probabilidad, esperanza y varianza
2. 📹 Video 5: Distribución de Bernoulli parte 1
2. 📹 Video 5: Distribución de Bernoulli parte 2
3. Binomial parte 1:


