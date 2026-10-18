from manim import *
import random
CYAN = "#00FFFF"
MAGENTA = "#FF00FF"
class CyberpunkBoxplot(Scene):
    def construct(self):
        # 1. Preparar elementos visuales
        numbers = VGroup()
        for i in range(7):
            for j in range(5):
                num = Text(str(random.randint(0, 9)), color=GREEN, font_size=36)
                num.move_to(RIGHT * (i - 3) + UP * (j - 2))
                numbers.add(num)
        
        box = Rectangle(height=2, width=1, color=CYAN)
        median = Line(LEFT*0.5, RIGHT*0.5, color=MAGENTA).move_to(box.get_center() + UP*0.2)
        whisker_top_line = Line(box.get_top(), box.get_top() + UP*1, color=CYAN)
        whisker_top_cap = Line(LEFT*0.2, RIGHT*0.2, color=CYAN).move_to(whisker_top_line.get_end())
        whisker_bottom_line = Line(box.get_bottom(), box.get_bottom() + DOWN*1, color=CYAN)
        whisker_bottom_cap = Line(LEFT*0.2, RIGHT*0.2, color=CYAN).move_to(whisker_bottom_line.get_end())
        
        boxplot = VGroup(box, median, whisker_top_line, whisker_top_cap, whisker_bottom_line, whisker_bottom_cap)
        boxplot.scale(1.5).move_to(UP * 0.5)

        texto = Text("Leer como un Profesional", font_size=40, color=MAGENTA)
        texto.to_edge(DOWN)

        # 2. ANIMACIÓN Y CONTROL DE TIEMPO (Total: 10.0 segundos)
        
        # [0.0s - 2.0s] Aparece la matriz de números lentamente
        self.play(FadeIn(numbers, shift=DOWN), run_time=2.0)
        
        # [2.0s - 3.0s] Pausa de suspenso
        self.wait(1.0)
        
        # [3.0s - 5.0s] Transformación al Boxplot
        self.play(Transform(numbers, boxplot), run_time=2.0)
        
        # [5.0s - 6.0s] Aparece el texto principal
        self.play(Write(texto), run_time=1.0)
        
        # [6.0s - 10.0s] Tiempo de lectura y visualización en pantalla
        self.wait(4.0)
        
        # Suma total: 2.0 + 1.0 + 2.0 + 1.0 + 4.0 = 10.0 segundos exactos.