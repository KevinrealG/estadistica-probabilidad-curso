Este es el diseño instruccional del laboratorio, estructurado estrictamente bajo un enfoque de trabajo individual, generación sintética de datos (sin recolección manual) y dividido en los dos bloques de 40 minutos solicitados. Para garantizar que cada estudiante tenga resultados únicos, la semilla de aleatoriedad estará atada a su código de estudiante.

---

# 💻 LABORATORIO PARTE 1: La Ilusión del Azar y la Muestra Aleatoria (40 min)

## **Competencias Por Desarrollar**

* Utilizar herramientas computacionales (Python/NumPy) para la generación de datos sintéticos que simulen el comportamiento de variables aleatorias discretas bajo incertidumbre.
* Aplicar técnicas de muestreo aleatorio simple mediante programación, garantizando la reproducibilidad y el control de sesgos a través de semillas de aleatoriedad.

## **Resultados de Aprendizaje**

* Generar poblaciones de datos sintéticos (arreglos numéricos) utilizando las funciones de distribución de la librería NumPy.
* Extraer muestras aleatorias de una población computacional estableciendo una semilla única (`random_state` o `seed`).
* Calcular y contrastar parámetros poblacionales frente a estadísticos muestrales básicos (media y varianza).

## **Temáticas que se desarrollan en esta práctica**

* Variables aleatorias discretas.
* Generación de números pseudoaleatorios y semillas lógicas.
* Población estadística vs. Muestra Aleatoria Simple.
* Cálculo de media y varianza poblacional y muestral.

# **Problema de aplicación**

**"El Auditor de Calidad Aislado"**
Trabajas como auditor de calidad independiente para una planta de manufactura de microchips. La máquina central produce diariamente $10,000$ chips, y cada uno puede presentar entre $0$ y $5$ micro-defectos de soldadura (variable discreta). Es imposible revisar los $10,000$ chips por cuestiones de tiempo y destrucción de material. Tu misión es utilizar un simulador para "crear" la producción del día y extraer una muestra aleatoria de inspección de $50$ chips. ¿Podrá la media de defectos de tu pequeña muestra de 50 acercarse a la realidad de los $10,000$ chips de la fábrica?

# Video y procedimiento

**Instrucción asincrónica sugerida:** Revisar previamente un video cápsula (5 min) sobre la función `np.random.randint` y el concepto de `seed` en Python.

**Procedimiento en Google Colab (Trabajo Individual):**

1. **Importar Librerías:** `import numpy as np`, `import pandas as pd`.
2. **Individualización (El paso crítico):** Cada estudiante debe configurar la semilla de aleatoriedad usando los últimos 4 dígitos de su código estudiantil: `np.random.seed(1234)`. *(Esto garantiza que ningún estudiante comparta los mismos datos).*
3. **Generar la Población Sintética:** Crear un arreglo de $10,000$ datos enteros aleatorios entre 0 y 5: `poblacion = np.random.randint(0, 6, 10000)`.
4. **Calcular la Realidad:** Calcular y guardar la media exacta de la población completa `np.mean(poblacion)`.
5. **Extraer la Muestra:** Utilizar la función de NumPy para elegir 50 datos al azar de la población: `muestra = np.random.choice(poblacion, size=50, replace=False)`.
6. **Contraste:** Calcular la media de la `muestra` y programar un `print()` que muestre la diferencia absoluta entre la media de la muestra y la media poblacional.

# **Paso 2. Compromisos de entrega en cada sesion**

* **Archivo:** Subir el archivo HTML generado.
* **Evidencia en el HTML:** Un bloque de texto al final del archivo de la Parte 1 que indique: *"Mi código de estudiante es [XXXX]. La media real de mi fábrica fue [Valor 1], y la media de mi muestra aleatoria fue [Valor 2]. El error de muestreo fue de [Diferencia]."*.

# ✅ **Rúbrica de Evaluación – para el informe del lab (Parte 1)**

* **Dominio Técnico (40%):** Genera correctamente la población de 10,000 datos y extrae la muestra sin reemplazo utilizando funciones de NumPy.
* **Individualización (30%):** Aplica correctamente la semilla (`seed`) utilizando los dígitos de su código. Los datos generados no son idénticos a los de ningún otro compañero.
* **Cálculo y Precisión (30%):** Calcula correctamente las medias y documenta el error de muestreo mediante código en Python.

---

## *(Transición de bloque: 40 minutos)*

# 📉 LABORATORIO PARTE 2: El Caos se Vuelve Orden (TLC y Muestreo Repetido) (40 min)

## **Competencias Por Desarrollar**

* Simular fenómenos estocásticos iterativos mediante estructuras de control en programación (bucles) para validar empíricamente teoremas estadísticos fundamentales.
* Traducir distribuciones de datos abstractas en representaciones visuales comprensibles para el análisis y toma de decisiones.

## **Resultados de Aprendizaje**

* Construir bucles (`for` loops) en Python para simular el proceso de extraer múltiples muestras de forma iterativa.
* Almacenar estadísticos calculados en cada iteración dentro de estructuras de datos (listas/arrays).
* Construir e interpretar histogramas utilizando Seaborn y Matplotlib para visualizar la distribución de las medias muestrales.
* Validar empíricamente la Ley de los Grandes Números y el Teorema del Límite Central (TLC).

## **Temáticas que se desarrollan en esta práctica**

* Muestreo repetido.
* Distribución de medias muestrales y error estándar.
* Construcción de Histogramas y estimación de densidad (KDE).
* Ley de los Grandes Números.
* Teorema del Límite Central (TLC).

# **Problema de aplicación**

**"El Colapso a la Normalidad"**
En la Parte 1 observaste que una sola muestra de $50$ chips tenía un margen de error frente a la población. Además, la población original tenía una distribución uniforme discreta (los valores 0, 1, 2, 3, 4 y 5 tenían la misma probabilidad).
Ahora actuarás como el Director Analítico. Vas a simular qué pasaría si repites el proceso de inspección tomando una muestra de $30$ chips, pero esta vez lo harás $2,000$ veces seguidas, guardando únicamente el promedio de cada inspección. ¿Qué forma geométrica tomará el gráfico si apilamos los promedios de esas $2,000$ inspecciones independientes?

# Video y procedimiento

**Instrucción asincrónica sugerida:** Cápsula de 4 minutos sobre cómo crear un bucle `for` básico en Python y cómo añadir elementos a una lista vacía con `.append()`.

**Procedimiento en Google Colab (Trabajo Individual):**

1. **Preparación visual:** `import seaborn as sns`, `import matplotlib.pyplot as plt`.
2. **El Bucle (El motor estadístico):**
* Crear una lista vacía: `medias_muestrales = []`.
* Construir un ciclo `for i in range(2000):`.


3. **Muestreo Repetido:** Dentro del bucle, extraer una muestra aleatoria de tamaño $n=30$ de la `poblacion` generada en la Parte 1.
4. **Almacenamiento:** Calcular la media de esa muestra específica y agregarla a la lista con `medias_muestrales.append()`.
5. **Visualización:** Fuera del bucle, utilizar `sns.histplot(medias_muestrales, kde=True, color='blue')` para dibujar el histograma de las 2,000 medias.
6. **El Contraste Final:** Generar un segundo histograma de los $10,000$ datos de la población original para evidenciar que la población NO es normal, pero las medias muestrales SÍ lo son.

# **Paso 2. Compromisos de entrega en cada sesion**

* **Archivo:** Captura de pantalla de los dos gráficos generados en Colab (El histograma de la población original vs. El histograma de las medias muestrales en forma de campana).
* **Análisis Metacognitivo:** Un párrafo de máximo 3 líneas (en la tarea de entrega) donde el estudiante explique con sus propias palabras por qué el segundo gráfico forma una "Campana de Gauss" si los datos originales eran una variable uniforme discreta.

# ✅ **Rúbrica de Evaluación – para el informe del lab (Parte 2)**

* **Dominio Lógico y Simulación (40%):** Estructura correctamente el bucle `for` iterando 2,000 veces y almacenando la media de cada nueva muestra en una lista sin errores de indentación o lógica.
* **Visualización de Datos (30%):** Construye ambos histogramas correctamente utilizando Seaborn, incluyendo la curva de densidad (KDE), diferenciando visualmente la distribución poblacional de la distribución de las medias.
* **Pensamiento Crítico y Argumentación (30%):** El estudiante redacta una conclusión precisa que demuestra comprensión del Teorema del Límite Central, identificando que el tamaño de muestra iterativo fuerza la normalidad independientemente de la distribución de origen.Este es el diseño instruccional del laboratorio, estructurado estrictamente bajo un enfoque de trabajo individual, generación sintética de datos (sin recolección manual) y dividido en los dos bloques de 40 minutos solicitados. Para garantizar que cada estudiante tenga resultados únicos, la semilla de aleatoriedad estará atada a su código de estudiante.

---

# 💻 LABORATORIO PARTE 1: La Ilusión del Azar y la Muestra Aleatoria (40 min)

## **Competencias Por Desarrollar**

* Utilizar herramientas computacionales (Python/NumPy) para la generación de datos sintéticos que simulen el comportamiento de variables aleatorias discretas bajo incertidumbre.
* Aplicar técnicas de muestreo aleatorio simple mediante programación, garantizando la reproducibilidad y el control de sesgos a través de semillas de aleatoriedad.

## **Resultados de Aprendizaje**

* Generar poblaciones de datos sintéticos (arreglos numéricos) utilizando las funciones de distribución de la librería NumPy.
* Extraer muestras aleatorias de una población computacional estableciendo una semilla única (`random_state` o `seed`).
* Calcular y contrastar parámetros poblacionales frente a estadísticos muestrales básicos (media y varianza).

## **Temáticas que se desarrollan en esta práctica**

* Variables aleatorias discretas.
* Generación de números pseudoaleatorios y semillas lógicas.
* Población estadística vs. Muestra Aleatoria Simple.
* Cálculo de media y varianza poblacional y muestral.

# **Problema de aplicación**

**"El Auditor de Calidad Aislado"**
Trabajas como auditor de calidad independiente para una planta de manufactura de microchips. La máquina central produce diariamente $10,000$ chips, y cada uno puede presentar entre $0$ y $5$ micro-defectos de soldadura (variable discreta). Es imposible revisar los $10,000$ chips por cuestiones de tiempo y destrucción de material. Tu misión es utilizar un simulador para "crear" la producción del día y extraer una muestra aleatoria de inspección de $50$ chips. ¿Podrá la media de defectos de tu pequeña muestra de 50 acercarse a la realidad de los $10,000$ chips de la fábrica?

# Video y procedimiento

**Instrucción asincrónica sugerida:** Revisar previamente un video cápsula (5 min) sobre la función `np.random.randint` y el concepto de `seed` en Python.

**Procedimiento en Google Colab (Trabajo Individual):**

1. **Importar Librerías:** `import numpy as np`, `import pandas as pd`.
2. **Individualización (El paso crítico):** Cada estudiante debe configurar la semilla de aleatoriedad usando los últimos 4 dígitos de su código estudiantil: `np.random.seed(1234)`. *(Esto garantiza que ningún estudiante comparta los mismos datos).*
3. **Generar la Población Sintética:** Crear un arreglo de $10,000$ datos enteros aleatorios entre 0 y 5: `poblacion = np.random.randint(0, 6, 10000)`.
4. **Calcular la Realidad:** Calcular y guardar la media exacta de la población completa `np.mean(poblacion)`.
5. **Extraer la Muestra:** Utilizar la función de NumPy para elegir 50 datos al azar de la población: `muestra = np.random.choice(poblacion, size=50, replace=False)`.
6. **Contraste:** Calcular la media de la `muestra` y programar un `print()` que muestre la diferencia absoluta entre la media de la muestra y la media poblacional.

# **Paso 2. Compromisos de entrega en cada sesion**

* **Archivo:** Subir el archivo HTML generado.
* **Evidencia en el HTML:** Un bloque de texto al final del archivo de la Parte 1 que indique: *"Mi código de estudiante es [XXXX]. La media real de mi fábrica fue [Valor 1], y la media de mi muestra aleatoria fue [Valor 2]. El error de muestreo fue de [Diferencia]."*.

# ✅ **Rúbrica de Evaluación – para el informe del lab (Parte 1)**

* **Dominio Técnico (40%):** Genera correctamente la población de 10,000 datos y extrae la muestra sin reemplazo utilizando funciones de NumPy.
* **Individualización (30%):** Aplica correctamente la semilla (`seed`) utilizando los dígitos de su código. Los datos generados no son idénticos a los de ningún otro compañero.
* **Cálculo y Precisión (30%):** Calcula correctamente las medias y documenta el error de muestreo mediante código en Python.

---

## *(Transición de bloque: 40 minutos)*

# 📉 LABORATORIO PARTE 2: El Caos se Vuelve Orden (TLC y Muestreo Repetido) (40 min)

## **Competencias Por Desarrollar**

* Simular fenómenos estocásticos iterativos mediante estructuras de control en programación (bucles) para validar empíricamente teoremas estadísticos fundamentales.
* Traducir distribuciones de datos abstractas en representaciones visuales comprensibles para el análisis y toma de decisiones.

## **Resultados de Aprendizaje**

* Construir bucles (`for` loops) en Python para simular el proceso de extraer múltiples muestras de forma iterativa.
* Almacenar estadísticos calculados en cada iteración dentro de estructuras de datos (listas/arrays).
* Construir e interpretar histogramas utilizando Seaborn y Matplotlib para visualizar la distribución de las medias muestrales.
* Validar empíricamente la Ley de los Grandes Números y el Teorema del Límite Central (TLC).

## **Temáticas que se desarrollan en esta práctica**

* Muestreo repetido.
* Distribución de medias muestrales y error estándar.
* Construcción de Histogramas y estimación de densidad (KDE).
* Ley de los Grandes Números.
* Teorema del Límite Central (TLC).

# **Problema de aplicación**

**"El Colapso a la Normalidad"**
En la Parte 1 observaste que una sola muestra de $50$ chips tenía un margen de error frente a la población. Además, la población original tenía una distribución uniforme discreta (los valores 0, 1, 2, 3, 4 y 5 tenían la misma probabilidad).
Ahora actuarás como el Director Analítico. Vas a simular qué pasaría si repites el proceso de inspección tomando una muestra de $30$ chips, pero esta vez lo harás $2,000$ veces seguidas, guardando únicamente el promedio de cada inspección. ¿Qué forma geométrica tomará el gráfico si apilamos los promedios de esas $2,000$ inspecciones independientes?

# Video y procedimiento

**Instrucción asincrónica sugerida:** Cápsula de 4 minutos sobre cómo crear un bucle `for` básico en Python y cómo añadir elementos a una lista vacía con `.append()`.

**Procedimiento en Google Colab (Trabajo Individual):**

1. **Preparación visual:** `import seaborn as sns`, `import matplotlib.pyplot as plt`.
2. **El Bucle (El motor estadístico):**
* Crear una lista vacía: `medias_muestrales = []`.
* Construir un ciclo `for i in range(2000):`.


3. **Muestreo Repetido:** Dentro del bucle, extraer una muestra aleatoria de tamaño $n=30$ de la `poblacion` generada en la Parte 1.
4. **Almacenamiento:** Calcular la media de esa muestra específica y agregarla a la lista con `medias_muestrales.append()`.
5. **Visualización:** Fuera del bucle, utilizar `sns.histplot(medias_muestrales, kde=True, color='blue')` para dibujar el histograma de las 2,000 medias.
6. **El Contraste Final:** Generar un segundo histograma de los $10,000$ datos de la población original para evidenciar que la población NO es normal, pero las medias muestrales SÍ lo son.

# **Paso 2. Compromisos de entrega en cada sesion**

* **Archivo:** Captura de pantalla de los dos gráficos generados en Colab (El histograma de la población original vs. El histograma de las medias muestrales en forma de campana).
* **Análisis Metacognitivo:** Un párrafo de máximo 3 líneas (en la tarea de entrega) donde el estudiante explique con sus propias palabras por qué el segundo gráfico forma una "Campana de Gauss" si los datos originales eran una variable uniforme discreta.

# ✅ **Rúbrica de Evaluación – para el informe del lab (Parte 2)**

* **Dominio Lógico y Simulación (40%):** Estructura correctamente el bucle `for` iterando 2,000 veces y almacenando la media de cada nueva muestra en una lista sin errores de indentación o lógica.
* **Visualización de Datos (30%):** Construye ambos histogramas correctamente utilizando Seaborn, incluyendo la curva de densidad (KDE), diferenciando visualmente la distribución poblacional de la distribución de las medias.
* **Pensamiento Crítico y Argumentación (30%):** El estudiante redacta una conclusión precisa que demuestra comprensión del Teorema del Límite Central, identificando que el tamaño de muestra iterativo fuerza la normalidad independientemente de la distribución de origen.