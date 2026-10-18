from manim import *

class BaseballBoxplot(Scene):
    def construct(self):
        # 1. Preparar elementos visuales
        
        # Fondo oscuro (Manim usa fondo negro por defecto, ideal para este caso)
        
        # Título superior
        title = Text("Porcentaje de Embasado (OBP)", font_size=36, color=BLUE_C)
        title.to_edge(UP)

        # Función auxiliar para crear Boxplots rápidamente
        def make_boxplot(center_pos, box_h, median_offset, w_top, w_bot, color, label_str):
            box = Rectangle(height=box_h, width=1.2, color=color).move_to(center_pos)
            median = Line(box.get_left(), box.get_right(), color=WHITE).shift(UP * median_offset)
            
            top_line = Line(box.get_top(), box.get_top() + UP * w_top, color=color)
            top_cap = Line(LEFT*0.25, RIGHT*0.25, color=color).move_to(top_line.get_end())
            
            bot_line = Line(box.get_bottom(), box.get_bottom() + DOWN * w_bot, color=color)
            bot_cap = Line(LEFT*0.25, RIGHT*0.25, color=color).move_to(bot_line.get_end())
            
            label = Text(label_str, font_size=28, color=WHITE).next_to(bot_cap, DOWN, buff=0.5)
            
            return VGroup(box, median, top_line, top_cap, bot_line, bot_cap, label)

        # Jugador A (Ej: Muy consistente, caja pequeña)
        boxplot_A = make_boxplot(LEFT * 3 + DOWN * 0.5, box_h=1.5, median_offset=0.2, w_top=0.8, w_bot=0.8, color=YELLOW, label_str="Jugador A")
        
        # Jugador B (Ej: Muy variable, caja grande pero mediana más alta)
        boxplot_B = make_boxplot(RIGHT * 3 + DOWN * 0.5, box_h=3.0, median_offset=0.8, w_top=1.5, w_bot=1.0, color=RED_C, label_str="Jugador B")

        # Pregunta final
        question = Text("¿A quién contratas?", font_size=42, color=GREEN_C)
        question.to_edge(DOWN).shift(UP * 0.5)

        # 2. ANIMACIÓN Y CONTROL DE TIEMPO (Total: 8.0 segundos)
        
        # [0.0s - 2.0s] Aparece el contexto del problema (OBP)
        self.play(Write(title), run_time=2.0)
        
        # [2.0s - 4.0s] Aparecen los Boxplots de ambos jugadores simultáneamente
        self.play(
            Create(boxplot_A), 
            Create(boxplot_B), 
            run_time=2.0
        )
        
        # [4.0s - 5.0s] Escribe la pregunta clave que hace de gancho
        self.play(Write(question), run_time=1.0)
        
        # [5.0s - 8.0s] Pausa para leer y pensar (y para escuchar el "batacazo" en edición)
        self.wait(3.0)
        
        # Suma total: 2.0 + 2.0 + 1.0 + 3.0 = 8.0 segundos exactos.