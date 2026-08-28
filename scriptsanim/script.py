from manim import *

# El formato 16:9 (1920x1080) es el predeterminado en Manim, 
# por lo que no requerimos forzar la configuración de píxeles al inicio.

class DispersionHorizontal(Scene):
    def construct(self):
        # 1. HOOK: El Engaño del Promedio
        titulo = Text("¿EL PROMEDIO MIENTE?", font_size=48, color=YELLOW, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(titulo))
        
        # Ejes más anchos y menos separados verticalmente para el lienzo 16:9
        eje_a = NumberLine(x_range=[0, 5, 1], length=10).shift(UP * 1.5)
        eje_b = NumberLine(x_range=[0, 5, 1], length=10).shift(DOWN * 1.5)
        
        puntos_a = VGroup(*[Dot(eje_a.n2p(x), color=GREEN, radius=0.15) for x in [3.3, 3.4, 3.5, 3.6, 3.7]])
        puntos_b = VGroup(*[Dot(eje_b.n2p(x), color=RED, radius=0.15) for x in [1.5, 2.5, 3.5, 4.5, 5.0]])
        
        label_a = Text("Curso A", font_size=30).next_to(eje_a, UP)
        label_b = Text("Curso B", font_size=30).next_to(eje_b, UP)
        
        self.play(Create(eje_a), Create(eje_b), FadeIn(label_a, label_b))
        self.play(FadeIn(puntos_a, shift=DOWN), FadeIn(puntos_b, shift=DOWN))
        
        # Línea de Promedio
        linea_promedio = DashedLine(start=UP*2.5, end=DOWN*2.5, color=WHITE).move_to(eje_a.n2p(3.5) + DOWN*1.5)
        label_prom = Text("Promedio 3.5", font_size=30, color=YELLOW).next_to(linea_promedio, RIGHT)
        self.play(Create(linea_promedio), Write(label_prom))
        self.wait(11)
        
        # 2. RANGO
        self.play(FadeOut(titulo, eje_a, puntos_a, label_a, linea_promedio, label_prom))
        self.play(eje_b.animate.shift(UP * 2), puntos_b.animate.shift(UP * 2), label_b.animate.shift(UP * 2))
        
        llave_rango = Brace(VGroup(puntos_b[0], puntos_b[-1]), DOWN, color=BLUE)
        texto_rango = MathTex(r"Rango = X_{max} - X_{min} = 3.5", font_size=40).next_to(llave_rango, DOWN)
        self.play(GrowFromCenter(llave_rango), Write(texto_rango))
        self.wait(25)
        
        # 3. VARIANZA
        self.play(FadeOut(llave_rango, texto_rango))
        prom_b = Dot(eje_b.n2p(3.5), color=YELLOW, radius=0.15)
        lineas_dist = VGroup(*[Line(prom_b.get_center(), p.get_center(), color=BLUE) for p in puntos_b])
        self.wait(20)
        texto_var = MathTex(r"s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}", font_size=50).next_to(eje_b, DOWN, buff=1.5)
        self.play(FadeIn(prom_b), Create(lineas_dist), Write(texto_var))
        
        cuadrados = VGroup(*[Square(side_length=l.get_length(), color=BLUE_D, fill_opacity=0.5).move_to(l.get_center()) for l in lineas_dist])
        self.play(Transform(lineas_dist, cuadrados))
        self.wait(15)
        lineas_dist_2 = VGroup(*[Line(prom_b.get_center(), p.get_center(), color=BLUE) for p in puntos_b])
        self.play(Transform(cuadrados, lineas_dist_2))
        # 3.5 DESVIACIÓN ESTÁNDAR
        # La fórmula se mete en una raíz cuadrada
        texto_std = MathTex(r"s = \sqrt{s^2}", font_size=50).next_to(eje_b, DOWN, buff=1.5)
        
        # Los cuadrados encogen y vuelven a ser líneas (raíz cuadrada visual)
        self.play(
            ReplacementTransform(texto_var, texto_std)
            
        )
        
        
        self.wait(17)
        
        # Aplicación: Comparación de predictibilidad
        texto_predict_a = Text("En ingeniería o inversiones", font_size=25, color=GREEN).to_corner(DL).shift(UP)
        texto_predict_b = Text("un proceso con baja desviación estándar es predecible y seguro", font_size=25, color=RED).next_to(texto_predict_a, DOWN, aligned_edge=LEFT)
        
        self.play(Write(texto_predict_a), Write(texto_predict_b))
        self.wait(5)
        
        # Limpieza para dar paso al Coeficiente de Variación
        self.play(FadeOut(texto_predict_a, texto_predict_b,texto_std,lineas_dist_2))
        # 4. COEFICIENTE DE VARIACIÓN
        self.play(FadeOut(eje_b, puntos_b, label_b, lineas_dist, prom_b, texto_var))
        
        texto_cv_titulo = Text("¿Elefantes vs Notas?", font_size=45, color=YELLOW).shift(UP * 2.5)
        formula_cv = MathTex(r"CV = \left( \frac{s}{\bar{x}} \right) \times 100\%", font_size=55).next_to(texto_cv_titulo, DOWN, buff=1)
        
        self.play(Write(texto_cv_titulo), Write(formula_cv))
        self.wait(30)
        barra_cv = NumberLine(x_range=[0, 100, 10], length=10, include_numbers=True).shift(DOWN * 1.5)
        zona_verde = Line(barra_cv.n2p(0), barra_cv.n2p(30), color=GREEN, stroke_width=10)
        zona_roja = Line(barra_cv.n2p(30), barra_cv.n2p(100), color=RED, stroke_width=10)
        
        label_homo = Text("< 30% Homogéneo", font_size=30, color=GREEN).next_to(zona_verde, UP)
        label_hetero = Text("> 30% Caos", font_size=30, color=RED).next_to(zona_roja, UP)
        
        self.play(Create(barra_cv))
        self.play(Create(zona_verde), Create(zona_roja))
        self.play(FadeIn(label_homo), FadeIn(label_hetero))
        self.wait(25)
        
        # 5. CIERRE
        self.clear()
        cierre = Text("Si CV = 50%...\n¿Qué significa? 👇", font_size=48,  color=WHITE)
        self.play(Write(cierre))
        self.wait(2)