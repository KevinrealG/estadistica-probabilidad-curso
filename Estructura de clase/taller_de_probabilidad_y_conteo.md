# TALLER PRÁCTICO N°2: REGLAS BÁSICAS DE PROBABILIDAD Y TÉCNICAS DE CONTEO

**Curso:** Estadística y Probabilidad
**Temática:** Regla de la suma, probabilidad condicional, eventos independientes, combinaciones y permutaciones.

---

## 🎲 PARTE I: Reglas Básicas de Probabilidad

**Ejercicio 1: Regla de la Suma (Eventos no excluyentes)**
En una escuela, el 40% de los estudiantes juegan fútbol, el 30% juegan baloncesto y el 20% juegan ambos deportes. Si se selecciona un estudiante al azar, ¿cuál es la probabilidad de que juegue al menos uno de estos dos deportes?

**Ejercicio 2: Probabilidad Condicional y Regla de la Multiplicación**
En una línea de ensamblaje de una fábrica, el 5% de los productos salen defectuosos. Si un producto es verdaderamente defectuoso, la probabilidad de que sea detectado por el inspector de calidad es de 0.90. ¿Cuál es la probabilidad de que un producto seleccionado al azar sea defectuoso Y además sea detectado por el inspector?

**Ejercicio 3: Eventos Independientes**
Se lanzan dos dados justos de seis caras de forma simultánea. ¿Cuál es la probabilidad de obtener exactamente un "3" en el primer dado y un número par en el segundo dado?

**Ejercicio 4: Muestreo sin Reemplazo (Dependencia)**
En una urna hay 5 bolas rojas y 4 bolas azules. Se extraen dos bolas consecutivamente sin devolverlas a la urna. ¿Cuál es la probabilidad de que la primera bola extraída sea roja y la segunda sea azul?

**Ejercicio 5: Teorema de Bayes (Probabilidad Inversa)**
Tres máquinas (A, B y C) producen el 50%, 30% y 20% de las piezas de una fábrica, respectivamente. El porcentaje de piezas defectuosas de cada máquina es 1%, 2% y 3%. Si se selecciona una pieza al azar del inventario final y resulta ser defectuosa, ¿cuál es la probabilidad de que haya sido producida por la máquina C?

---

## 🧮 PARTE II: Técnicas de Conteo (Permutaciones y Combinaciones)

**Ejercicio 6: Regla Multiplicativa del Conteo**
¿Cuántos números de 3 dígitos se pueden formar utilizando únicamente los dígitos $\{1, 2, 3, 4, 5\}$ si:
a) Los dígitos se pueden repetir en el mismo número?
b) Los dígitos NO se pueden repetir?

**Ejercicio 7: Permutaciones con Elementos Repetidos**
¿Cuántas palabras o cadenas de texto diferentes (con o sin sentido) se pueden formar reordenando todas las letras de la palabra "MISSISSIPPI"?

**Ejercicio 8: Combinaciones con Restricciones**
Se debe conformar un comité corporativo de 4 personas a partir de un grupo de 10 candidatos disponibles. ¿De cuántas formas diferentes se puede conformar el comité si:
a) No hay ninguna restricción en la selección?
b) Dos personas específicas (ej. el Presidente y el Vicepresidente) deben estar obligatoriamente incluidas en el comité?

**Ejercicio 9: Permutaciones Simples Lineales**
¿De cuántas maneras diferentes puede acomodarse una reunión de 7 personas en una fila de 7 sillas dispuestas de derecha a izquierda?

**Ejercicio 10: Permutaciones con Agrupamiento (Bloques)**
¿De cuántas maneras diferentes 3 hombres y 2 mujeres pueden acomodarse en una fila de 5 asientos para resolver cuestionarios individuales si:
a) Los hombres deben sentarse estrictamente juntos y las mujeres también deben sentarse juntas?
b) Justamente las mujeres deciden sentarse juntas (sin importar si los hombres se separan o no)?

---
---

## 🔑 ANEXO: CLAVE DE RESPUESTAS (Para el Docente)

*   **1)** $P(F \cup B) = P(F) + P(B) - P(F \cap B) = 0.40 + 0.30 - 0.20 = 0.50$ (50%).
*   **2)** $P(D \cap \text{Detectado}) = P(D) \times P(\text{Detectado} | D) = 0.05 \times 0.90 = 0.045$ (4.5%).
*   **3)** Eventos independientes. $P(3) = 1/6$. $P(\text{Par}) = 3/6$. Probabilidad conjunta $= (1/6) \times (3/6) = 3/36 = 1/12 \approx 0.0833$ (8.33%).
*   **4)** $P(\text{Roja}_1 \cap \text{Azul}_2) = P(\text{Roja}_1) \times P(\text{Azul}_2 | \text{Roja}_1) = (5/9) \times (4/8) = 20 / 72 = 5/18 \approx 0.277$ (27.7%).
*   **5)** Probabilidad Total de Defectuoso: $P(D) = (0.5 \times 0.01) + (0.3 \times 0.02) + (0.2 \times 0.03) = 0.005 + 0.006 + 0.006 = 0.017$.
    Bayes: $P(C|D) = \frac{P(D|C) \times P(C)}{P(D)} = \frac{0.006}{0.017} = \frac{6}{17} \approx 0.3529$ (35.29%).
*   **6a)** Con repetición: $5 \times 5 \times 5 = 125$ números.
*   **6b)** Sin repetición (Permutación): $5 \times 4 \times 3 = 60$ números.
*   **7)** 11 letras en total (1 'M', 4 'I', 4 'S', 2 'P').
    Fórmula: $P_{11}^{1,4,4,2} = \frac{11!}{1! \times 4! \times 4! \times 2!} = \frac{39,916,800}{1 \times 24 \times 24 \times 2} = \frac{39,916,800}{1152} = 34,650$ palabras.
*   **8a)** Sin orden (Combinación). $C(10,4) = \frac{10!}{4! \times 6!} = 210$ comités.
*   **8b)** Si 2 están fijos, quedan 2 cupos para disputarse entre 8 personas. $C(8,2) = \frac{8!}{2! \times 6!} = 28$ comités.
*   **9)** Permutación lineal de todos los elementos: $7! = 5,040$ maneras.
*   **10a)** Tratar hombres y mujeres como 2 grandes "bloques". Hay $2!$ formas de ordenar los bloques (HM o MH). Dentro del bloque H, hay $3!$ formas de ordenarlos. Dentro del bloque M, hay $2!$ formas.
    Total $= 2! \times 3! \times 2! = 2 \times 6 \times 2 = 24$ maneras.
*   **10b)** Tratar a las mujeres como 1 gran "bloque" y a los 3 hombres como elementos individuales. En total hay 4 "elementos" para ordenar en la fila. Hay $4!$ formas de ordenar estos elementos. Internamente, las mujeres se pueden ordenar de $2!$ formas.
    Total $= 4! \times 2! = 24 \times 2 = 48$ maneras.