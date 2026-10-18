from manim import *

class ExplicacionAsimetria(Scene):
    def construct(self):
        # 1. Preparar elementos visuales
        
        # Recreamos el Boxplot del Jugador B pero empezará pequeño para simular el zoom
        box = Rectangle(height=4.0, width=2.0, color=RED_C)
        median = Line(box.get_left(), box.get_right(), color=WHITE)
        
        top_line = Line(box.get_top(), box.get_top() + UP * 1.5, color=RED_C)
        top_cap = Line(LEFT*0.5, RIGHT*0.5, color=RED_C).move_to(top_line.get_end())
        
        bot_line = Line(box.get_bottom(), box.get_bottom() + DOWN * 1.0, color=RED_C)
        bot_cap = Line(LEFT*0.5, RIGHT*0.5, color=RED_C).move_to(bot_line.get_end())
        
        boxplot_B = VGroup(box, median, top_line, top_cap, bot_line, bot_cap)
        boxplot_B.move_to(ORIGIN)
        
        # Empezamos con una escala del 10% para luego hacer "zoom in" (escala al 100%)
        boxplot_B.scale(0.1)
        
        # Textos auxiliares
        text_mediana = Text("Mediana", font_size=32, color=YELLOW)
        texto_sesgo = Text("Mediana descentrada = Asimetría (Sesgo)", font_size=40, color=RED_A)
        texto_sesgo.to_edge(DOWN).shift(UP * 0.5)

        # 2. ANIMACIÓN Y CONTROL DE TIEMPO (Total: 19.0 segundos)
        
        # [0.0s - 2.0s] Hacemos zoom a la caja del Jugador B
        self.play(boxplot_B.animate.scale(10), run_time=2.0)
        
        # [2.0s - 4.0s] Explicación: "La línea del centro es la Mediana"
        text_mediana.next_to(median, RIGHT, buff=0.5)
        self.play(
            median.animate.set_color(YELLOW).set_stroke(width=6), 
            Write(text_mediana), 
            run_time=2.0
        )
        
        # [4.0s - 6.0s] Pausa para locución ("Si no está exactamente en el medio...")
        self.wait(2.0)
        
        # [6.0s - 7.0s] Movimiento brusco de la mediana hacia abajo (Aquí va el corte metálico)
        # La movemos drásticamente cerca del cuartil inferior (fondo de la caja)
        new_median_pos = box.get_bottom() + UP * 0.8
        self.play(
            median.animate.move_to(new_median_pos),
            FadeOut(text_mediana),
            run_time=1.0
        )
        
        # [7.0s - 9.0s] Tiñendo el área superior de rojo ("...¡hay sesgo!")
        # Calculamos la altura y el centro exacto del área que quedó por encima de la nueva mediana
        upper_height = box.get_top()[1] - new_median_pos[1]
        upper_center_y = (box.get_top()[1] + new_median_pos[1]) / 2
        
        upper_area = Rectangle(
            width=1.9, 
            height=upper_height - 0.05, 
            fill_color=RED_E, 
            fill_opacity=0.7, 
            stroke_width=0
        )
        upper_area.move_to(UP * upper_center_y)
        
        self.play(FadeIn(upper_area), run_time=2.0)
        
        # [9.0s - 11.0s] Aparece la conclusión en texto
        self.play(Write(texto_sesgo), run_time=2.0)
        
        # [11.0s - 19.0s] Pausa de visualización e interiorización ("Indica rachas inusuales hacia un extremo")
        self.wait(8.0)
        
        # Suma total: 2.0 + 2.0 + 2.0 + 1.0 + 2.0 + 2.0 + 8.0 = 19.0 segundos exactos.