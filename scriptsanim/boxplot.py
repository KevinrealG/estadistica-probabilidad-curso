from manim import *

class BoxplotHorizontal(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # BLOQUE 1: HOOK (12 segundos)
        # ---------------------------------------------------------
        hook_text = Text("¡No confíes en el promedio!", font_size=55, color=RED, weight=BOLD).shift(UP*2)
        self.play(Write(hook_text), run_time=2)
        self.wait(8)
        self.play(FadeOut(hook_text), run_time=2)

        # ---------------------------------------------------------
        # BLOQUE 2: EL PROBLEMA (12 segundos | Acumulado: 0:24)
        # ---------------------------------------------------------
        title = Text("Tiempos de Carga (ms)", font_size=45).shift(UP*3)
        number_line = NumberLine(
            x_range=[0, 14, 2],
            length=12,
            include_numbers=True
        ).shift(DOWN*1.5)
        
        data = [1, 2, 2.5, 3, 3, 3.5, 4, 4, 4.5, 4.5, 5, 5.5, 6, 7, 8, 12]
        dots = VGroup(*[Dot(number_line.n2p(x), color=LIGHT_GREY, radius=0.15) for x in data])
        
        self.play(Write(title), Create(number_line), run_time=2)
        self.play(LaggedStart(*[FadeIn(dot, shift=DOWN) for dot in dots], lag_ratio=0.1), run_time=4)
        self.wait(6)

        # ---------------------------------------------------------
        # BLOQUE 3: LA CAJA E IQR (25 segundos | Acumulado: 0:49)
        # ---------------------------------------------------------
        q1, median, q3 = 3.25, 4.25, 5.625
        box_width = number_line.n2p(q3)[0] - number_line.n2p(q1)[0]
        
        box = Rectangle(
            width=box_width, height=2, color=BLUE, fill_opacity=0.3
        ).move_to(number_line.n2p((q1+q3)/2) + UP*1.5)
        
        q1_label = MathTex(r"Q_1", font_size=35).next_to(box.get_corner(DL), DOWN)
        q3_label = MathTex(r"Q_3", font_size=35).next_to(box.get_corner(DR), DOWN)
        box_text = Text("Caja: Contiene el 50%\nde los datos", font_size=35, color=BLUE_B).next_to(box, UP, buff=0.5)

        self.play(Create(box), run_time=3)
        self.play(Write(q1_label), Write(q3_label), Write(box_text), run_time=3)
        
        dots_iqr = VGroup(*[d for x, d in zip(data, dots) if q1 <= x <= q3])
        self.play(dots_iqr.animate.set_color(BLUE), run_time=2)
        self.wait(17)

        # ---------------------------------------------------------
        # BLOQUE 4: LA MEDIANA (15 segundos | Acumulado: 1:04)
        # ---------------------------------------------------------
        median_line = Line(box.get_bottom(), box.get_top(), color=YELLOW, stroke_width=6)
        median_label = MathTex(r"\text{Mediana } (\tilde{x})", color=YELLOW, font_size=40).next_to(median_line, UP, buff=1.5)

        self.play(Create(median_line), Write(median_label), run_time=3)
        self.wait(12)

        # ---------------------------------------------------------
        # BLOQUE 5: LOS BIGOTES (42 segundos | Acumulado: 1:46)
        # (El bloque más largo para cubrir tu explicación del 1.5 IQR)
        # ---------------------------------------------------------
        iqr = q3 - q1
        lower_bound = max(0, q1 - 1.5 * iqr)
        upper_bound = q3 + 1.5 * iqr
        
        min_val = min([x for x in data if x >= lower_bound])
        max_val = max([x for x in data if x <= upper_bound])

        whisker_left = Line(box.get_left(), number_line.n2p(min_val) + UP*1.5, color=WHITE)
        whisker_right = Line(box.get_right(), number_line.n2p(max_val) + UP*1.5, color=WHITE)
        tick_left = Line(UP*0.5, DOWN*0.5).move_to(whisker_left.get_start())
        tick_right = Line(UP*0.5, DOWN*0.5).move_to(whisker_right.get_end())
        
        whiskers_text = Text("Bigotes: El rango esperado (1.5x IQR)", font_size=35).next_to(title, DOWN, buff=0.5)

        self.play(FadeOut(box_text), FadeOut(median_label), run_time=2)
        self.play(Create(whisker_left), Create(tick_left), Create(whisker_right), Create(tick_right), run_time=4)
        self.play(Write(whiskers_text), run_time=3)
        self.wait(33)

        # ---------------------------------------------------------
        # BLOQUE 6: EL OUTLIER (22 segundos | Acumulado: 2:08)
        # ---------------------------------------------------------
        outlier_dot = dots[-1] 
        outlier_text = Text("Outlier:\n¡Anomalía!", font_size=40, color=RED, weight=BOLD).next_to(outlier_dot, UP, buff=1.5)
        arrow = Arrow(outlier_text.get_bottom(), outlier_dot.get_top(), color=RED)

        self.play(outlier_dot.animate.set_color(RED).scale(2.5), run_time=2)
        self.play(GrowArrow(arrow), Write(outlier_text), run_time=2)
        
        for _ in range(3):
            self.play(outlier_dot.animate.set_opacity(0.2), run_time=0.5)
            self.play(outlier_dot.animate.set_opacity(1), run_time=0.5)
            
        self.wait(15)

        # ---------------------------------------------------------
        # BLOQUE 7: CIERRE (20 segundos | Acumulado: 2:28)
        # ---------------------------------------------------------
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=3)
        
        cierre_text = Text("Caja pequeña, bigotes largos...\n¿Qué significa para la App?\n\n👇 ¡Comenta! 👇", 
                           font_size=45, color=WHITE)
        self.play(Write(cierre_text), run_time=3)
        self.wait(14)