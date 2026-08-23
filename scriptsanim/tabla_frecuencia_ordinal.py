from manim import *
import random

# ============================================================
# TABLA DE FRECUENCIAS - VARIABLE CUALITATIVA ORDINAL
# ============================================================

class TablaFrecuenciaOrdinal(Scene):

    def construct(self):

        # ====================================================
        # PALETA
        # ====================================================

        FONDO = BLACK

        ROJO = "#FF4D5A"
        NARANJA = "#FF9F43"
        AMARILLO = "#FFD166"
        VERDE = "#55D187"
        AZUL = "#4D96FF"
        MORADO = "#A66CFF"
        BLANCO = WHITE
        GRIS = GREY_B

        # ====================================================
        # DATOS
        # ====================================================

        datos = [
            "Bueno",
            "Excelente",
            "Regular",
            "Bueno",
            "Bueno",
            "Pésimo",
            "Excelente",
            "Bueno",
            "Regular",
            "Bueno",
            "Excelente",
            "Bueno",
            "Bueno",
            "Regular",
            "Bueno",
            "Pésimo",
            "Excelente",
            "Bueno",
            "Excelente",
            "Bueno"
        ]

        # Orden natural de la variable ordinal
        categorias = [
            "Pésimo",
            "Regular",
            "Bueno",
            "Excelente"
        ]

        # Frecuencias
        frecuencias = {
            "Pésimo": 2,
            "Regular": 3,
            "Bueno": 10,
            "Excelente": 5
        }

        total = 20

        # Frecuencias relativas
        relativas = {
            "Pésimo": "10%",
            "Regular": "15%",
            "Bueno": "50%",
            "Excelente": "25%"
        }

        # Frecuencias acumuladas
        acumuladas = {
            "Pésimo": 2,
            "Regular": 5,
            "Bueno": 15,
            "Excelente": 20
        }

        # Relativas acumuladas
        relativas_acum = {
            "Pésimo": "10%",
            "Regular": "25%",
            "Bueno": "75%",
            "Excelente": "100%"
        }

        colores_categoria = {
            "Pésimo": ROJO,
            "Regular": NARANJA,
            "Bueno": VERDE,
            "Excelente": AZUL
        }

        # ====================================================
        # ESCENA 1 - HOOK
        # ====================================================

        titulo = Text(
            "¿Cómo mides el éxito?",
            font_size=46,
            color=BLANCO
        )

        titulo.move_to(UP * 1.0)

        pregunta = Text(
            "¿Si las respuestas son palabras y no números?",
            font_size=30,
            color=AMARILLO
        )

        pregunta.next_to(
            titulo,
            DOWN,
            buff=0.35
        )

        self.play(
            Write(titulo),
            run_time=0.9
        )

        self.play(
            Write(pregunta),
            run_time=1
        )

        # Indicadores visuales
        niveles = VGroup()

        expresiones = [
            ("PÉSIMO", ROJO),
            ("REGULAR", NARANJA),
            ("BUENO", VERDE),
            ("EXCELENTE", AZUL)
        ]

        for texto, color in expresiones:

            item = Text(
                texto,
                font_size=26,
                color=color
            )

            niveles.add(item)

        niveles.arrange(
            RIGHT,
            buff=0.45
        )

        niveles.move_to(
            DOWN * 1.3
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        item,
                        scale=1.3
                    )
                    for item in niveles
                ],
                lag_ratio=0.15
            ),
            run_time=1.5
        )

        self.wait(1)

        self.play(
            FadeOut(titulo),
            FadeOut(pregunta),
            FadeOut(niveles)
        )

        # ====================================================
        # ESCENA 2 - LLUVIA DE DATOS
        # ====================================================

        titulo_datos = Text(
            "20 asistentes. 20 respuestas.",
            font_size=34,
            color=AMARILLO
        )

        titulo_datos.to_edge(UP)

        self.play(
            FadeIn(titulo_datos)
        )

        # Crear respuestas
        palabras = VGroup()

        posiciones = []

        for i, palabra in enumerate(datos):

            texto = Text(
                palabra,
                font_size=22,
                color=colores_categoria[palabra]
            )

            # posiciones iniciales aleatorias
            x = random.uniform(-6, 6)
            y = random.uniform(-3.2, 3.0)

            texto.move_to(
                [x, y, 0]
            )

            palabras.add(texto)

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        palabra,
                        shift=DOWN * 0.5
                    )
                    for palabra in palabras
                ],
                lag_ratio=0.04
            ),
            run_time=2.2
        )

        self.wait(1)

        mensaje = Text(
            "Datos cualitativos ordinales",
            font_size=27,
            color=AMARILLO
        )

        mensaje.to_edge(
            DOWN,
            buff=0.35
        )

        self.play(
            FadeIn(
                mensaje,
                shift=UP
            )
        )

        self.wait(1)

        # ====================================================
        # ESCENA 3 - ORDEN NATURAL
        # ====================================================

        self.play(
            FadeOut(mensaje),
            FadeOut(titulo_datos)
        )

        titulo_orden = Text(
            "Primero respetamos su orden natural",
            font_size=31,
            color=BLANCO
        )

        titulo_orden.to_edge(UP)

        self.play(
            FadeIn(titulo_orden)
        )

        # Posiciones ordenadas
        posiciones_orden = {
            "Pésimo": LEFT * 4.5,
            "Regular": LEFT * 1.5,
            "Bueno": RIGHT * 1.5,
            "Excelente": RIGHT * 4.5
        }

        orden_visual = VGroup()

        for categoria in categorias:

            palabra = Text(
                categoria,
                font_size=28,
                color=colores_categoria[categoria]
            )

            palabra.move_to(
                posiciones_orden[categoria]
                + DOWN * 0.2
            )

            orden_visual.add(palabra)

        # Flecha inferior
        flecha = Arrow(
            LEFT * 5.4 + DOWN * 1.0,
            RIGHT * 5.4 + DOWN * 1.0,
            color=AMARILLO,
            stroke_width=5,
            buff=0
        )

        etiqueta = Text(
            "menor satisfacción → mayor satisfacción",
            font_size=22,
            color=GRIS
        )

        etiqueta.next_to(
            flecha,
            DOWN,
            buff=0.15
        )

        # Las palabras de datos se agrupan
        self.play(
            FadeOut(palabras),
            run_time=0.7
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        palabra,
                        shift=UP
                    )
                    for palabra in orden_visual
                ],
                lag_ratio=0.2
            ),
            Create(flecha),
            FadeIn(etiqueta),
            run_time=1.5
        )

        self.wait(1.5)

        self.play(
            FadeOut(orden_visual),
            FadeOut(flecha),
            FadeOut(etiqueta),
            FadeOut(titulo_orden)
        )

        # ====================================================
        # ESCENA 4 - TABLA VACÍA
        # ====================================================

        titulo_tabla = Text(
            "Construimos la tabla de frecuencias",
            font_size=32,
            color=AMARILLO
        )

        titulo_tabla.to_edge(UP)

        self.play(
            FadeIn(titulo_tabla)
        )

        # ----------------------------------------------------
        # DIMENSIONES
        # ----------------------------------------------------

        x_left = -5.7
        x_right = 5.7

        y_top = 2.55
        y_header = 1.55
        y_bottom = -2.6

        # Líneas verticales
        v1 = Line(
            [x_left, y_top, 0],
            [x_left, y_bottom, 0],
            color=GRIS
        )

        v2 = Line(
            [-1.8, y_top, 0],
            [-1.8, y_bottom, 0],
            color=GRIS
        )

        v3 = Line(
            [0.45, y_top, 0],
            [0.45, y_bottom, 0],
            color=GRIS
        )

        v4 = Line(
            [2.7, y_top, 0],
            [2.7, y_bottom, 0],
            color=GRIS
        )

        v5 = Line(
            [x_right, y_top, 0],
            [x_right, y_bottom, 0],
            color=GRIS
        )

        # Líneas horizontales
        h_top = Line(
            [x_left, y_top, 0],
            [x_right, y_top, 0],
            color=GRIS
        )

        h_header = Line(
            [x_left, y_header, 0],
            [x_right, y_header, 0],
            color=GRIS
        )

        # Filas
        y_filas = [
            0.85,
            -0.05,
            -0.95,
            -1.85
        ]

        h_filas = []

        for y in [-0.5, -1.4, -2.3]:

            h_filas.append(
                Line(
                    [x_left, y, 0],
                    [x_right, y, 0],
                    color=GRIS
                )
            )

        # Línea total
        h_total = Line(
            [x_left, -2.3, 0],
            [x_right, -2.3, 0],
            color=GRIS
        )

        # Crear estructura
        self.play(
            Create(h_top),
            Create(h_header),
            Create(v1),
            Create(v2),
            Create(v3),
            Create(v4),
            Create(v5),
            run_time=1
        )

        # ====================================================
        # ENCABEZADOS SIN MATHTEX
        # ====================================================

        encabezado_categoria = Text(
            "Nivel de satisfacción",
            font_size=23,
            color=BLANCO
        )

        encabezado_categoria.move_to(
            [-3.75, 2.0, 0]
        )

        encabezado_fi = Text(
            "fi",
            font_size=26,
            color=VERDE
        )

        encabezado_fi.move_to(
            [-0.68, 2.0, 0]
        )

        encabezado_fri = Text(
            "fri (%)",
            font_size=24,
            color=AZUL
        )

        encabezado_fri.move_to(
            [1.57, 2.0, 0]
        )

        encabezado_Fi = Text(
            "Fi",
            font_size=26,
            color=NARANJA
        )

        encabezado_Fi.move_to(
            [3.78, 2.0, 0]
        )

        encabezado_Fri = Text(
            "Fri (%)",
            font_size=24,
            color=MORADO
        )

        encabezado_Fri.move_to(
            [4.95, 2.0, 0]
        )

        # Para evitar que los encabezados se choquen,
        # reducimos un poco el último.
        encabezado_Fri.scale(0.8)

        self.play(
            FadeIn(encabezado_categoria),
            FadeIn(encabezado_fi),
            FadeIn(encabezado_fri),
            FadeIn(encabezado_Fi),
            FadeIn(encabezado_Fri),
            run_time=1
        )

        # ====================================================
        # CATEGORÍAS
        # ====================================================

        textos_categoria = VGroup()

        for categoria, y in zip(
            categorias,
            y_filas
        ):

            texto = Text(
                categoria,
                font_size=25,
                color=colores_categoria[categoria]
            )

            texto.move_to(
                [-3.75, y, 0]
            )

            textos_categoria.add(texto)

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        texto,
                        shift=RIGHT
                    )
                    for texto in textos_categoria
                ],
                lag_ratio=0.15
            ),
            run_time=1.2
        )

        self.wait(1)

        # ====================================================
        # ESCENA 5 - FRECUENCIA ABSOLUTA
        # ====================================================

        etiqueta_fi = Text(
            "Frecuencia absoluta",
            font_size=23,
            color=VERDE
        )

        etiqueta_fi.to_edge(
            DOWN,
            buff=0.3
        )

        self.play(
            FadeIn(etiqueta_fi)
        )

        valores_fi = []

        for categoria, y in zip(
            categorias,
            y_filas
        ):

            numero = Text(
                str(frecuencias[categoria]),
                font_size=29,
                color=VERDE
            )

            numero.move_to(
                [-0.68, y, 0]
            )

            valores_fi.append(numero)

            self.play(
                FadeIn(
                    numero,
                    scale=1.4
                ),
                run_time=0.35
            )

        self.wait(1)

        self.play(
            FadeOut(etiqueta_fi)
        )

        # ====================================================
        # ESCENA 6 - FRECUENCIA RELATIVA
        # ====================================================

        etiqueta_fri = Text(
            "Frecuencia relativa",
            font_size=23,
            color=AZUL
        )

        etiqueta_fri.to_edge(
            DOWN,
            buff=0.3
        )

        self.play(
            FadeIn(etiqueta_fri)
        )

        valores_fri = []

        for categoria, y in zip(
            categorias,
            y_filas
        ):

            numero = Text(
                relativas[categoria],
                font_size=27,
                color=AZUL
            )

            numero.move_to(
                [1.57, y, 0]
            )

            valores_fri.append(numero)

            self.play(
                FadeIn(
                    numero,
                    scale=1.3
                ),
                run_time=0.3
            )

        self.wait(1)

        # ====================================================
        # FORMULA VISUAL SIN MATHTEX
        # ====================================================

        formula_label = Text(
            "fri = fi / n",
            font_size=28,
            color=AMARILLO
        )

        formula_label.to_edge(
            RIGHT,
            buff=0.35
        )

        formula_label.shift(
            DOWN * 3.1
        )

        self.play(
            FadeIn(
                formula_label,
                shift=UP
            )
        )

        self.wait(1)

        self.play(
            FadeOut(formula_label),
            FadeOut(etiqueta_fri)
        )

        # ====================================================
        # ESCENA 7 - FRECUENCIA ACUMULADA
        # ====================================================

        etiqueta_acum = Text(
            "Ahora acumulamos",
            font_size=24,
            color=NARANJA
        )

        etiqueta_acum.to_edge(
            DOWN,
            buff=0.3
        )

        self.play(
            FadeIn(etiqueta_acum)
        )

        valores_Fi = []

        # Mostrar primero 2
        numero1 = Text(
            "2",
            font_size=29,
            color=NARANJA
        )

        numero1.move_to(
            [3.78, y_filas[0], 0]
        )

        valores_Fi.append(numero1)

        self.play(
            FadeIn(
                numero1,
                scale=1.4
            )
        )

        # 2 + 3 = 5
        suma1 = Text(
            "2 + 3 = 5",
            font_size=23,
            color=AMARILLO
        )

        suma1.move_to(
            [0, -3.0, 0]
        )

        self.play(
            FadeIn(suma1),
            run_time=0.5
        )

        numero2 = Text(
            "5",
            font_size=29,
            color=NARANJA
        )

        numero2.move_to(
            [3.78, y_filas[1], 0]
        )

        valores_Fi.append(numero2)

        self.play(
            FadeIn(
                numero2,
                scale=1.4
            )
        )

        self.play(
            FadeOut(suma1)
        )

        # 5 + 10 = 15
        suma2 = Text(
            "5 + 10 = 15",
            font_size=23,
            color=AMARILLO
        )

        suma2.move_to(
            [0, -3.0, 0]
        )

        self.play(
            FadeIn(suma2)
        )

        numero3 = Text(
            "15",
            font_size=29,
            color=NARANJA
        )

        numero3.move_to(
            [3.78, y_filas[2], 0]
        )

        valores_Fi.append(numero3)

        self.play(
            FadeIn(
                numero3,
                scale=1.4
            )
        )

        self.play(
            FadeOut(suma2)
        )

        # 15 + 5 = 20
        suma3 = Text(
            "15 + 5 = 20",
            font_size=23,
            color=AMARILLO
        )

        suma3.move_to(
            [0, -3.0, 0]
        )

        self.play(
            FadeIn(suma3)
        )

        numero4 = Text(
            "20",
            font_size=29,
            color=NARANJA
        )

        numero4.move_to(
            [3.78, y_filas[3], 0]
        )

        valores_Fi.append(numero4)

        self.play(
            FadeIn(
                numero4,
                scale=1.4
            )
        )

        self.play(
            FadeOut(suma3),
            FadeOut(etiqueta_acum)
        )

        self.wait(1)

        # ====================================================
        # ESCENA 8 - RELATIVA ACUMULADA
        # ====================================================

        etiqueta_Fri = Text(
            "Frecuencia relativa acumulada",
            font_size=23,
            color=MORADO
        )

        etiqueta_Fri.to_edge(
            DOWN,
            buff=0.3
        )

        self.play(
            FadeIn(etiqueta_Fri)
        )

        valores_Fri = []

        for categoria, y in zip(
            categorias,
            y_filas
        ):

            numero = Text(
                relativas_acum[categoria],
                font_size=25,
                color=MORADO
            )

            numero.move_to(
                [4.95, y, 0]
            )

            valores_Fri.append(numero)

            self.play(
                FadeIn(
                    numero,
                    scale=1.3
                ),
                run_time=0.3
            )

        self.wait(1)

        self.play(
            FadeOut(etiqueta_Fri)
        )

        # ====================================================
        # TOTAL
        # ====================================================

        total_texto = Text(
            "Total",
            font_size=25,
            color=AMARILLO
        )

        total_texto.move_to(
            [-3.75, -2.48, 0]
        )

        total_fi = Text(
            "20",
            font_size=28,
            color=VERDE
        )

        total_fi.move_to(
            [-0.68, -2.48, 0]
        )

        total_fri = Text(
            "100%",
            font_size=26,
            color=AZUL
        )

        total_fri.move_to(
            [1.57, -2.48, 0]
        )

        total_Fi = Text(
            "20",
            font_size=28,
            color=NARANJA
        )

        total_Fi.move_to(
            [3.78, -2.48, 0]
        )

        total_Fri = Text(
            "100%",
            font_size=25,
            color=MORADO
        )

        total_Fri.move_to(
            [4.95, -2.48, 0]
        )

        self.play(
            FadeIn(total_texto),
            FadeIn(total_fi),
            FadeIn(total_fri),
            FadeIn(total_Fi),
            FadeIn(total_Fri),
            run_time=1
        )

        self.wait(2)

        # ====================================================
        # ESCENA 9 - RESALTAR BUENO
        # ====================================================

        highlight_bueno = SurroundingRectangle(
            VGroup(
                textos_categoria[2],
                valores_fi[2],
                valores_fri[2],
                valores_Fi[2],
                valores_Fri[2]
            ),
            color=VERDE,
            fill_color=VERDE,
            fill_opacity=0.15,
            stroke_opacity=0,
            buff=0.12
        )

        self.play(
            FadeIn(highlight_bueno),
            run_time=0.6
        )

        mensaje_bueno = Text(
            "La mayoría respondió: BUENO",
            font_size=25,
            color=VERDE
        )

        mensaje_bueno.to_edge(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(
                mensaje_bueno,
                shift=UP
            )
        )

        self.wait(2)

        self.play(
            FadeOut(highlight_bueno),
            FadeOut(mensaje_bueno)
        )

        # ====================================================
        # ESCENA 10 - GRÁFICO DE BARRAS
        # ====================================================

        self.play(
        FadeOut(titulo_tabla),
        FadeOut(encabezado_categoria),
        FadeOut(encabezado_fi),
        FadeOut(encabezado_fri),
        FadeOut(encabezado_Fi),
        FadeOut(encabezado_Fri),

        FadeOut(textos_categoria),

        # LISTAS → usar *
        FadeOut(*valores_fi),
        FadeOut(*valores_fri),
        FadeOut(*valores_Fi),
        FadeOut(*valores_Fri),

        FadeOut(total_texto),
        FadeOut(total_fi),
        FadeOut(total_fri),
        FadeOut(total_Fi),
        FadeOut(total_Fri),

        FadeOut(h_top),
        FadeOut(h_header),
        FadeOut(v1),
        FadeOut(v2),
        FadeOut(v3),
        FadeOut(v4),
        FadeOut(v5),

        run_time=1
        )

        titulo_grafico = Text(
            "Nivel de satisfacción",
            font_size=34,
            color=AMARILLO
        )

        titulo_grafico.to_edge(UP)

        self.play(
            FadeIn(titulo_grafico)
        )

        # ====================================================
        # BARRAS
        # ====================================================

        eje_x = Line(
            [-5, -2.7, 0],
            [5, -2.7, 0],
            color=WHITE
        )

        eje_y = Line(
            [-5, -2.7, 0],
            [-5, 2.3, 0],
            color=WHITE
        )

        self.play(
            Create(eje_x),
            Create(eje_y)
        )

        ancho_barra = 1.6

        posiciones_x_barras = [
            -3.5,
            -1.2,
            1.1,
            3.4
        ]

        barras = VGroup()

        for categoria, x in zip(
            categorias,
            posiciones_x_barras
        ):

            altura = frecuencias[categoria] * 0.3

            barra = Rectangle(
                width=ancho_barra,
                height=altura,
                fill_color=colores_categoria[categoria],
                fill_opacity=0.85,
                stroke_color=colores_categoria[categoria]
            )

            barra.move_to(
                [
                    x,
                    -2.7 + altura / 2,
                    0
                ]
            )

            barras.add(barra)

            etiqueta = Text(
                categoria,
                font_size=18,
                color=colores_categoria[categoria]
            )

            etiqueta.move_to(
                [x, -3.1, 0]
            )

            self.play(
                GrowFromEdge(
                    barra,
                    DOWN
                ),
                FadeIn(etiqueta),
                run_time=0.5
            )

        self.wait(1)

        # ====================================================
        # VALORES SOBRE LAS BARRAS
        # ====================================================

        numeros_barras = VGroup()

        for categoria, x in zip(
            categorias,
            posiciones_x_barras
        ):

            altura = frecuencias[categoria] * 0.3

            numero = Text(
                str(frecuencias[categoria]),
                font_size=25,
                color=WHITE
            )

            numero.move_to(
                [
                    x,
                    -2.7 + altura + 0.25,
                    0
                ]
            )

            numeros_barras.add(numero)

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        numero,
                        scale=1.2
                    )
                    for numero in numeros_barras
                ],
                lag_ratio=0.15
            ),
            run_time=1
        )

        # ====================================================
        # CIERRE
        # ====================================================

        cierre = Text(
            "¿Qué otra variable con orden jerárquico analizarías?",
            font_size=25,
            color=AMARILLO
        )

        cierre.to_edge(
            DOWN,
            buff=0.35
        )

        self.play(
            FadeIn(
                cierre,
                shift=UP
            )
        )

        self.wait(3)