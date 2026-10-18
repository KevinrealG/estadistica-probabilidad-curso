from manim import *

class ComparacionAplicacion(Scene):
    def construct(self):
        # 1. Preparar elementos visuales
        
        # Pantalla dividida
        split_line = DashedLine(UP * 4, DOWN * 4, color=GRAY, dashed_ratio=0.5)
        
        # Función auxiliar para Boxplots
        def make_boxplot(center_pos, box_h, box_w, median_offset, w_top, w_bot, color):
            box = Rectangle(height=box_h, width=box_w, color=color).move_to(center_pos)
            median = Line(box.get_left(), box.get_right(), color=WHITE).shift(UP * median_offset)
            
            top_line = Line(box.get_top(), box.get_top() + UP * w_top, color=color)
            top_cap = Line(LEFT*(box_w/3), RIGHT*(box_w/3), color=color).move_to(top_line.get_end())
            
            bot_line = Line(box.get_bottom(), box.get_bottom() + DOWN * w_bot, color=color)
            bot_cap = Line(LEFT*(box_w/3), RIGHT*(box_w/3), color=color).move_to(bot_line.get_end())
            
            return VGroup(box, median, top_line, top_cap, bot_line, bot_cap)

        # Jugador A (Izquierda): Máquina predecible, sólido, verde, angosto
        boxplot_A = make_boxplot(LEFT * 3.5, box_h=1.2, box_w=0.8, median_offset=0.1, w_top=0.6, w_bot=0.6, color=GREEN)
        
        # Jugador B (Derecha): Inestable, gigante, sesgado, rojo, ancho
        boxplot_B = make_boxplot(RIGHT * 3.5, box_h=3.5, box_w=1.8, median_offset=1.0, w_top=1.5, w_bot=0.5, color=RED)
        
        # Textos en pantalla
        text_A = Text('"A" = Predecible', font_size=36, color=GREEN).move_to(LEFT * 3.5 + DOWN * 3)
        text_B = Text('"B" = Inestable', font_size=36, color=RED).move_to(RIGHT * 3.5 + DOWN * 3)
        
        # Check (marca de verificación) dibujado manualmente para evitar errores de fuentes
        check_mark = VGroup(
            Line(LEFT*0.3 + UP*0.1, LEFT*0.05 + DOWN*0.2, color=GREEN_C, stroke_width=8),
            Line(LEFT*0.05 + DOWN*0.2, RIGHT*0.4 + UP*0.5, color=GREEN_C, stroke_width=8)
        ).next_to(boxplot_A, UP, buff=0.8)

        # 2. ANIMACIÓN Y CONTROL DE TIEMPO (Total: 19.0 segundos)
        
        # [0.0s - 2.0s] Aparece la pantalla dividida y ambos boxplots
        self.play(
            Create(split_line),
            FadeIn(boxplot_A, shift=UP),
            FadeIn(boxplot_B, shift=UP),
            run_time=2.0
        )
        
        # [2.0s - 4.0s] Escribe texto de B y B empieza a temblar (Wiggle)
        self.play(
            Write(text_B),
            Wiggle(boxplot_B, scale_value=1.1, rotation_angle=0.05),
            run_time=2.0
        )
        
        # [4.0s - 7.0s] B sigue temblando mientras locución enfatiza la inestabilidad
        self.play(
            Wiggle(boxplot_B, scale_value=1.15, rotation_angle=0.08),
            run_time=3.0
        )
        
        # [7.0s - 9.0s] Aparece el texto del Jugador A (A se mantiene sólido y calmado)
        self.play(Write(text_A), run_time=2.0)
        
        # [9.0s - 10.0s] Aparece el Check gigante sobre A (Aquí va el sonido de "Confirmación pesada")
        self.play(Create(check_mark), run_time=1.0)
        
        # [10.0s - 19.0s] Pausa larga de cierre visual para llegar a los 19 segundos exactos
        self.wait(9.0)
        
        # Suma total: 2.0 + 2.0 + 3.0 + 2.0 + 1.0 + 9.0 = 19.0 segundos exactos.