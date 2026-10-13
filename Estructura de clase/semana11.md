# PLANIFICACIÓN SEMANA 11: PROBABILIDAD Y TOMA DE DECISIONES
**Curso:** Estadística y Probabilidad
**Duración por clase:** 60 minutos
**Metodología:** Aprendizaje Activo (Indagación, Construcción, Aplicación)

---

## 🎲 CLASE 1: Definiciones de Probabilidad y Axiomas

**1. Información General y Recursos**
*   **Objetivo:** Comprender los tres enfoques de la probabilidad (clásico, frecuentista, axiomático) y aplicar los axiomas de Kolmogórov.
*   **Recursos necesarios:** Dados físicos, monedas (o simuladores web proyectados), proyector, hojas en blanco para los estudiantes.

**2. Estructura de la Sesión (60 min)**
*   **Apertura (10 min):** *El Reto de la Certeza.* Lanzar una moneda y preguntar: "¿Qué probabilidad hay de que salga cara?". Luego preguntar: "Si tiro una chincheta (tachuela), ¿qué probabilidad hay de que caiga con la punta hacia arriba? ¿Puedo usar la misma matemática?". 
*   **Exploración y Desarrollo (15 min):** Explicar los tres enfoques a partir del reto inicial:
    *   *Clásico (Laplace):* Casos favorables / Casos posibles (Sirve para la moneda, no para la chincheta).
    *   *Frecuentista:* Repetir el experimento muchas veces (Sirve para la chincheta).
    *   *Axiomático (Kolmogórov):* Las reglas inquebrantables del juego matemático.
*   **Actividad Colaborativa (20 min):** *El Taller de los Axiomas.* Entregar a los grupos 3 escenarios con errores intencionales (ej. un evento con probabilidad de 1.2, o la suma del espacio muestral dando 0.8). Deben identificar qué axioma se viola y corregirlo.
*   **Aplicación (10 min):** Aplicar la regla de aditividad en un escenario real: Probabilidad de que un proyecto falle por falta de presupuesto (A) o por falta de tiempo (B), sabiendo que son mutuamente excluyentes.
*   **Cierre (5 min):** Pregunta metacognitiva: "¿Por qué el enfoque clásico falla en la vida real (ej. predecir si lloverá o no)?".

**3. Estructura de las Diapositivas (Apoyo Visual)**
*   **Slide 1: El Límite del Azar:** Pregunta proyectada sobre la chincheta vs. la moneda.
*   **Slide 2: Los Tres Enfoques:** Tabla comparativa visual (Laplace, Frecuencias, Axiomas).
*   **Slide 3: Los Pilares de Kolmogórov:** Los 3 axiomas en lenguaje simple y matemático.
*   **Slide 4: Reto de Auditoría:** Los escenarios con errores para la actividad grupal.

---

## ⚕️ CLASE 2: Propiedades de la Probabilidad y Probabilidad Condicional

**1. Información General y Recursos**
*   **Objetivo:** Interpretar y calcular probabilidades cuando se posee información previa, reduciendo el espacio muestral.
*   **Recursos necesarios:** Tablas de contingencia impresas o dataset en Excel, casos de falsos positivos médicos.

**2. Estructura de la Sesión (60 min)**
*   **Apertura (10 min):** *El Dilema Médico.* "Te haces una prueba para una enfermedad rara (1 en 10,000 personas la tienen). La prueba tiene una fiabilidad del 99%. Si das positivo, ¿estás 99% seguro de estar enfermo?". (Respuesta intuitiva: Sí. Respuesta real: No, la probabilidad es bajísima).
*   **Desarrollo Conceptual (15 min):** 
    *   Concepto de reducción del espacio muestral: P(A|B). "Ya sabemos que B ocurrió, así que el universo se encoge".
    *   Fórmula general y la Regla del Producto (P(A ∩ B) = P(A|B) * P(B)).
    *   Diferencia fundamental entre eventos dependientes e independientes.
*   **Actividad Guiada (20 min):** *Análisis Cruzado.* Entregar una tabla de contingencia real de la universidad (ej. Facultad vs. Nivel de Estrés). Los estudiantes calculan P(Estrés Alto | Ingeniería) vs P(Estrés Alto | Artes).
*   **Aplicación (10 min):** Analizar si la facultad y el estrés son variables independientes estadísticamente comparando P(A|B) con P(A).
*   **Cierre (5 min):** Ticket de salida: "Escribe con tus propias palabras qué significa el símbolo '|' en probabilidad".

**3. Estructura de las Diapositivas (Apoyo Visual)**
*   **Slide 1: El Diagnóstico:** El caso médico proyectado con grandes letras para generar choque cognitivo.
*   **Slide 2: Encogiendo el Universo:** Gráfico visual (Diagrama de Venn) mostrando cómo P(A|B) recorta todo lo que está fuera de B.
*   **Slide 3: Regla del Producto e Independencia:** Las fórmulas con una analogía de la vida real (ej. probabilidad de que llueva Y lleve paraguas).
*   **Slide 4: La Tabla de Contingencia:** El ejercicio de Facultad vs. Estrés para resolver en el aula.

---

## 🕵️ CLASE 3: Teorema de Bayes y Técnicas de Conteo

**1. Información General y Recursos**
*   **Objetivo:** Diferenciar permutaciones de combinaciones e invertir probabilidades condicionales para actualizar creencias (Bayes).
*   **Recursos necesarios:** Un candado de combinación de 3 dígitos (físico), video del Problema de Monty Hall (opcional).

**2. Estructura de la Sesión (60 min)**
*   **Apertura (15 min):** *Conteo (Permutaciones vs Combinaciones).* Mostrar el candado de 3 dígitos. "¿Por qué debería llamarse 'candado de permutación' y no de combinación?". Explicar la regla de oro: Si el orden importa, es Permutación (contraseñas). Si el orden no importa, es Combinación (equipos de trabajo).
*   **Desarrollo Conceptual (15 min):** 
    *   Diagramas de Árbol como herramienta visual para el Teorema de Probabilidad Total.
    *   Teorema de Bayes: Invertir el condicional. Conocer el efecto y buscar la causa (P(Causa | Efecto)).
*   **Actividad Colaborativa (20 min):** *Filtro Anti-Spam (Caso Bayes).* Un software detecta la palabra "oferta". Históricamente, el 80% de los correos spam tienen esa palabra, pero el 10% de los correos legítimos también la usan. Si el 20% de todos los correos son spam, calcular la probabilidad real de que el correo sea spam dado que dice "oferta". Deben resolverlo dibujando el árbol.
*   **Aplicación (5 min):** Reflexión sobre cómo funciona la Inteligencia Artificial moderna (Machine Learning) utilizando actualizaciones bayesianas.
*   **Cierre (5 min):** Resumen de la semana. "La probabilidad no adivina el futuro, solo actualiza nuestras creencias con cada nuevo dato".

**3. Estructura de las Diapositivas (Apoyo Visual)**
*   **Slide 1: ¿Importa el orden?:** Imagen de un candado vs. Imagen de un equipo de trabajo (Fórmulas nPr y nCr).
*   **Slide 2: Mapeando las Rutas:** Ejemplo visual de un diagrama de árbol de dos niveles.
*   **Slide 3: La Lupa de Bayes:** Fórmula de Bayes explicada con colores (Prior, Likelihood, Posterior).
*   **Slide 4: Reto Anti-Spam:** Planteamiento del problema del correo electrónico para el taller grupal.


