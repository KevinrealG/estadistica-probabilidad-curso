# 📹 Video 1: Construcción de Tablas de Frecuencias Agrupadas- Sturges
Aquí tienes el guion aplicando la estructura de tu nueva habilidad. He situado el ejemplo de los Airbnb en Cartagena (aprovechando tu ciudad) y he incluido a tu estudiante Kevin para darle un toque narrativo muy dinámico.

---

### Escena 1: El Gancho (Storytelling)

* **[VISUAL - Manim]:** Pantalla en negro. Hace `FadeIn` un mapa simplificado de Cartagena. Empiezan a aparecer puntos de ubicación (`Dot`) en el mapa. Sobre cada punto, flotan números aleatorios en color rojo: "$150k", "$320k", "$80k", "$500k", "$120k". La pantalla se llena de tantos números que se vuelve un caos visual. Luego, todos los números colapsan hacia el centro (`Transform`) formando un bloque de texto gigante que dice "CAOS DE DATOS".
* **[AUDIO - Locutor]:** "Imagina que quieres rentar un Airbnb en Cartagena para el fin de semana. Entras a la aplicación y ves cientos de precios: 150 mil, 320 mil, 80 mil, medio millón... ¡Es un caos! Si solo miras los números sueltos, no vas a entender si te están cobrando de más o si encontraste una ganga. Para encontrar el precio justo, necesitamos organizar ese caos. Hoy aprenderemos a dominar los datos construyendo una Tabla de Frecuencias Agrupadas usando la poderosa Regla de Sturges."

### Escena 2: Paso 1 - Tamaño de muestra (n) y Regla de Sturges (k)

* **[VISUAL - Manim]:** El texto de caos desaparece. Aparece un conjunto ordenado de 50 pequeños iconos de casas (`VGroup` de SVGs). En la esquina superior izquierda se escribe con `MathTex`: $n = 50$. Luego, entra desde la derecha la fórmula de Sturges: $k = 1 + 3.322 \log_{10}(n)$. La variable $n$ parpadea en amarillo y es reemplazada por el número 50. El resultado se calcula paso a paso, mostrando $k \approx 6.64$, y luego una flecha verde (`Arrow`) lo redondea al entero más cercano: $k = 7$.
* **[AUDIO - Locutor]:** "Paso número uno: ¿Cuántos datos tenemos? Digamos que recolectamos $n=50$ precios. Ahora, ¿en cuántos grupos o 'cajas' los dividimos? Kevin, uno de mis estudiantes, siempre me pregunta: '¿Profe, los agrupo de 5 en 5 o de 10 en 10?'. ¡Nada de adivinar a ojo! Para eso usamos la Regla de Sturges. Su fórmula matemática es $1 + 3.322$ por el logaritmo en base 10 de $n$. Al meter nuestros 50 datos en la fórmula, nos da 6.64. Redondeamos al entero más cercano y... ¡listo! Necesitamos 7 intervalos. Siete cajas perfectas para organizar nuestros precios."

### Escena 3: Paso 2 - El Rango y la Amplitud

* **[VISUAL - Manim]:** Aparece una línea numérica horizontal plana (`NumberLine`). Un punto azul cae en la marca de "80" (Mínimo) y un punto rojo en "500" (Máximo). Una llave de agrupación (`Brace`) abarca la distancia entre ambos, y arriba aparece el texto: $Rango = 500 - 80 = 420$.
Luego, la ecuación de Amplitud aparece debajo: $A = Rango / k$. Se sustituyen los valores ($A = 420 / 7$), dando como resultado un cuadro brillante con el número $60$.
* **[AUDIO - Locutor]:** "Paso dos: Calcular el Rango y el ancho de cada intervalo. Encontramos el Airbnb más barato, que está en 80 mil pesos, y el más caro, en 500 mil pesos. El Rango es simplemente la diferencia entre el máximo y el mínimo: 420 mil pesos. Ahora, para saber qué tan ancha será cada una de nuestras 7 cajas, dividimos ese Rango entre $k$. 420 entre 7 nos da 60. Ese es nuestro ancho de intervalo o amplitud. Cada grupo abarcará 60 mil pesos exactos."

### Escena 4: Paso 3 - Construcción de los Intervalos

* **[VISUAL - Manim]:** Se dibuja el esqueleto de una tabla (`Table` en Manim). Aparece el título de la primera columna: "Intervalos". Se hace un zoom a la primera fila. Aparece un corchete azul `[`, el número 80, una coma, el número 140 ($80+60$), y un paréntesis rojo `)`. Aparece un cuadro de texto aclaratorio: `[ Incluye el número` y `) No incluye el número`. Se autocompletan las siguientes 6 filas de forma acelerada usando un `LaggedStart`.
* **[AUDIO - Locutor]:** "Paso tres: ¡A construir las cajas! Empezamos con nuestro valor mínimo: 80. Le sumamos el ancho de 60, llegando a 140. ¡Pero mucho ojo a la notación! El límite inferior siempre es cerrado; usamos corchete, lo que significa que el precio de 80 mil sí entra aquí. El límite superior es abierto; usamos paréntesis. Esto significa que llegamos hasta el 139 mil, porque el 140 exacto pasa al siguiente grupo. Aplicamos esta misma lógica bajando fila por fila hasta completar nuestros 7 intervalos."

### Escena 5: Paso 4 - Marcas de Clase

* **[VISUAL - Manim]:** Se añade una segunda columna a la tabla: "$x_i$ (Marca de Clase)". En la primera fila (80 a 140), los números salen de la tabla y flotan hacia arriba. Aparece la fórmula: $\frac{80 + 140}{2} = 110$. El 110 se pinta de verde y regresa a la casilla correspondiente en la tabla. Las demás casillas de la columna se llenan rápidamente.
* **[AUDIO - Locutor]:** "Paso cuatro: La Marca de Clase, que representaremos como $x_i$. Este número es el embajador o punto medio de cada grupo. ¿Cómo lo sacas? Facilísimo: sumas el límite inferior más el límite superior, y lo divides entre dos. Para nuestro primer grupo, la mitad entre 80 y 140 es 110. Este valor va a ser vital más adelante si queremos calcular el precio promedio general del mercado."

### Escena 6: Paso 5 - Frecuencias Absolutas

* **[VISUAL - Manim]:** Se añade la tercera columna: "$f_i$ (Frecuencia)". Al lado derecho de la pantalla aparece una nube de 50 pequeños puntos (los datos iniciales). Los puntos empiezan a volar como un enjambre hacia las diferentes filas de la tabla. A medida que entran, el número de frecuencia de cada fila va aumentando como un contador digital. Al final, se hace un recuento inferior (`Sigma`) mostrando que la suma total de las frecuencias es exactamente 50.
* **[AUDIO - Locutor]:** "Paso cinco: Contar. Aquí calculamos la Frecuencia Absoluta. Es simplemente tomar nuestros 50 datos originales y ver cuántos caen en cada intervalo. Por ejemplo, al contar, encontramos que 15 de los apartamentos cuestan entre 80 mil y 140 mil pesos. Los vamos asignando a sus filas correspondientes. La prueba de fuego aquí es que, si sumas toda esta columna al final, te debe dar obligatoriamente el tamaño de tu muestra original: ¡nuestros 50 Airbnbs!"

### Escena 7: Paso 6 - Sacar Conclusiones

* **[VISUAL - Manim]:** La tabla completa se desliza hacia la izquierda. En el lado derecho, los datos de la tabla se transforman suavemente (`Transform`) en un Histograma. Las barras se elevan. La barra más alta (el intervalo con mayor frecuencia) se ilumina en un color cálido brillante (naranja o dorado) y una flecha la señala.
* **[AUDIO - Locutor]:** "Finalmente, el paso seis: Las conclusiones. ¿Para qué hicimos todo esto? Los datos no sirven de nada si no nos cuentan una historia. Viendo nuestra tabla, o mucho mejor, graficándola en un histograma, podemos ver inmediatamente dónde se concentra el mercado. ¡Miren este pico! La gran mayoría de los Airbnbs se concentran entre los 140 mil y 200 mil pesos. Ahora ya no estamos a ciegas. Si vas a buscar alojamiento, ya sabes cuál es el estándar y cuándo un lugar es un verdadero lujo. Así es como la estadística te da el control."

# Video 2: Kurtosis y Sesgo
Aquí tienes el guion aplicando la estructura de nuestra habilidad. Para hacer estos dos conceptos abstractos mucho más digeribles, usaremos el ejemplo de las calificaciones de un examen y las edades en un salón de clases, integrando las definiciones exactas de tus enlaces y la interacción con tu estudiante Kevin.

---

### Escena 1: El Gancho (Storytelling)

* **[VISUAL - Manim]:** Pantalla con fondo oscuro. Aparecen dos gráficas de campana (distribuciones) dibujadas con la clase `Axes`. Ambas comparten el mismo promedio (una línea punteada vertical que marca "Media = 50"). De repente, la curva de la izquierda se estira drásticamente hacia la derecha volviéndose deforme, y la curva de la derecha se estira hacia arriba volviéndose un pico afilado como una aguja (`Transform`). Aparece el título en texto gigante: "MÁS ALLÁ DEL PROMEDIO".
* **[AUDIO - Locutor]:** "Imagínate que dos profesores presumen que el promedio de calificaciones en sus exámenes fue de 50 sobre 100. Suena a que sus grupos son idénticos, ¿verdad? ¡Falso! En el primer grupo, casi todos sacaron cero, pero un par de genios sacaron 100, distorsionando todo. En el segundo grupo, absolutamente todos sacaron 50 exactos. El promedio nos miente si no vemos la *forma* de los datos. Hoy aprenderemos a desenmascarar distribuciones usando dos superpoderes estadísticos: la Asimetría y la Curtosis."

### Escena 2: Asimetría (Hacia dónde se inclina la balanza)

* **[VISUAL - Manim]:** Aparece una curva normal (`FunctionGraph`) perfectamente simétrica en color blanco. Luego, la curva se transforma (`ReplacementTransform`) en una curva sesgada hacia la derecha (Asimetría Positiva) coloreada en rojo. Aparece un icono de un examen difícil. Luego se transforma en una curva sesgada hacia la izquierda (Asimetría Negativa) en color azul, con el icono de un examen muy fácil.
* **[AUDIO - Locutor]:** "Empecemos por la Asimetría. Como su nombre indica, mide si nuestros datos están repartidos por igual a la izquierda y a la derecha de la media. Imagina un examen de cálculo súper difícil. La gran mayoría de los estudiantes sacará notas bajas, apilando la gráfica a la izquierda, dejando una 'cola' larga hacia la derecha por unos pocos genios. Esto es Asimetría Positiva. Por el contrario, si el examen es facilísimo, casi todos sacan 100, la gráfica se apila a la derecha y la cola apunta a la izquierda. ¡Asimetría Negativa!"

### Escena 3: El Coeficiente de Fisher

* **[VISUAL - Manim]:** La curva asimétrica se minimiza y pasa a la esquina superior. En el centro aparece un texto: "¿Cómo lo medimos?". Aparecen tres nombres en lista: "Pearson, Bowley, Fisher". Los dos primeros se desvanecen (`FadeOut`) y el de Fisher se agranda, revelando su fórmula matemática ($g_1$) con `MathTex`. Se muestran tres condicionales rápidos: $g_1 > 0$ (Positiva), $g_1 = 0$ (Simétrica), $g_1 < 0$ (Negativa).
* **[AUDIO - Locutor]:** "Aquí es donde mi estudiante Kevin levanta la mano y me dice: 'Profe, yo no puedo andar dibujando gráficas para miles de datos, ¿no hay un número que me diga esto directamente?'. ¡Claro que sí, Kevin! Existen varios coeficientes, como el de Pearson o el de Bowley, pero el rey indiscutible que usan todos los softwares es el Coeficiente de Asimetría de Fisher. La regla es simple: si Fisher te da un número mayor a cero, tienes asimetría positiva. Si te da exactamente cero, es perfectamente simétrica. Y si es menor a cero, es negativa. Un solo número te cuenta toda la historia."

### Escena 4: El Concepto de Curtosis

* **[VISUAL - Manim]:** Limpiamos la pantalla. Regresa la curva normal simétrica. Una mano animada (o dos flechas) aplastan la campana desde arriba, haciéndola más ancha y chata (`Transform`). Luego, las flechas la estiran desde la punta hacia el cielo, haciéndola puntiaguda con colas más gruesas. Aparece la palabra clave: "CURTOSIS".
* **[AUDIO - Locutor]:** "Pero, ¿qué pasa si nuestros datos sí son simétricos, pero la gráfica se ve... rara? Entramos al territorio de la Curtosis. La curtosis no mide hacia dónde se inclina la campana, sino qué tan puntiaguda o aplastada está. En términos más formales, mide el grado de concentración de los valores en la zona central y, muy importante, el peso de sus colas, es decir, qué tantos valores extremos o atípicos tenemos."

### Escena 5: Los 3 tipos de Curtosis (Ejemplos de la vida real)

* **[VISUAL - Manim]:** La pantalla se divide en tres columnas verticales.
* **Izquierda:** Curva muy puntiaguda (Leptocúrtica). Aparece un icono de monedas/cripto.
* **Centro:** Curva normal (Mesocúrtica). Aparece un icono de personas midiéndose la estatura.
* **Derecha:** Curva plana (Platicúrtica). Aparece un icono de estudiantes con un birrete.
Aparecen las etiquetas matemáticas: $g_2 > 0$, $g_2 = 0$, y $g_2 < 0$.


* **[AUDIO - Locutor]:** "Tenemos tres tipos. Primera: La Leptocúrtica. Imagina el precio de una criptomoneda estable; la mayoría de los días no cambia de precio (pico central alto), pero cuando hay una crisis, el precio salta locamente (colas gruesas por valores extremos). Segunda: La Mesocúrtica. Es nuestra querida curva normal, el equilibrio perfecto. Un ejemplo es la estatura de las personas en tu ciudad. Tercera: La Platicúrtica, una curva plana como una meseta. Imagina las edades de los estudiantes de primer semestre de universidad: casi todos tienen 17, 18 o 19 años. Los datos están esparcidos uniformemente en ese rango sin picos dramáticos y sin extremos locos."

### Escena 6: Conclusión

* **[VISUAL - Manim]:** Las tres curvas de curtosis y las dos de asimetría flotan en pantalla como hologramas (`VGroup` flotante). En el centro, un ícono de un científico de datos (o un cerebro brillando) analiza los hologramas. Se escribe en texto grande: "ASIMETRÍA = DIRECCIÓN" y "CURTOSIS = EXTREMOS".
* **[AUDIO - Locutor]:** "En resumen: la asimetría te dice hacia dónde se inclina la balanza de tus datos, y la curtosis te advierte qué tantos valores extremos te vas a encontrar. Juntas, te dan un retrato hablado perfecto de tu base de datos sin tener que leer un solo registro. ¿Listo para analizar tu propio dataset? ¡Escribe tus dudas en los comentarios y nos vemos en la próxima clase!"

# Video 4: Interpretación de Histogramas
Aquí tienes el guion aplicando la estructura de tu habilidad `creador-guiones-educativos`. He diseñado este guion para que la transición entre el concepto de la altura (simétrica) y el peso (asimétrica) sea muy visual e intuitiva para tus estudiantes, incluyendo la participación de Kevin.

---

### Escena 1: El Gancho (Storytelling)

* **[VISUAL - Manim]:** Pantalla negra. Aparece una lista gigante de números blancos desplazándose rápidamente hacia arriba (como el código de *Matrix*). Luego, la pantalla se divide en dos columnas. A la izquierda dice "1,000 Alturas", a la derecha "1,000 Pesos". Los números siguen cayendo a toda velocidad. Un gran símbolo de interrogación rojo aparece en el centro.
* **[AUDIO - Locutor]:** "Si te entrego una lista en Excel con mil estaturas y mil pesos de personas, ¿qué ves? Seguramente solo un dolor de cabeza numérico. Es imposible que tu cerebro procese mil datos de golpe para encontrar un patrón. Necesitamos traducir esos números a un idioma que nuestros ojos entiendan al instante. Hoy vamos a aprender a interpretar la herramienta más poderosa de la estadística visual: El Histograma. Y descubriremos por qué la naturaleza es simétrica para algunas cosas, pero muy injusta para otras."

### Escena 2: Fundamentos - ¿Qué estamos mirando?

* **[VISUAL - Manim]:** Los números de la izquierda (Alturas) empiezan a caer y apilarse en la base de la pantalla, formando pequeños bloques (`Square`). Estos bloques se agrupan por intervalos (ej: 160-165cm, 165-170cm) construyendo las barras de un histograma clásico en color azul. Aparecen las etiquetas de los ejes: "Eje X: Estatura (cm)" y "Eje Y: Cantidad de Personas".
* **[AUDIO - Locutor]:** "Antes de analizar, recordemos las reglas del juego. Un histograma no es un simple gráfico de barras separadas. Fíjate que aquí las columnas están pegadas, abrazándose unas a otras. Esto es porque estamos trabajando con datos continuos. El eje horizontal nos muestra los intervalos, como 'personas entre 1.70 y 1.75', y la altura de la barra en el eje vertical nos grita: '¡Aquí hay 200 personas!'."

### Escena 3: El Histograma de Alturas (La Simetría Perfecta)

* **[VISUAL - Manim]:** El histograma de alturas azul ocupa el centro. Una línea dorada (`FunctionGraph`) se dibuja suavemente sobre las barras, trazando una campana de Gauss perfecta y simétrica. Aparece el texto flotante: "DISTRIBUCIÓN NORMAL". Una flecha señala la gran barra central y luego dos flechas más pequeñas señalan los extremos.
* **[AUDIO - Locutor]:** "Miremos el histograma de las estaturas. Si dibujamos una línea sobre sus picos, vemos la famosa Campana de Gauss. Es perfectamente simétrica. ¿Qué nos cuenta esta forma? Nos dice que la biología es muy equilibrada. La inmensa mayoría de nosotros somos de estatura 'promedio', acumulándonos en esta enorme torre central. A medida que nos alejamos hacia los extremos, la cantidad de personas cae drásticamente y por igual: es igual de raro encontrar a alguien de 2 metros con 10 centímetros, que a alguien de 1 metro con 30. Equilibrio total."

### Escena 4: El Histograma de Pesos (El Sesgo o Asimetría)

* **[VISUAL - Manim]:** El histograma azul se desliza a la izquierda. A la derecha, los "1,000 Pesos" caen formando un nuevo histograma en color rojo. Este gráfico tiene una torre muy alta a la izquierda (ej: 60-70 kg) y una 'cola' larga y bajita que se extiende hacia la derecha (hasta 130+ kg). Se dibuja una línea sobre las barras que evidencia el sesgo.
* **[AUDIO - Locutor]:** "Pero ahora miremos el histograma de los pesos. La campana bonita desapareció. La torre más alta está tirada hacia la izquierda, y hacia la derecha se arrastra una especie de 'cola' larga. En estadística, llamamos a esto Asimetría Positiva o Sesgo a la derecha. La forma del gráfico nos está gritando que el peso humano no se comporta como la altura."

### Escena 5: La Duda de Kevin (Data Storytelling)

* **[VISUAL - Manim]:** Aparece un avatar o ícono de un estudiante (Kevin) con un globo de diálogo: "¿Por qué los pesos se deforman hacia un lado?". En el histograma rojo, aparece un candado o muro de ladrillos en el lado izquierdo (cerca de los 40kg) mostrando que no se puede bajar infinitamente, y una flecha infinita hacia la derecha (marcando 120kg, 150kg...).
* **[AUDIO - Locutor]:** "Aquí mi estudiante Kevin siempre me hace una excelente pregunta: 'Profe, ¿por qué pasa esto si ambas son medidas del cuerpo humano?'. La respuesta está en la interpretación de los límites. Biológicamente, hay un peso mínimo indispensable para la supervivencia humana; no puedes pesar menos de cero, ni menos de 40 kilos siendo adulto sin estar grave. El lado izquierdo tiene un muro, un límite natural. Sin embargo, hacia la derecha... no hay muro. Por factores de estilo de vida, dieta o metabolismo, una persona puede llegar a pesar 120, 150 o más kilos. Esa pequeña cantidad de personas jala el gráfico formando esa larga cola derecha."

### Escena 6: Conclusión

* **[VISUAL - Manim]:** Ambos histogramas (azul y rojo) están lado a lado. Se encierran en un recuadro brillante. Aparece un texto final: "LA FORMA ES LA HISTORIA".
* **[AUDIO - Locutor]:** "Como ves, un histograma no es solo para pasar un examen de estadística. Es un traductor. Te permite ver con un solo vistazo el comportamiento de una población entera. Te muestra dónde está la mayoría, y dónde se esconden los casos excepcionales. La próxima vez que veas unos datos, no mires los números, busca su forma. ¡Y si quieres aprender a programar estos gráficos en Python, no te pierdas el siguiente video!"