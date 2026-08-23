from manim import *


class ConteoFrecuencias(Scene):

    def construct(self):

        # =====================================================
        # PALETA
        # =====================================================

        VERDE_WHATSAPP = GREEN
        ROSADO_INSTAGRAM = PINK
        AZUL_FACEBOOK = BLUE
        BLANCO_TIKTOK = WHITE
        AMARILLO = YELLOW

        # =====================================================
        # DATOS
        # =====================================================

        datos = [
            "Facebook", "WhatsApp", "Instagram", "TikTok",
            "WhatsApp", "Instagram", "Facebook", "TikTok",
            "WhatsApp", "Instagram",

            "WhatsApp", "Facebook", "Instagram", "TikTok",
            "WhatsApp", "Instagram", "Facebook", "WhatsApp",
            "TikTok", "Instagram",

            "WhatsApp", "Facebook", "Instagram", "WhatsApp",
            "TikTok", "Instagram", "Facebook", "WhatsApp",
            "Instagram", "TikTok"
        ]

        # =====================================================
        # FUNCIÓN DE COLOR
        # =====================================================

        def obtener_color(nombre):

            if nombre == "WhatsApp":
                return VERDE_WHATSAPP

            elif nombre == "Instagram":
                return ROSADO_INSTAGRAM

            elif nombre == "Facebook":
                return AZUL_FACEBOOK

            else:
                return BLANCO_TIKTOK

        # =====================================================
        # TÍTULO
        # =====================================================

        titulo = Text(
            "Contemos las observaciones",
            font_size=34,
            color=WHITE
        )

        titulo.to_edge(UP)

        self.play(
            FadeIn(titulo, shift=DOWN),
            run_time=0.8
        )

        # =====================================================
        # CREAR LAS 30 PALABRAS
        # =====================================================

        palabras = VGroup()

        for dato in datos:

            palabra = Text(
                dato,
                font_size=19,
                color=obtener_color(dato)
            )

            palabras.add(palabra)

        # =====================================================
        # POSICIONES INICIALES
        # =====================================================

        posiciones_iniciales = []

        for fila in range(5):

            for columna in range(6):

                x = (columna - 2.5) * 2.05
                y = 1.55 - fila * 0.72

                posiciones_iniciales.append(
                    np.array([x, y, 0])
                )

        for palabra, posicion in zip(
            palabras,
            posiciones_iniciales
        ):
            palabra.move_to(posicion)

        # =====================================================
        # APARICIÓN DE LAS 30 OBSERVACIONES
        # =====================================================

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        palabra,
                        scale=0.8
                    )
                    for palabra in palabras
                ],
                lag_ratio=0.03
            ),
            run_time=2
        )

        self.wait(1)

        # =====================================================
        # CATEGORÍAS
        # =====================================================

        categorias = [
            "WhatsApp",
            "Instagram",
            "Facebook",
            "TikTok"
        ]

        colores = [
            VERDE_WHATSAPP,
            ROSADO_INSTAGRAM,
            AZUL_FACEBOOK,
            BLANCO_TIKTOK
        ]

        frecuencias = [
            9,
            9,
            6,
            6
        ]

        # =====================================================
        # CENTROS DE CADA GRUPO
        # =====================================================
        #
        # IMPORTANTE:
        # Este es un DICCIONARIO.
        # Le damos un nombre diferente a la función
        # que calcula las posiciones.
        # =====================================================

        centros_grupo = {

            "WhatsApp":
                LEFT * 4.0 + UP * 1.0,

            "Instagram":
                RIGHT * 1.0 + UP * 1.0,

            "Facebook":
                LEFT * 4.0 + DOWN * 1.7,

            "TikTok":
                RIGHT * 1.0 + DOWN * 1.7
        }

        # =====================================================
        # SEPARAR LAS PALABRAS POR CATEGORÍA
        # =====================================================

        grupos = {
            "WhatsApp": VGroup(),
            "Instagram": VGroup(),
            "Facebook": VGroup(),
            "TikTok": VGroup()
        }

        for palabra, dato in zip(
            palabras,
            datos
        ):

            grupos[dato].add(palabra)

        # =====================================================
        # FUNCIÓN PARA CALCULAR POSICIONES
        # =====================================================

        def calcular_posiciones_grupo(
            cantidad,
            centro
        ):

            posiciones = []

            columnas = 3

            for i in range(cantidad):

                fila = i // columnas
                columna = i % columnas

                x = (
                    columna - 1
                ) * 1.15

                y = (
                    0.35
                    - fila * 0.55
                )

                posiciones.append(
                    centro
                    + RIGHT * x
                    + UP * y
                )

            return posiciones

        # =====================================================
        # AGRUPAR LAS PALABRAS
        # =====================================================

        animaciones = []

        for categoria in categorias:

            grupo = grupos[categoria]

            # AQUÍ ESTABA EL ERROR ORIGINAL
            #
            # Antes:
            # posiciones_grupo[categoria]
            #
            # Ahora:
            # centros_grupo[categoria]

            posiciones = calcular_posiciones_grupo(
                len(grupo),
                centros_grupo[categoria]
            )

            for palabra, posicion in zip(
                grupo,
                posiciones
            ):

                animaciones.append(
                    palabra.animate.move_to(
                        posicion
                    )
                )

        # =====================================================
        # ANIMACIÓN DE AGRUPAMIENTO
        # =====================================================

        self.play(
            LaggedStart(
                *animaciones,
                lag_ratio=0.025
            ),
            run_time=3
        )

        self.wait(1)

        # =====================================================
        # CAJAS DE CADA CATEGORÍA
        # =====================================================

        cajas = VGroup()
        nombres = VGroup()

        for categoria, color in zip(
            categorias,
            colores
        ):

            caja = SurroundingRectangle(
                grupos[categoria],
                color=color,
                buff=0.18,
                corner_radius=0.12,
                stroke_width=3
            )

            nombre = Text(
                categoria,
                font_size=24,
                color=color
            )

            nombre.next_to(
                caja,
                UP,
                buff=0.12
            )

            cajas.add(caja)
            nombres.add(nombre)

        self.play(
            LaggedStart(
                *[
                    Create(caja)
                    for caja in cajas
                ],
                lag_ratio=0.15
            ),
            LaggedStart(
                *[
                    FadeIn(nombre)
                    for nombre in nombres
                ],
                lag_ratio=0.15
            ),
            run_time=1.5
        )

        self.wait(1)

        # =====================================================
        # QUITAR TÍTULO
        # =====================================================

        self.play(
            FadeOut(titulo),
            run_time=0.5
        )

        # =====================================================
        # POSICIONES DE LOS CONTADORES
        # =====================================================

        posiciones_contador = [

            LEFT * 1.55 + UP * 0.95,

            RIGHT * 3.55 + UP * 0.95,

            LEFT * 1.55 + DOWN * 1.9,

            RIGHT * 3.55 + DOWN * 1.9
        ]

        contadores = []

        # =====================================================
        # FUNCIÓN PARA ANIMAR EL CONTEO
        # =====================================================

        def animar_conteo(
            posicion,
            frecuencia,
            color
        ):

            actual = Text(
                "0",
                font_size=36,
                color=color
            )

            actual.move_to(posicion)

            self.play(
                FadeIn(
                    actual,
                    scale=1.4
                ),
                run_time=0.3
            )

            # ---------------------------------------------
            # 0 → 1 → 2 → ... → frecuencia
            # ---------------------------------------------

            for numero in range(
                1,
                frecuencia + 1
            ):

                nuevo = Text(
                    str(numero),
                    font_size=36,
                    color=color
                )

                nuevo.move_to(
                    posicion
                )

                self.play(
                    Transform(
                        actual,
                        nuevo
                    ),
                    run_time=0.12
                )

            return actual

        # =====================================================
        # HACER LOS CONTEOS
        # =====================================================

        for posicion, frecuencia, color in zip(
            posiciones_contador,
            frecuencias,
            colores
        ):

            contador = animar_conteo(
                posicion,
                frecuencia,
                color
            )

            contadores.append(contador)

        self.wait(1)

        # =====================================================
        # RESALTAR RESULTADOS
        # =====================================================

        for contador in contadores:

            self.play(
                Indicate(
                    contador,
                    color=AMARILLO,
                    scale_factor=1.2
                ),
                run_time=0.5
            )

        # =====================================================
        # TOTAL
        # =====================================================

        linea = Line(
            LEFT * 5.2 + DOWN * 3.15,
            RIGHT * 5.2 + DOWN * 3.15,
            color=WHITE,
            stroke_width=2
        )

        total_texto = Text(
            "Total",
            font_size=30,
            color=WHITE
        )

        total_texto.move_to(
            LEFT * 3.5 + DOWN * 3.55
        )

        total = Text(
            "0",
            font_size=38,
            color=AMARILLO
        )

        total.move_to(
            RIGHT * 3.5 + DOWN * 3.55
        )

        self.play(
            Create(linea),
            FadeIn(total_texto),
            FadeIn(total, scale=1.3),
            run_time=0.8
        )

        # =====================================================
        # 0 → 30
        # =====================================================

        for numero in range(1, 31):

            nuevo_total = Text(
                str(numero),
                font_size=38,
                color=AMARILLO
            )

            nuevo_total.move_to(
                total.get_center()
            )

            self.play(
                Transform(
                    total,
                    nuevo_total
                ),
                run_time=0.05
            )

        self.wait(1)

        # =====================================================
        # MENSAJE FINAL
        # =====================================================

        mensaje = Text(
            "Frecuencia absoluta",
            font_size=30,
            color=AMARILLO
        )

        mensaje.to_edge(DOWN)

        self.play(
            FadeIn(
                mensaje,
                shift=UP
            )
        )

        self.wait(3)