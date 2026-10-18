from manim import *
CYAN = "#00FFFF"
MAGENTA = "#FF00FF"
class ExplicacionIQR(Scene):
    def construct(self):
        # 1. Preparar elementos visuales
        
        # Recrear el Boxplot del Jugador A (caja angosta) en el centro
        box_h = 1.5
        box = Rectangle(height=box_h, width=1.2, color=YELLOW).move_to(ORIGIN)
        median = Line(box.get_left(), box.get_right(), color=WHITE).shift(UP * 0.2)
        
        top_line = Line(box.get_top(), box.get_top() + UP * 0.8, color=YELLOW)
        top_cap = Line(LEFT*0.25, RIGHT*0.25, color=YELLOW).move_to(top_line.get_end())
        
        bot_line = Line(box.get_bottom(), box.get_bottom() + DOWN * 0.8, color=YELLOW)
        bot_cap = Line(LEFT*0.25, RIGHT*0.25, color=YELLOW).move_to(bot_line.get_end())
        
        boxplot_A = VGroup(box, median, top_line, top_cap, bot_line, bot_cap)
        
        # Elementos de resalte (caja remarcada con un brillo "tecnológico")
        box_highlight = Rectangle(height=box_h, width=1.2, color=CYAN)
        box_highlight.move_to(ORIGIN).set_fill(CYAN, opacity=0.3)
        
        # Texto "Caja (IQR)"
        text_iqr = Text("Caja (IQR)", font_size=36, color=CYAN).next_to(box, LEFT, buff=1.0)
        arrow_iqr = Arrow(text_iqr.get_right(), box.get_left(), color=CYAN)
        
        # Calibrador (Caliper) midiendo la altura de la caja (representando el escáner)
        caliper_top = Line(box.get_top() + RIGHT*0.8, box.get_top() + RIGHT*2.0, color=WHITE)
        caliper_bot = Line(box.get_bottom() + RIGHT*0.8, box.get_bottom() + RIGHT*2.0, color=WHITE)
        caliper_measurer = DoubleArrow(caliper_bot.get_center(), caliper_top.get_center(), color=GREEN_C, buff=0)
        
        # Texto "Angosta = Consistente"
        text_consistente = Text("Angosta = Consistente", font_size=42, color=GREEN_C).to_edge(DOWN).shift(UP*0.5)

        # 2. ANIMACIÓN Y CONTROL DE TIEMPO (Total: 8.0 segundos)
        
        # [0.0s - 1.0s] Aparece el Boxplot del Jugador A (como si viniera de la escena anterior)
        self.play(FadeIn(boxplot_A), run_time=1.0)
        
        # [1.0s - 2.5s] Se resalta la caja y aparece "Caja (IQR)"
        self.play(
            Create(box_highlight),
            Write(text_iqr),
            GrowArrow(arrow_iqr),
            run_time=1.5
        )
        
        # [2.5s - 4.5s] El "calibrador" aparece midiendo la caja (Aquí iría el sonido de escáner en post)
        self.play(
            Create(caliper_top),
            Create(caliper_bot),
            run_time=0.5
        )
        self.play(
            GrowFromCenter(caliper_measurer),
            run_time=1.5
        )
        
        # [4.5s - 5.5s] Aparece la conclusión: "Angosta = Consistente"
        self.play(Write(text_consistente), run_time=1.0)
        
        # [5.5s - 8.0s] Pausa de asimilación visual para llegar a los 8 segundos
        self.wait(2.5)
        
        # Suma total: 1.0 + 1.5 + 0.5 + 1.5 + 1.0 + 2.5 = 8.0 segundos exactos.