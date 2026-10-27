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
5. Teorema de BAyes
5. Tecnicas de Conteo 1. yt tecnicas de conteo 2.
1. 📹 Video 4: Distribuciones de probabilidad discretas

2. 📹 Video 5: Distribución de Bernoulli
3. Binomial
