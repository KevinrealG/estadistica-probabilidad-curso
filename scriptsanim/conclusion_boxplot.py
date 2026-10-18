from manim import *
CYAN = "#00FFFF"
MAGENTA = "#FF00FF"
class ConclusionBoxplot(Scene):
    def construct(self):
        # 1. Preparar elementos visuales
        titulo = Text("En conclusión, un Boxplot sirve para:", font_size=40, color=CYAN)
        titulo.to_edge(UP, buff=1.0)

        # Puntos del resumen
        p1 = Text("1. Medir consistencia y homogeneidad", font_size=32)
        p2 = Text("2. Identificar valores atípicos (outliers)", font_size=32)
        p3 = Text("3. Evaluar la simetría (sesgo)", font_size=32)
        p4 = Text("4. Comparar grupos fácilmente", font_size=32)

        # Agrupar y alinear a la izquierda
        lista = VGroup(p1, p2, p3, p4).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        lista.next_to(titulo, DOWN, buff=1.0)

        # Caja decorativa final para encerrar el resumen
        caja_resumen = SurroundingRectangle(lista, color=YELLOW, buff=0.4)

        # 2. ANIMACIÓN Y CONTROL DE TIEMPO (Total: 30.0 segundos)
        
        # [0.0s - 2.0s] Aparece el título
        self.play(Write(titulo), run_time=2.0)
        
        # [2.0s - 5.0s] Punto 1 y pausa
        self.play(FadeIn(p1, shift=RIGHT), run_time=1.0)
        self.wait(2.0)
        
        # [5.0s - 8.0s] Punto 2 y pausa
        self.play(FadeIn(p2, shift=RIGHT), run_time=1.0)
        self.wait(2.0)
        
        # [8.0s - 11.0s] Punto 3 y pausa
        self.play(FadeIn(p3, shift=RIGHT), run_time=1.0)
        self.wait(2.0)
        
        # [11.0s - 14.0s] Punto 4 y pausa
        self.play(FadeIn(p4, shift=RIGHT), run_time=1.0)
        self.wait(2.0)
        
        # [14.0s - 16.0s] Se dibuja la caja resumen dorada
        self.play(Create(caja_resumen), run_time=2.0)
        
        # [16.0s - 30.0s] Pausa prolongada para lectura, voz en off de cierre y fin del video
        self.wait(14.0)
        
        # Suma total: 2 + (1+2)*4 + 2 + 14 = 30.0 segundos exactos.