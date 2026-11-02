## Video 9: Teorema de la Probabilidad Total

**Gancho (0:00 - 0:40)**

* **Visual (Manim):** En pantalla aparece el diagrama de árbol médico del video anterior. Se ilumina el nodo inicial: *"Paciente"*. De ahí salen dos ramas principales: *"Enfermo (10%)"* y *"Sano (90%)"*. De la rama "Enfermo", sale una sub-rama brillante: *"Prueba Positiva (95%)"*. De la rama "Sano", sale otra sub-rama que también brilla: *"Prueba Positiva (5% - falso positivo)"*.
> **Audio:** Retomemos la gran pregunta que dejamos pendiente. Tienes este árbol de decisión para una prueba médica. Puedes dar positivo porque realmente estás enfermo, o puedes dar positivo por un error de la máquina estando perfectamente sano. Si eres el director del hospital y te pregunto: "¿Cuál es la probabilidad TOTAL de que un paciente cualquiera que entre por la puerta dé positivo en esta prueba?", ya no basta con mirar una sola línea. Tenemos que sumar los caminos.

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
> **Audio:** Ya sabemos que la probabilidad de dar positivo es del 14%. Pero ahora, pongámonos en tus zapatos. Imagina que te haces la prueba y... ¡das positivo! El evento ya ocurrió. Ahora quieres saber: dado que ya tengo el papel con el positivo en la mano, ¿cuál es la probabilidad de que REALMENTE esté enfermo? Para responder esto, tenemos que viajar en el tiempo, recorrer el árbol matemático hacia atrás. Y para lograr eso, necesitamos la joya de la corona de la estadística: El Teorema de Bayes. Ese es nuestro próximo video. ¡Suscríbete y vamos a descubrirlo!
## Reglas de Probabilidad
Video 10: El Teorema de Bayes
Gancho (0:00 - 0:45)
 * Visual (Manim/Simulación): Una animación en primera persona. Unas manos virtuales abren un sobre blanco de laboratorio. El papel en su interior tiene un sello rojo gigante que dice: "RESULTADO: POSITIVO". Un latido de corazón acelerado suena de fondo. Aparece un texto flotante: "Precisión de la prueba: 95%".
 * Audio: Imagina esto: te haces una prueba médica de rutina para una enfermedad. Abres el sobre y dice "Positivo". Entras en pánico porque recuerdas que el doctor te dijo que la prueba tiene una precisión del 95%. Tu intuición te grita que tienes un 95% de probabilidades de estar enfermo. ¡Pero detente ahí! Tu intuición te está mintiendo. Esa es la trampa más grande de la estadística. La probabilidad real de que estés enfermo es mucho menor, y para demostrarlo, vamos a viajar en el tiempo matemático.
Intro y Promesa (0:45 - 1:00)
 * Visual (Manim): El papel médico se desvanece en partículas. De esas partículas se forma una ecuación elegante y brillante en el centro de la pantalla. Título: "TEOREMA DE BAYES". Subtítulo: "Actualizando la realidad con nueva evidencia".
 * Audio: Bienvenidos a la joya de la corona de la estadística: El Teorema de Bayes. Hoy aprenderemos la fórmula que permite a la inteligencia artificial, a los científicos y a los médicos "reversar" las probabilidades y descubrir la verdad cuando aparece nueva evidencia.
Desarrollo: La Trampa de la Intuición y la Fórmula (1:00 - 1:50)
 * Visual (Manim): Aparece la gran fórmula de Bayes:
   
   
   Se reescribe automáticamente al contexto médico:
   
 * Audio: El Teorema de Bayes nos permite responder nuestra gran pregunta: ¿Cuál es la probabilidad de estar Enfermo, dado que ya di Positivo? La fórmula nos dice que esto es igual a la probabilidad de dar positivo estando enfermo (la eficacia de la prueba), multiplicado por la probabilidad inicial de estar enfermo en la población, todo esto dividido por la probabilidad TOTAL de dar positivo. ¡Exacto, el resultado de nuestro video anterior!
Desarrollo: Resolviendo el Misterio (1:50 - 2:40)
 * Visual (Manim): Regresa el árbol de decisión del video anterior.
   * Nodo inicial \to Enfermo (10%) \to Prueba Positiva (95%). Camino total: 0.095.
   * La caja de suma final abajo dice: "Probabilidad Total de Positivo = 14% (0.14)".
     Una flecha animada hace el recorrido hacia atrás, desde la caja del 14% hacia la rama de "Enfermo" (0.095).
 * Audio: En nuestro video anterior, descubrimos que la probabilidad de que cualquier persona elegida al azar esté enferma es apenas del 10%. Y calculamos que la probabilidad TOTAL de obtener un examen positivo (mezclando a los enfermos reales y a los falsos positivos de los sanos) era del 14%, o 0.14.
 * Visual (Manim): Los números reemplazan las variables en la fórmula:
   
   
   El resultado se calcula en pantalla con un efecto de caja registradora: 0.678 (67.8%).
 * Audio: Apliquemos Bayes. Tomamos el camino de los que realmente están enfermos y dan positivo, que es 0.095, y lo dividimos por nuestro universo de todos los que dieron positivo, que es 0.14. ¿El resultado? 67.8%. ¡Boom! A pesar de que tu prueba tiene una eficacia del 95%, tu probabilidad real de estar enfermo es solo de un 68%.
Desarrollo: ¿Por qué ocurre esto? (La Paradoja) (2:40 - 3:20)
 * Visual (Manim): Se muestran 1,000 avatares pequeños en pantalla. 100 se pintan de rojo (Enfermos) y 900 de verde (Sanos). La máquina de pruebas ilumina a 95 rojos (verdaderos positivos) y, debido a su 5% de error, ilumina a 45 verdes (falsos positivos).
 * Audio: ¿Por qué bajó tanto? A esto se le llama ignorar la tasa base. Como la enfermedad es rara (solo el 10% de la población la tiene), hay muchísimas más personas sanas haciéndose la prueba. Ese 5% de error de la máquina aplicado a una enorme multitud de sanos genera un montón de falsos positivos que "diluyen" los resultados. Bayes toma en cuenta el contexto completo, tu intuición no.
Cierre, Aplicaciones y CTA (3:20 - 4:00)
 * Visual (Manim / Gráficos de tecnología): Aparece un filtro de Gmail enviando correos con la palabra "Oferta" a la carpeta de Spam. Luego un submarino amarillo con un radar mapeando el fondo del océano.
 * Audio: El Teorema de Bayes no solo salva vidas evitando diagnósticos apresurados. Es el motor principal detrás de los filtros de Spam en tu correo y los algoritmos de Machine Learning. Incluso se usó matemáticamente para encontrar submarinos perdidos en el océano, actualizando el mapa de búsqueda cada vez que encontraban una nueva pista.
 * Visual (Manim): Un mosaico con pequeñas miniaturas abstractas de los conceptos vistos en toda la serie: Dados (Clásica), Gráficas (Frecuentista), Relojes (Geométrica), Árboles (Multiplicación) y la Fórmula de Bayes brillando en el centro.
 * Audio: Con esto cerramos nuestro viaje por las leyes de la probabilidad. Desde los simples juegos de azar hasta la matemática predictiva que domina la inteligencia artificial. Si dominas esto, dominarás los datos. Si te gustó esta serie, suscríbete, deja un buen like, y cuéntame en los comentarios qué otra rama de las matemáticas o la programación quieres que exploremos. ¡Hasta la próxima!

##  Reglas básicas de probabilidad 
## Tecnicas de Conteo 1. yt tecnicas de conteo 2.
