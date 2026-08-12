
from manim import *


class TablaFrecuencia(Scene):

    def construct(self):

        # =====================================================
        # PALETA
        # =====================================================

        VERDE_WHATSAPP = GREEN
        ROSADO_INSTAGRAM = PINK
        AZUL_FACEBOOK = BLUE
        BLANCO_TIKTOK = WHITE

        AMARILLO = YELLOW
        GRIS = GREY_B

        # =====================================================
        # FUNCIÓN PARA CREAR SUBÍNDICES
        # =====================================================

        def subindice(
            base,
            indice,
            color=WHITE,
            tam_base=30,
            tam_indice=18
        ):

            letra = Text(
                base,
                font_size=tam_base,
                color=color
            )

            sub = Text(
                indice,
                font_size=tam_indice,
                color=color
            )

            # Colocar el subíndice
            sub.next_to(
                letra,
                DOWN + RIGHT,
                buff=-0.05
            )

            sub.shift(
                LEFT * 0.05
            )

            return VGroup(
                letra,
                sub
            )

        # =====================================================
        # f_i
        # =====================================================

        def crear_fi(color=WHITE,
                    tam_base=30,
                    tam_indice=18):

                return subindice(
                "f",
                "i",
                color=color,
                tam_base=tam_base,
                tam_indice=tam_indice
                    )
                    

        # =====================================================
        # f_ri
        # =====================================================

        def crear_fri(
            color=WHITE,
            tam_base=30,
            tam_indice=16
            ):

            return subindice(
                "f",
                "ri",
                color=color,
                tam_base=tam_base,
                tam_indice=tam_indice
            )

        # =====================================================
        # DATOS
        # =====================================================

        redes = [
            "WhatsApp",
            "Instagram",
            "Facebook",
            "TikTok",
            "Total"
        ]

        frecuencias = [
            "9",
            "9",
            "6",
            "6",
            "30"
        ]

        frecuencias_relativas = [
            "30%",
            "30%",
            "20%",
            "20%",
            "100%"
        ]

        colores = [
            VERDE_WHATSAPP,
            ROSADO_INSTAGRAM,
            AZUL_FACEBOOK,
            BLANCO_TIKTOK,
            WHITE
        ]

        # =====================================================
        # TÍTULO
        # =====================================================

        titulo = Text(
            "Construcción de la tabla de frecuencias",
            font_size=32,
            color=WHITE
        )

        titulo.to_edge(UP)

        self.play(
            FadeIn(titulo, shift=DOWN),
            run_time=0.8
        )

        self.wait(0.5)

        # =====================================================
        # POSICIONES
        # =====================================================

        x_red = -4.1
        x_f = -1.0
        x_fr = 1.8

        y_header = 2.0

        # =====================================================
        # ENCABEZADO RED SOCIAL
        # =====================================================

        encabezado_red = Text(
            "Red Social",
            font_size=25,
            color=AMARILLO
        )

        encabezado_red.move_to(
            [x_red, y_header, 0]
        )

        self.play(
            FadeIn(
                encabezado_red,
                shift=UP
            ),
            run_time=0.6
        )

        # =====================================================
        # ENCABEZADO f_i
        # =====================================================

        encabezado_f = crear_fi(
            color=AMARILLO
        )

        encabezado_f.move_to(
            [x_f, y_header, 0]
        )

        self.play(
            FadeIn(
                encabezado_f,
                scale=1.2
            ),
            run_time=0.7
        )

        # =====================================================
        # ENCABEZADO f_ri %
        # =====================================================

        encabezado_fr = VGroup()

        fri = crear_fri(
            color=AMARILLO
        )

        porcentaje = Text(
            "%",
            font_size=24,
            color=AMARILLO
        )

        porcentaje.next_to(
            fri,
            RIGHT,
            buff=0.08
        )

        encabezado_fr.add(
            fri,
            porcentaje
        )

        encabezado_fr.move_to(
            [x_fr, y_header, 0]
        )

        self.play(
            FadeIn(
                encabezado_fr,
                scale=1.2
            ),
            run_time=0.7
        )

        # =====================================================
        # LÍNEAS DE LA TABLA
        # =====================================================

        linea_superior = Line(
            [-5.3, 1.65, 0],
            [3.1, 1.65, 0],
            color=WHITE,
            stroke_width=2
        )

        linea_1 = Line(
            [-2.5, 1.65, 0],
            [-2.5, -2.15, 0],
            color=GRIS,
            stroke_width=2
        )

        linea_2 = Line(
            [0.0, 1.65, 0],
            [0.0, -2.15, 0],
            color=GRIS,
            stroke_width=2
        )

        self.play(
            Create(linea_superior),
            Create(linea_1),
            Create(linea_2),
            run_time=0.8
        )

        # =====================================================
        # COLUMNA RED SOCIAL
        # =====================================================

        objetos_redes = VGroup()

        for i, (red, color) in enumerate(
            zip(redes, colores)
        ):

            y = 1.15 - i * 0.65

            texto = Text(
                red,
                font_size=24,
                color=color
            )

            texto.move_to(
                [x_red, y, 0]
            )

            objetos_redes.add(texto)

            self.play(
                FadeIn(
                    texto,
                    shift=RIGHT
                ),
                run_time=0.25
            )

        # =====================================================
        # COLUMNA f_i
        # =====================================================

        objetos_f = VGroup()

        for i, frecuencia in enumerate(
            frecuencias
        ):

            y = 1.15 - i * 0.65

            numero = Text(
                frecuencia,
                font_size=25,
                color=WHITE
            )

            numero.move_to(
                [x_f, y, 0]
            )

            objetos_f.add(numero)

            self.play(
                FadeIn(
                    numero,
                    scale=1.2
                ),
                run_time=0.25
            )

        # =====================================================
        # COLUMNA f_ri %
        # =====================================================

        objetos_fr = VGroup()

        for i, frecuencia in enumerate(
            frecuencias_relativas
        ):

            y = 1.15 - i * 0.65

            numero = Text(
                frecuencia,
                font_size=25,
                color=WHITE
            )

            numero.move_to(
                [x_fr, y, 0]
            )

            objetos_fr.add(numero)

            self.play(
                FadeIn(
                    numero,
                    scale=1.2
                ),
                run_time=0.25
            )

        # =====================================================
        # LÍNEA FINAL
        # =====================================================

        linea_final = Line(
            [-5.3, -2.15, 0],
            [3.1, -2.15, 0],
            color=WHITE,
            stroke_width=2
        )

        self.play(
            Create(linea_final),
            run_time=0.5
        )

        self.wait(1)

        # =====================================================
        # RESALTAR TOTAL
        # =====================================================

        fila_total = SurroundingRectangle(
            VGroup(
                objetos_redes[-1],
                objetos_f[-1],
                objetos_fr[-1]
            ),
            color=AMARILLO,
            buff=0.15
        )

        self.play(
            Create(fila_total),
            run_time=0.7
        )

        self.wait(1)

        # =====================================================
        # PANEL DE LA FÓRMULA
        # =====================================================

        panel = RoundedRectangle(
            width=4.4,
            height=2.8,
            corner_radius=0.2,
            color=GRIS,
            stroke_width=2
        )

        panel.to_edge(
            RIGHT,
            buff=0.35
        )

        panel.shift(
            DOWN * 0.15
        )

        self.play(
            FadeIn(
                panel,
                shift=LEFT
            ),
            run_time=0.7
        )

        # =====================================================
        # TEXTO DEL PANEL
        # =====================================================

        titulo_formula = Text(
            "Frecuencia relativa",
            font_size=22,
            color=WHITE
        )

        titulo_formula.move_to(
            panel.get_top()
            + DOWN * 0.4
        )

        self.play(
            FadeIn(titulo_formula),
            run_time=0.5
        )

        # =====================================================
        # CONSTRUIR f_ri = f_i / n
        # =====================================================

        formula_fri = crear_fri(
            color=AMARILLO
        )

        igualdad = Text(
            "=",
            font_size=32,
            color=WHITE
        )

        # =====================================================
        # FRACCIÓN
        # =====================================================

        numerador = crear_fi(
            color=WHITE,
            tam_base=27,
            tam_indice=16
        )

        denominador = Text(
            "n",
            font_size=27,
            color=WHITE
        )

        linea_fraccion = Line(
            LEFT * 0.45,
            RIGHT * 0.45,
            color=WHITE,
            stroke_width=2
        )

        fraccion = VGroup(
            numerador,
            linea_fraccion,
            denominador
        )

        numerador.next_to(
            linea_fraccion,
            UP,
            buff=0.08
        )

        denominador.next_to(
            linea_fraccion,
            DOWN,
            buff=0.08
        )

        formula_completa = VGroup(
            formula_fri,
            igualdad,
            fraccion
        )

        formula_fri.next_to(
            igualdad,
            LEFT,
            buff=0.15
        )

        fraccion.next_to(
            igualdad,
            RIGHT,
            buff=0.15
        )

        formula_completa.move_to(
            panel.get_center()
            + DOWN * 0.05
        )

        # =====================================================
        # ANIMAR FÓRMULA
        # =====================================================

        self.play(
            FadeIn(
                formula_fri,
                shift=LEFT
            ),
            run_time=0.5
        )

        self.play(
            Write(igualdad),
            run_time=0.4
        )

        self.play(
            FadeIn(
                fraccion,
                shift=RIGHT
            ),
            run_time=0.8
        )

        # =====================================================
        # EXPLICACIÓN
        # =====================================================

        explicacion = Text(
            "f absoluta  ÷  total",
            font_size=20,
            color=WHITE
        )

        explicacion.move_to(
            panel.get_bottom()
            + UP * 0.45
        )

        self.play(
            FadeIn(
                explicacion,
                shift=UP
            ),
            run_time=0.6
        )

        self.wait(1)

        # =====================================================
        # EJEMPLO 9 / 30
        # =====================================================

        ejemplo_titulo = Text(
            "Ejemplo:",
            font_size=20,
            color=VERDE_WHATSAPP
        )

        ejemplo_titulo.next_to(
            panel,
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(ejemplo_titulo),
            run_time=0.5
        )

        # =====================================================
        # FRACCIÓN 9/30 = 30%
        # =====================================================

        nueve = Text(
            "9",
            font_size=28,
            color=VERDE_WHATSAPP
        )

        treinta = Text(
            "30",
            font_size=28,
            color=WHITE
        )

        linea_ejemplo = Line(
            LEFT * 0.35,
            RIGHT * 0.35,
            color=WHITE,
            stroke_width=2
        )

        nueve.next_to(
            linea_ejemplo,
            UP,
            buff=0.06
        )

        treinta.next_to(
            linea_ejemplo,
            DOWN,
            buff=0.06
        )

        fraccion_ejemplo = VGroup(
            nueve,
            linea_ejemplo,
            treinta
        )

        igual_ejemplo = Text(
            "=",
            font_size=28,
            color=WHITE
        )

        resultado = Text(
            "30%",
            font_size=30,
            color=VERDE_WHATSAPP
        )

        ejemplo = VGroup(
            fraccion_ejemplo,
            igual_ejemplo,
            resultado
        )

        igual_ejemplo.next_to(
            fraccion_ejemplo,
            RIGHT,
            buff=0.25
        )

        resultado.next_to(
            igual_ejemplo,
            RIGHT,
            buff=0.25
        )

        ejemplo.next_to(
            ejemplo_titulo,
            RIGHT,
            buff=0.25
        )

        self.play(
            FadeIn(
                ejemplo,
                scale=1.1
            ),
            run_time=0.8
        )

        self.wait(2)

        # =====================================================
        # RESALTAR EL 9 Y EL 30 DE LA TABLA
        # =====================================================

        self.play(
            Indicate(
                objetos_f[0],
                color=VERDE_WHATSAPP,
                scale_factor=1.3
            ),
            run_time=0.7
        )

        self.play(
            Indicate(
                objetos_f[-1],
                color=AMARILLO,
                scale_factor=1.3
            ),
            run_time=0.7
        )

        self.wait(2)

