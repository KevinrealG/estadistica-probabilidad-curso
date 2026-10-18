from manim import *
CYAN = "#00FFFF"
MAGENTA = "#FF00FF"

class ExplicacionOutliers(Scene):
    def construct(self):
        # 1. Preparar elementos visuales
        
        # Base del Boxplot del Jugador B (La caja y la mediana descentrada de la escena anterior)
        # Lo posicionamos un poco más abajo para dar espacio al outlier en la parte superior
        box = Rectangle(height=2.5, width=1.5, color=RED_C).move_to(DOWN * 1.5)
        median = Line(box.get_left(), box.get_right(), color=YELLOW).shift(DOWN * 2.2) 
        
        boxplot_base = VGroup(box, median)
        
        # Bigotes (Whiskers)
        # Bigote superior
        top_line = Line(box.get_top(), box.get_top() + UP * 2.0, color=RED_C)
        top_cap = Line(LEFT*0.4, RIGHT*0.4, color=RED_C).move_to(top_line.get_end())
        
        # Bigote inferior
        bot_line = Line(box.get_bottom(), box.get_bottom() + DOWN * 1.0, color=RED_C)
        bot_cap = Line(LEFT*0.4, RIGHT*0.4, color=RED_C).move_to(bot_line.get_end())
        
        whiskers = VGroup(top_line, top_cap, bot_line, bot_cap)
        
        # Llave y texto indicando el cálculo del límite (1.5 x IQR)
        brace_top = Brace(top_line, direction=RIGHT, color=CYAN)
        text_15iqr = brace_top.get_tex("1.5 \\times IQR").set_color(CYAN)
        
        # Outlier (Punto atípico muy por encima del bigote superior)
        outlier = Dot(point=top_line.get_end() + UP * 1.5, radius=0.15, color=GREEN_C)
        
        # Texto inferior destacado
        texto_outlier = Text("Outlier: Fuera de 1.5×IQR", font_size=40, color=GREEN_C)
        texto_outlier.to_edge(DOWN).shift(UP * 0.5)

        # 2. ANIMACIÓN Y CONTROL DE TIEMPO (Total: 21.0 segundos)
        
        # [0.0s - 1.0s] Aparece la caja base del Jugador B
        self.play(FadeIn(boxplot_base), run_time=1.0)
        
        # [1.0s - 4.0s] Trazado de los bigotes y aparición de la llave "1.5xIQR"
        # (Aquí va el efecto de "Trazado láser" en edición)
        self.play(
            Create(whiskers),
            GrowFromCenter(brace_top),
            Write(text_15iqr),
            run_time=3.0
        )
        
        # [4.0s - 7.0s] Pausa para la locución ("Los bigotes limitan lo predecible...")
        self.wait(3.0)
        
        # [7.0s - 8.0s] Aparece el Outlier de forma sorpresiva 
        # (Aquí va el sonido de "Bloop de alerta" en edición)
        self.play(GrowFromCenter(outlier), run_time=1.0)
        
        # [8.0s - 10.0s] El Outlier brilla o palpita ("¡Un punto fuera de ellos...!")
        self.play(Indicate(outlier, color=GREEN_E, scale_factor=1.5), run_time=2.0)
        
        # [10.0s - 12.0s] Escribe la conclusión en pantalla
        self.play(Write(texto_outlier), run_time=2.0)
        
        # [12.0s - 21.0s] Pausa larga de asimilación ("¡Un partido atípico extraordinario o desastroso!")
        # Rellena el resto del tiempo hasta llegar a los 21 segundos
        self.wait(9.0)
        
        # Suma total: 1.0 + 3.0 + 3.0 + 1.0 + 2.0 + 2.0 + 9.0 = 21.0 segundos exactos.