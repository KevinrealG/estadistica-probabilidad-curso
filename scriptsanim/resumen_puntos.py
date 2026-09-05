from manim import *

class ResumenCincoPuntos(Scene):
    def construct(self):
        # Título
        titulo = Text("El Resumen de 5 Puntos", font_size=45, color=YELLOW).to_edge(UP)
        
        # Aclaración (Entre el título y el gráfico)
        nota_extremos = Text("* Nota: Los extremos (mín. y máx.) dentro de los bigotes excluyen a los outliers.", 
                             font_size=24, color=RED_B).next_to(titulo, DOWN, buff=0.5)

        # Eje
        eje = NumberLine(x_range=[0, 10, 1], length=12).shift(DOWN * 1.5)
        
        # Animación inicial secuencial
        self.play(Write(titulo))
        self.play(Write(nota_extremos), run_time=1.5)
        self.play(Create(eje))

        # Geometría base del Boxplot estático
        q1, med, q3 = 3, 5, 7.5
        y_box = UP * 1
        
        caja = Rectangle(width=eje.n2p(q3)[0] - eje.n2p(q1)[0], height=1.5, color=BLUE, fill_opacity=0.3).move_to(eje.n2p((q1+q3)/2) + y_box)
        mediana = Line(caja.get_bottom(), caja.get_top(), color=YELLOW, stroke_width=5)
        
        bigote_izq = Line(eje.n2p(1) + y_box, caja.get_left(), color=WHITE)
        bigote_der = Line(caja.get_right(), eje.n2p(9) + y_box, color=WHITE)
        tick_izq = Line(UP*0.4, DOWN*0.4).move_to(bigote_izq.get_start())
        tick_der = Line(UP*0.4, DOWN*0.4).move_to(bigote_der.get_end())

        self.play(Create(caja), Create(mediana), Create(bigote_izq), Create(bigote_der), Create(tick_izq), Create(tick_der))

        # Coordenadas y textos de los 5 puntos clave
        puntos_info = [
            (tick_izq.get_center(), "1. Mínimo"),
            (caja.get_bottom() + LEFT*(caja.width/2), "2. Cuartil 1 (Q1)"),
            (mediana.get_bottom(), "3. Mediana"),
            (caja.get_bottom() + RIGHT*(caja.width/2), "4. Cuartil 3 (Q3)"),
            (tick_der.get_center(), "5. Máximo")
        ]

        # Animación secuencial de etiquetas
        for pos, texto in puntos_info:
            dot = Dot(pos, color=RED, radius=0.15)
            label = Text(texto, font_size=28).next_to(pos, DOWN, buff=1.5)
            flecha = Arrow(label.get_top(), dot.get_bottom(), buff=0.1, color=RED)
            
            self.play(FadeIn(dot, scale=0.5), GrowArrow(flecha), Write(label), run_time=1.5)
            self.wait(1)
        
        self.wait(3)