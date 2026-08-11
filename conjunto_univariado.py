from manim import *
import random


class ConjuntoUnivariado(Scene):

    def construct(self):

        random.seed(42)

        # =====================================================
        # PALETA
        # =====================================================

        AZUL = BLUE
        NARANJA = ORANGE
        BLANCO = WHITE

        # =====================================================
        # LAS 30 OBSERVACIONES
        # =====================================================

        palabras = [
            "TikTok", "Instagram", "X", "Facebook",
            "Instagram", "TikTok", "Facebook", "X",
            "TikTok", "Instagram", "Instagram", "Facebook",
            "X", "TikTok", "Facebook", "Instagram",
            "TikTok", "X", "Facebook", "TikTok",
            "Instagram", "X", "TikTok", "Facebook",
            "Instagram", "TikTok", "X", "Facebook",
            "Instagram", "TikTok"
        ]

        # =====================================================
        # TÍTULO
        # =====================================================

        titulo = Text(
            "Observemos los datos",
            font_size=36,
            color=BLANCO
        ).to_edge(UP)

        self.play(
            FadeIn(titulo, shift=DOWN),
            run_time=0.8
        )

        self.wait(0.5)

        # =====================================================
        # CREAR PALABRAS
        # =====================================================

        palabras_mobjects = VGroup()

        colores = [AZUL, BLANCO, NARANJA]

        for palabra in palabras:

            texto = Text(
                palabra,
                font_size=random.randint(22, 30),
                color=random.choice(colores)
            )

            # Posición inicial aleatoria
            texto.move_to([
                random.uniform(-6, 6),
                random.uniform(-2.5, 2.5),
                0
            ])

            palabras_mobjects.add(texto)

        self.play(
            LaggedStart(
                *[
                    FadeIn(palabra, scale=0.7)
                    for palabra in palabras_mobjects
                ],
                lag_ratio=0.04
            ),
            run_time=2.5
        )

        self.wait(1)

        # =====================================================
        # ORGANIZAR LAS 30 PALABRAS
        # =====================================================

        # Posiciones en una cuadrícula 6 x 5
        posiciones = []

        for fila in range(5):
            for columna in range(6):

                x = -5.5 + columna * 2.2
                y = 1.8 - fila * 0.85

                posiciones.append(
                    [x, y, 0]
                )

        movimientos = []

        for palabra, posicion in zip(
            palabras_mobjects,
            posiciones
        ):

            movimientos.append(
                palabra.animate.move_to(posicion)
            )

        self.play(
            LaggedStart(
                *movimientos,
                lag_ratio=0.04
            ),
            run_time=3
        )

        self.wait(1)

        # =====================================================
        # ENCERRAR EL CONJUNTO
        # =====================================================

        caja = SurroundingRectangle(
            palabras_mobjects,
            color=NARANJA,
            buff=0.45,
            corner_radius=0.15,
            stroke_width=5
        )

        # Efecto de brillo simulado
        caja_brillo = SurroundingRectangle(
            palabras_mobjects,
            color=NARANJA,
            buff=0.55,
            corner_radius=0.18,
            stroke_width=2
        )

        self.play(
            Create(caja_brillo),
            run_time=0.7
        )

        self.play(
            Create(caja),
            run_time=1
        )

        # =====================================================
        # TEXTO "CONJUNTO UNIVARIADO"
        # =====================================================

        conjunto_texto = Text(
            "Conjunto Univariado",
            font_size=42,
            color=NARANJA
        )

        conjunto_texto.move_to(
            UP * 3.1
        )

        self.play(
            FadeIn(
                conjunto_texto,
                shift=UP,
                scale=0.8
            ),
            run_time=1
        )

        self.wait(1)

        # =====================================================
        # LÍNEA DE CONEXIÓN
        # =====================================================

        flecha = Arrow(
            conjunto_texto.get_bottom(),
            caja.get_top(),
            buff=0.15,
            color=NARANJA,
            stroke_width=3
        )

        self.play(
            GrowArrow(flecha),
            run_time=0.7
        )

        self.wait(1)

        # =====================================================
        # DEFINICIÓN INFERIOR
        # =====================================================

        definicion = Text(
            "Variable Cualitativa Nominal: Red Social Favorita",
            font_size=27,
            color=BLANCO
        )

        definicion.to_edge(DOWN, buff=0.45)

        self.play(
            FadeIn(
                definicion,
                shift=UP
            ),
            run_time=1
        )

        self.wait(3)

        # =====================================================
        # RESALTAR LA VARIABLE
        # =====================================================

        variable = Text(
            "Red Social Favorita",
            font_size=29,
            color=NARANJA
        )

        variable.move_to(definicion)

        self.play(
            Transform(
                definicion,
                variable
            ),
            run_time=1
        )

        self.wait(2)

        # =====================================================
        # CIERRE
        # =====================================================

        self.play(
            Indicate(caja, color=NARANJA, scale_factor=1.03),
            run_time=1.5
        )

        self.wait(2)