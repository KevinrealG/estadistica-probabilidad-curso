1. Geometrica -> c
## Video 5: Probabilidad Geométrica

**Gancho (0:00 - 0:35)**

* **Visual (Manim):** Un reloj digital avanza rápidamente. Se traza una línea de tiempo continua en la pantalla que va desde las 12:30 hasta las 13:10. Se resalta en verde el intervalo de 12:30 a 12:45 . Un avatar o un marcador parpadea en la línea indicando la "llegada".
> **Audio:** Tienes una reunión clave a la 1:00 de la tarde. Sabes que vas a llegar en algún momento exacto entre las 12:30 y la 1:10, y por cómo está el tráfico, cualquier instante en ese lapso es igual de probable. Quieres ser puntual y llegar por lo menos 15 minutos antes de la reunión, es decir, entre las 12:30 a 12:45. ¿Cuál es la probabilidad real de lograrlo? No puedes usar la probabilidad clásica porque no hay "casos" que contar; el tiempo no da saltos, fluye continuamente.

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** La línea de tiempo se transforma en un eje de coordenadas $X$. Aparece el título *"PROBABILIDAD GEOMÉTRICA"* con una animación de escritura, seguido del subtítulo *"Cuando el tiempo y el espacio son continuos"*.
> **Audio:** Bienvenidos a la dimensión continua. Hoy aprenderemos sobre la Probabilidad Geométrica, la poderosa herramienta matemática que nos permite calcular eventos en líneas, áreas y volúmenes donde es imposible contar.

**Desarrollo (0:50 - 2:45)**

 **Visual (Manim):** Aparece la clásica regla de Laplace y, con un efecto de transformación matemática, se reescribe como:

$$P(A) = \frac{\text{Medida}(A)}{\text{Medida}(\Omega)}$$


>**Audio:** La Probabilidad Geométrica es una adaptación directa de la Regla de Laplace, pero diseñada para experimentos con espacios muestrales continuos, no discretos. La probabilidad de que un punto aleatorio caiga dentro de tu evento, se define como la razón entre la "medida" de tu evento y la "medida" total del espacio.
* **Visual (Manim):** Aparecen 4 bloques enumerados: 1. Espacio Muestral ($\Omega$), 2. Evento ($A$), 3. Uniformidad, 4. Medida. Junto a "Medida", surgen íconos de una regla (Longitud 1D), un cuadrado (Área 2D) y un cubo (Volumen 3D).
> **Audio:** Tiene 4 elementos clave: El Espacio Muestral Continuo, el Evento, la Medida (que puede ser longitud si es una línea, área en 2D o volumen en 3D), y el supuesto más importante: la Uniformidad. Esto significa que cualquier punto en el espacio total tiene exactamente la misma probabilidad de ser el resultado.
* **Visual (Manim):** Se dibuja un segmento de línea horizontal etiquetado como $L = 10\text{ cm}$. Sobre él, un segmento azul más pequeño etiquetado como $l = 2\text{ cm}$ se desliza al azar de un lado a otro. Se muestra la ecuación $P(A) = 2/10 = 0.2$.
> **Audio:** Un ejemplo clásico: Imagina un segmento de línea de 10 centímetros en total. Si elegimos un punto aleatorio en él, ¿cuál es la probabilidad de que caiga dentro de un subsegmento específico de 2 centímetros? Muy fácil: la longitud de nuestro evento, 2, dividida por la longitud total, 10. Eso nos da un 20% de probabilidad.
* **Visual (Manim):** Regresa la línea de tiempo del gancho. El intervalo total $\Omega$ (12:30 a 1:10) se acota mostrando su medida: $40\text{ min}$. El evento $A$ (12:30 a 12:45 ) se acota mostrando: $15\text{ min}$. Se calcula la división en pantalla: $15/40 = 0.375$.
> **Audio:** ¡Ahora resolvamos el problema de tu reunión! Nuestro espacio muestral es el tiempo total entre las 12:30 y la 1:10; eso nos da una "medida" de 40 minutos. Nuestro evento ganador es el bloque de 15 minutos entre las 12:45 y la 1:00. Si dividimos 15 entre 40, obtenemos 0.375. ¡Tienes exactamente un 37.5% de probabilidad de ser puntual!
* **Visual (Manim):** Pantalla dividida en cuadrículas: un tablero de dardos con un dardo golpeando un área circular plana, un mapa GPS trazando un radio de encuentro con restricciones, y un modelo de colisión de partículas en 3D.
> **Audio:** De manera general, siempre que tu espacio muestral sea continuo, vas a usar esta probabilidad. Ya sea calculando el área para predecir si un dardo dará en el blanco, definiendo la probabilidad de puntos de encuentro en mapas, o analizando colisiones en física de fluidos.

**Cierre y CTA (2:45 - 3:10)**

* **Visual (Manim):** Aparecen 4 pilares: *Clásica*, *Frecuentista*, *Subjetiva* y *Geométrica*. Un haz de luz brillante los une en un solo libro o teorema dorado que dice: *"Axiomas de probabilidad"*.
> **Audio:** Ya dominamos los enfoques de la probabilidad: el teórico, el basado en datos, la intuición y el geométrico continuo. Pero en matemáticas, necesitamos reglas irrompibles que unan todo bajo un mismo idioma. En nuestro próximo video, construiremos el pilar de toda la estadística: La Definición Axiomática, la que nos permite obtener las propiedades y teoremas definitivos. ¡Suscríbete para no perdértelo!

2. Axiomática.
Aquí tienes el guion para el sexto video, manteniendo la regla de usar **exclusivamente animaciones en Manim y código**, sin apariciones a cámara, y estructurado como el cimiento matemático definitivo.

## Video 6: Probabilidad Axiomática

**Gancho (0:00 - 0:35)**

* **Visual (Manim):** Aparecen cuatro pilares ilustrados (etiquetados como *Clásica, Frecuentista, Subjetiva* y *Geométrica*). De repente, los pilares tiemblan ligeramente. Desde abajo, un bloque de concreto masivo e irrompible sube y se coloca debajo de todos ellos, dándoles estabilidad total. Sobre este bloque se graba la firma *"A. Kolmogórov, 1933"*.
> **Audio:** Hasta ahora, hemos calculado probabilidades de muchas formas: contando resultados, lanzando monedas miles de veces, usando la intuición de un experto o midiendo áreas en el tiempo. Pero para que las matemáticas puras te tomen en serio, todos estos métodos deben sostenerse sobre un cimiento inquebrantable. Ya no nos bastan simples fracciones o aproximaciones.

**Intro y Promesa (0:35 - 0:50)**

* **Visual (Manim):** El bloque de concreto se expande a toda la pantalla. Letras brillantes y precisas forman el título: *"PROBABILIDAD AXIOMÁTICA"*. Debajo, aparece el subtítulo: *"El Cimiento Matemático"*.
> **Audio:** Bienvenidos a la Probabilidad Axiomática. Hoy descubriremos cómo la probabilidad deja de ser una simple razón para convertirse en una función matemática pura, sostenida por tres axiomas absolutos e innegociables.

**Desarrollo (0:50 - 2:40)**

* **Visual (Manim):** Se dibuja una "máquina de funciones" matemática clásica etiquetada como $P(A)$. En el lado izquierdo, tenemos un espacio muestral $\Omega$ (un conjunto universo). Un evento $A$ entra en la máquina y por la derecha sale un número real en una recta numérica.
> **Audio:** En este nivel avanzado, la definición cambia. La probabilidad se define estrictamente como una función matemática $P$. Esta función le asigna a cada evento $A$, que está dentro de tu espacio muestral Omega, un número real. Y para que esta función exista estadísticamente, debe cumplir tres axiomas.
* **Visual (Manim):**
* Aparece en pantalla: **"Axioma 1: No negatividad"**.
* Fórmula: 
$$P(A) \ge 0$$


.
* Un medidor (tipo velocímetro) intenta ir hacia los números negativos, pero una barrera roja se lo impide, rebotando siempre hacia el cero o valores positivos.


> **Audio:** Axioma 1: No negatividad. Es simple, la probabilidad no puede ser negativa. Es matemáticamente imposible tener una probabilidad de "menos veinte por ciento". El límite inferior absoluto es siempre cero.
* **Visual (Manim):**
* Aparece en pantalla: **"Axioma 2: Probabilidad del espacio muestral"**.
* Fórmula: 
$$P(\Omega) = 1$$


.
* Se dibuja el conjunto universo $\Omega$ completo, iluminándose en un verde intenso al 100%.


> **Audio:** Axioma 2: La probabilidad del evento seguro. Si agrupamos todo el espacio muestral, es decir, todo lo que es posible que ocurra en tu experimento, es 100% seguro que al menos uno de esos resultados pasará. Por tanto, la probabilidad del espacio completo siempre es exactamente 1.
* **Visual (Manim / Simulación 3D):** Un dado perfecto de seis caras gira en la pantalla. Se dibujan 6 esferas separadas en un diagrama de Venn: $A (1)$, $B (2)$, $C (3)$, $D (4)$, $E (5)$, $F (6)$. Ninguna esfera se toca entre sí. Aparece el texto: *"Eventos Mutuamente Excluyentes"*.
> **Audio:** Antes del tercer axioma, definamos qué son los eventos mutuamente excluyentes. Imagina lanzar nuestro dado de seis caras. El Evento A es obtener un 1, el B un 2, el C un 3, y así hasta el Evento F que es sacar un 6. Al lanzar un solo dado, es físicamente imposible sacar un 2 y un 5 al mismo tiempo. No tienen nada en común, son eventos ajenos.
* **Visual (Manim):**
* Aparece en pantalla: **"Axioma 3: Aditividad para eventos ajenos"**.
* Fórmula: Si $A_i \cap A_j = \emptyset$ (para $i \ne j$), entonces 
$$P(\bigcup_{i=1}^{\infty} A_i) = \sum_{i=1}^{\infty} P(A_i)$$


* Las esferas del 1 y del 2 se unen matemáticamente con un signo de suma ($+$).


> **Audio:** Aquí entra el Axioma 3: Aditividad. Nos dice que, si tienes una secuencia de eventos mutuamente excluyentes (es decir, su intersección es vacía), la probabilidad de que ocurra uno "O" el otro, es simplemente la suma directa de sus probabilidades individuales. Con estas tres reglas, podemos demostrar todas las propiedades matemáticas de la estadística.

**Cierre y Conexión (2:40 - 3:00)**

* **Visual (Manim):** Las esferas separadas del diagrama de Venn de repente se mueven y se superponen creando una intersección brillante en el medio. Un gran signo de interrogación se dibuja sobre el área donde chocan.
> **Audio:** Pero aquí surge una gran pregunta: ¿qué pasa cuando los eventos sí se cruzan? ¿Qué ocurre si la probabilidad de un evento cambia drásticamente porque sabemos que otro evento *ya ocurrió*? Ahí es donde la matemática se vuelve fascinante con la Probabilidad Condicional. Y ese es exactamente el tema de nuestro próximo video. ¡Suscríbete y nos vemos allá!
3. Probabiliad condicional.
Aquí tienes el guion para el séptimo video de la serie, manteniendo la estructura de animaciones en Manim y simulaciones, sin apariciones a cámara, y utilizando un *storytelling* inmersivo.

## Video 7: Probabilidad Condicional

**Gancho (0:00 - 0:45)**

* **Visual (Manim/Simulación):** Pantalla estilo panel de aeropuerto. Un avión despega y el estado cambia a "ON TIME" (A Tiempo) en verde brillante.
> **Audio:** Imagina que tienes un vuelo con una conexión crítica. Miras las estadísticas de la aerolínea: la probabilidad de que sus vuelos salgan a tiempo es del 83% ($0.83$), y la probabilidad de que lleguen a tiempo es del 82% ($0.82$). Además, la probabilidad de que el vuelo haga ambas cosas (salga y llegue a tiempo) es del 78% ($0.78$). De repente, anuncian tu vuelo: ¡salió a tiempo! La pregunta es: sabiendo esta nueva información, ¿sigue siendo tu probabilidad de llegar a tiempo un 82%? No. Esa información extra acaba de cambiar las reglas del juego.

**Intro y Promesa (0:45 - 1:00)**

* **Visual (Manim):** El avión vuela a través de un anillo que actúa como un filtro matemático. Aparece el título en pantalla: *"PROBABILIDAD CONDICIONAL"*, con el subtítulo: *"Cuando la información transforma el futuro"*.
> **Audio:** Bienvenidos a la Probabilidad Condicional. Hoy aprenderemos a calcular cómo cambia la probabilidad de un evento cuando ya sabemos con absoluta certeza que otro evento acaba de ocurrir.

**Desarrollo: Concepto y Aplicación (1:00 - 1:45)**

* **Visual (Manim):** Aparece la fórmula matemática iluminada:

$$P(B\vert{}A) = \frac{P(A \cap B)}{P(A)}$$



Se resalta la barra vertical "$\vert{}$" y aparece el texto: *"Dado que / Sabiendo que"*.
> **Audio:** Su definición matemática nos dice que la probabilidad de que ocurra $B$, *dado que* ya ocurrió $A$, es igual a la probabilidad de que ocurran ambos (la intersección), dividida por la probabilidad del evento que ya pasó ($A$). Al dividir, lo que hace la matemática es "encoger" tu espacio muestral.
* **Visual (Manim):** Se muestran íconos de personas representando una población global (100%). Se aplica un filtro (embudo) que deja solo a "mujeres asiáticas de 35 a 50 años", y luego otro para "hombres hispanos de 40 a 60 años". Aparece un ícono médico (diabetes).
> **Audio:** ¿Para qué sirve esto? Piensa en la epidemiología. En lugar de calcular la probabilidad de que cualquier persona al azar en el mundo tenga diabetes, es mucho más útil e interesante conocer esta probabilidad condicionada a un grupo distinto. Por ejemplo, calcular el riesgo sabiendo que el paciente es una mujer asiática entre 35 y 50 años, o un hombre hispano entre 40 y 60 años. La información reduce el universo.

**Desarrollo: Ejemplo Práctico (1:45 - 2:40)**

* **Visual (Manim):** Se recrea la tabla de datos exactos en pantalla. El título dice "Tabla 2.1: Clasificación de los adultos de una pequeña ciudad". Aparecen columnas para "Empleado", "Desempleado" y "Total", y filas para "Hombre" y "Mujer". El Total absoluto en la esquina inferior derecha resalta: 900.


> **Audio:** Veamos este ejemplo: tenemos 900 adultos en una pequeña ciudad clasificados por género y situación laboral. Se elegirá a uno al azar para promover nuevas industrias.


* **Visual (Manim):** Aparece la pregunta: *¿Probabilidad de elegir a un Hombre ($M$), DADO QUE el elegido tiene Empleo ($E$)?* -> $P(M\vert{}E)$.


> **Audio:** Queremos saber la probabilidad de elegir a un hombre (evento M), pero condicionado a que sabemos que la persona elegida tiene empleo (evento E).


* **Visual (Manim):** ¡Magia visual! La columna "Desempleado" se oscurece o desaparece. La fila "Total" inferior ahora solo resalta el número de "Empleados": 600. El espacio muestral se ha reducido. Dentro de esta columna iluminada, la celda de "Hombre" (460) se marca en verde.


> **Audio:** Como ya sabemos que tiene empleo, eliminamos de nuestra mente a los desempleados. Nuestro espacio muestral se reduce de 900 a solo los 600 que tienen empleo. De esos 600, los casos favorables (los hombres) son 460.


* **Visual (Manim):** Se escribe la ecuación final:

$$P(M\vert{}E) = \frac{460}{600} = \frac{23}{30}$$


.


> **Audio:** Aplicando la fórmula, dividimos 460 entre 600, lo que simplificado nos da 23 sobre 30. ¡Así de fácil, el universo se ajustó a nuestra nueva información!



**Cierre y Conexión (2:40 - 3:10)**

* **Visual (Manim):** Regresamos a la pantalla del aeropuerto del inicio.
La ecuación se resuelve rápidamente: $P(\text{Llegar a tiempo} \vert{} \text{Salir a tiempo}) = 0.78 / 0.83 = 0.939$. El número "82%" se rompe y es reemplazado por un "94%".
> **Audio:** Volviendo a tu vuelo: la probabilidad de llegar a tiempo era 82%, pero sabiendo que *salió* a tiempo, aplicamos la regla (0.78 entre 0.83) y tu probabilidad se dispara a casi el 94%. Los eventos están conectados. Pero, ¿qué pasaría si un evento no afecta en lo absoluto al otro? Es decir, ¿qué pasa si el resultado de una moneda no afecta a la siguiente? Eso nos lleva a los Eventos Independientes, Dependientes y la famosa Regla de la Multiplicación, nuestro tema para el próximo video. ¡Suscríbete y no te lo pierdas!
4. Reglas de la multiplicación(eventos independientes y dependientes)
## Video 8: Eventos Independientes, Dependientes y la Regla de la Multiplicación

**Gancho (0:00 - 0:45)**

* **Visual (Manim/Simulación):** Animación 2D de un escenario de concurso televisivo. Hay tres puertas cerradas ($1, 2$ y $3$). Un jugador (silueta) elige la Puerta 1. De repente, el presentador, que tiene un portafolios con un guion que dice "Respuestas", abre la Puerta 3 para revelar una cabra que mastica pasto. Quedan las puertas 1 y 2. Aparece un gran texto flotante: *"¿Cambias de puerta?"* y dos porcentajes enfrentados: *"50/50" vs "33/66"*.
> **Audio:** Estás en un concurso de televisión. Hay tres puertas: detrás de una hay un auto deportivo, y detrás de las otras dos, cabras. Eliges la puerta 1. El presentador, que sabe exactamente dónde está el auto, abre la puerta 3 y te muestra una cabra. Luego te pregunta: "¿Quieres cambiar a la puerta 2?". La mayoría de la gente cree que, al quedar dos puertas, la probabilidad es 50/50, asumiendo que lo que hizo el presentador es un evento "independiente". Pero se equivocan. La decisión del presentador *depende* de tu elección inicial, y al cambiar de puerta, ¡tu probabilidad de ganar se duplica al 66%! Bienvenido a la Paradoja de Monty Hall.

**Intro y Promesa (0:45 - 1:00)**

* **Visual (Manim):** Las puertas se desvanecen y se transforman en ramas de un árbol matemático. Aparece el título: *"Eventos Independientes y Dependientes"*, y debajo: *"La Regla de la Multiplicación"*.
> **Audio:** Hoy vamos a dominar la diferencia entre eventos independientes y dependientes. Usaremos diagramas de árbol para visualizar el futuro y aprenderemos la Regla de la Multiplicación, o regla de la cadena, para calcular la probabilidad de que ocurran múltiples eventos seguidos.

**Desarrollo: Independientes vs Dependientes con Árboles (1:00 - 2:00)**

* **Visual (Manim):** Pantalla dividida.
* **Izquierda (Independiente):** Un árbol de decisión lanzando una moneda. Nodo inicial $\to$ Cara (0.5) / Sello (0.5). De la rama "Cara", salen otras dos: Cara (0.5) / Sello (0.5). Los números nunca cambian.
* **Derecha (Dependiente):** Un árbol de pruebas médicas. Nodo inicial $\to$ Enfermo (0.1) / Sano (0.9). De la rama "Enfermo" sale "Prueba Positiva (0.95)". De la rama "Sano" sale "Prueba Positiva (falso positivo) (0.05)". Los números cambian drásticamente dependiendo de la rama anterior.


> **Audio:** Visualicemos esto. A la izquierda, eventos independientes: lanzar una moneda dos veces. A la segunda tirada no le importa en lo absoluto qué salió en la primera; no tiene memoria. Las probabilidades de las ramas se mantienen siempre en 50/50.
A la derecha, eventos dependientes: una prueba médica. La probabilidad de que des positivo en el test *depende* por completo de si estás realmente enfermo o sano en el primer paso. El resultado del primer evento altera drásticamente las matemáticas del segundo.

**Desarrollo: La Regla de la Multiplicación (2:00 - 2:30)**

* **Visual (Manim):** El árbol de la moneda desaparece. Se centra el foco en las fórmulas matemáticas, que se dibujan dinámicamente con trazos brillantes:
* Texto *"Si son Independientes:"* 
$$P(A \cap B) = P(A) \times P(B)$$


* Texto *"Si son Dependientes:"* 
$$P(A \cap B) = P(A) \times P(B\vert{}A)$$




> **Audio:** ¿Cómo calculamos que pasen dos o más cosas en secuencia? Es decir, el evento A *Y* el evento B. Usamos la Regla de la Multiplicación. Si son independientes, simplemente multiplicas la probabilidad de A por la de B. Pero si son dependientes, multiplicas la probabilidad de A por la probabilidad condicional de B *dado que* A ya ocurrió, usando lo que aprendimos en el video anterior.

**Desarrollo: Ejercicio Práctico (2:30 - 3:15)**

* **Visual (Manim):** Se dibuja una baraja de 52 cartas. Se extrae un As de Picas. El contador de cartas totales baja a 51 y el de Ases baja a 3. Se extrae un segundo As (de Corazones).
Ecuación en pantalla:

$$P(\text{As}_1 \cap \text{As}_2) = \left(\frac{4}{52}\right) \times \left(\frac{3}{51}\right)$$


$$P(\text{As}_1 \cap \text{As}_2) = 0.0769 \times 0.0588 \approx 0.0045 \text{ (o } 0.45\%)$$


> **Audio:** Hagamos un ejercicio clásico de eventos dependientes. Sacar dos Ases seguidos de una baraja, sin devolver la primera carta. La probabilidad del primer As es 4 de 52. Pero ahora la baraja cambió. Para el segundo As, solo quedan 3 Ases en un total de 51 cartas. Multiplicamos la primera probabilidad (4 sobre 52) por nuestra probabilidad condicional (3 sobre 51). El resultado es un 0.45%. ¡Las probabilidades en cadena caen rapidísimo!

**Desarrollo: Otras Aplicaciones (3:15 - 3:40)**

* **Visual (Manim / Iconos animados):** Aparecen tres servidores de red conectados. Uno falla y los otros dos ajustan su carga (Dependencia). Luego, un filtro de correo analizando palabras clave: "Oferta" y "Gratis", tratándolas como independientes (Clasificador Naive Bayes).
> **Audio:** ¿Dónde más aplicamos la regla de la multiplicación? En ingeniería de software, para calcular si un sistema entero colapsará si falla un servidor del que dependen los demás. En Machine Learning, los algoritmos como Naive Bayes calculan si un correo es Spam asumiendo de manera simplificada que la aparición de palabras como "oferta" y "gratis" son eventos independientes y multiplicando sus probabilidades.

**Cierre y Conexión (3:40 - 4:10)**

* **Visual (Manim):** Regresa a pantalla completa el diagrama de árbol de las pruebas médicas. Se resaltan en un amarillo brillante las palabras "Prueba Positiva" al final de la rama de los "Enfermos", y también el "Prueba Positiva" al final de la rama de los "Sanos". Aparece un signo de interrogación inmenso y la ecuación: 
$$P(\text{Prueba Positiva Total}) = ?$$


> **Audio:** Ya sabemos cómo multiplicar para movernos a través de una sola rama del árbol. Pero, mira este árbol médico: puedes dar positivo porque estás enfermo, O puedes dar positivo por un error de la máquina estando sano. Si te pregunto: "¿Cuál es la probabilidad TOTAL de dar positivo en general?", ya no nos sirve multiplicar una sola línea. Necesitamos una regla maestra que sume todos los caminos posibles. Acompáñame en el próximo video para descubrir el Teorema de la Probabilidad Total y preparar el terreno para la fórmula más famosa de la estadística. ¡Suscríbete!
4. Probabilidad total
