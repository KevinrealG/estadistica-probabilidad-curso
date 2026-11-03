## Video 9: Teorema de la Probabilidad Total

**Gancho (0:00 - 0:40)**

* **Visual (Manim):** En pantalla aparece el diagrama de árbol médico del video anterior. Se ilumina el nodo inicial: *"Paciente"*. De ahí salen dos ramas principales: *"Enfermo (10%)"* y *"Sano (90%)"*. De la rama "Enfermo", sale una sub-rama brillante: *"Prueba Positiva (95%)"*. De la rama "Sano", sale otra sub-rama que también brilla: *"Prueba Positiva (5% - falso positivo)"*.
> **Audio:** Retomemos la  pregunta que dejamos pendiente. Tienes este árbol de decisión para una prueba médica. Puedes dar positivo porque realmente estás enfermo, o puedes dar positivo por un error de la prueba estando perfectamente sano. Si eres el director del hospital y te pregunto: "¿Cuál es la probabilidad TOTAL de que un paciente cualquiera que entre por la puerta dé positivo en esta prueba?", ya no basta con mirar una sola línea. Tenemos que sumar los caminos.

**Intro y Promesa (0:40 - 0:55)**

* **Visual (Manim):** Los caminos brillantes del árbol convergen en el centro de la pantalla formando una ecuación gigante. Aparece el título: *"TEOREMA DE LA PROBABILIDAD TOTAL"*.
> **Audio:** Bienvenidos al Teorema de la Probabilidad Total. Hoy aprenderemos la regla matemática para calcular la probabilidad global de un evento cuando este puede ocurrir a través de múltiples escenarios diferentes.

**Desarrollo: Diagrama de Venn y el Árbol (0:55 - 1:55)**

* **Visual (Manim):** La pantalla se divide.
* **Derecha:** Se mantiene el árbol con las dos ramas finales de "Prueba Positiva" parpadeando.
* **Izquierda:** Se dibuja un gran rectángulo (el espacio muestral $\Omega$). Se traza una línea vertical que divide el rectángulo en dos bloques: $B_1$ (Enfermo) y $B_2$ (Sano). Luego, se dibuja un círculo rojo brillante (Evento $A$: Prueba Positiva) que se superpone justo en el medio, abarcando un trozo de $B_1$ y un trozo de $B_2$.


> **Audio:** Visualmente, esto es lo que está pasando. A la izquierda, nuestro universo de pacientes está partido en dos grupos que no se mezclan: enfermos y sanos. A esto se le llama una partición. Nuestro evento objetivo, el círculo rojo que representa "dar positivo", existe en ambos mundos.
* **Visual (Manim):** El círculo rojo se separa en dos piezas de rompecabezas. En la pieza izquierda se escribe $P(A \cap B_1)$ y en la derecha $P(A \cap B_2)$. Luego se unen con un signo de suma. Aparece la fórmula general: 
$$P(A) = \sum P(B_i) \times P(A\vert{}B_i)$$


> **Audio:** Para saber el área total del círculo rojo, simplemente sumamos el pedazo que cae en los enfermos más el pedazo que cae en los sanos. Traducido al árbol de la derecha: multiplicamos las probabilidades de la primera rama para encontrar su intersección, hacemos lo mismo con la segunda rama, y sumamos ambos resultados.

**Desarrollo: Resolviendo el Ejercicio (1:55 - 2:45)**

* **Visual (Manim):** El árbol toma toda la pantalla y los números cobran protagonismo.
* *Camino 1 (Enfermo y Positivo):* $0.10 \times 0.95 = 0.095$ (Baja de la rama como una gota de luz hasta una caja de suma).
* *Camino 2 (Sano y Positivo):* $0.90 \times 0.05 = 0.045$ (Baja como otra gota a la misma caja).
* *Caja de suma:* $0.095 + 0.045 = 0.14$.


> **Audio:** Resolvamos el ejercicio del hospital. Camino 1, ser un paciente enfermo y dar positivo: multiplicamos el 10% de probabilidad de estar enfermo por el 95% de efectividad de la prueba. Eso nos da 0.095. Camino 2, ser un paciente sano pero recibir un falso positivo: multiplicamos el 90% de probabilidad de estar sano por el 5% de error. Eso nos da 0.045. Finalmente, sumamos 0.095 más 0.045 y obtenemos 0.14. ¡Exactamente un 14% de probabilidad total de que cualquier prueba salga positiva!

**Desarrollo: Aplicaciones y Casos Parecidos (2:45 - 3:15)**

* **Visual (Manim / Gráficos de vectores):** Aparece un gráfico financiero de acciones subiendo, alimentado por tres tuberías: "Economía en auge (30%)", "Economía estable (50%)", "Recesión (20%)". Luego, el esquema de una fábrica donde un celular defectuoso puede venir de la Máquina A, la Máquina B o la Máquina C.
> **Audio:** Esta lógica aplica en todas partes. En finanzas, para predecir la probabilidad total de que una acción suba, sumando los escenarios de que la economía esté en auge, estable o en recesión. O en ingeniería de calidad, para saber la probabilidad de que un producto salga defectuoso si es fabricado por tres máquinas diferentes, cada una con su propia tasa de error y volumen de producción. Siempre que un evento dependa de varios escenarios, usas esta ley.

**Cierre y Conexión (3:15 - 3:45)**

* **Visual (Manim):** Volvemos al árbol médico. La palabra *"POSITIVO"* en rojo domina la pantalla. Una flecha empieza a recorrer el árbol **hacia atrás**, desde "Positivo" buscando el camino de regreso hacia el nodo de "Enfermo". Aparece un enorme signo de interrogación.
> **Audio:** Ya sabemos que la probabilidad de dar positivo es del 14%. Pero ahora, pongámonos en tus zapatos. Imagina que te haces la prueba y... ¡das positivo! El evento ya ocurrió. Ahora quieres saber: dado que ya tengo el papel con el positivo en la mano, ¿cuál es la probabilidad de que REALMENTE esté enfermo? Para responder esto, tenemos que viajar en el tiempo, recorrer el árbol matemático hacia atrás. Y para lograr eso necesitamos : El Teorema de Bayes. Ese es nuestro próximo video. ¡Suscríbete y vamos a descubrirlo!
## Reglas de Probabilidad
Aquí tienes el guion para el siguiente video, enfocado en las reglas fundamentales de la probabilidad (Complemento y Suma), utilizando tu interés por el béisbol (sabermetría) y las artes marciales como motor del *storytelling*, y manteniendo estrictamente el formato 100% visual y de código.

## Video 11: Reglas de Probabilidad (Complemento)

**Gancho (0:00 - 0:40)**

* **Visual (Manim o Animación de IA):** Vista de un estadio de béisbol en 2D. En la caja de bateo, una silueta que representa a Shohei Ohtani. Aparece una estadística flotante: *"Promedio de Bateo: .300 (30%)"*. El marcador indica que Ohtani tendrá 4 turnos al bate en el juego. Aparece el reto en pantalla gigante: *"¿Probabilidad de conectar AL MENOS UN hit en el juego?"*.
> **Audio:** Imagina que estás analizando las estadísticas de Shohei Ohtani. Sabes que tiene un 30% de probabilidad de conectar un hit en cada turno. Hoy va a batear 4 veces. ¿Cuál es la probabilidad de que conecte *al menos un* hit en todo el partido? Tu instinto matemático te dirá: "¡Fácil! Calculo la probabilidad de que pegue 1 hit, más la probabilidad de que pegue 2, más la de 3, más la de 4". ¡Detente! Hacer todos esos cálculos te tomará una eternidad. ¿Qué pasaría si te dijera que hay un atajo para resolver esto en un solo paso?

**Intro y Promesa (0:40 - 0:55)**

* **Visual (Manim):** El campo de béisbol se contrae hasta convertirse en un círculo de diagrama de Venn. Se despliega el título central: *"REGLAS DE PROBABILIDAD"*, y debajo una rama brillante: *"El Complemento"* 
> **Audio:** Regla deel complemento

**Desarrollo: La Regla del Complemento (0:55 - 1:55)**

* **Visual (Manim):** Aparece un círculo verde grande que representa el $100\%$ ($1.0$). Dentro de él, un círculo más pequeño marcado como $P(A)$. El espacio sobrante se ilumina en azul y se marca como $P(A^c)$ (o $P(A')$).
Se dibuja la fórmula: 
$$P(A) + P(A^c) = 1 \implies P(A) = 1 - P(A^c)$$


> **Audio:** Empecemos con el atajo de Ohtani: La Regla del Complemento. Esta regla nos dice que la probabilidad de que un evento ocurra, más la probabilidad de que *no* ocurra, siempre es igual a 1 (o 100%). Si calcular todos los escenarios ganadores es muy difícil, simplemente calculamos el único escenario perdedor y se lo restamos a 1.
* **Visual (Manim):** En pantalla aparece el cálculo.
Probabilidad de NO dar hit = $70\%$ ($0.70$).
Para 4 turnos: 
$$0.70 \times 0.70 \times 0.70 \times 0.70 = 0.2401$$


 (24%).

$$P(\text{Al menos 1 hit}) = 1 - 0.24 = 0.76$$



El número **76%** estalla en pantalla con luces de celebración.
> **Audio:** Volvamos al béisbol. ¿Qué es lo contrario de conectar "al menos un hit"? Pues irse en blanco, es decir, fallar los 4 turnos seguidos. Si Ohtani tiene 30% de dar hit, tiene 70% de fallar. Elevamos 0.70 a la cuarta potencia para sus cuatro turnos, y nos da 24%. Ahora, a nuestro 100% le restamos ese 24%... ¡y boom! Tiene un 76% de probabilidad de conectar al menos un hit hoy. ¡Un solo cálculo!

**Desarrollo: La Regla de la Suma (1:55 - 3:00)**

* **Visual (Manim):** La escena cambia. Se dibuja un DataFrame de Pandas (o un panel de Excel) titulado *"Club GunJu - Base de Datos"*. El contador muestra 100 estudiantes totales. Aparecen dos Diagramas de Venn intersectados:
* Círculo Azul (Taekwondo): $60$ alumnos.
* Círculo Rojo (Hapkido): $50$ alumnos.
Se cruzan en el medio, y en la intersección brilla el número $20$.


> **Audio:** Ahora, ¿qué pasa cuando queremos saber si ocurre un evento *O* el otro? Para eso usamos la Regla de la Suma. Digamos que administras la base de datos de las clases de artes marciales del Club GunJu. Tienes 100 estudiantes en total. 60 practican Taekwondo y 50 practican Hapkido.
* **Visual (Manim):** Aparece la pregunta: $$*P(\text{Taekwondo} \cup \text{Hapkido}) = ?*
> **Audio:** Si elijo a un estudiante al azar, ¿cuál es la probabilidad de que practique Taekwondo O Hapkido? Si simplemente sumas 60 más 50, te da 110. ¡Imposible, solo tienes 100 alumnos! ¿Qué salió mal?
* **Visual (Manim):** Se dibuja la fórmula de la Regla General de la Suma:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$



Los círculos parpadean. Se suma 60 (azul), se suma 50 (rojo) y se elimina visualmente (se resta) el centro para no contarlo doble: $-20$.
El resultado aparece: $P = \frac{60 + 50 - 20}{100} = \frac{90}{100} = 90\%$.
> **Audio:** El error es que hay estudiantes doblemente talentosos: 20 de ellos practican *ambas* artes marciales. Al sumar los grupos totales, contaste a esos 20 dos veces. Por eso, la regla general de la suma nos obliga a sumar la probabilidad de A, más la probabilidad de B, y luego *restar* la intersección para eliminar el doble conteo. Así, $60 + 50$ menos $20$ nos da 90. Tienes un 90% de probabilidad de elegir a alguien que practique al menos una de las dos.

**Cierre y CTA (3:00 - 3:30)**

* **Visual (Manim):** La pantalla se divide en tres recuadros abstractos: una moneda cayendo (experimento aleatorio), los números resultantes mapeándose en una recta (Variables Aleatorias) y, finalmente, un hermoso gráfico de campana de Gauss dibujándose (Distribución).
> **Audio:** Con estas reglas y teoremas, nuestro cinturón negro en cálculo de probabilidades básicas está completo. Ya no te dejas engañar por el azar. Pero, ¿qué pasa cuando queremos predecir el comportamiento masivo de miles de datos a la vez, creando gráficas completas de probabilidad? Para dar ese salto profesional, necesitamos introducir el concepto de las Variables Aleatorias. Y ese, será nuestro próximo gran desafío. ¡Suscríbete, deja tu like y nos vemos en el siguiente video!
##  Teorema de BAyes
## Video 10: El Teorema de Bayes

**Gancho (0:00 - 0:45)**

* **Visual (Manim/Simulación):** Una animación en primera persona. Unas manos virtuales abren un sobre blanco de laboratorio. El papel en su interior tiene un sello rojo gigante que dice: *"RESULTADO: POSITIVO"*. Un latido de corazón acelerado suena de fondo. Aparece un texto flotante: *"Precisión de la prueba: 95%"*.
> **Audio:** Imagina esto: te haces una prueba médica de rutina para una enfermedad. Abres el sobre y dice "Positivo". Entras en pánico porque recuerdas que el doctor te dijo que la prueba tiene una precisión del 95%. Tu intuición te grita que tienes un 95% de probabilidades de estar enfermo. ¡Pero detente ahí! Tu intuición te está mintiendo. Esa es la trampa más grande de la estadística. La probabilidad real de que estés enfermo es mucho menor, y para demostrarlo, vamos a viajar en el tiempo matemático.

**Intro y Promesa (0:45 - 1:00)**

* **Visual (Manim):** El papel médico se desvanece en partículas. De esas partículas se forma una ecuación elegante y brillante en el centro de la pantalla. Título: *"TEOREMA DE BAYES"*. Subtítulo: *"Actualizando la realidad con nueva evidencia"*.
> **Audio:** Bienvenidos a la joya de la corona de la estadística: El Teorema de Bayes. Hoy aprenderemos la fórmula que permite a la inteligencia artificial, a los científicos y a los médicos "reversar" las probabilidades y descubrir la verdad cuando aparece nueva evidencia.

**Desarrollo: La Trampa de la Intuición y la Fórmula (1:00 - 1:50)**

* **Visual (Manim):** Aparece la gran fórmula de Bayes:

$$P(A\vert{}B) = \frac{P(B\vert{}A) \times P(A)}{P(B)}$$



Se reescribe automáticamente al contexto médico:

$$P(\text{Enfermo}\vert{}\text{Positivo}) = \frac{P(\text{Positivo}\vert{}\text{Enfermo}) \times P(\text{Enfermo})}{P(\text{Positivo Total})}$$


> **Audio:** El Teorema de Bayes nos permite responder nuestra gran pregunta: ¿Cuál es la probabilidad de estar Enfermo, *dado que* ya di Positivo? La fórmula nos dice que esto es igual a la probabilidad de dar positivo estando enfermo (la eficacia de la prueba), multiplicado por la probabilidad inicial de estar enfermo en la población, todo esto dividido por la probabilidad TOTAL de dar positivo. ¡Exacto, el resultado de nuestro video anterior!

**Desarrollo: Resolviendo el Misterio (1:50 - 2:40)**

* **Visual (Manim):** Regresa el árbol de decisión del video anterior.
* Nodo inicial $\to$ Enfermo (10%) $\to$ Prueba Positiva (95%). Camino total: $0.095$.
* La caja de suma final abajo dice: *"Probabilidad Total de Positivo = 14% (0.14)"*.
Una flecha animada hace el recorrido **hacia atrás**, desde la caja del 14% hacia la rama de "Enfermo" ($0.095$).


> **Audio:** En nuestro video anterior, descubrimos que la probabilidad de que cualquier persona elegida al azar esté enferma es apenas del 10%. Y calculamos que la probabilidad TOTAL de obtener un examen positivo (mezclando a los enfermos reales y a los falsos positivos de los sanos) era del 14%, o 0.14.
* **Visual (Manim):** Los números reemplazan las variables en la fórmula:

$$P(\text{Enfermo}\vert{}\text{Positivo}) = \frac{0.095}{0.14}$$



El resultado se calcula en pantalla con un efecto de caja registradora: **$0.678$ (67.8%)**.
> **Audio:** Apliquemos Bayes. Tomamos el camino de los que realmente están enfermos y dan positivo, que es 0.095, y lo dividimos por nuestro universo de todos los que dieron positivo, que es 0.14. ¿El resultado? 67.8%. ¡Boom! A pesar de que tu prueba tiene una eficacia del 95%, tu probabilidad real de estar enfermo es solo de un 68%.

**Desarrollo: ¿Por qué ocurre esto? (La Paradoja) (2:40 - 3:20)**

* **Visual (Manim):** Se muestran 1,000 avatares pequeños en pantalla. 100 se pintan de rojo (Enfermos) y 900 de verde (Sanos). La máquina de pruebas ilumina a 95 rojos (verdaderos positivos) y, debido a su 5% de error, ilumina a 45 verdes (falsos positivos).
> **Audio:** ¿Por qué bajó tanto? A esto se le llama ignorar la tasa base. Como la enfermedad es rara (solo el 10% de la población la tiene), hay muchísimas más personas sanas haciéndose la prueba. Ese 5% de error de la máquina aplicado a una enorme multitud de sanos genera un montón de falsos positivos que "diluyen" los resultados. Bayes toma en cuenta el contexto completo, tu intuición no.

**Cierre, Aplicaciones y CTA (3:20 - 4:00)**

* **Visual (Manim / Gráficos de tecnología):** Aparece un filtro de Gmail enviando correos con la palabra "Oferta" a la carpeta de Spam. Luego un submarino amarillo con un radar mapeando el fondo del océano.
> **Audio:** El Teorema de Bayes no solo salva vidas evitando diagnósticos apresurados. Es el motor principal detrás de los filtros de Spam en tu correo y los algoritmos de Machine Learning. Incluso se usó matemáticamente para encontrar submarinos perdidos en el océano, actualizando el mapa de búsqueda cada vez que encontraban una nueva pista.
* **Visual (Manim):** Un mosaico con pequeñas miniaturas abstractas de los conceptos vistos en toda la serie: Dados (Clásica), Gráficas (Frecuentista), Relojes (Geométrica), Árboles (Multiplicación) y la Fórmula de Bayes brillando en el centro.
> **Audio:** Con esto cerramos nuestro viaje por las leyes de la probabilidad. Desde los simples juegos de azar hasta la matemática predictiva que domina la inteligencia artificial. Si dominas esto, dominarás los datos. Si te gustó esta serie, suscríbete, deja un buen like, y cuéntame en los comentarios qué otra rama de las matemáticas o la programación quieres que exploremos. ¡Hasta la próxima!


Aquí tienes el guion enfocado exclusivamente en la Regla de la Suma, utilizando tu ejemplo de la escuela y los deportes, y manteniendo el formato 100% visual y matemático (sin apariciones a cámara) como acordamos.

## Video: La Regla de la Suma en Probabilidad

**Gancho (0:00 - 0:40)**

* **Visual (Manim):** Un fondo que simula un campo de césped. En la pantalla aparece un totalizador: *"Escuela: 200 Estudiantes"*. Del lado izquierdo, caen pelotas de béisbol formando un grupo con el número 80. Del lado derecho, caen balones de fútbol formando un grupo con el número 100.
* **Audio:** Imagina que eres el director de deportes de una escuela de 200 estudiantes. Revisas tus listas y ves que 80 estudiantes juegan béisbol y 100 juegan fútbol. Si eliges a un estudiante completamente al azar, ¿cuál es la probabilidad de que juegue *al menos uno* de estos deportes? Si tu cerebro sumó rápidamente "80 más 100 son 180, ¡entonces 180 de 200!", acabas de caer en una de las trampas más comunes de la estadística. Estás contando datos por duplicado, y te voy a mostrar por qué.

**Intro y Promesa (0:40 - 0:55)**

* **Visual (Manim):** Los balones y pelotas se desvanecen. En el centro de la pantalla se dibuja un título dinámico: *"LA REGLA DE LA SUMA"*. Debajo, aparecen los símbolos matemáticos de unión e intersección: $\cup$ y $\cap$.
* **Audio:** Bienvenidos de nuevo. Hoy vamos a dominar la Regla de la Suma en probabilidad. Aprenderás a calcular la probabilidad de que ocurra un evento "O" el otro, sin duplicar tu información y usando la lógica de conjuntos.

**Desarrollo: La Trampa del Doble Conteo (0:55 - 1:45)**

* **Visual (Manim):** Se dibuja un Diagrama de Venn.
Un gran círculo azul a la izquierda etiquetado como *"Béisbol (A)"* con el número 80.
Un gran círculo verde a la derecha etiquetado como *"Fútbol (B)"* con el número 100.
Los círculos se mueven hacia el centro y se superponen. La zona de intersección en el medio se ilumina en amarillo brillante y aparece el número 30.
* **Audio:** Miremos los datos reales con un Diagrama de Venn. Tienes 80 beisbolistas y 100 futbolistas. Pero aquí está el secreto: hay 30 estudiantes con un talento doble que practican *ambos* deportes. Cuando sumaste 80 más 100 hace un momento, sumaste a esos 30 estudiantes dos veces: una vez en la lista de béisbol y otra vez en la de fútbol.

**Desarrollo: La Fórmula y el Cálculo (1:45 - 2:30)**

* **Visual (Manim):** Aparece la fórmula matemática en la parte superior:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$



Los elementos del Diagrama de Venn saltan hacia la fórmula mientras se mencionan.
* **Audio:** Para corregir este error, usamos la Regla General de la Suma. Ésta nos dice que la probabilidad de A *unión* B (es decir, béisbol O fútbol) es igual a la probabilidad de A, más la probabilidad de B, *menos* la intersección de ambos.
* **Visual (Manim):** La ecuación se llena con los números de la escuela:

$$P(\text{Béisbol} \cup \text{Fútbol}) = \frac{80}{200} + \frac{100}{200} - \frac{30}{200}$$



El cálculo se resuelve visualmente: $\frac{180}{200} - \frac{30}{200} = \frac{150}{200}$.
El resultado final salta en grande: **$0.75$ o $75\%$**.
* **Audio:** Si lo aplicamos a nuestra escuela: 80 más 100 es 180. A eso le restamos los 30 estudiantes que contamos dos veces, lo que nos da 150 estudiantes únicos que hacen deporte. 150 dividido entre nuestro universo de 200 estudiantes, nos da exactamente un 75%. Tienes un 75% de probabilidad de elegir a alguien que juegue al menos un deporte.

**Desarrollo: ¿Cuándo Aplicar esta Regla? (2:30 - 3:00)**

* **Visual (Manim):** El Diagrama de Venn se separa. Ahora los dos círculos (A y B) están completamente aislados, sin tocarse. El símbolo de intersección $\cap$ marca $0$. Aparece el texto: *"Eventos Mutuamente Excluyentes"*.
* **Audio:** ¿Cuándo debes aplicar esta regla? Siempre que en tu pregunta aparezca la palabra "O"; cuando busques que suceda una condición o la otra. Pero ten cuidado: si los eventos son *mutuamente excluyentes*, es decir, es físicamente imposible que ocurran al mismo tiempo y su intersección es cero, entonces simplemente sumas las dos probabilidades directas. Pero si comparten datos, ¡nunca olvides restar el centro!

**Cierre y Conexión al Siguiente Tema (3:00 - 3:30)**

* **Visual (Manim):** Se muestra un dado lanzándose, que se transforma en un código de barras, luego en un histograma, y finalmente en una hermosa curva de campana (Distribución Normal) trazándose suavemente.
* **Audio:** Ahora ya sabes sumar probabilidades como un profesional. Pero hasta ahora, en todos nuestros ejemplos solo hemos calculado un par de resultados específicos. ¿Qué pasaría si quisiéramos graficar *todos* los resultados posibles de un experimento y ver cómo se distribuyen visualmente? Para dar ese salto de la probabilidad básica a la estadística avanzada, necesitamos introducir las Variables Aleatorias. Y ese, será nuestro próximo video. ¡Suscríbete, deja un like y nos vemos allá!
