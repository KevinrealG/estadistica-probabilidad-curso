from manim import *
import random


class TablaFrecuencias(Scene):

    def construct(self):

        # =====================================================
        # PALETA
        # =====================================================

        AZUL = BLUE
        NARANJA = ORANGE
        BLANCO = WHITE

        random.seed(42)

        # =====================================================
        # TÍTULO
        # =====================================================

        titulo = Text(
            "De los datos a la información",
            font_size=38,
            color=BLANCO
        ).to_edge(UP)

        self.play(
            FadeIn(titulo, shift=DOWN),
            run_time=0.8
        )

        # =====================================================
        # 30 DATOS
        # =====================================================

        datos = [
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
        # CREAR PALABRAS DESORDENADAS
        # =====================================================

        palabras = VGroup()

        for dato in datos:

            texto = Text(
                dato,
                font_size=random.randint(20, 28),
                color=random.choice(
                    [AZUL, BLANCO, NARANJA]
                )
            )

            texto.move_to([
                random.uniform(-6, 6),
                random.uniform(-2.5, 2.5),
                0
            ])

            palabras.add(texto)

        self.play(
            LaggedStart(
                *[
                    FadeIn(p, scale=0.7)
                    for p in palabras
                ],
                lag_ratio=0.025
            ),
            run_time=2
        )

        self.wait(1)

        # =====================================================
        # MENSAJE
        # =====================================================

        mensaje = Text(
            "Contemos cuántos hay de cada uno...",
            font_size=30,
            color=NARANJA
        ).to_edge(DOWN)

        self.play(
            FadeIn(mensaje, shift=UP)
        )

        self.wait(1)

        # =====================================================
        # TABLA
        # =====================================================

        tabla = Table(
            [
                ["TikTok", "15", "50%"],
                ["Instagram", "10", "33%"],
                ["Facebook", "5", "17%"],
            ],
            col_labels=[
                Text("Red Social"),
                Text("f"),
                Text("fr %")
            ],
            include_outer_lines=True,
            h_buff=1.2,
            v_buff=0.6
        )

        tabla.scale(0.85)
        tabla.move_to(ORIGIN)

        # =====================================================
        # TRANSFORMACIÓN VISUAL
        # =====================================================

        # Primero hacemos que las palabras se agrupen
        # hacia el centro.

        grupo_centro = VGroup(
            *[
                palabra.copy().move_to(
                    ORIGIN + UP * random.uniform(-0.3, 0.3)
                )
                for palabra in palabras
            ]
        )

        self.play(
            FadeOut(mensaje),
            LaggedStart(
                *[
                    palabra.animate.move_to(
                        ORIGIN + UP * random.uniform(-0.5, 0.5)
                    )
                    for palabra in palabras
                ],
                lag_ratio=0.02
            ),
            run_time=2
        )

        # =====================================================
        # TRANSFORM
        # =====================================================

        self.play(
            Transform(
                palabras,
                tabla,
                path_arc=PI / 8
            ),
            run_time=3
        )

        self.wait(1)

        # =====================================================
        # ASEGURAR TABLA
        # =====================================================

        self.remove(palabras)
        self.add(tabla)

        # =====================================================
        # RESALTAR CABECERA
        # =====================================================

        cabecera = VGroup(
            tabla.get_entries((1, 1)),
            tabla.get_entries((1, 2)),
            tabla.get_entries((1, 3))
        )

        caja_cabecera = SurroundingRectangle(
            cabecera,
            color=NARANJA,
            buff=0.15,
            stroke_width=4
        )

        self.play(
            Create(caja_cabecera),
            run_time=1
        )

        self.wait(1)

        # =====================================================
        # RESALTAR f
        # =====================================================

        self.play(
            FadeOut(caja_cabecera),
            run_time=0.5
        )

        columna_f = VGroup(
            tabla.get_entries((1, 2)),
            tabla.get_entries((2, 2)),
            tabla.get_entries((3, 2)),
            tabla.get_entries((4, 2))
        )

        caja_f = SurroundingRectangle(
            columna_f,
            color=AZUL,
            buff=0.12,
            stroke_width=4
        )

        self.play(
            Create(caja_f),
            run_time=1
        )

        self.wait(1)

        # =====================================================
        # ANIMAR FRECUENCIAS
        # =====================================================

        frecuencias = [
            tabla.get_entries((2, 2)),
            tabla.get_entries((3, 2)),
            tabla.get_entries((4, 2))
        ]

        for numero in frecuencias:
            numero.set_opacity(0)

        for numero in frecuencias:

            numero.set_opacity(1)

            self.play(
                FadeIn(
                    numero,
                    scale=1.6
                ),
                run_time=0.7
            )

            self.wait(0.3)

        self.wait(1)

        # =====================================================
        # FRECUENCIA RELATIVA
        # =====================================================

        self.play(
            FadeOut(caja_f),
            run_time=0.5
        )

        columna_fr = VGroup(
            tabla.get_entries((1, 3)),
            tabla.get_entries((2, 3)),
            tabla.get_entries((3, 3)),
            tabla.get_entries((4, 3))
        )

        caja_fr = SurroundingRectangle(
            columna_fr,
            color=NARANJA,
            buff=0.12,
            stroke_width=4
        )

        self.play(
            Create(caja_fr),
            run_time=1
        )

        self.wait(1)

        # =====================================================
        # PORCENTAJES
        # =====================================================

        porcentajes = [
            tabla.get_entries((2, 3)),
            tabla.get_entries((3, 3)),
            tabla.get_entries((4, 3))
        ]

        for numero in porcentajes:
            numero.set_opacity(0)

        for numero in porcentajes:

            numero.set_opacity(1)

            self.play(
                FadeIn(
                    numero,
                    scale=1.6
                ),
                run_time=0.7
            )

            self.wait(0.3)

        self.wait(1)

        # =====================================================
        # FÓRMULA SIN LATEX
        # =====================================================

        self.play(
            FadeOut(caja_fr),
            run_time=0.5
        )

        formula = Text(
            "fr = f / n",
            font_size=34,
            color=AZUL
        ).to_edge(DOWN)

        self.play(
            Write(formula),
            run_time=1
        )

        self.wait(2)

        # =====================================================
        # MENSAJE FINAL
        # =====================================================

        mensaje_final = Text(
            "Una tabla transforma datos en información",
            font_size=30,
            color=NARANJA
        ).to_edge(DOWN)

        self.play(
            Transform(
                formula,
                mensaje_final
            ),
            run_time=1
        )

        self.wait(3)