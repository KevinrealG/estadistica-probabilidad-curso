from manim import *

class ConclusionBoxplot(Scene):
    def construct(self):
        # Configuración del eje base
        number_line = NumberLine(
            x_range=[0, 10, 1],
            length=10,
            color=WHITE,
            include_numbers=False
        ).shift(DOWN * 1)
        
        self.play(Create(number_line))

        # 1. Consistencia u homogeneidad
        # Reemplazamos .c2p por .n2p(x) + UP * y
        box = Rectangle(width=3, height=0.8, color=BLUE, fill_opacity=0.5).move_to(number_line.n2p(5) + UP * 1)
        median = Line(box.get_bottom(), box.get_top(), color=YELLOW, stroke_width=4).move_to(box.get_center())
        whisker_left = Line(number_line.n2p(2) + UP * 1, box.get_left(), color=WHITE)
        whisker_right = Line(box.get_right(), number_line.n2p(8) + UP * 1, color=WHITE)
        
        boxplot_group = VGroup(box, median, whisker_left, whisker_right)
        
        self.play(Create(boxplot_group))
        
        # Efecto visual de consistencia (pulso)
        self.play(box.animate.stretch_to_fit_width(1.5), run_time=1)
        self.play(box.animate.stretch_to_fit_width(3), run_time=1)
        self.wait(20) 

        # 2. Valores Atípicos
        outlier_1 = Dot(number_line.n2p(1) + UP * 1, color=RED)
        outlier_2 = Dot(number_line.n2p(9.5) + UP * 1, color=RED)
        
        self.play(FadeIn(outlier_1, scale=0.5), FadeIn(outlier_2, scale=0.5))
        self.play(Indicate(outlier_1), Indicate(outlier_2), color=YELLOW)
        self.wait(20)

        # 3. Distribución Simétrica o Sesgada
        self.play(FadeOut(outlier_1), FadeOut(outlier_2))
        self.play(
            median.animate.shift(LEFT * 1),
            box.animate.set_color(PURPLE),
            run_time=2
        )
        self.wait(20)

        # 4. Comparar entre dos subgrupos
        self.play(boxplot_group.animate.shift(UP * 1.5))
        
        # Creamos el segundo grupo para comparar
        box2 = Rectangle(width=1.5, height=0.8, color=ORANGE, fill_opacity=0.5).move_to(number_line.n2p(6) + UP * 1)
        median2 = Line(box2.get_bottom(), box2.get_top(), color=YELLOW, stroke_width=4).move_to(box2.get_center())
        whisker_left2 = Line(number_line.n2p(4.5) + UP * 1, box2.get_left(), color=WHITE)
        whisker_right2 = Line(box2.get_right(), number_line.n2p(7.5) + UP * 1, color=WHITE)
        
        boxplot_group2 = VGroup(box2, median2, whisker_left2, whisker_right2)
        
        self.play(Create(boxplot_group2))
        self.wait(20)
        
        # Salida
        self.play(FadeOut(boxplot_group), FadeOut(boxplot_group2), FadeOut(number_line))