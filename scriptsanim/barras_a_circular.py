from manim import *


class PieChartSimple(Scene):

    def construct(self):

        # ==========================================
        # PALETA
        # ==========================================

        AZUL = BLUE
        NARANJA = ORANGE
        BLANCO = WHITE

        # ==========================================
        # DATOS
        # ==========================================

        valores = [15, 10, 5]
        nombres = ["TikTok", "Instagram", "Facebook"]
        porcentajes = ["50%", "33%", "17%"]
        colores = [AZUL, NARANJA, BLANCO]

        total = sum(valores)

        # ==========================================
        # TÍTULO
        # ==========================================

        titulo = Text(
            "Red Social Favorita",
            font_size=36,
            color=BLANCO
        )

        titulo.to_edge(UP)

        self.play(
            FadeIn(titulo, shift=DOWN),
            run_time=0.8
        )

        # ==========================================
        # CREAR PIE CHART
        # ==========================================

        sectores = VGroup()

        angulo_actual = PI / 2

        for valor, color in zip(valores, colores):

            angulo = TAU * valor / total

            sector = Sector(
                radius=2.5,
                start_angle=angulo_actual,
                angle=angulo,
                fill_color=color,
                fill_opacity=0.9,
                stroke_color=BLANCO,
                stroke_width=3
            )

            sectores.add(sector)

            angulo_actual += angulo

        # ==========================================
        # ANIMACIÓN DE LOS SECTORES
        # ==========================================

        self.play(
            LaggedStart(
                *[
                    GrowFromCenter(sector)
                    for sector in sectores
                ],
                lag_ratio=0.2
            ),
            run_time=2
        )

        self.wait(1)

        # ==========================================
        # ETIQUETAS
        # ==========================================

        etiquetas = VGroup()

        angulo_actual = PI / 2

        for valor, nombre, porcentaje in zip(
            valores,
            nombres,
            porcentajes
        ):

            angulo = TAU * valor / total

            angulo_medio = (
                angulo_actual + angulo / 2
            )

            posicion = 1.35 * np.array([
                np.cos(angulo_medio),
                np.sin(angulo_medio),
                0
            ])

            etiqueta = Text(
                f"{nombre}\n{porcentaje}",
                font_size=20,
                color=BLANCO
            )

            etiqueta.move_to(posicion)

            etiquetas.add(etiqueta)

            angulo_actual += angulo

        # ==========================================
        # MOSTRAR ETIQUETAS
        # ==========================================

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        etiqueta,
                        scale=0.8
                    )
                    for etiqueta in etiquetas
                ],
                lag_ratio=0.2
            ),
            run_time=1.5
        )

        self.wait(3)