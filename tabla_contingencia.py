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

        self.play(
            FadeOut(pares),
            FadeOut(mensaje),
            FadeOut(subtitulo),
            run_time=0.8
        )

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

        ancho = 8
        alto = 4.6

        tabla = Rectangle(
            width=ancho,
            height=alto,
            color=BLANCO,
            stroke_width=2
        )

        tabla.move_to(
            LEFT * 1
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

        total_columna.move_to(
            [3.0, 1.35, 0]
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
            "F": -0.1,
            "M": 2.1
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
                    3.0,
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
            [3.0, -2.75, 0]
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