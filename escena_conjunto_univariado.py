from manim import *
import random


class ConjuntoUnivariado(Scene):

    def construct(self):

        # =====================================================
        # PALETA DE COLORES
        # =====================================================

        VERDE_WHATSAPP = GREEN
        ROSADO_INSTAGRAM = PINK
        AZUL_FACEBOOK = BLUE
        BLANCO_TIKTOK = WHITE

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
        # FUNCIÓN PARA ASIGNAR COLOR
        # =====================================================

        def color_red_social(nombre):

            if nombre == "WhatsApp":
                return VERDE_WHATSAPP

            elif nombre == "Instagram":
                return ROSADO_INSTAGRAM

            elif nombre == "Facebook":
                return AZUL_FACEBOOK

            else:
                return BLANCO_TIKTOK

        # =====================================================
        # TÍTULO INICIAL
        # =====================================================

        titulo = Text(
            "¿Qué red social prefieren?",
            font_size=34,
            color=WHITE
        )

        titulo.to_edge(UP)

        self.play(
            FadeIn(titulo, shift=DOWN),
            run_time=0.8
        )

        self.wait(0.5)

        # =====================================================
        # CREAR LAS 30 PALABRAS
        # =====================================================

        palabras = VGroup()

        for dato in datos:

            palabra = Text(
                dato,
                font_size=21,
                color=color_red_social(dato)
            )

            palabras.add(palabra)

        # =====================================================
        # POSICIONES FINALES
        # 5 FILAS × 6 COLUMNAS
        # =====================================================

        posiciones = []

        columnas = 6
        filas = 5

        espacio_x = 2.05
        espacio_y = 0.72

        for fila in range(filas):

            for columna in range(columnas):

                x = (
                    columna - (columnas - 1) / 2
                ) * espacio_x

                y = (
                    1.35
                    - fila * espacio_y
                )

                posiciones.append(
                    np.array([x, y, 0])
                )

        # =====================================================
        # APARICIÓN DESORDENADA
        # =====================================================

        random.seed(15)

        for palabra in palabras:

            palabra.move_to(
                np.array([
                    random.uniform(-7, 7),
                    random.uniform(-3.5, 3.5),
                    0
                ])
            )

        # =====================================================
        # LAS PALABRAS VUELAN HACIA SU POSICIÓN
        # =====================================================

        animaciones = []

        for palabra, posicion in zip(
            palabras,
            posiciones
        ):

            animaciones.append(
                palabra.animate.move_to(posicion)
            )

        self.play(
            LaggedStart(
                *animaciones,
                lag_ratio=0.035
            ),
            run_time=3
        )

        # =====================================================
        # LAS PALABRAS SE DETIENEN
        # =====================================================

        self.wait(1)

        # =====================================================
        # CAJA ALREDEDOR DE LAS 30 OBSERVACIONES
        # =====================================================

        caja = SurroundingRectangle(
            palabras,
            color=YELLOW,
            buff=0.35,
            corner_radius=0.15,
            stroke_width=4
        )

        # =====================================================
        # EFECTO DE BRILLO
        # =====================================================

        brillo = SurroundingRectangle(
            palabras,
            color=YELLOW,
            buff=0.42,
            corner_radius=0.18,
            stroke_width=10
        )

        brillo.set_stroke(
            opacity=0.25
        )

        # =====================================================
        # APARECE LA CAJA
        # =====================================================

        self.play(
            Create(brillo),
            Create(caja),
            run_time=1.2
        )

        self.wait(0.5)

        # =====================================================
        # TEXTO "CONJUNTO UNIVARIADO"
        # =====================================================

        concepto = Text(
            "Conjunto Univariado",
            font_size=38,
            color=YELLOW
        )

        concepto.next_to(
            caja,
            UP,
            buff=0.35
        )

        # =====================================================
        # TEXTO INFERIOR
        # =====================================================

        subtitulo = Text(
            "Variable Cualitativa Nominal: Red Social Favorita",
            font_size=25,
            color=WHITE
        )

        subtitulo.to_edge(DOWN)

        # =====================================================
        # ANIMACIÓN DE LOS TEXTOS
        # =====================================================

        self.play(
            FadeIn(
                concepto,
                shift=DOWN
            ),
            run_time=1
        )

        self.play(
            FadeIn(
                subtitulo,
                shift=UP
            ),
            run_time=1
        )

        # =====================================================
        # PEQUEÑO DESTELLO FINAL
        # =====================================================

        self.play(
            Indicate(
                caja,
                color=YELLOW,
                scale_factor=1.02
            ),
            run_time=1.2
        )

        self.wait(3)