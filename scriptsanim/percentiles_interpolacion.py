from manim import *

# ============================================================
# CONFIGURACIÓN HORIZONTAL 16:9 (TV / PORTÁTIL)
# ============================================================

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_width = 14.222
config.frame_height = 8



# ============================================================
# PALETA
# ============================================================

FONDO = "#0B1020"
AZUL = "#42A5F5"
VERDE = "#66BB6A"
VERDE_NEON = "#00FF9C"
ROJO = "#EF5350"
AMARILLO = "#FFD54F"
BLANCO = WHITE
GRIS = "#B0BEC5"
NARANJA = "#FF9800"


class PercentilesInterpolacion(Scene):

    def construct(self):

        self.camera.background_color = FONDO

        # ====================================================
        # DATOS
        # ====================================================

        datos = [
            45, 52, 60, 63, 67,
            70, 72, 75, 78, 80,
            82, 85, 87, 90, 92,
            94, 96, 97, 98, 100
        ]

        # ====================================================
        # ESCENA 1
        # HOOK
        # ====================================================

        titulo = Text(
            "¿ESTÁ REALMENTE\nEN EL 15% SUPERIOR?",
            font_size=46,
            weight=BOLD,
            color=BLANCO,
            line_spacing=0.8
        )

        titulo.to_edge(UP, buff=0.8)

        examen = RoundedRectangle(
            corner_radius=0.15,
            width=6.5,
            height=3.6,
            stroke_color=BLANCO,
            stroke_width=3
        )

        nota = Text(
            "85 / 100",
            font_size=72,
            weight=BOLD,
            color=ROJO
        )

        nota.move_to(examen)

        sello = Text(
            "15% SUPERIOR",
            font_size=30,
            weight=BOLD,
            color=AMARILLO
        )

        sello.next_to(
            examen,
            DOWN,
            buff=0.5
        )

        self.play(
            FadeIn(titulo, shift=DOWN * 0.3),
            run_time=1
        )

        self.play(
            Create(examen),
            Write(nota),
            run_time=1.2
        )

        self.play(
            Write(sello),
            run_time=0.7
        )

        self.wait(0.8)

        # ====================================================
        # TRANSICIÓN
        # ====================================================

        self.play(
            FadeOut(titulo),
            FadeOut(examen),
            FadeOut(nota),
            FadeOut(sello),
            run_time=0.8
        )

        # ====================================================
        # ESCENA 2
        # LOS 20 DATOS
        # ====================================================

        titulo_datos = Text(
            "20 notas ordenadas",
            font_size=38,
            color=BLANCO
        )

        titulo_datos.to_edge(UP, buff=0.5)

        self.play(
            Write(titulo_datos)
        )

        datos_mobj = VGroup()

        for i, valor in enumerate(datos):

            texto = Text(
                str(valor),
                font_size=30,
                color=BLANCO
            )

            datos_mobj.add(texto)

        # 20 datos en 4 filas × 5 columnas
        datos_mobj.arrange_in_grid(
            rows=4,
            cols=5,
            buff=(0.45, 0.45)
        )

        datos_mobj.move_to(ORIGIN + DOWN * 0.3)

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        dato,
                        shift=DOWN * 0.25
                    )
                    for dato in datos_mobj
                ],
                lag_ratio=0.06
            ),
            run_time=2
        )

        # Resaltar 85
        indice_85 = datos.index(85)

        caja_85 = SurroundingRectangle(
            datos_mobj[indice_85],
            color=ROJO,
            buff=0.12,
            corner_radius=0.08
        )

        self.play(
            Create(caja_85),
            datos_mobj[indice_85].animate.set_color(ROJO),
            run_time=0.8
        )

        etiqueta_n = Text(
            "N = 20",
            font_size=34,
            color=AZUL
        )

        etiqueta_n.to_edge(DOWN, buff=0.7)

        self.play(
            Write(etiqueta_n)
        )

        self.wait(1)

        # ====================================================
        # ESCENA 3
        # PERCENTIL 85
        # ====================================================

        self.play(
            FadeOut(titulo_datos),
            FadeOut(caja_85),
            FadeOut(etiqueta_n),
            FadeOut(datos_mobj),
            run_time=0.8
        )

        titulo_p = Text(
            "Buscamos el Percentil 85",
            font_size=40,
            color=BLANCO
        )

        titulo_p.to_edge(UP, buff=0.6)

        self.play(
            Write(titulo_p)
        )

        p85 = MathTex(
            r"P_{85}",
            font_size=65,
            color=AMARILLO
        )

        p85.move_to(UP * 2.2)

        self.play(
            Write(p85)
        )

        explicacion = Text(
            "15% superior  →  85% por debajo",
            font_size=30,
            color=GRIS
        )

        explicacion.next_to(
            p85,
            DOWN,
            buff=0.35
        )

        self.play(
            FadeIn(explicacion)
        )

        # Fórmula
        formula = MathTex(
            r"i=\frac{K(N-1)}{100}+1",
            font_size=55
        )

        formula.move_to(ORIGIN)

        self.play(
            Write(formula),
            run_time=1.2
        )

        # ====================================================
        # SUSTITUCIÓN
        # ====================================================

        sustitucion = MathTex(
            r"i=\frac{85(20-1)}{100}+1",
            font_size=52,
            color=AZUL
        )

        sustitucion.next_to(
            formula,
            DOWN,
            buff=0.55
        )

        self.play(
            Write(sustitucion),
            run_time=1
        )

        resultado_pos = MathTex(
            r"i=17.15",
            font_size=62,
            color=VERDE_NEON
        )

        resultado_pos.next_to(
            sustitucion,
            DOWN,
            buff=0.55
        )

        self.play(
            Write(resultado_pos),
            run_time=1
        )

        self.wait(1.2)

        # ====================================================
        # ESCENA 4
        # POSICIONES 17 Y 18
        # ====================================================

        self.play(
            FadeOut(titulo_p),
            FadeOut(p85),
            FadeOut(explicacion),
            FadeOut(formula),
            FadeOut(sustitucion),
            FadeOut(resultado_pos),
            run_time=0.8
        )

        titulo_pos = Text(
            "¿Entre qué valores está 17.15?",
            font_size=38,
            color=BLANCO
        )

        titulo_pos.to_edge(UP, buff=0.6)

        self.play(
            Write(titulo_pos)
        )

        # Línea numérica
        linea = NumberLine(
            x_range=[16, 19, 1],
            length=7,
            include_numbers=True,
            include_ticks=True,
            font_size=28
        )

        linea.move_to(DOWN * 0.4)

        self.play(
            Create(linea),
            run_time=1
        )

        punto_17 = Dot(
            linea.n2p(17),
            radius=0.12,
            color=AZUL
        )

        punto_18 = Dot(
            linea.n2p(18),
            radius=0.12,
            color=AZUL
        )

        self.play(
            FadeIn(punto_17, scale=0.5),
            FadeIn(punto_18, scale=0.5)
        )

        valor_17 = Text(
            "96",
            font_size=65,
            weight=BOLD,
            color=AMARILLO
        )

        valor_18 = Text(
            "97",
            font_size=65,
            weight=BOLD,
            color=AMARILLO
        )

        valor_17.next_to(
            punto_17,
            UP,
            buff=0.3
        )

        valor_18.next_to(
            punto_18,
            UP,
            buff=0.3
        )

        self.play(
            Write(valor_17),
            Write(valor_18)
        )

        posiciones = MathTex(
            r"X_{17}=96",
            r"\qquad",
            r"X_{18}=97",
            font_size=42
        )

        posiciones.to_edge(DOWN, buff=0.8)

        self.play(
            Write(posiciones)
        )

        # ====================================================
        # INDICAR EL 0.15
        # ====================================================

        punto_interpolado = Dot(
            linea.n2p(17.15),
            radius=0.15,
            color=VERDE_NEON
        )

        self.play(
            Create(
                DashedLine(
                    linea.n2p(17),
                    linea.n2p(17.15),
                    color=VERDE_NEON
                )
            ),
            FadeIn(punto_interpolado, scale=0.5)
        )

        decimal = MathTex(
            r"d=0.15",
            font_size=40,
            color=VERDE_NEON
        )

        decimal.next_to(
            punto_interpolado,
            DOWN,
            buff=0.45
        )

        self.play(
            Write(decimal)
        )

        self.wait(1)

        # ====================================================
        # ESCENA 5
        # INTERPOLACIÓN LINEAL
        # ====================================================

        self.play(
            FadeOut(titulo_pos),
            FadeOut(linea),
            FadeOut(punto_17),
            FadeOut(punto_18),
            FadeOut(valor_17),
            FadeOut(valor_18),
            FadeOut(posiciones),
            FadeOut(punto_interpolado),
            FadeOut(decimal),
            run_time=0.8
        )

        titulo_inter = Text(
            "Interpolación lineal",
            font_size=42,
            color=BLANCO
        )

        titulo_inter.to_edge(UP, buff=0.6)

        self.play(
            Write(titulo_inter)
        )

        formula_inter = MathTex(
            r"P_k=X_{[i]}+d\left(X_{[i+1]}-X_{[i]}\right)",
            font_size=48
        )

        formula_inter.move_to(UP * 1.6)

        self.play(
            Write(formula_inter),
            run_time=1.2
        )

        # Sustitución
        paso_1 = MathTex(
            r"P_{85}=96+0.15(97-96)",
            font_size=52,
            color=AZUL
        )

        paso_1.move_to(ORIGIN)

        self.play(
            Write(paso_1),
            run_time=1
        )

        paso_2 = MathTex(
            r"P_{85}=96+0.15(1)",
            font_size=52
        )

        paso_2.next_to(
            paso_1,
            DOWN,
            buff=0.45
        )

        self.play(
            TransformMatchingTex(
                paso_1.copy(),
                paso_2
            ),
            run_time=1
        )

        resultado = MathTex(
            r"P_{85}=96.15",
            font_size=72,
            color=VERDE_NEON
        )

        resultado.next_to(
            paso_2,
            DOWN,
            buff=0.6
        )

        caja_resultado = SurroundingRectangle(
            resultado,
            color=VERDE_NEON,
            buff=0.25,
            corner_radius=0.12
        )

        self.play(
            Write(resultado),
            Create(caja_resultado),
            run_time=1
        )

        self.wait(1.5)

        # ====================================================
        # ESCENA 6
        # COMPARACIÓN FINAL
        # ====================================================

        self.play(
            FadeOut(titulo_inter),
            FadeOut(formula_inter),
            FadeOut(paso_1),
            FadeOut(paso_2),
            FadeOut(resultado),
            FadeOut(caja_resultado),
            run_time=0.8
        )

        titulo_final = Text(
            "¿85 está en el 15% superior?",
            font_size=40,
            color=BLANCO
        )

        titulo_final.to_edge(UP, buff=0.6)

        self.play(
            Write(titulo_final)
        )

        # Línea de comparación
        linea_final = NumberLine(
            x_range=[80, 100, 5],
            length=7.5,
            include_numbers=True,
            include_ticks=True,
            font_size=26
        )

        linea_final.move_to(DOWN * 0.3)

        self.play(
            Create(linea_final),
            run_time=1
        )

        # Punto 85
        punto_85_final = Dot(
            linea_final.n2p(85),
            radius=0.14,
            color=ROJO
        )

        etiqueta_85 = Text(
            "85",
            font_size=48,
            weight=BOLD,
            color=ROJO
        )

        etiqueta_85.next_to(
            punto_85_final,
            UP,
            buff=0.25
        )

        # Punto 96.15
        punto_9615 = Dot(
            linea_final.n2p(96.15),
            radius=0.16,
            color=VERDE_NEON
        )

        etiqueta_9615 = Text(
            "96.15",
            font_size=48,
            weight=BOLD,
            color=VERDE_NEON
        )

        etiqueta_9615.next_to(
            punto_9615,
            UP,
            buff=0.25
        )

        self.play(
            FadeIn(punto_85_final, scale=0.5),
            Write(etiqueta_85)
        )

        self.play(
            FadeIn(punto_9615, scale=0.5),
            Write(etiqueta_9615)
        )

        # Línea entre ambos
        distancia = DashedLine(
            punto_85_final.get_center(),
            punto_9615.get_center(),
            color=ROJO,
            stroke_width=5
        )

        self.play(
            Create(distancia),
            run_time=0.8
        )

        mensaje = Text(
            "El 15% superior comienza en 96.15",
            font_size=30,
            color=VERDE_NEON
        )

        mensaje.to_edge(DOWN, buff=0.8)

        self.play(
            Write(mensaje),
            run_time=1
        )

        self.wait(2)

        # ====================================================
        # CIERRE
        # ====================================================

        self.play(
            FadeOut(titulo_final),
            FadeOut(linea_final),
            FadeOut(punto_85_final),
            FadeOut(etiqueta_85),
            FadeOut(punto_9615),
            FadeOut(etiqueta_9615),
            FadeOut(distancia),
            FadeOut(mensaje),
            run_time=0.8
        )

        pregunta = Text(
            "Si N = 50 y K = 25...\n¿cuál sería la posición?",
            font_size=42,
            color=BLANCO,
            line_spacing=0.8
        )

        pregunta.move_to(ORIGIN)

        self.play(
            Write(pregunta),
            run_time=1.2
        )

        formula_final = MathTex(
            r"i=\frac{25(50-1)}{100}+1",
            font_size=55,
            color=AMARILLO
        )

        formula_final.next_to(
            pregunta,
            DOWN,
            buff=0.6
        )

        self.play(
            Write(formula_final)
        )

        cta = Text(
            "¡Calcula y comenta tu respuesta!",
            font_size=32,
            color=VERDE_NEON
        )

        cta.to_edge(DOWN, buff=0.7)

        self.play(
            Write(cta)
        )

        self.wait(3)