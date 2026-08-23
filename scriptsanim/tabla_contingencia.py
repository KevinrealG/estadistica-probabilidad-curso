from manim import *


class TablaContingencia(Scene):

    def construct(self):

        # =====================================================
        # PALETA
        # =====================================================

        VERDE = GREEN
        ROSADO = PINK
        AZUL = BLUE
        NARANJA = ORANGE
        AMARILLO = YELLOW

        GRIS = GREY_B
        BLANCO = WHITE

        # =====================================================
        # DATOS
        # =====================================================
        #
        # Variable 1: Red social favorita
        # Variable 2: Sexo
        #
        # Cada elemento representa una observación:
        #
        # (Red social, Sexo)
        #
        # =====================================================

        datos = [
            ("WhatsApp", "M"),
            ("Instagram", "F"),
            ("Facebook", "M"),
            ("TikTok", "F"),
            ("WhatsApp", "F"),
            ("Instagram", "M"),
            ("Facebook", "F"),
            ("TikTok", "M"),

            ("WhatsApp", "M"),
            ("Instagram", "F"),
            ("WhatsApp", "F"),
            ("Facebook", "M"),
            ("Instagram", "F"),
            ("TikTok", "M"),
            ("WhatsApp", "M"),
            ("Instagram", "F"),

            ("Facebook", "F"),
            ("WhatsApp", "M"),
            ("TikTok", "F"),
            ("Instagram", "M")
        ]

        # =====================================================
        # CATEGORÍAS
        # =====================================================

        redes = [
            "WhatsApp",
            "Instagram",
            "Facebook",
            "TikTok"
        ]

        sexos = [
            "F",
            "M"
        ]

        # =====================================================
        # COLORES
        # =====================================================

        colores_redes = {
            "WhatsApp": VERDE,
            "Instagram": ROSADO,
            "Facebook": AZUL,
            "TikTok": BLANCO
        }

        colores_sexo = {
            "F": ROSADO,
            "M": AZUL
        }

        # =====================================================
        # TÍTULO
        # =====================================================

        titulo = Text(
            "Organización de un conjunto bivariado",
            font_size=32,
            color=BLANCO
        )

        titulo.to_edge(UP)

        self.play(
            FadeIn(
                titulo,
                shift=DOWN
            ),
            run_time=0.8
        )

        # =====================================================
        # SUBTÍTULO
        # =====================================================

        subtitulo = Text(
            "Dos variables categóricas por observación",
            font_size=22,
            color=GRIS
        )

        subtitulo.next_to(
            titulo,
            DOWN,
            buff=0.15
        )

        self.play(
            FadeIn(subtitulo),
            run_time=0.6
        )

        self.wait(1)

        # =====================================================
        # CREAR LOS PARES
        # =====================================================

        pares = VGroup()

        for red, sexo in datos:

            texto_red = Text(
                red,
                font_size=20,
                color=colores_redes[red]
            )

            separador = Text(
                "—",
                font_size=18,
                color=GRIS
            )

            texto_sexo = Text(
                sexo,
                font_size=20,
                color=colores_sexo[sexo]
            )

            par = VGroup(
                texto_red,
                separador,
                texto_sexo
            ).arrange(
                RIGHT,
                buff=0.12
            )

            pares.add(par)

        # =====================================================
        # DISTRIBUIR LOS PARES
        # =====================================================

        for i, par in enumerate(pares):

            fila = i // 5
            columna = i % 5

            x = (
                columna - 2
            ) * 2.3

            y = (
                1.0
                - fila * 0.65
            )

            par.move_to(
                [x, y, 0]
            )

        # =====================================================
        # APARECEN LOS DATOS
        # =====================================================

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        par,
                        scale=0.8
                    )
                    for par in pares
                ],
                lag_ratio=0.04
            ),
            run_time=2.5
        )

        self.wait(1)

        # =====================================================
        # MENSAJE
        # =====================================================

        mensaje = Text(
            "Cada observación tiene DOS variables",
            font_size=24,
            color=AMARILLO
        )

        mensaje.to_edge(
            DOWN,
            buff=0.4
        )

        self.play(
            FadeIn(
                mensaje,
                shift=UP
            )
        )

        self.wait(1)

        # =====================================================
        # DESAPARECEN LOS DATOS
        # =====================================================

        # =====================================================
# ESCENA INTERMEDIA
# DATOS + TABLA DE CONTINGENCIA AL LADO
# =====================================================

        self.play(
            FadeOut(mensaje),
            FadeOut(subtitulo),
            run_time=0.5
        )

        # -----------------------------------------------------
        # TÍTULO DE LA ESCENA
        # -----------------------------------------------------

        titulo_intermedio = Text(
            "De los datos a la tabla",
            font_size=30,
            color=AMARILLO
        )

        titulo_intermedio.to_edge(UP)

        self.play(
            Transform(
                titulo,
                titulo_intermedio
            ),
            run_time=0.7
        )

        # -----------------------------------------------------
        # MOVER LOS DATOS A LA IZQUIERDA
        # -----------------------------------------------------

        self.play(
            pares.animate.scale(0.68).move_to(
                LEFT * 4.1
            ),
            run_time=1
        )

        # -----------------------------------------------------
        # CREAR UNA TABLA PEQUEÑA A LA DERECHA
        # -----------------------------------------------------

        # Dimensiones
        ancho_tabla = 5.0
        alto_tabla = 4.6

        tabla_preview = Rectangle(
            width=ancho_tabla,
            height=alto_tabla,
            color=WHITE,
            stroke_width=2
        )

        tabla_preview.move_to(
            RIGHT * 2.3
            + DOWN * 0.25
        )

        # -----------------------------------------------------
        # LÍNEAS DE LA TABLA
        # -----------------------------------------------------

        # Separación entre nombre de red y columnas
        linea_vertical_preview = Line(
            tabla_preview.get_top() + LEFT * 0.65,
            tabla_preview.get_bottom() + LEFT * 0.65,
            color=GREY_B
        )

        # Línea debajo de encabezados
        linea_horizontal_preview = Line(
            tabla_preview.get_left() + UP * 1.15,
            tabla_preview.get_right() + UP * 1.15,
            color=GREY_B
        )

        # -----------------------------------------------------
        # ENCABEZADOS
        # -----------------------------------------------------

        red_social_preview = Text(
            "Red social",
            font_size=19,
            color=WHITE
        )

        red_social_preview.move_to(
            tabla_preview.get_left()
            + RIGHT * 0.65
            + UP * 1.55
        )

        f_preview = Text(
            "F",
            font_size=24,
            color=ROSADO
        )

        f_preview.move_to(
            tabla_preview.get_center()
            + LEFT * 0.25
            + UP * 1.55
        )

        m_preview = Text(
            "M",
            font_size=24,
            color=AZUL
        )

        m_preview.move_to(
            tabla_preview.get_center()
            + RIGHT * 1.0
            + UP * 1.55
        )

        total_preview = Text(
            "Total",
            font_size=19,
            color=AMARILLO
        )

        total_preview.move_to(
            tabla_preview.get_right()
            + LEFT * 0.45
            + UP * 1.55
        )

        # -----------------------------------------------------
        # CATEGORÍAS DE LAS FILAS
        # -----------------------------------------------------

        filas_preview = VGroup()

        for i, red in enumerate(redes):

            texto = Text(
                red,
                font_size=17,
                color=colores_redes[red]
            )

            texto.move_to(
                tabla_preview.get_left()
                + RIGHT * 0.65
                + DOWN * (0.05 + i * 0.72)
            )

            filas_preview.add(texto)

        # -----------------------------------------------------
        # APARECER LA ESTRUCTURA
        # -----------------------------------------------------

        self.play(
            Create(tabla_preview),
            Create(linea_vertical_preview),
            Create(linea_horizontal_preview),
            run_time=0.8
        )

        self.play(
            FadeIn(red_social_preview),
            FadeIn(f_preview),
            FadeIn(m_preview),
            FadeIn(total_preview),
            run_time=0.6
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        fila,
                        shift=RIGHT
                    )
                    for fila in filas_preview
                ],
                lag_ratio=0.12
            ),
            run_time=1
        )

        self.wait(1)

        # -----------------------------------------------------
        # MENSAJE EXPLICATIVO
        # -----------------------------------------------------

        mensaje_intermedio = Text(
            "Organizamos las observaciones según dos variables",
            font_size=21,
            color=WHITE
        )

        mensaje_intermedio.to_edge(
            DOWN,
            buff=0.3
        )

        self.play(
            FadeIn(
                mensaje_intermedio,
                shift=UP
            ),
            run_time=0.7
        )

        self.wait(2)

        # -----------------------------------------------------
        # DESTACAR LAS DOS VARIABLES
        # -----------------------------------------------------

        highlight_red = SurroundingRectangle(
            VGroup(
                *[
                    p[0]
                    for p in pares
                ]
            ),
            color=GREEN,
            stroke_width=2,
            buff=0.1
        )

        highlight_sexo = SurroundingRectangle(
            VGroup(
                *[
                    p[2]
                    for p in pares
                ]
            ),
            color=BLUE,
            stroke_width=2,
            buff=0.1
        )

        self.play(
            Create(highlight_red),
            run_time=0.6
        )

        self.wait(0.6)

        self.play(
            Create(highlight_sexo),
            run_time=0.6
        )

        self.wait(1)

        # -----------------------------------------------------
        # LIMPIAR ESCENA
        # -----------------------------------------------------

        self.play(
            FadeOut(pares),
            FadeOut(highlight_red),
            FadeOut(highlight_sexo),
            FadeOut(tabla_preview),
            FadeOut(linea_vertical_preview),
            FadeOut(linea_horizontal_preview),
            FadeOut(red_social_preview),
            FadeOut(f_preview),
            FadeOut(m_preview),
            FadeOut(total_preview),
            FadeOut(filas_preview),
            FadeOut(mensaje_intermedio),
            run_time=1
        )

        self.wait(0.5)

        # =====================================================
        # NUEVO TÍTULO
        # =====================================================

        titulo2 = Text(
            "Tabla de contingencia",
            font_size=34,
            color=AMARILLO
        )

        titulo2.to_edge(UP)

        self.play(
            Transform(
                titulo,
                titulo2
            ),
            run_time=0.8
        )

        # =====================================================
        # CREAR ESTRUCTURA VACÍA
        # =====================================================

        ancho = 9
        alto = 4.6

        tabla = Rectangle(
            width=ancho,
            height=alto,
            color=BLANCO,
            stroke_width=2
        )

        tabla.move_to(
            LEFT * 0.5
            + DOWN * 0.2
        )

        self.play(
            Create(tabla),
            run_time=0.8
        )

        # =====================================================
        # LÍNEAS PRINCIPALES
        # =====================================================

        # Línea vertical
        linea_vertical = Line(
            tabla.get_top() + LEFT * 1.8,
            tabla.get_bottom() + LEFT * 1.8,
            color=GRIS
        )

        # Línea horizontal
        linea_horizontal = Line(
            tabla.get_left() + UP * 1.25,
            tabla.get_right() + UP * 1.25,
            color=GRIS
        )

        self.play(
            Create(linea_vertical),
            Create(linea_horizontal),
            run_time=0.7
        )

        # =====================================================
        # COLUMNAS
        # =====================================================

        columnas = VGroup()

        for i, sexo in enumerate(sexos):

            texto = Text(
                sexo,
                font_size=28,
                color=colores_sexo[sexo]
            )

            x = -0.1 + i * 2.2

            texto.move_to(
                [x, 1.35, 0]
            )

            columnas.add(texto)

        # =====================================================
        # TOTAL COLUMNA
        # =====================================================

        total_columna = Text(
            "Total",
            font_size=25,
            color=AMARILLO
        )

        # Más hacia la derecha, dentro de su propia columna
        total_columna.move_to(
            [3.45, 1.35, 0]
        )
        # =====================================================
        # FILAS
        # =====================================================

        filas = VGroup()

        for i, red in enumerate(redes):

            texto = Text(
                red,
                font_size=22,
                color=colores_redes[red]
            )

            y = 0.65 - i * 0.85

            texto.move_to(
                [-3.6, y, 0]
            )

            filas.add(texto)

        total_fila = Text(
            "Total",
            font_size=24,
            color=AMARILLO
        )

        total_fila.move_to(
            [-3.6, -2.75, 0]
        )

        # =====================================================
        # ANIMAR ENCABEZADOS
        # =====================================================

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        c,
                        shift=DOWN
                    )
                    for c in columnas
                ],
                lag_ratio=0.2
            ),
            FadeIn(
                total_columna,
                shift=DOWN
            ),
            run_time=1
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        f,
                        shift=RIGHT
                    )
                    for f in filas
                ],
                lag_ratio=0.15
            ),
            FadeIn(
                total_fila,
                shift=RIGHT
            ),
            run_time=1.2
        )

        self.wait(1)

        # =====================================================
        # CONTAR LAS COMBINACIONES
        # =====================================================

        conteos = {}

        for red in redes:

            conteos[red] = {}

            for sexo in sexos:

                conteos[red][sexo] = 0

        for red, sexo in datos:

            conteos[red][sexo] += 1

        # =====================================================
        # POSICIONES DE CELDAS
        # =====================================================

        posiciones_x = {
            "F": -0.3,
            "M": 1.9
        }

        posiciones_y = {
            "WhatsApp": 0.65,
            "Instagram": -0.2,
            "Facebook": -1.05,
            "TikTok": -1.9
        }

        # =====================================================
        # CREAR CONTADORES
        # =====================================================

        valores = VGroup()

        for red in redes:

            for sexo in sexos:

                valor = conteos[red][sexo]

                numero = Text(
                    str(valor),
                    font_size=28,
                    color=BLANCO
                )

                numero.move_to(
                    [
                        posiciones_x[sexo],
                        posiciones_y[red],
                        0
                    ]
                )

                valores.add(numero)

                self.play(
                    FadeIn(
                        numero,
                        scale=1.4
                    ),
                    run_time=0.25
                )

        self.wait(1)

        # =====================================================
        # TOTALES POR FILA
        # =====================================================

        totales_fila = []

        for red in redes:

            total = sum(
                conteos[red].values()
            )

            numero = Text(
                str(total),
                font_size=26,
                color=AMARILLO
            )

            numero.move_to(
                [
                    3.45,
                    posiciones_y[red],
                    0
                ]
            )

            totales_fila.append(numero)

            self.play(
                FadeIn(
                    numero,
                    scale=1.3
                ),
                run_time=0.3
            )

        # =====================================================
        # TOTALES POR COLUMNA
        # =====================================================

        totales_columna = {}

        for sexo in sexos:

            total = sum(
                conteos[red][sexo]
                for red in redes
            )

            numero = Text(
                str(total),
                font_size=26,
                color=AMARILLO
            )

            numero.move_to(
                [
                    posiciones_x[sexo],
                    -2.75,
                    0
                ]
            )

            totales_columna[sexo] = numero

            self.play(
                FadeIn(
                    numero,
                    scale=1.3
                ),
                run_time=0.3
            )

        # =====================================================
        # TOTAL GENERAL
        # =====================================================

        total_general = Text(
            str(len(datos)),
            font_size=30,
            color=AMARILLO
        )

        total_general.move_to(
            [3.45, -2.75, 0]
        )

        self.play(
            FadeIn(
                total_general,
                scale=1.4
            ),
            run_time=0.5
        )

        self.wait(1)

        # =====================================================
        # RESALTAR UNA CELDA
        # =====================================================

        highlight = SurroundingRectangle(
            valores[0],
            color=VERDE,
            fill_color=VERDE,
            fill_opacity=0.25,
            stroke_opacity=0,
            buff=0.18
        )

        self.play(
            FadeIn(highlight),
            run_time=0.5
        )

        self.wait(1)

        self.play(
            FadeOut(highlight),
            run_time=0.4
        )

        # =====================================================
        # MENSAJE FINAL
        # =====================================================

        mensaje_final = Text(
            "Cada celda muestra una combinación de categorías",
            font_size=23,
            color=AMARILLO
        )

        mensaje_final.to_edge(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(
                mensaje_final,
                shift=UP
            )
        )

        self.wait(3)