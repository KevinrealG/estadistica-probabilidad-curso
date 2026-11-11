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
> **Audio: Eres un analista de seguridad intentando abrir este maletín. El código tiene exactamente 3 dígitos, y sabes que el dueño solo configuró el sistema usando los números del 1 al 5. Pero aquí está el verdadero dilema del hacker: ¿el sistema permite repetir números como "3-3-3", o cada dígito debe ser único, como "1-4-2"? Esa simple regla dicta si tienes el tiempo suficiente para adivinar el código o si estás perdiendo el tiempo.

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** El maletín se abre, liberando números que flotan formando ecuaciones. Aparece el título en pantalla: "CONTEO: Con y Sin Repetición".
> **Audio: Bienvenidos de nuevo.  Usaremos el principio multiplicativo para calcular exactamente cuántas combinaciones existen cuando las reglas permiten repetir datos, y cómo se desploma ese número cuando la repetición está prohibida.

**Desarrollo: Con Repetición (0:50 - 1:45)**

* **Visual (Manim):** Se dibujan tres casillas vacías en el centro de la pantalla: `[ ] [ ] [ ]`. Arriba, flotan los cinco números disponibles envueltos en esferas de luz: `{1, 2, 3, 4, 5}`. Para la primera casilla, una llave inglesa (representando el algoritmo) cuenta las esferas y aparece un 5 debajo de la primera casilla. Para la segunda casilla, las esferas no desaparecen, siguen siendo cinco y aparece otro 5 debajo. Para la tercera, ocurre lo mismo y aparece un tercer 5, formando finalmente la ecuación: $5 \times 5 \times 5 = 5^3 = 125$.
> **Audio: Empecemos con el escenario donde sí hay repetición. Imagina tus tres espacios vacíos. Para el primer dígito del código, tienes 5 opciones posibles. Como el sistema te permite usar el mismo número varias veces, para el segundo dígito sigues teniendo las mismas 5 opciones. Y para el tercero, adivinaste, otras 5 opciones. Por el principio fundamental del conteo, simplemente multiplicamos 5 por 5 por 5. Esto nos da 125 números distintos posibles.

**Desarrollo: Sin Repetición (1:45 - 2:35)**

* **Visual (Manim):** La pantalla se reinicia. Vuelven las tres casillas vacías y las cinco esferas numéricas. Para la primera casilla, hay 5 opciones, el número "2" baja a la casilla y desaparece del grupo de arriba. Para la segunda casilla, la llave inglesa cuenta las esferas restantes, ¡solo quedan 4!, aparece un 4 debajo de la segunda casilla y el número "5" baja y desaparece. Para la tercera casilla, solo quedan 3 esferas, aparece un 3 y la ecuación se traza matemáticamente: $5 \times 4 \times 3 = 60$.
> **Audio: Ahora, ¿qué pasa si el sistema de seguridad es estricto y no permite repetición? Esto es una permutación sin reemplazo. Para tu primer espacio, sigues teniendo 5 opciones. Pero cuidado: el número que elijas se agota, ya no puedes volver a usarlo. Así que, para tu segundo espacio, tu piscina de opciones se reduce a 4. Y para tu último espacio, solo te quedan 3 números disponibles. Multiplicamos 5 por 4 por 3, y el resultado es 60.

**Cierre y Conexión (2:35 - 3:00)**

* **Visual (Manim):** Los dos resultados se enfrentan en pantalla como en un ring de boxeo: 125 (Con Repetición) vs 60 (Sin Repetición). El número 125 es más del doble de grande, destacando visualmente la inmensa diferencia. Luego, ambos números se disuelven y empiezan a formar puntos de datos que trazan una campana de Gauss.
> **Audio: Con solo bloquear la capacidad de repetir elementos, tus opciones se redujeron a menos de la mitad, pasando de 125 a solo 60. Las reglas de reemplazo cambian la realidad entera de tus probabilidades. 
# Principio de Multiplicación (Regla del "y")

## Video: Principio de la Multiplicación (La Regla del "Y")

**Gancho (0:00 - 0:35)**

* **Visual (Manim / Simulación 2D):** Una escena en estilo *pixel art* de un videojuego retro de escape. Un personaje (un ladrón) está dentro de la bóveda con el botín. La interfaz del juego muestra en pantalla: *"PLAN DE ESCAPE"*. Paso 1: Elegir Salida (aparecen 3 íconos: Ventilación, Puerta Principal, Alcantarillas). Paso 2: Elegir Vehículo (aparecen 4 íconos: Moto, Furgoneta, Helicóptero, Patineta). Un reloj hace una cuenta regresiva rápida.
> **Audio: Imagina que estás jugando un videojuego de escapes y acabas de vaciar la bóveda. Ahora debes planear tu escape perfecto. El juego te obliga a elegir una ruta de salida entre 3 opciones: la ventilación, la puerta principal o las alcantarillas. Pero eso no es todo, también debes elegir un vehículo de escape entre 4 opciones: una moto, una furgoneta, un helicóptero o una patineta. Si obligatoriamente necesitas elegir una salida "Y" un vehículo para ganar, ¿cuántos planes de escape únicos puedes formar en total antes de que se acabe el tiempo?

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** El videojuego se pausa. Las palabras *"PRINCIPIO MULTIPLICATIVO"* aparecen en letras de *pixel art*, y luego se transforman en un elegante y brillante texto matemático en LaTeX. Debajo, se enciende un letrero de neón que dice: *"LA REGLA DEL 'Y'"*.
> **Audio:  Hoy vamos a dominar el Principio de la Multiplicación. Vas a aprender cómo calcular el tamaño de tus opciones totales de forma instantánea cuando necesitas que ocurra un evento y luego otro evento de forma consecutiva.

**Desarrollo: Construyendo el árbol (0:50 - 1:45)**

* **Visual (Manim):** Se dibuja un diagrama de árbol clásico. Desde un nodo inicial salen 3 ramas gruesas (las 3 salidas). Luego, desde el final de *cada una* de esas 3 ramas, brotan 4 nuevas ramas más pequeñas (los 4 vehículos). Los 12 puntos finales se iluminan uno por uno contando del 1 al 12. Finalmente, el árbol se encoge y da paso a una enorme ecuación central en una caja brillante: $3 \times 4 = 12$.
> **Audio: Si intentáramos dibujar cada plan de escape uno por uno usando un diagrama de árbol, veríamos que por cada una de las 3 salidas posibles, se abren 4 nuevos caminos correspondientes a los vehículos. Si contamos los puntos finales, tenemos 12 rutas. Pero en la vida real, con datos masivos, los árboles se vuelven gigantescos e imposibles de dibujar. Aquí es donde el principio multiplicativo nos salva la vida: si tienes una cantidad de opciones para una primera etapa, y otra cantidad para una segunda, simplemente multiplicas ambos números. Tres salidas multiplicadas por cuatro vehículos, nos da exactamente los mismos 12 planes de escape, pero en un segundo.

**Desarrollo: La palabra clave "Y" (1:45 - 2:30)**

* **Visual (Manim):** La pantalla se divide. A la izquierda, la letra *"Y"* se resalta en verde brillante junto a un símbolo de multiplicación ($\times$). A la derecha, la letra *"O"* se resalta en rojo junto a un símbolo de suma ($+$). Luego, la pantalla se centra en un candado numérico cilíndrico de 4 ruedas (dígitos del 0 al 9). Las ruedas giran velozmente mientras se forma la ecuación: $10 \times 10 \times 10 \times 10 = 10,000$.
> **Audio: El secreto definitivo para saber cuándo usar este principio está en el lenguaje: la letra "Y". Siempre que tu problema exija que ocurra la etapa A, "Y" la etapa B, "Y" la etapa C para completar un proceso, debes multiplicar. Piensa en un candado numérico de 4 ruedas. Necesitas configurar el primer número, "Y" el segundo, "Y" el tercero, "Y" el cuarto. Como cada rueda es independiente y tiene 10 opciones, multiplicamos 10 por 10 por 10 por 10, lo que nos da 10,000 combinaciones posibles al instante, sin dibujar ni un solo diagrama.

**Cierre y Conexión (2:30 - 3:00)**

* **Visual (Manim):** El candado numérico se abre de golpe, liberando esferas de luz que se agrupan en el centro para formar el enorme símbolo matemático del Factorial ($!$). Las esferas comienzan a alinearse en fila, intercambiando posiciones rápidamente de todas las formas posibles como si compitieran por el primer lugar.
> **Audio: La regla de la multiplicación es la base de las tecnicas de conteo. Pero, ¿qué pasaría si en lugar de elegir entre opciones separadas, tuvieras un grupo cerrado de elementos y simplemente quisieras saber de cuántas formas puedes ordenarlos absolutamente todos en una sola fila? Ahí es donde la multiplicación consecutiva evoluciona hacia una de las operaciones más utiles de la matemática: El Factorial. Y ese, será nuestro próximo video. 


# Video 1: El Factorial

**Gancho (0:00 - 0:35)**

* **Visual (Manim / Simulación 2D):** Una interfaz de una aplicación de música. Se muestra una lista de reproducción con exactamente 5 canciones. Un cursor animado hace clic en el icono de "Modo Aleatorio" (Shuffle). Inmediatamente, las canciones comienzan a cambiar de lugar a gran velocidad. Aparece un texto brillante parpadeando en la pantalla: *"¿Probabilidad de que suenen en tu orden perfecto?"*.
> **Audio: Imagina que tienes una lista de reproducción con tus 5 canciones favoritas y le das al botón de modo aleatorio. ¿Cuál es la probabilidad de que la aplicación decida reproducirlas mágicamente en tu orden perfecto, desde la mejor hasta la menos buena? Para calcularlo, primero necesitas descubrir de cuántas formas diferentes se pueden llegar a ordenar esas 5 canciones. Si intentas adivinar, puede que tu mente diga 10 o 20 formas, pero la matemática detrás de esto te va a sorprender.

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** La interfaz de música se desintegra y sus píxeles forman un gigantesco signo de exclamación ($!$) que brilla con luces de neón. Aparece el título: *"EL FACTORIAL"*. Debajo, se escribe el subtítulo: *"La matemática del orden total"*.
> **Audio: Hoy vamos a conocer el Factorial, la operación maestra que nos permite calcular instantáneamente de cuántas formas distintas podemos ordenar un grupo completo de elementos en una sola fila.

**Desarrollo: Construyendo el Orden (0:50 - 1:45)**

* **Visual (Manim):** Aparecen 5 espacios vacíos en pantalla: `[ ] [ ] [ ] [ ] [ ]`. Sobre ellos flotan 5 notas musicales de distintos colores. Para la primera casilla, el número "5" aparece debajo y una nota cae dentro. Para la segunda, aparece un "4" y cae otra nota. Luego un "3", un "2" y un "1". Debajo de las casillas se forma y se resuelve la ecuación: $5 \times 4 \times 3 \times 2 \times 1 = 120$.
> **Audio: Para resolver el problema, usemos el principio multiplicativo. Tienes 5 espacios vacíos. Para elegir la primera canción, la aplicación tiene 5 opciones posibles. Una vez que elige una, le quedan 4 opciones para el segundo lugar. Luego le quedan 3, luego 2 y finalmente 1 sola canción obligatoria para el último lugar. Al multiplicar todas estas opciones de forma descendente, el resultado es 120. ¡Existen 120 formas distintas de ordenar solo 5 canciones! Tu probabilidad de obtener tu orden perfecto es de 1 en 120.

**Desarrollo: El Símbolo y la Regla (1:45 - 2:40)**

* **Visual (Manim):** La larga ecuación multiplicativa se comprime matemáticamente hasta convertirse simplemente en $5!$. El símbolo pulsa. Luego, una nota dorada aparece con el texto: *"Regla de oro: $0! = 1$"*. Finalmente, se dibuja una baraja de 52 cartas. Se aplica el factorial ($52!$) y el resultado estalla llenando la pantalla con el número $8.06 \times 10^{67}$ mientras aparece una galaxia de fondo.
> **Audio: En probabilidad, esta acción de multiplicar un número entero por todos sus enteros anteriores hasta llegar al uno es tan recurrente que los matemáticos le inventaron su propio símbolo: el signo de exclamación. Esto se lee como "Cinco Factorial". Como regla de oro para que las ecuaciones avanzadas no se rompan, debes saber que el cero factorial siempre es igual a uno. Y ten cuidado, porque los factoriales crecen de forma monstruosa: si intentas ordenar una baraja de 52 cartas, el resultado de "52 factorial" es un número tan masivo que supera a la cantidad de átomos en todo el universo observable.

**Cierre y Conexión (2:40 - 3:10)**

* **Visual (Manim):** Regresan las 5 notas musicales a la pantalla. Un brazo robótico desciende, agarra aleatoriamente solo 3 notas y las guarda en una carpeta que dice *"Mini-Playlist"*. El símbolo de factorial ($!$) mira la acción con un enorme signo de interrogación arriba.
> **Audio: Ordenar absolutamente todo el grupo de datos es fascinante. Pero, ¿qué pasaría si no queremos escuchar las 5 canciones? ¿Qué pasa si solo queremos seleccionar 3 de ellas al azar para hacer una mini-lista y no nos importa en lo absoluto en qué orden suenen? El factorial directo ya no nos sirve porque nos daría datos duplicados. Para resolver esto, necesitamos una nueva herramienta: Los Números Combinatorios. Y ese, será nuestro próximo video. 

---

# Video 2: Los Números Combinatorios

**Gancho (0:00 - 0:35)**

* **Visual (Manim / Simulación 2D):** Una vista esquemática de la sala de control de una agencia espacial. Un holograma en el centro muestra el planeta Marte. En la base de la pantalla, hay 8 avatares distintos de astronautas. Una interfaz parpadea: *"MISIÓN MARTE: Seleccionar 3 tripulantes"*.
> **Audio: Imagina que eres el director de una agencia espacial. Tienes a tu disposición un grupo de 8 astronautas de élite, pero la cápsula que viajará a Marte solo tiene 3 asientos. Los roles en la nave son cooperativos y exactamente iguales. Eso significa que enviar a los astronautas Alice, Bob y Charlie, es exactamente el mismo equipo que enviar a Charlie, Bob y Alice. Si necesitas calcular cuántos equipos diferentes puedes formar en total, usar un factorial normal arruinará tus cálculos porque estarías contando el mismo equipo múltiples veces.

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** Los avatares se desvanecen. En el centro de la pantalla se dibujan unos paréntesis grandes, con el número 8 en la parte superior y el número 3 en la inferior: $\binom{8}{3}$. Aparece el título: *"NÚMEROS COMBINATORIOS"*. Subtítulo: *"Elegir sin importar el orden"*.
> **Audio:  Hoy descubriremos los Números Combinatorios, la estructura matemática que nos permite calcular con precisión cuántos subgrupos únicos podemos extraer de un conjunto más grande cuando el orden no importa en lo absoluto.

**Desarrollo: La Estructura y la Fórmula (0:50 - 1:45)**

* **Visual (Manim):** El símbolo $\binom{8}{3}$ se desplaza a la izquierda y se expande en su fórmula general: $\frac{n!}{k!(n-k)!}$. El $n$ (grupo total) se reemplaza por el 8. El $k$ (asientos) se reemplaza por el 3. La ecuación se transforma paso a paso hasta quedar como: $\frac{8!}{3! \times 5!}$.
> **Audio: Un número combinatorio se escribe como dos números apilados entre paréntesis, y se lee como "8 sobre 3". Para calcular su valor real, usamos la fórmula matemática de las combinaciones. En la parte de arriba del fraccionario, ponemos el factorial de nuestro grupo total, es decir, el 8. En la parte de abajo, ponemos el factorial de los espacios que vamos a llenar, que es el 3, multiplicado por la diferencia entre los dos, que es 8 menos 3, dándonos 5 factorial.

**Desarrollo: El Truco de la Cancelación (1:45 - 2:35)**

* **Visual (Manim):** La ecuación se desarrolla. El numerador pasa de $8!$ a escribirse como $8 \times 7 \times 6 \times 5!$. El denominador se mantiene como $3 \times 2 \times 1 \times 5!$. Una línea roja tipo "slash" tacha el $5!$ de arriba y el $5!$ de abajo, eliminándolos. Nos queda la fracción $\frac{8 \times 7 \times 6}{6}$, que se simplifica y estalla revelando el número **56**. Se dibujan 56 mini-cohetes en el fondo.
> **Audio:  En lugar de desarrollar todo el 8 factorial hasta el número uno, lo escribimos solo como 8 por 7 por 6... por 5 factorial. ¿Para qué? Para poder cancelar directamente ese 5 factorial de arriba con el 5 factorial de abajo. El problema se reduce a 8 por 7 por 6, dividido entre 3 por 2 por 1. Al resolver esa simple fracción, el resultado es 56. ¡Tienes exactamente 56 formas únicas de armar tu tripulación a Marte!

**Cierre y Conexión (2:35 - 3:00)**

* **Visual (Manim):** Los 56 mini-cohetes se agrupan, apilándose uno sobre otro para formar las barras de un histograma. Una línea curva y suave atraviesa las puntas de las barras formando la gráfica de una Distribución Binomial. En una esquina, la fórmula de la Binomial aparece resaltando su componente combinatorio: $\binom{n}{k} p^k q^{n-k}$.
> **Audio: Estos números combinatorios son la pieza fundamental que nos faltaba en nuestro arsenal estadístico. Ahora que sabemos cómo comtar estos subgrupos de forma limpia, estamos listos para insertarlos dentro de fórmulas predictivas reales. 


# Video: Permutación Básica

**Gancho (0:00 - 0:35)**

* **Visual (Manim / Simulación 2D):** Un mapa digital oscuro estilo radar aparece en pantalla con 5 nodos brillantes etiquetados del $A$ al $E$ (representando ciudades o servidores). Un dron de entregas (o paquete de datos) se sitúa en el centro. Se traza rápidamente una ruta: $A \to B \to C$, marcando un tiempo de "15 ms". Luego la ruta se borra y se traza a la inversa: $C \to B \to A$, marcando un tiempo de "45 ms" debido a la resistencia de la red. Un reloj de batería parpadea en rojo.
> **Audio: Eres el ingeniero  a cargo de trazar la ruta de un dron de entregas urgentes. Tienes 5 destinos críticos en el mapa, pero la batería solo alcanza para visitar exactamente 3 antes de volver a la base. ¿El orden importa? Por supuesto. Volar de la ciudad A a la B y luego a la C toma un tiempo y energía completamente distintos que hacer la ruta a la inversa debido al viento y la distancia. Si necesitas programar un algoritmo para encontrar la ruta más rápida, primero debes saber exactamente cuántas rutas posibles existen.

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** El mapa digital se desintegra en partículas geométricas que se reagrupan en el centro para formar el título brillante: *"PERMUTACIÓN BÁSICA"*. Debajo, un subtítulo dinámico se escribe como si fuera código: `orden == True`.
> **Audio: Hoy vamos a dominar la Permutación Básica, la herramienta estadística que te permite calcular al instante de cuántas formas puedes elegir y ordenar un grupo específico de elementos cuando la posición de cada uno cambia por completo el resultado final.

**Desarrollo: La Lógica del Espacio (0:50 - 1:45)**

* **Visual (Manim):** Se dibujan tres ranuras vacías en pantalla: `[ ] [ ] [ ]`. Sobre ellas flotan los cinco nodos del mapa: $\{A, B, C, D, E\}$. Para la primera ranura, el número $5$ aparece debajo y el nodo $C$ cae dentro. Para la segunda ranura, aparece un $4$ y el nodo $A$ ocupa el lugar. Para la tercera ranura, aparece un $3$ y el nodo $E$ se inserta. Debajo de las ranuras, la ecuación se escribe sola: $5 \times 4 \times 3 = 60$.
> **Audio: A diferencia del factorial puro donde estábamos obligados a ordenar absolutamente todos los elementos de un conjunto, en una permutación básica solo tomamos una fracción del grupo total. Si aplicamos el principio multiplicativo a nuestra ruta: para la primera parada, el dron tiene 5 opciones posibles. Una vez que hace esa entrega, le quedan 4 destinos disponibles para la segunda parada. Y para la tercera y última parada, su universo se reduce a solo 3 opciones. Si multiplicamos 5 por 4 por 3, obtenemos 60. Existen exactamente 60 rutas únicas.

**Desarrollo: La Fórmula Matemática (1:45 - 2:35)**

* **Visual (Manim):** Las ranuras desaparecen y la fórmula oficial de la permutación se escribe en elegante formato LaTeX: $$P(n,r) = \frac{n!}{(n-r)!}$$. La variable $n$ se ilumina y se transforma en un $5$ (Destinos Totales). La variable $r$ se transforma en un $3$ (Paradas). La ecuación se actualiza a:  $$\frac{5!}{(5-3)!} = \frac{5!}{2!}$$. El numerador se expande como $5 \times 4 \times 3 \times 2!$, y una animación de corte de espada ("slash" rojo) cancela el $2!$ de arriba con el $2!$ de abajo. El resultado brillante $60$ ocupa la pantalla.
> **Audio: Para no tener que hacer multiplicaciones manuales cuando trabajes con bases de datos de miles de registros, usamos la fórmula general de la permutación. "$n$" es tu número total de elementos disponibles (tus 5 destinos), y "$r$" es el número de espacios que vas a llenar (tus 3 paradas). Arriba colocamos 5 factorial, y abajo la resta de 5 menos 3, es decir, 2 factorial. desarrollamos el 5 factorial solo hasta el 2 factorial para cancelarlo directamente con el de abajo, dejándonos exactamente la misma operación: 5 por 4 por 3. ¡60 rutas!

**Cierre y Conexión (2:35 - 3:00)**

* **Visual (Manim):** El número $60$ se transforma en un bloque de código y se guarda en un candado cerrado marcado como *"Permutación"*. A su lado, aparece un candado abierto marcado como *"Con Repetición"*. El número $60$ salta al candado abierto, se divide por $3!$, y se transforma en un número $10$. Aparece un signo de interrogación.
> **Audio: La permutación  es el motor de los algoritmos de enrutamiento y las contraseñas, porque asume que cada ligero cambio de posición crea un universo nuevo. Pero, ¿y que pasa si algunos de los elementos son iguales? Como vamos a menejar las permutaciones. Ese será nuestro próximo video

6. #  Permutaciones con Repetición

## Video: Permutaciones con Repetición

**Gancho (0:00 - 0:40)**

* **Visual (Manim / Simulación 2D):** Una pantalla de terminal estilo *hacker* o ciencia ficción. Una barra de progreso llega al 100%. El sistema debe mostrar el mensaje de confirmación "SUCCESS" (Éxito). Sin embargo, un efecto de *glitch* rojo distorsiona la pantalla y las letras se mezclan, arrojando el texto: *"C S U C S S E"*. Un cartel parpadea: *"ERROR DE COMPILACIÓN: Analizando combinaciones"*.
> **Audio: Imagina que estás programando un sistema y esperas el mensaje de confirmación "SUCCESS" de siete letras. Pero un error en la memoria mezcla los caracteres y te arroja algo como "CSUCSSE". Si intentas calcular de cuántas formas distintas la computadora pudo haber mezclado estas siete letras usando una permutación tradicional de 7 factorial, la matemática te dirá que existen más de 5,000 formas posibles. ¡Pero detente! Ese cálculo está totalmente equivocado. Estás asumiendo que las siete letras son diferentes, ignorando que hay letras repetidas que son clones exactos.

**Intro y Promesa (0:40 - 0:55)**

* **Visual (Manim):** Las letras corruptas en la terminal estallan en fragmentos de código. Esos fragmentos se reagrupan en el centro para formar el título brillante: *"PERMUTACIONES CON REPETICIÓN"*. Debajo, un subtítulo en fuente de código se despliega: *"Cuando los clones engañan a las matemáticas"*.
> **Audio: Hoy descubriremos las Permutaciones con Repetición, la técnica  que nos permite calcular el número real de arreglos posibles cuando en nuestro universo existen objetos repetidos.

**Desarrollo: La Trampa de los Clones Invisibles (0:55 - 1:45)**

* **Visual (Manim):** Se dibuja la palabra correcta *"S U C C E S S"*. Para que el espectador lo note, a cada letra idéntica se le asigna un pequeño subíndice de color: $S_1, S_2, S_3$ y $C_1, C_2$. Una animación rápida intercambia la posición de la $S_1$ (al inicio) con la $S_3$ (al final). Los subíndices desaparecen un segundo, revelando que la palabra se ve exactamente igual. Aparece una alerta en rojo: *"DUPLICADO FANTASMA DETECTADO"*.
> **Audio: Volvamos a la palabra "SUCCESS". Tiene siete letras en total. Si calculas un 7 factorial clásico, estás tratando a las tres letras "S" como si fueran completamente distintas entre sí, y a las dos letras "C" como si fueran diferentes. El problema es que, si la computadora simplemente intercambia la primera "S" con la última "S", el resultado visual es exactamente la misma palabra. Si no ajustamos nuestro cálculo estadístico, estaremos contando miles de palabras fantasma que son copias visualmente idénticas.

**Desarrollo: La Fórmula del Ajuste (1:45 - 2:40)**

* **Visual (Manim):** La palabra desaparece y da paso a la poderosa fórmula en formato LaTeX: 
$$P = \frac{n!}{n_1! \cdot n_2! \cdot \dots \cdot n_k!}$$ Las variables se iluminan. El numerador $n!$ se transforma en el total de letras: $7!$. El denominador se construye destacando las repeticiones: $3!$ (por las tres S) multiplicado por $2!$ (por las dos C). La ecuación queda: $$\frac{7!}{3! \times 2!}$$El cálculo se desarrolla fluidamente: el $7!$ de arriba ($5,040$) se divide por el producto de abajo ($6 \times 2 = 12$). El resultado final de $5,040 / 12$ salta a la pantalla y brilla en dorado: **$420$**.
> **Audio: Para eliminar a estos clones invisibles, usamos la fórmula de la permutación con repetición. En el numerador, ponemos el factorial de nuestro total absoluto de elementos, es decir, 7 factorial. Pero la magia ocurre en el denominador: aquí vamos a dividir por el factorial de las repeticiones de cada elemento idéntico. Como tenemos tres letras "S", dividimos entre 3 factorial. Y como tenemos dos letras "C", multiplicamos ese fondo por 2 factorial. Al dividir, matemáticamente estamos "borrando" de nuestro conteo todas las veces que los clones cambiaron de lugar entre ellos. Tu espacio muestral real cae de 5,040 a tan solo 420 formas únicas.

**Cierre y Conexión (2:40 - 3:10)**

* **Visual (Manim):** El número $420$ se descompone en 420 pequeños bloques de texto que forman una matriz perfecta en el fondo. .
> **Audio: Ahora ya sabes cómo corregir tus cálculos cuando la realidad te lanza objetos idénticos. 
4. #  Principio de Adición (Regla del "o")

**Gancho (0:00 - 0:40)**

* **Visual (Manim / Simulación 2D):** Un mapa digital estilo GPS muestra un punto marcado como "Ciudad A" y otro como "Ciudad B". Un avatar en la Ciudad A tiene un símbolo de alerta roja parpadeando sobre su cabeza. El mapa despliega las opciones de ruta: por el aire, se dibujan 3 aviones pequeños (representando 3 aerolíneas distintas); por tierra, se dibujan 2 autobuses (representando 2 empresas). Un cronómetro gigante hace una cuenta regresiva.
> **Audio: Imagina que estás en la ciudad A y tienes una emergencia absoluta: necesitas llegar a la ciudad B hoy mismo. Abres tu aplicación de viajes y el algoritmo te muestra tus opciones. Puedes tomar un vuelo rápido, donde operan 3 aerolíneas distintas, o puedes irte por tierra en un autobús, donde tienes 2 empresas de transporte disponibles. Si la base de datos necesita calcular de cuántas formas totalmente diferentes puedes hacer este viaje, ¿qué harías? ¿Multiplicarías las opciones como hicimos en el video anterior? Si haces eso, la matemática colapsa. Aquí es físicamente imposible viajar en avión y en bus al mismo tiempo. Tienes que tomar una decisión.

**Intro y Promesa (0:40 - 0:55)**

* **Visual (Manim):** Los íconos de aviones y autobuses vuelan al centro de la pantalla y colisionan, transformándose en un gigantesco y brillante signo de suma ($+$). Aparece el título en tipografía audaz: *"PRINCIPIO DE ADICIÓN"*, y debajo el subtítulo que pulsa lentamente: *"La Regla del 'O'"*.
> **Audio:  Hoy vamos a dominar el Principio de Adición, también conocido como la Regla del "O". Descubrirás por qué en ciertos escenarios multiplicar destruye la lógica, y cómo la suma es la única herramienta matemática capaz de abarcar tus universos posibles cuando los caminos nunca se cruzan.

**Desarrollo: La Lógica Básica (0:55 - 1:40)**

* **Visual (Manim):** La pantalla se divide en dos carriles. Carril superior (Aire): 3 aviones se alinean. Carril inferior (Tierra): 2 autobuses se alinean. En el medio de ambos carriles aparece una gran letra "O" ($\cup$). La ecuación se escribe de forma fluida: $3 + 2 = 5$.
> **Audio: Volvamos a tu viaje de emergencia. La clave definitiva para usar este principio es la palabra "O". Viajas en avión, "O" viajas en autobús. Como no puedes estar en dos lugares a la vez, estos eventos son mutuamente excluyentes; si eliges uno, anulas instantáneamente la existencia del otro. Cuando te enfrentas a decisiones paralelas que no ocurren en secuencia, abandonamos la multiplicación y aplicamos el Principio de Adición. Simplemente sumas tus 3 opciones de aerolíneas con tus 2 opciones de autobuses, dándote un gran total de 5 formas distintas de llegar a tu destino.

**Desarrollo: Combinando Universos (El Comité) (1:40 - 2:30)**

* **Visual (Manim):** La pantalla se limpia y aparece un salón de clases representado por avatares: 9 niños (en azul) y 3 niñas (en morado). Un marco dorado vacío con 4 asientos aparece abajo bajo el título: *"COMITÉ NACIONAL"*. Una regla estricta parpadea en letras rojas: *"REQUISITO: Al menos 1 niña"*.
> **Audio: Pero, ¿qué pasa si el algoritmo se enfrenta a un problema complejo donde necesitamos usar la multiplicación y la suma al mismo tiempo? Imagina una clase con 9 niños y 3 niñas. Debes escoger al azar un comité de exactamente 4 estudiantes para un congreso nacional, pero hay una restricción obligatoria en el código: el comité debe tener "por lo menos" una niña. Esa pequeña frase "por lo menos" divide nuestro problema en tres escenarios diferentes. Como un comité no puede tener 1 niña y 3 niñas al mismo tiempo, estos escenarios son mutuamente excluyentes.

**Desarrollo: Calculando los Casos (2:30 - 3:30)**

* **Visual (Manim):** Se abren tres recuadros paralelos en pantalla, resolviendo las ecuaciones combinatorias en simultáneo:* *Caso 1 (1 Niña y 3 Niños):* $\binom{3}{1} \times \binom{9}{3} = 3 \times 84 = 252$ * *Caso 2 (2 Niñas y 2 Niños):* $\binom{3}{2} \times \binom{9}{2} = 3 \times 36 = 108$ * *Caso 3 (3 Niñas y 1 Niño):* $\binom{3}{3} \times \binom{9}{1} = 1 \times 9 = 9$ Finalmente, los tres resultados caen a una caja sumadora final: $252 + 108 + 9 = 369$.
> **Audio: Desglosemos los tres casos. Caso 1: que el comité tenga exactamente 1 niña "Y" 3 niños. Usando combinaciones (porque el orden no importa), combinamos 1 de 3 niñas, por 3 de 9 niños, dándonos 252 formas. Caso 2: tener 2 niñas y 2 niños. Hacemos la combinatoria y nos da 108 formas. Caso 3: llevar a las 3 niñas y a 1 solo niño. La combinatoria nos arroja 9 formas. Ahora aplicamos nuestro principio maestro. Como solo puede ocurrir el Caso 1, "O" el Caso 2, "O" el Caso 3, sumamos los universos: 252 más 108 más 9. ¡Existen exactamente 369 maneras totales de armar este comité cumpliendo la regla!

Cierre y Conexión (3:30 - 4:00) reescrito:
Visual (Manim): El gran número $369$ brilla en el centro y se desintegra en partículas. Estas partículas se transforman en una caja fuerte abierta de la cual salen flotando distintos objetos (avatares, esferas de colores y bloques). Algunos de estos objetos son únicos, pero de repente, varios de ellos comienzan a clonarse repetidamente llenando la pantalla. Sobre esta nube de clones aparece un gran signo de interrogación brillante y las palabras "¿Y si se repiten?".
Audio: Hasta ahora, al formar nuestros equipos y comités, siempre usamos combinaciones asumiendo lógicamente que no podemos elegir a la misma persona dos veces. Pero, ¿qué pasa cuando la regla cambia y el sistema sí te permite elegir elementos repetidos? para terminar las tecnicas de conteo nos vemos en el siguiente video, en el próximo video dominaremos las Combinaciones con y sin repetición. 

# Video: Combinaciones (Con y Sin Repetición)

**Gancho (0:00 - 0:40)**

* **Visual (Manim / Simulación 2D):** Una interfaz estilo tienda de tecnología. Tienes un chasis de servidor vacío con exactamente 4 ranuras (slots) para tarjetas gráficas (GPUs). En el inventario de la tienda hay 3 marcas con un símbolo de infinito ($\infty$) sobre ellas: *"Nvidia"*, *"AMD"*, y *"Intel"*. Un brazo robótico toma 2 Nvidias, 1 AMD y 1 Intel, arrojándolas en un carrito de compras. Al caer en el carrito, las cajas rebotan y se mezclan, dejando claro que su orden final no importa en lo absoluto. Aparece un cartel rojo: *"Error de fórmula clásica"*.
> **Audio: Imagina que estás construyendo un servidor para entrenar modelos de Inteligencia Artificial y tienes espacio para instalar exactamente 4 tarjetas gráficas. La tienda ofrece 3 marcas distintas, pero tienen un inventario muy grande, por lo que puedes comprar varias de la misma marca. Además, como van en el mismo servidor, no importa en qué orden las saques de la caja, el rendimiento final será idéntico. Sabes que si el orden no importa es una combinación, pero ¿cómo la calculas matemáticamente si estás repitiendo marcas? Nuestra fórmula clásica acaba de quedarse corta.

**Intro y Promesa (0:40 - 0:55)**

* **Visual (Manim):** El carrito de compras se transforma en un cubo de datos luminoso. Aparece el título en la pantalla: *"COMBINACIONES: Con y Sin Repetición"*. Las letras del título se duplican rápidamente, simulando el efecto de repetición.
> **Audio:  Hoy dominaremos las combinaciones en sus dos facetas. Repasaremos la regla clásica donde todo es único, y descubriremos la elegante fórmula oculta para calcular nuestro universo cuando sí podemos clonar nuestras opciones.

**Desarrollo: Sin Repetición (El Mundo Único) (0:55 - 1:40)**

* **Visual (Manim):** La pantalla se divide. Del lado izquierdo aparece el texto: *"Sin Repetición"*. Se dibujan 5 avatares de ingenieros distintos. Se abre un recuadro de "Comité" con 3 espacios. Se seleccionan 3 ingenieros, y los avatares originales desaparecen del grupo de origen. La fórmula clásica se ejecuta: $C(5,3) = \frac{5!}{3!(5-3)!} = 10$.
> **Audio: Para que el contraste sea evidente, recordemos rápido la combinación sin repetición de nuestro video anterior. Digamos que tienes 5 ingenieros y debes elegir un comité de 3. El orden no importa, pero como son seres humanos, no puedes clonarlos; una vez que eliges a uno, se agota y desaparece de tus opciones. Al aplicar nuestra fórmula tradicional del factorial, sabemos que existen 10 equipos posibles. Es un universo cerrado, estricto y sin reemplazo.

**Desarrollo: Con Repetición (El Mundo Infinito) (1:40 - 2:35)**

* **Visual (Manim):** Del lado derecho aparece el texto: *"Con Repetición"*. Regresamos a las 3 marcas de GPU ($n=3$) y las 4 ranuras a llenar ($k=4$). La nueva y poderosa fórmula de Combinación con Repetición aparece en formato LaTeX:  $$CR(n,k) = \binom{n+k-1}{k} = \frac{(n+k-1)!}{k!(n-1)!}$$ Las variables se iluminan. El numerador se vuelve $(3+4-1)! = 6!$. El denominador se vuelve $4!(3-1)! = 4!2!$. La ecuación $\frac{6!}{4! \times 2!}$ se resuelve rápidamente cancelando factoriales, dando un resultado brillante: **$15$**.
> **Audio: Pero volvamos a tu servidor. Tienes 3 marcas disponibles, que es tu variable "$n$", y debes hacer 4 selecciones, tu variable "$k$", con permiso total para repetir. Para esto usamos la fórmula de Combinaciones con Repetición. En el numerador del fraccionario, sumamos nuestras opciones "$n$", más nuestras selecciones "$k$", le restamos 1, y a todo eso le sacamos el factorial. En el denominador, multiplicamos "$k$" factorial por "$n$" menos 1 factorial. Si reemplazamos con nuestros datos, nos queda 6 factorial dividido entre 4 factorial por 2 factorial. Al resolverlo, descubrimos que tienes exactamente 15 formas únicas de armar tu servidor de Inteligencia Artificial.

Cierre y Conexión Modificado (Video Anterior)

Visual (Manim): El número 15 se eleva en la pantalla. Las 15 configuraciones posibles caen desde arriba y, al tocar el fondo, se transforman en las intersecciones de un mapa urbano cuadriculado estilo GPS. Un punto luminoso empieza a trazar múltiples caminos diferentes y caóticos desde la esquina inferior izquierda del mapa hasta la superior derecha. Un cartel holográfico parpadea con el texto: "Calculando rutas posibles...".

Audio: Con esta última fórmula dominas por completo las reglas de los elementos idénticos. Las combinaciones y las repeticiones ya no tienen secretos para ti en la teoría. Pero, ¿qué pasa si sacamos estas fórmulas de los números y las letras, y las llevamos al espacio físico? ¿Podemos usar este mismo poder matemático para calcular exactamente cuántas rutas alternativas existen en el plano de una ciudad, o incluso en un tablero de ajedrez? En nuestro próximo video, aplicaremos esta lógica para dominar el Conteo de Rutas en Cuadrículas. 
8. # Aplicación: Conteo de Rutas en una Cuadrícula 
**Gancho (0:00 - 0:40)**

* **Visual (Manim / Simulación 3D):** Un tablero de ajedrez clásico de $8 \times 8$ casillas flota en un espacio oscuro. Una Torre de cristal iluminada se sitúa en la esquina inferior izquierda (casilla A1). La casilla diagonalmente opuesta en la esquina superior derecha (H8) brilla en rojo como el objetivo. Un texto advierte las reglas del juego: *"Movimientos permitidos: SOLO Arriba o Derecha"*. La Torre empieza a trazar rápidamente dos caminos distintos dejando una estela de luz. Un contador gigante arriba empieza a girar rápidamente buscando el total.
> **Audio: Imagina que tienes una Torre en un tablero de ajedrez en la esquina inferior izquierda, y necesitas llevarla hasta la esquina superior derecha, al otro lado del tablero. Para hacerlo interesante, la regla es que la Torre solo puede moverse hacia adelante o hacia la derecha, nunca puede retroceder. Si te pregunto cuántos caminos únicos y distintos puede tomar esa Torre para llegar a su destino final, ¿qué dirías? ¿20 caminos? ¿100 caminos? La verdad es que son miles, y para calcular el número exacto en un solo segundo no necesitas un motor de ajedrez, solo necesitas reciclar una fórmula que ya conoces.

**Intro y Promesa (0:40 - 0:55)**

* **Visual (Manim):** El tablero de ajedrez gira y se aplana hasta convertirse en un plano cartesiano. El título se dibuja con líneas rectas y precisas: *"CONTEO DE RUTAS"*. Debajo aparece el subtítulo matemático: *"La geometría de las combinaciones"*.
> **Audio: Hoy aprenderemos a calcular el número exacto de caminos posibles en cualquier cuadrícula o mapa urbano, transformando un problema de rutas físicas en un simple juego de palabras matemáticas.

**Desarrollo: Traduciendo el Mapa a Letras (0:55 - 1:50)**

* **Visual (Manim):** Se dibuja el mapa de una ciudad pequeña. Se marcan $4$ calles verticales y $3$ calles horizontales. Un auto en la esquina inferior izquierda debe ir a la superior derecha. Las flechas muestran los espacios entre las calles: para llegar al objetivo, obligatoriamente se deben avanzar $3$ manzanas a la Derecha ($D, D, D$) y $2$ manzanas hacia Arriba ($A, A$). El auto hace una ruta ($D-A-D-A-D$) y la deja escrita en la pantalla como una palabra.
> **Audio: Empecemos con una ciudad. Tienes un mapa con 4 calles verticales y 3 horizontales, y quieres ir de la esquina inferior izquierda a la superior derecha. Si cuentas los bloques, verás que sin importar la ruta que elijas, obligatoriamente tendrás que moverte 3 espacios a la Derecha y 2 espacios hacia Arriba para llegar. Es decir, tu ruta siempre será una combinación de tres letras "D" y dos letras "A". Por ejemplo: Derecha, Arriba, Derecha, Arriba, Derecha. ¡Acabamos de transformar un mapa en una palabra de cinco letras! Y como descubrimos en videos anteriores, si queremos saber cuántas formas hay de ordenar un grupo de letras donde hay repetidos, usamos: la permutación con repetición.

**Desarrollo: La Fórmula y la Solución del Ajedrez (1:50 - 2:45)**

* **Visual (Manim):** La palabra $D-D-D-A-A$ se eleva y se convierte en la ecuación combinatoria: $$\frac{5!}{3! \times 2!} = 10 \text{ rutas}$$Inmediatamente, la pantalla vuelve al tablero de ajedrez de $8 \times 8$ casillas. Se trazan las flechas de movimiento: para ir de la primera casilla a la octava, hay que dar $7$ pasos a la Derecha ($7D$) y $7$ pasos hacia Arriba ($7A$). Total: $14$ pasos. Aparece la súper fórmula:  $$\frac{14!}{7! \times 7!}$$o $\binom{14}{7}$. El cálculo rápido cancela los factoriales y el resultado final estalla en pantalla: **$3,432$ rutas**.
> **Audio: En la ciudad, tu total de pasos es 5. Divides 5 factorial entre 3 factorial (por las derechas) y 2 factorial (por los arribas), lo que te da 10 rutas posibles. ¡Fácil! Ahora resolvamos el problema de la Torre de ajedrez. Un tablero tiene 8 por 8 casillas. Para cruzarlo de esquina a esquina, la Torre debe dar exactamente 7 saltos a la Derecha y 7 saltos hacia Arriba. En total, siempre dará 14 movimientos. Aplicamos la fórmula: 14 factorial dividido por la multiplicación de 7 factorial por 7 factorial. Los factoriales se cancelan, la computadora hace la magia y el resultado es: ¡Existen 3,432 caminos completamente diferentes para llevar esa Torre a su destino!

Visual (Manim): Los 3,432 caminos dibujados sobre el tablero de ajedrez se levantan en 3D y se transforman en una sola línea recta de 5 sillas vacías. Un candado rojo brillante aparece y bloquea de golpe dos de las sillas uniéndolas con una cadena. Aparece un cartel parpadeante que dice: "RESTRICCIÓN DETECTADA".

Audio: Convertimos un problema de espacio físico en un simple arreglo de letras. Pero espera, antes de dar el gran salto hacia las gráficas, nos queda una última tecnica de conteo. ¿Qué pasa cuando las reglas del juego te obligan a que ciertos elementos nunca se separen? Si estás organizando una fila y te dicen "estas personas tienen que sentarse juntas obligatoriamente", toda la matemática que hemos visto tiene que ajustarse. En nuestro próximo y último video de esta serie, dominaremos las Permutaciones con Restricciones.
# Permutaciones y combinaciones con restricciones (bloques, puestos fijos, elementos fijos)


## Video: Permutaciones con Restricciones (El Método de los Bloques)

**Gancho (0:00 - 0:40)**

* **Visual (Manim / Simulación 2D):** Una sala de exámenes. Hay 5 sillas en una sola fila. Arriba de cada silla flota un cuestionario diferente marcado del 1 al 5 (entregados en orden de izquierda a derecha). Aparecen 5 avatares en pantalla: 3 hombres (en azul) y 2 mujeres (en morado). Un cronómetro inicia.
> **Audio: Imagina que tienes 5 sillas en fila y 5 cuestionarios diferentes que deben ser entregados en estricto orden de izquierda a derecha. Tienes a 3 hombres y 2 mujeres esperando para sentarse y resolverlos. Si se sentaran al azar sin que les importe nada, usaríamos una simple permutación de "5 factorial" y obtendríamos 120 formas. Pero, ¿y si te exigen reglas estrictas? Por ejemplo, ¿qué pasa si las mujeres deciden que obligatoriamente se van a sentar juntas, y los hombres también? Si intentas adivinar el número de formas de ordenarlos con esas barreras, necesitamos un truco estadístico.

**Intro y Promesa (0:40 - 0:55)**

* **Visual (Manim):** Los avatares se agrupan y una cuerda de luz brillante amarra a los hombres por un lado y a las mujeres por el otro, formando "cajas". Aparece el título dinámico: *"PERMUTACIONES CON RESTRICCIONES"*. Debajo, un subtítulo en letras doradas: *"El Método de los Bloques"*.
> **Audio:  Hoy dominaremos las Permutaciones con Restricciones usando el "Método de los Bloques". Aprenderás a calcular combinaciones exactas cuando ciertos elementos están obligados a permanecer pegados.

**Desarrollo: Caso A - Hombres juntos y Mujeres juntas (0:55 - 1:55)**

* **Visual (Manim):** La pantalla muestra las 5 sillas. Los 3 avatares de hombres se meten dentro de una caja azul gigante translúcida (Bloque 1). Las 2 mujeres se meten dentro de una caja morada (Bloque 2).
Dentro de la caja azul, los hombres intercambian de lugar ($3! = 6$). Dentro de la caja morada, las mujeres cambian de lugar ($2! = 2$). Luego, las dos cajas gigantes completas intercambian posiciones entre sí ($2!$). La ecuación se escribe abajo: $3! \times 2! \times 2! = 6 \times 2 \times 2 = 24$.
> **Audio: Primer reto: Los hombres deben sentarse juntos, y las mujeres también. El truco  aquí es empaquetarlos. Metemos a los 3 hombres en un solo "súper-bloque", y a las 2 mujeres en otro bloque distinto. Ahora hacemos la matemática por capas. Dentro de su propio bloque, los 3 hombres pueden cambiar de asiento entre ellos de "3 factorial" formas. Las 2 mujeres dentro de su bloque pueden cambiar de "2 factorial" formas. Y a nivel general, tenemos dos grandes bloques que pueden intercambiar de lugar: los hombres primero y mujeres después, o viceversa, lo que nos da otro "2 factorial". Multiplicamos los tres aislamientos: 3 factorial (que es 6), por 2 factorial (que es 2), por 2 factorial. Seis por dos por dos, ¡nos da exactamente 24 formas únicas de sentarlos!

**Desarrollo: Caso B - Solo las mujeres juntas (1:55 - 2:45)**

* **Visual (Manim):** La restricción se reinicia. Ahora, solo las 2 mujeres están unidas por la cuerda de luz morada (un solo bloque). Los 3 hombres se liberan de su caja y quedan totalmente sueltos.
Una mano robótica cuenta los elementos en pantalla que se pueden mover libremente: el bloque de mujeres (1) + Hombre A (2) + Hombre B (3) + Hombre C (4). Total = $4$ elementos.
Ecuación central: $4!$ (movimiento de los 4 elementos) $\times 2!$ (movimiento de las mujeres dentro del bloque). Se resuelve: $24 \times 2 = 48$. El número $48$ brilla en verde.
> **Audio**: Ahora cambiemos las reglas del cuestionario. ¿Qué pasa si *justamente* las mujeres exigen sentarse juntas, pero a los hombres les da exactamente igual si están juntos o separados? Aplicamos el método otra vez: Atamos a las dos mujeres en un solo súper-bloque. Ahora, ¿cuántas entidades independientes tenemos en total en la fila? Tenemos a los 3 hombres sueltos, más nuestro súper-bloque indivisible de mujeres. ¡Son 4 entidades! Estos 4 elementos pueden ordenarse y mezclarse en la fila de "4 factorial" formas. Y no olvides que, en secreto dentro de su bloque, las dos mujeres pueden intercambiar asientos de "2 factorial" formas. Multiplicamos 4 factorial (que es 24) por 2 factorial (que es 2), ¡y obtenemos 48 formas de acomodar los exámenes!

**Cierre y CTA Final (2:45 - 3:20)**

* **Visual (Manim):** El número 48 destella y se descompone en 48 candados abriéndose simultáneamente. Los avatares y las sillas se transforman en puntos de datos de un plano cartesiano. Una línea curva y perfecta se traza formando una espectacular campana de Gauss (Distribución de Probabilidad) mientras el plano gira en 3D.
> **Audio: Al empaquetar tus objetos en bloques, puedes dominar cualquier restricción extrema que te ponga un algoritmo o un problema de lógica. Con este truco, ahora sí, oficialmente cerramos nuestro entrenamiento en el mundo del conteo y la probabilidad discreta. Tienes todo el arsenal matemático en tus manos. Nos vemos en nuestra próxima serie donde daremos el gran salto evolutivo hacia la estadística predictiva moderna: Las Variables Aleatorias y sus distribuciones.



