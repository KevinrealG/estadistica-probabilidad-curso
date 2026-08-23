from manim import *
import random

# ============================================================
# TABLA DE FRECUENCIAS PARA VARIABLE CUANTITATIVA DISCRETA
# Cantidad de boletas compradas por persona
# ============================================================


class TablaFrecuenciaDiscreta(Scene):

    def construct(self):

        # ====================================================
        # PALETA
        # ====================================================

        FONDO = "#05070D"

        AZUL = "#4D96FF"
        AZUL_CLARO = "#72C9FF"
        NARANJA = "#FF9F43"
        AMARILLO = "#FFD166"
        VERDE = "#55D187"
        MORADO = "#A66CFF"
        ROJO = "#FF5C6C"
        BLANCO = WHITE
        GRIS = "#8D96A8"

        self.camera.background_color = FONDO

        # ====================================================
        # DATOS
        # ====================================================

        datos = [
            1, 2, 3, 2, 1, 4, 2, 3, 1, 2,
            5, 3, 2, 1, 4, 2, 3, 2, 1, 2,
            4, 3, 2, 1, 5, 2, 3, 4, 2, 1
        ]

        categorias = [1, 2, 3, 4, 5]

        fi = {
            1: 7,
            2: 11,
            3: 6,
            4: 4,
            5: 2
        }

        fri_decimal = {
            1: "0.2333",
            2: "0.3667",
            3: "0.2000",
            4: "0.1333",
            5: "0.0667"
        }

        Fi = {
            1: 7,
            2: 18,
            3: 24,
            4: 28,
            5: 30
        }

        Fri_decimal = {
            1: "0.2333",
            2: "0.6000",
            3: "0.8000",
            4: "0.9333",
            5: "1.0000"
        }

        fri_pct = {
            1: "23.33%",
            2: "36.67%",
            3: "20.00%",
            4: "13.33%",
            5: "6.67%"
        }

        Fri_pct = {
            1: "23.33%",
            2: "60.00%",
            3: "80.00%",
            4: "93.33%",
            5: "100.00%"
        }

        # ====================================================
        # FUNCIONES AUXILIARES
        # ====================================================

        def subscript_text(base, sub, color=WHITE,
                           base_size=27, sub_size=16):

            b = Text(
                base,
                font_size=base_size,
                color=color
            )

            s = Text(
                sub,
                font_size=sub_size,
                color=color
            )

            s.next_to(
                b,
                DOWN + RIGHT * 0.12,
                buff=0.01
            )

            return VGroup(b, s)

        def crear_celda(texto, posicion, color=WHITE,
                        size=23):

            obj = Text(
                str(texto),
                font_size=size,
                color=color
            )

            obj.move_to(posicion)

            return obj

        # ====================================================
        # ESCENA 1
        # HOOK
        # ====================================================

        hook = Text(
            "PREDICE TUS VENTAS",
            font_size=46,
            color=AMARILLO,
            weight=BOLD
        )

        hook.move_to(UP * 1.6)

        subtitulo = Text(
            "Tabla de Frecuencias",
            font_size=30,
            color=AZUL_CLARO
        )

        subtitulo.next_to(
            hook,
            DOWN,
            buff=0.3
        )

        # Ecualizador
        barras_audio = VGroup()

        alturas = [
            0.5, 1.2, 0.8, 1.8, 2.5,
            1.4, 2.8, 1.0, 2.2, 1.5,
            2.7, 1.1, 2.0, 0.7
        ]

        for i, altura in enumerate(alturas):

            barra = Rectangle(
                width=0.28,
                height=altura,
                fill_color=AZUL,
                fill_opacity=0.85,
                stroke_width=0
            )

            barra.move_to(
                [
                    -4.2 + i * 0.65,
                    -1.2,
                    0
                ]
            )

            barras_audio.add(barra)

        self.play(
            LaggedStart(
                *[
                    GrowFromEdge(
                        barra,
                        DOWN
                    )
                    for barra in barras_audio
                ],
                lag_ratio=0.04
            ),
            run_time=1.2
        )

        self.play(
            FadeIn(hook, scale=1.2),
            FadeIn(subtitulo),
            run_time=0.8
        )

        # Marco tipo dashboard
        marco = SurroundingRectangle(
            VGroup(hook, subtitulo),
            color=AZUL,
            buff=0.35,
            stroke_width=2
        )

        self.play(
            Create(marco),
            run_time=0.5
        )

        self.wait(1)

        self.play(
            FadeOut(barras_audio),
            FadeOut(hook),
            FadeOut(subtitulo),
            FadeOut(marco)
        )

        # ====================================================
        # ESCENA 2
        # DATOS ORIGINALES
        # ====================================================

        titulo = Text(
            "30 compras de un concierto",
            font_size=34,
            color=BLANCO
        )

        titulo.to_edge(UP)

        pregunta = Text(
            "¿Cuántas boletas compró cada persona?",
            font_size=25,
            color=AZUL_CLARO
        )

        pregunta.next_to(
            titulo,
            DOWN,
            buff=0.2
        )

        self.play(
            FadeIn(titulo),
            FadeIn(pregunta)
        )

        # Crear los 30 datos
        datos_mobjects = VGroup()

        posiciones = []

        for fila in range(5):
            for col in range(6):

                x = -4.8 + col * 1.9
                y = 1.0 - fila * 0.85

                posiciones.append(
                    np.array([x, y, 0])
                )

        for i, valor in enumerate(datos):

            numero = Text(
                str(valor),
                font_size=30,
                color=AZUL_CLARO
            )

            numero.move_to(
                posiciones[i]
            )

            datos_mobjects.add(numero)

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        numero,
                        shift=DOWN * 0.3
                    )
                    for numero in datos_mobjects
                ],
                lag_ratio=0.025
            ),
            run_time=2
        )

        etiqueta_xi = subscript_text(
            "x",
            "i",
            color=AMARILLO,
            base_size=30,
            sub_size=18
        )

        etiqueta_xi.to_edge(
            LEFT,
            buff=0.5
        )

        etiqueta_xi.shift(
            DOWN * 2.5
        )

        descripcion = Text(
            "Boletas por persona",
            font_size=22,
            color=GRIS
        )

        descripcion.next_to(
            etiqueta_xi,
            RIGHT,
            buff=0.25
        )

        self.play(
            FadeIn(etiqueta_xi),
            FadeIn(descripcion)
        )

        self.wait(1.5)

        # ====================================================
        # ESCENA 3
        # VALORES DISCRETOS
        # ====================================================

        self.play(
            FadeOut(datos_mobjects),
            FadeOut(etiqueta_xi),
            FadeOut(descripcion),
            FadeOut(titulo),
            FadeOut(pregunta)
        )

        titulo_valores = Text(
            "Valores de la variable",
            font_size=34,
            color=BLANCO
        )

        titulo_valores.to_edge(UP)

        self.play(
            FadeIn(titulo_valores)
        )

        valores = VGroup()

        for valor in categorias:

            numero = Text(
                str(valor),
                font_size=48,
                color=AZUL_CLARO
            )

            valores.add(numero)

        valores.arrange(
            RIGHT,
            buff=0.75
        )

        valores.move_to(
            UP * 0.4
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        numero,
                        shift=DOWN
                    )
                    for numero in valores
                ],
                lag_ratio=0.15
            ),
            run_time=1.2
        )

        llave = Text(
            "Valores enteros y separados",
            font_size=25,
            color=AMARILLO
        )

        llave.next_to(
            valores,
            DOWN,
            buff=0.5
        )

        self.play(
            FadeIn(llave)
        )

        self.wait(1)

        # ====================================================
        # ESCENA 4
        # CREACIÓN DE TABLA
        # ====================================================

        self.play(
            FadeOut(valores),
            FadeOut(llave),
            FadeOut(titulo_valores)
        )

        titulo_tabla = Text(
            "Construimos la tabla de frecuencias",
            font_size=30,
            color=AMARILLO
        )

        titulo_tabla.to_edge(UP)

        self.play(
            FadeIn(titulo_tabla)
        )

        # ====================================================
        # POSICIONES DE LA TABLA
        # ====================================================

        x_positions = [
            -5.2,   # xi
            -3.55,  # fi
            -1.85,  # fri
            -0.05,  # Fi
            1.75,   # Fri
            3.45,   # fri %
            5.05    # Fri %
        ]

        y_header = 2.1

        y_rows = [
            1.15,
            0.25,
            -0.65,
            -1.55,
            -2.45
        ]

        # ====================================================
        # LÍNEAS
        # ====================================================

        left = -5.8
        right = 5.8
        top = 2.65
        bottom = -2.75

        # Verticales
        verticales = VGroup()

        for x in [
            left,
            -4.35,
            -2.7,
            -1.0,
            0.85,
            2.65,
            4.25,
            right
        ]:

            linea = Line(
                [x, top, 0],
                [x, bottom, 0],
                color=GRIS,
                stroke_width=1.5
            )

            verticales.add(linea)

        # Horizontales
        horizontales = VGroup()

        for y in [
            top,
            1.65,
            0.7,
            -0.2,
            -1.1,
            -2.0,
            bottom
        ]:

            linea = Line(
                [left, y, 0],
                [right, y, 0],
                color=GRIS,
                stroke_width=1.5
            )

            horizontales.add(linea)

        self.play(
            Create(verticales),
            Create(horizontales),
            run_time=1.2
        )

        # ====================================================
        # ENCABEZADOS
        # ====================================================

        encabezados = VGroup()

        h_xi = subscript_text(
            "x",
            "i",
            color=AMARILLO,
            base_size=28,
            sub_size=16
        )

        h_fi = subscript_text(
            "f",
            "i",
            color=VERDE,
            base_size=28,
            sub_size=16
        )

        h_fri = subscript_text(
            "f",
            "ri",
            color=AZUL,
            base_size=27,
            sub_size=14
        )

        h_Fi = subscript_text(
            "F",
            "i",
            color=NARANJA,
            base_size=28,
            sub_size=16
        )

        h_Fri = subscript_text(
            "F",
            "ri",
            color=MORADO,
            base_size=27,
            sub_size=14
        )

        h_frip = Text(
            "fri %",
            font_size=23,
            color=AZUL
        )

        h_Frip = Text(
            "Fri %",
            font_size=23,
            color=MORADO
        )

        encabezados.add(
            h_xi,
            h_fi,
            h_fri,
            h_Fi,
            h_Fri,
            h_frip,
            h_Frip
        )

        for obj, x in zip(
            encabezados,
            x_positions
        ):
            obj.move_to(
                [x, y_header, 0]
            )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        obj,
                        shift=DOWN
                    )
                    for obj in encabezados
                ],
                lag_ratio=0.1
            ),
            run_time=1
        )

        # ====================================================
        # ESCENA 5
        # xi
        # ====================================================

        texto_exp = Text(
            "1 a 5 boletas",
            font_size=23,
            color=AMARILLO
        )

        texto_exp.to_edge(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(texto_exp)
        )

        celdas_xi = VGroup()

        for categoria, y in zip(
            categorias,
            y_rows
        ):

            obj = Text(
                str(categoria),
                font_size=27,
                color=AMARILLO
            )

            obj.move_to(
                [x_positions[0], y, 0]
            )

            celdas_xi.add(obj)

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        obj,
                        scale=1.2
                    )
                    for obj in celdas_xi
                ],
                lag_ratio=0.15
            ),
            run_time=1
        )

        self.play(
            FadeOut(texto_exp)
        )

        # ====================================================
        # ESCENA 6
        # FRECUENCIA ABSOLUTA
        # ====================================================

        explicacion = Text(
            "Contamos cuántas personas compraron cada cantidad",
            font_size=21,
            color=VERDE
        )

        explicacion.to_edge(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(explicacion)
        )

        celdas_fi = VGroup()

        for categoria, y in zip(
            categorias,
            y_rows
        ):

            obj = Text(
                str(fi[categoria]),
                font_size=27,
                color=VERDE
            )

            obj.move_to(
                [x_positions[1], y, 0]
            )

            celdas_fi.add(obj)

            self.play(
                FadeIn(
                    obj,
                    scale=1.5
                ),
                run_time=0.25
            )

        # Destacar 11
        highlight_11 = SurroundingRectangle(
            celdas_fi[1],
            color=AMARILLO,
            buff=0.1,
            stroke_width=4
        )

        self.play(
            Create(highlight_11),
            run_time=0.4
        )

        once = Text(
            "11 personas",
            font_size=24,
            color=AMARILLO
        )

        once.next_to(
            highlight_11,
            DOWN,
            buff=0.15
        )

        self.play(
            FadeIn(once)
        )

        self.wait(1)

        self.play(
            FadeOut(highlight_11),
            FadeOut(once),
            FadeOut(explicacion)
        )

        # ====================================================
        # ESCENA 7
        # FRECUENCIA RELATIVA
        # ====================================================

        explicacion = Text(
            "Dividimos cada frecuencia entre 30",
            font_size=23,
            color=AZUL
        )

        explicacion.to_edge(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(explicacion)
        )

        formula = Text(
            "fri = fi / 30",
            font_size=29,
            color=AMARILLO
        )

        formula.to_edge(
            LEFT,
            buff=0.3
        )

        formula.shift(
            DOWN * 3.0
        )

        self.play(
            FadeIn(
                formula,
                shift=UP
            )
        )

        celdas_fri = VGroup()

        for categoria, y in zip(
            categorias,
            y_rows
        ):

            obj = Text(
                fri_decimal[categoria],
                font_size=22,
                color=AZUL
            )

            obj.move_to(
                [x_positions[2], y, 0]
            )

            celdas_fri.add(obj)

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        obj,
                        scale=1.2
                    )
                    for obj in celdas_fri
                ],
                lag_ratio=0.1
            ),
            run_time=1
        )

        # Animación especial del 11 / 30
        calculo = Text(
            "11 / 30 = 0.3667",
            font_size=25,
            color=AMARILLO
        )

        calculo.to_edge(
            RIGHT,
            buff=0.4
        )

        calculo.shift(
            DOWN * 3.0
        )

        self.play(
            FadeIn(calculo)
        )

        self.wait(1)

        self.play(
            FadeOut(formula),
            FadeOut(calculo),
            FadeOut(explicacion)
        )

        # ====================================================
        # ESCENA 8
        # FRECUENCIA ACUMULADA
        # ====================================================

        titulo_acum = Text(
            "¡SUMA EN ZIGZAG!",
            font_size=31,
            color=AMARILLO
        )

        titulo_acum.to_edge(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(
                titulo_acum,
                scale=1.15
            )
        )

        celdas_Fi = VGroup()

        # Primera frecuencia acumulada
        valores_acum = [7, 18, 24, 28, 30]

        # ====================================================
        # 7
        # ====================================================

        obj1 = Text(
            "7",
            font_size=27,
            color=NARANJA
        )

        obj1.move_to(
            [x_positions[3], y_rows[0], 0]
        )

        celdas_Fi.add(obj1)

        self.play(
            FadeIn(
                obj1,
                scale=1.3
            )
        )

        # ====================================================
        # FLECHA 7 + 11 = 18
        # ====================================================

        flecha1 = CurvedArrow(
            [x_positions[3], y_rows[0] - 0.25, 0],
            [x_positions[3], y_rows[1] + 0.25, 0],
            color=AMARILLO,
            stroke_width=4,
            angle=-PI / 3
        )

        suma1 = Text(
            "7 + 11 = 18",
            font_size=21,
            color=AMARILLO
        )

        suma1.next_to(
            flecha1,
            RIGHT,
            buff=0.15
        )

        self.play(
            Create(flecha1),
            FadeIn(suma1),
            run_time=0.7
        )

        obj2 = Text(
            "18",
            font_size=27,
            color=NARANJA
        )

        obj2.move_to(
            [x_positions[3], y_rows[1], 0]
        )

        celdas_Fi.add(obj2)

        self.play(
            FadeIn(
                obj2,
                scale=1.4
            )
        )

        self.play(
            FadeOut(flecha1),
            FadeOut(suma1)
        )

        # ====================================================
        # 18 + 6 = 24
        # ====================================================

        flecha2 = CurvedArrow(
            [x_positions[3], y_rows[1] - 0.25, 0],
            [x_positions[3], y_rows[2] + 0.25, 0],
            color=AMARILLO,
            stroke_width=4,
            angle=-PI / 3
        )

        suma2 = Text(
            "18 + 6 = 24",
            font_size=21,
            color=AMARILLO
        )

        suma2.next_to(
            flecha2,
            RIGHT,
            buff=0.15
        )

        self.play(
            Create(flecha2),
            FadeIn(suma2)
        )

        obj3 = Text(
            "24",
            font_size=27,
            color=NARANJA
        )

        obj3.move_to(
            [x_positions[3], y_rows[2], 0]
        )

        celdas_Fi.add(obj3)

        self.play(
            FadeIn(
                obj3,
                scale=1.4
            )
        )

        self.play(
            FadeOut(flecha2),
            FadeOut(suma2)
        )

        # ====================================================
        # 24 + 4 = 28
        # ====================================================

        flecha3 = CurvedArrow(
            [x_positions[3], y_rows[2] - 0.25, 0],
            [x_positions[3], y_rows[3] + 0.25, 0],
            color=AMARILLO,
            stroke_width=4,
            angle=-PI / 3
        )

        suma3 = Text(
            "24 + 4 = 28",
            font_size=21,
            color=AMARILLO
        )

        suma3.next_to(
            flecha3,
            RIGHT,
            buff=0.15
        )

        self.play(
            Create(flecha3),
            FadeIn(suma3)
        )

        obj4 = Text(
            "28",
            font_size=27,
            color=NARANJA
        )

        obj4.move_to(
            [x_positions[3], y_rows[3], 0]
        )

        celdas_Fi.add(obj4)

        self.play(
            FadeIn(
                obj4,
                scale=1.4
            )
        )

        self.play(
            FadeOut(flecha3),
            FadeOut(suma3)
        )

        # ====================================================
        # 28 + 2 = 30
        # ====================================================

        flecha4 = CurvedArrow(
            [x_positions[3], y_rows[3] - 0.25, 0],
            [x_positions[3], y_rows[4] + 0.25, 0],
            color=AMARILLO,
            stroke_width=4,
            angle=-PI / 3
        )

        suma4 = Text(
            "28 + 2 = 30",
            font_size=21,
            color=AMARILLO
        )

        suma4.next_to(
            flecha4,
            RIGHT,
            buff=0.15
        )

        self.play(
            Create(flecha4),
            FadeIn(suma4)
        )

        obj5 = Text(
            "30",
            font_size=27,
            color=NARANJA
        )

        obj5.move_to(
            [x_positions[3], y_rows[4], 0]
        )

        celdas_Fi.add(obj5)

        self.play(
            FadeIn(
                obj5,
                scale=1.4
            )
        )

        self.play(
            FadeOut(flecha4),
            FadeOut(suma4),
            FadeOut(titulo_acum)
        )

        # ====================================================
        # ESCENA 9
        # FRECUENCIA RELATIVA ACUMULADA
        # ====================================================

        explicacion = Text(
            "Acumulamos también las proporciones",
            font_size=23,
            color=MORADO
        )

        explicacion.to_edge(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(explicacion)
        )

        celdas_Fri = VGroup()

        for categoria, y in zip(
            categorias,
            y_rows
        ):

            obj = Text(
                Fri_decimal[categoria],
                font_size=21,
                color=MORADO
            )

            obj.move_to(
                [x_positions[4], y, 0]
            )

            celdas_Fri.add(obj)

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        obj,
                        scale=1.15
                    )
                    for obj in celdas_Fri
                ],
                lag_ratio=0.1
            ),
            run_time=1
        )

        self.play(
            FadeOut(explicacion)
        )

        # ====================================================
        # ESCENA 10
        # PORCENTAJES
        # ====================================================

        explicacion_pct = Text(
            "Convertimos las proporciones a porcentaje",
            font_size=23,
            color=AZUL_CLARO
        )

        explicacion_pct.to_edge(
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(explicacion_pct)
        )

        celdas_fri_pct = VGroup()
        celdas_Fri_pct = VGroup()

        for categoria, y in zip(
            categorias,
            y_rows
        ):

            obj1 = Text(
                fri_pct[categoria],
                font_size=20,
                color=AZUL_CLARO
            )

            obj1.move_to(
                [x_positions[5], y, 0]
            )

            celdas_fri_pct.add(obj1)

            obj2 = Text(
                Fri_pct[categoria],
                font_size=20,
                color=MORADO
            )

            obj2.move_to(
                [x_positions[6], y, 0]
            )

            celdas_Fri_pct.add(obj2)

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        obj,
                        scale=1.15
                    )
                    for obj in celdas_fri_pct
                ],
                lag_ratio=0.08
            ),
            run_time=0.8
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        obj,
                        scale=1.15
                    )
                    for obj in celdas_Fri_pct
                ],
                lag_ratio=0.08
            ),
            run_time=0.8
        )

        self.wait(1)

        self.play(
            FadeOut(explicacion_pct)
        )

        # ====================================================
        # ESCENA 11
        # RESALTAR FILA 2 BOLETAS
        # ====================================================

        # Rectángulo que cubre TODA la fila
        fila_2 = Rectangle(
            width=11.35,
            height=0.78,
            stroke_color=VERDE,
            stroke_width=3,
            fill_color=VERDE,
            fill_opacity=0.10
        )

        fila_2.move_to(
            [0, y_rows[1], 0]
        )

        self.play(
            Create(fila_2),
            run_time=0.5
        )

        # Resaltar 60%
        sesenta = SurroundingRectangle(
            celdas_Fri_pct[1],
            color=AMARILLO,
            buff=0.12,
            stroke_width=4
        )

        self.play(
            Create(sesenta),
            run_time=0.5
        )

        dato_clave = Text(
            "EL DATO CLAVE",
            font_size=30,
            color=AMARILLO,
            weight=BOLD
        )

        dato_clave.to_edge(
            DOWN,
            buff=0.55
        )

        dato_60 = Text(
            "60% = máximo 2 boletas",
            font_size=31,
            color=VERDE
        )

        dato_60.next_to(
            dato_clave,
            DOWN,
            buff=0.15
        )

        self.play(
            FadeIn(
                dato_clave,
                shift=UP
            ),
            FadeIn(
                dato_60,
                shift=UP
            )
        )

        self.wait(2)

        # ====================================================
        # ESCENA 12
        # CIERRE
        # ====================================================

        self.play(
            FadeOut(fila_2),
            FadeOut(sesenta),
            FadeOut(dato_clave),
            FadeOut(dato_60)
        )

        cierre = Text(
            "2 boletas = la cantidad más frecuente",
            font_size=27,
            color=AMARILLO
        )

        cierre.to_edge(
            DOWN,
            buff=0.3
        )

        self.play(
            FadeIn(cierre)
        )

        # Resaltar fi = 11
        highlight_fi = SurroundingRectangle(
            celdas_fi[1],
            color=VERDE,
            buff=0.12,
            stroke_width=4
        )

        self.play(
            Create(highlight_fi)
        )

        self.wait(1.5)

        self.play(
            FadeOut(highlight_fi),
            FadeOut(cierre)
        )

        # ====================================================
        # PREGUNTA FINAL
        # ====================================================

        pregunta_final = Text(
            "¿Lanzarías un combo en pareja?",
            font_size=39,
            color=AMARILLO,
            weight=BOLD
        )

        pregunta_final.move_to(
            ORIGIN
        )

        subtitulo_final = Text(
            "Usa tus datos para tomar decisiones.",
            font_size=25,
            color=AZUL_CLARO
        )

        subtitulo_final.next_to(
            pregunta_final,
            DOWN,
            buff=0.35
        )

        self.play(
            FadeIn(
                pregunta_final,
                scale=1.15
            ),
            FadeIn(
                subtitulo_final,
                shift=UP
            )
        )

        self.wait(3)

        self.play(
            FadeOut(pregunta_final),
            FadeOut(subtitulo_final),
            FadeOut(verticales),
            FadeOut(horizontales),
            FadeOut(encabezados),
            FadeOut(celdas_xi),
            FadeOut(celdas_fi),
            FadeOut(celdas_fri),
            FadeOut(celdas_Fi),
            FadeOut(celdas_Fri),
            FadeOut(celdas_fri_pct),
            FadeOut(celdas_Fri_pct),
            run_time=1
        )