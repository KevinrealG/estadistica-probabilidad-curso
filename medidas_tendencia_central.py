from manim import *
import random
import math


config.pixel_width = 1920
config.pixel_height = 1080
config.frame_width = 14.222
config.frame_height = 8



# ============================================================
# PALETA
# ============================================================

ROJO = "#FF4D5A"
AMARILLO = "#FFD166"
VERDE = "#55D187"
AZUL = "#4D96FF"
NARANJA = "#FF9F43"
MORADO = "#B56CFF"
BLANCO = WHITE
GRIS = "#AAB2BD"


class MedidasTendenciaCentral(Scene):

    def construct(self):

        # ====================================================
        # DATOS
        # ====================================================

        datos = [
            14, 15, 15, 16, 16, 16, 17, 17, 17, 17,
            18, 18, 18, 18, 18,
            19, 19, 19, 19,
            20, 20,
            21, 21,
            22,
            23,
            24,
            25,
            27,
            28,
            30
        ]

        n = len(datos)

        # Valores matemáticamente correctos
        suma = sum(datos)
        media = suma / n

        mediana = (datos[14] + datos[15]) / 2

        # Moda
        frecuencia = {}

        for valor in datos:
            frecuencia[valor] = frecuencia.get(valor, 0) + 1

        moda = max(
            frecuencia,
            key=frecuencia.get
        )

        # ====================================================
        # FUNCIÓN AUXILIAR
        # ====================================================

        def crear_titulo(texto, color=BLANCO, size=38):

            titulo = Text(
                texto,
                font_size=size,
                color=color,
                weight=BOLD
            )

            titulo.to_edge(
                UP,
                buff=0.55
            )

            return titulo

        # ====================================================
        # ESCENA 1
        # HOOK
        # ====================================================

        hook = Text(
            "¿EL PROMEDIO\nMIENTE?",
            font_size=58,
            color=ROJO,
            weight=BOLD,
            line_spacing=0.8
        )

        hook.to_edge(UP, buff=0.8)

        subtitulo = Text(
            "Una pregunta de estadística...",
            font_size=25,
            color=GRIS
        )

        subtitulo.next_to(
            hook,
            DOWN,
            buff=0.4
        )

        self.play(
            Write(hook),
            run_time=0.9
        )

        self.play(
            FadeIn(
                subtitulo,
                shift=UP
            )
        )

        # Datos grandes y ordenados desde el inicio
        numeros_caos = VGroup()

        for valor in datos:

            numero = Text(
                str(valor),
                font_size=32,
                color=BLANCO
            )

            numeros_caos.add(numero)

        numeros_caos.arrange_in_grid(
            rows=5,
            cols=6,
            buff=(0.22, 0.28)
        )

        numeros_caos.next_to(
            subtitulo,
            DOWN,
            buff=0.45
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        numero,
                        scale=0.3
                    )
                    for numero in numeros_caos
                ],
                lag_ratio=0.025
            ),
            run_time=1.5
        )

        self.wait(0.7)

        self.play(
            FadeOut(hook),
            FadeOut(subtitulo),
            FadeOut(numeros_caos)
        )

        # ====================================================
        # ESCENA 2
        # LOS 30 GAMERS
        # ====================================================

        titulo = crear_titulo(
            "Las edades de 30 gamers",
            AMARILLO,
            36
        )

        self.play(
            FadeIn(titulo)
        )

        # Número de muestra
        muestra = Text(
            "n = 30",
            font_size=36,
            color=AZUL,
            weight=BOLD
        )

        muestra.next_to(
            titulo,
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(muestra)
        )

        # ====================================================
        # NUMBER LINE
        # ====================================================

        linea = NumberLine(
            x_range=[14, 30, 2],
            length=7.8,
            include_numbers=False,
            font_size=22,
            color=GRIS
        )

        linea.move_to(
            DOWN * 0.7
        )

        numeros_recta = VGroup()

        for valor in range(14, 31, 2):
            etiqueta = Text(
                str(valor),
                font_size=30,
                color=WHITE
            )

            etiqueta.next_to(
                linea.n2p(valor),
                DOWN,
                buff=0.15
            )

            numeros_recta.add(etiqueta)

        self.play(
            Create(linea),
            LaggedStart(
                *[FadeIn(n, shift=UP * 0.15) for n in numeros_recta],
                lag_ratio=0.08
            ),
            run_time=2
        )

        # ====================================================
        # CREAR PUNTOS APILADOS
        # ====================================================

        puntos = VGroup()

        grupos = {}

        for valor in datos:

            grupos.setdefault(valor, [])

        for valor in grupos:

            cantidad = frecuencia[valor]

            for j in range(cantidad):

                punto = Dot(
                    point=linea.n2p(valor)
                    + UP * (0.28 + j * 0.38),
                    radius=0.14,
                    color=BLANCO
                )

                puntos.add(punto)

                grupos[valor].append(punto)

        self.play(
            LaggedStart(
                *[
                    FadeIn(
                        punto,
                        scale=0.5
                    )
                    for punto in puntos
                ],
                lag_ratio=0.025
            ),
            run_time=2
        )

        self.wait(1)

        self.play(
            FadeOut(titulo),
            FadeOut(muestra),
            run_time=0.6
        )

        # ====================================================
        # ESCENA 3
        # MODA
        # ====================================================

        texto_moda = Text(
            "MODA",
            font_size=42,
            color=AMARILLO,
            weight=BOLD
        )

        definicion_moda = Text(
            "El valor que aparece más veces",
            font_size=26,
            color=BLANCO
        )

        VGroup(
            texto_moda,
            definicion_moda
        ).arrange(
            DOWN,
            buff=0.2
        ).to_edge(
            DOWN,
            buff=0.4
        )

        self.play(
            FadeIn(
                texto_moda,
                scale=1.2
            )
        )

        self.play(
            FadeIn(definicion_moda)
        )

        # Resaltar torre del 18
        torre_18 = VGroup(
            *grupos[18]
        )

        circulo_moda = SurroundingRectangle(
            torre_18,
            color=AMARILLO,
            buff=0.18,
            corner_radius=0.15
        )

        etiqueta_18 = Text(
            "18",
            font_size=34,
            color=AMARILLO,
            weight=BOLD
        )

        etiqueta_18.next_to(
            torre_18,
            UP,
            buff=0.25
        )

        self.play(
            Create(circulo_moda),
            Indicate(
                torre_18,
                color=AMARILLO,
                scale_factor=1.2
            ),
            FadeIn(
                etiqueta_18,
                shift=UP
            ),
            run_time=1.2
        )

        self.wait(1)

        # Notación
        notacion_moda = Text(
            "Muestra: mₒ     |     Población: Mₒ",
            font_size=25,
            color=GRIS
        )

        notacion_moda.to_edge(
            DOWN,
            buff=0.4
        )

        self.play(
            FadeIn(notacion_moda)
        )

        self.wait(1)

        # ====================================================
        # MINI DEMOSTRACIÓN DE MODAS
        # ====================================================

        mini_titulo = Text(
            "Puede ser:",
            font_size=24,
            color=BLANCO
        )

        unimodal = Text(
            "Unimodal",
            font_size=20,
            color=AMARILLO
        )

        bimodal = Text(
            "Bimodal",
            font_size=20,
            color=AZUL
        )

        multimodal = Text(
            "Multimodal",
            font_size=20,
            color=MORADO
        )

        VGroup(
            mini_titulo,
            unimodal,
            bimodal,
            multimodal
        ).arrange(
            DOWN,
            buff=0.12,
            aligned_edge=LEFT
        ).to_edge(
            RIGHT,
            buff=0.7
        ).to_edge(
            DOWN,
            buff=0.45
        )

        self.play(
            FadeIn(mini_titulo),
            FadeIn(unimodal),
            FadeIn(bimodal),
            FadeIn(multimodal)
        )

        self.wait(1)

        self.play(
            FadeOut(texto_moda),
            FadeOut(definicion_moda),
            FadeOut(circulo_moda),
            FadeOut(etiqueta_18),
            FadeOut(notacion_moda),
            FadeOut(mini_titulo),
            FadeOut(unimodal),
            FadeOut(bimodal),
            FadeOut(multimodal)
        )

        # ====================================================
        # ESCENA 4
        # MEDIANA PARA N PAR
        # ====================================================

        titulo_mediana = crear_titulo(
            "MEDIANA",
            VERDE,
            42
        )

        self.play(
            FadeIn(titulo_mediana)
        )

        explicacion = Text(
            "Con 30 datos, el centro está entre dos valores",
            font_size=25,
            color=BLANCO
        )

        explicacion.to_edge(DOWN, buff=0.6)

        self.play(
            FadeIn(explicacion)
        )

        # Posiciones centrales:
        # 15 -> 18
        # 16 -> 19

        punto_18_central = grupos[18][-1]

        punto_19_central = grupos[19][0]

        # Líneas verticales
        linea_18 = DashedLine(
            punto_18_central.get_center() + DOWN * 0.15,
            punto_18_central.get_center() + UP * 1.7,
            color=VERDE,
            dash_length=0.08
        )

        linea_19 = DashedLine(
            punto_19_central.get_center() + DOWN * 0.15,
            punto_19_central.get_center() + UP * 1.7,
            color=VERDE,
            dash_length=0.08
        )

        self.play(
            Create(linea_18),
            Create(linea_19),
            run_time=0.8
        )

        # Etiquetas
        pos15 = Text(
            "15° dato",
            font_size=21,
            color=VERDE
        )

        pos15.next_to(
            linea_18,
            UP,
            buff=0.15
        )

        pos16 = Text(
            "16° dato",
            font_size=21,
            color=VERDE
        )

        pos16.next_to(
            linea_19,
            UP,
            buff=0.15
        )

        self.play(
            FadeIn(pos15),
            FadeIn(pos16)
        )

        # Línea central
        centro_mediana = Line(
            [
                linea_18.get_x(),
                -0.1,
                0
            ],
            [
                linea_19.get_x(),
                -0.1,
                0
            ],
            color=VERDE,
            stroke_width=8
        )

        self.play(
            Create(centro_mediana),
            run_time=0.7
        )

        # Fórmula visual
        formula_mediana = MathTex(
            r"\text{Me} = \frac{18 + 19}{2} = 18.5",
            font_size=30,
            color=VERDE
        )

        formula_mediana.to_edge(DOWN, buff=0.95)

        self.play(
            Write(formula_mediana),
            run_time=1
        )

        self.wait(2)

        self.play(
            FadeOut(titulo_mediana),
            FadeOut(explicacion),
            FadeOut(linea_18),
            FadeOut(linea_19),
            FadeOut(pos15),
            FadeOut(pos16),
            FadeOut(centro_mediana),
            FadeOut(formula_mediana)
        )

        # ====================================================
        # ESCENA 5
        # MEDIANA PARA N IMPAR
        # ====================================================

        titulo_impar = crear_titulo(
            "¿Y SI N ES IMPAR?",
            VERDE,
            38
        )

        self.play(
            FadeIn(titulo_impar)
        )

        explicacion_impar = Text(
            "Quitamos el valor máximo: 30",
            font_size=27,
            color=BLANCO
        )

        explicacion_impar.to_edge(DOWN, buff=0.65)

        self.play(
            FadeIn(explicacion_impar)
        )

        # Encontrar punto 30
        punto_30 = grupos[30][0]

        cruz_30 = Cross(
            punto_30,
            stroke_color=ROJO,
            stroke_width=6,
            scale_factor=0.35
        )

        self.play(
            Create(cruz_30),
            punto_30.animate.set_opacity(0),
            run_time=0.8
        )

        # Nueva mediana: dato 15 = 18
        linea_central_impar = DashedLine(
            punto_18_central.get_center() + DOWN * 0.2,
            punto_18_central.get_center() + UP * 2.1,
            color=VERDE,
            dash_length=0.08
        )

        self.play(
            Create(linea_central_impar),
            Indicate(
                punto_18_central,
                color=VERDE,
                scale_factor=1.5
            ),
            run_time=1
        )

        centro_18 = Text(
            "Dato central: 18",
            font_size=34,
            color=VERDE,
            weight=BOLD
        )

        centro_18.to_edge(
            DOWN,
            buff=0.45
        )

        self.play(
            FadeIn(
                centro_18,
                scale=1.2
            )
        )

        self.wait(2)

        # Restaurar 30
        self.play(
            punto_30.animate.set_opacity(1),
            FadeOut(cruz_30),
            FadeOut(linea_central_impar),
            FadeOut(centro_18),
            FadeOut(explicacion_impar),
            FadeOut(titulo_impar)
        )

        # ====================================================
        # ESCENA 6
        # MEDIA
        # ====================================================

        titulo_media = crear_titulo(
            "MEDIA",
            AZUL,
            44
        )

        self.play(
            FadeIn(titulo_media)
        )

        explicacion_media = Text(
            "El punto de equilibrio de los datos",
            font_size=27,
            color=BLANCO
        )

        explicacion_media.to_edge(DOWN, buff=0.6)

        self.play(
            FadeIn(explicacion_media)
        )

        # ====================================================
        # DESTELLOS SOBRE LOS DATOS
        # ====================================================

        for punto in puntos:

            self.play(
                Indicate(
                    punto,
                    color=AZUL,
                    scale_factor=1.15
                ),
                run_time=0.035
            )

        # Fórmula
        formula_media = MathTex(
            r"\bar{x} = \frac{\sum x_i}{n}",
            font_size=36,
            color=AZUL
        )
       

        formula_media.to_edge(DOWN, buff=1.0)

        self.play(
            Write(formula_media),
            run_time=0.9
        )

        # Suma
        suma_texto = MathTex(
            r"\sum x_i = 587",
            font_size=25,
            color=AMARILLO
        )

        suma_texto.next_to(
            formula_media,
            DOWN,
            buff=0.28
        )

        self.play(
            FadeIn(
                suma_texto,
                shift=UP
            )
        )

        # ====================================================
        # FULCRO
        # ====================================================

        # Posición aproximada de 19.57
        x_media = linea.n2p(media)

        fulcro = Triangle(
            color=AZUL,
            fill_color=AZUL,
            fill_opacity=0.9
        )

        fulcro.scale(0.3)

        fulcro.move_to(
            x_media + DOWN * 0.55
        )

        fulcro.rotate(
            PI
        )

        barra_equilibrio = Line(
            linea.n2p(14) + UP * 0.05,
            linea.n2p(30) + UP * 0.05,
            color=BLANCO,
            stroke_width=5
        )

        self.play(
            Create(barra_equilibrio),
            FadeIn(fulcro),
            run_time=1
        )

        etiqueta_media = MathTex(
            r"\bar{x} = 19.57",
            font_size=31,
            color=AZUL

        )

        etiqueta_media.next_to(
            fulcro,
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(
                etiqueta_media,
                shift=UP
            )
        )

        self.wait(2)

        # ====================================================
        # ESCENA 7
        # VALORES EXTREMOS
        # ====================================================

        self.play(
            FadeOut(explicacion_media),
            FadeOut(formula_media),
            FadeOut(suma_texto),
            run_time=0.6
        )

        extremos_titulo = Text(
            "¿Qué pasa con los extremos?",
            font_size=31,
            color=ROJO,
            weight=BOLD
        )

        extremos_titulo.to_edge(
            UP,
            buff=0.65
        )

        self.play(
            Transform(
                titulo_media,
                extremos_titulo
            )
        )

        extremos = [27, 28, 30]

        puntos_extremos = VGroup()

        for valor in extremos:

            for punto in grupos[valor]:

                puntos_extremos.add(punto)

        # Resaltar extremos
        self.play(
            LaggedStart(
                *[
                    Indicate(
                        punto,
                        color=ROJO,
                        scale_factor=1.6
                    )
                    for punto in puntos_extremos
                ],
                lag_ratio=0.25
            ),
            run_time=1.5
        )

        etiqueta_extremos = MathTex(
            r"27 & 28 & 30",
            font_size=31,
            color=ROJO
            
        )

        etiqueta_extremos.to_edge(DOWN, buff=0.9)

        self.play(
            FadeIn(etiqueta_extremos)
        )

        # ====================================================
        # DESPLAZAR FULCRO
        # ====================================================

        # Posición visual ligeramente hacia la derecha
        nuevo_fulcro = fulcro.copy()

        nuevo_fulcro.shift(
            RIGHT * 0.7
        )

        nueva_etiqueta = MathTex(
            r"\text{La media se desplaza } \rightarrow",
            font_size=27,
            color=ROJO
        )

        nueva_etiqueta.to_edge(
            DOWN,
            buff=1.0
        )

        self.play(
            Transform(
                fulcro,
                nuevo_fulcro
            ),
            Transform(
                etiqueta_media,
                nueva_etiqueta
            ),
            run_time=1.2
        )

        # Mediana permanece
        linea_mediana_fija = DashedLine(
            linea.n2p(18) + DOWN * 0.1,
            linea.n2p(18) + UP * 2,
            color=VERDE,
            dash_length=0.08
        )

        etiqueta_mediana_fija = MathTex(
            r"\text{Mediana} = 18.5",
            font_size=25,
            color=VERDE
        )

        etiqueta_mediana_fija.next_to(
            linea_mediana_fija,
            UP,
            buff=0.15
        )

        self.play(
            Create(linea_mediana_fija),
            FadeIn(etiqueta_mediana_fija)
        )

        # Moda permanece
        moda_fija = MathTex(
            r"\text{Mo} = 18",
            font_size=25,
            color=AMARILLO
        )

        moda_fija.to_edge(DOWN, buff=0.9)
        moda_fija.shift(LEFT * 2.5)

        self.play(
            FadeIn(moda_fija)
        )

        self.wait(2)

        # ====================================================
        # MENSAJE CONCEPTUAL
        # ====================================================

        self.play(
            FadeOut(etiqueta_media),
            run_time=0.4
        )

        mensaje = MathTex(
            r"\text{¡Los extremos afectan la media!}",
            font_size=34,
            color=ROJO
    
        )

        mensaje.to_edge(
            DOWN,
            buff=0.55
        )

        self.play(
            Transform(
                etiqueta_extremos,
                mensaje
            )
        )

        self.wait(2)

        # ====================================================
        # ESCENA FINAL
        # ====================================================

        grupo_final = VGroup(
            linea,
            puntos,
            barra_equilibrio,
            fulcro,
            linea_mediana_fija
        )

        self.play(
            FadeOut(grupo_final),
            FadeOut(moda_fija),
            FadeOut(etiqueta_mediana_fija),
            FadeOut(etiqueta_media),
            FadeOut(etiqueta_extremos),
            run_time=1
        )

        pregunta_final = Text(
            "¿MEDIA O MEDIANA?",
            font_size=52,
            color=AMARILLO,
            weight=BOLD
        )

        pregunta_final.move_to(
            UP * 1.5
        )

        contexto_final = Text(
            "Imagina una empresa donde\nel jefe es millonario...",
            font_size=29,
            color=BLANCO,
            line_spacing=0.9
        )

        contexto_final.move_to(
            DOWN * 0.3
        )

        comentario = Text(
            "¿Cuál usarías? ↓",
            font_size=35,
            color=AZUL,
            weight=BOLD
        )

        comentario.move_to(
            DOWN * 2.2
        )

        self.play(
            Write(pregunta_final),
            run_time=0.8
        )

        self.play(
            FadeIn(
                contexto_final,
                shift=UP
            )
        )

        self.play(
            FadeIn(
                comentario,
                shift=UP
            )
        )

        self.wait(3)