from manim import *

# Forzar resolución y proporción vertical (9:16) para Reels / TikTok / Shorts
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0

class ImpactoOrdenBateVertical(Scene):
    def construct(self):
        # ==========================================
        # FASE 1: VOLUMEN (PA/J)
        # ==========================================
        # Título adaptado a multi-línea para vertical
        title_vol = Text("1. Apariciones al Plato (PA/J) - MLB 2026", font_size=42, weight=BOLD)
        title_vol.to_edge(UP, buff=1)
        
        etiquetas_pa = ["1.º Bate", "2.º Bate", "3.er Bate", "4.º Bate"]
        valores_pa = [4.60, 4.41, 4.31, 4.18]
        colores_pa = [BLUE_D, BLUE_C, BLUE_B, BLUE_A]
        
        grupo_barras_pa = VGroup()
        
        # Posicionamiento en cascada
        for i in range(4):
            # Etiqueta arriba de la barra para ahorrar espacio horizontal
            lbl = Text(etiquetas_pa[i], font_size=32).move_to(LEFT * 3.5 + UP * (4 - i*2.2)).align_to(LEFT * 3.5, LEFT)
            
            # Longitud calculada
            longitud_visual = (valores_pa[i] - 3.5) * 6 
            
            barra = Rectangle(width=longitud_visual, height=0.6, color=colores_pa[i], fill_opacity=1)
            barra.next_to(lbl, DOWN, buff=0.2, aligned_edge=LEFT)
            
            val_text = Text(str(valores_pa[i]), font_size=32).next_to(barra, RIGHT, buff=0.3)
            
            grupo_barras_pa.add(VGroup(lbl, barra, val_text))
            
        self.play(Write(title_vol))
        
        for item in grupo_barras_pa:
            self.play(
                FadeIn(item[0], shift=DOWN*0.5), 
                GrowFromEdge(item[1], LEFT), 
                Write(item[2]), 
                run_time=0.7
            )
        self.wait(2.5)

        # ==========================================
        # FASE 2: EFICIENCIA (OBP)
        # ==========================================
        self.play(FadeOut(grupo_barras_pa))
        
        title_eff = Text("2. Eficiencia:\nPorcentaje de Embasarse", font_size=42, weight=BOLD)
        title_eff.to_edge(UP, buff=1)
        
        self.play(ReplacementTransform(title_vol, title_eff))
        
        etiquetas_obp = ["Shohei Ohtani (1.º)", "Juan Soto (2.º)"]
        valores_obp = [0.390, 0.419]
        colores_obp = [BLUE_D, GREEN_D]
        
        grupo_barras_obp = VGroup()
        
        for i in range(2):
            lbl = Text(etiquetas_obp[i], font_size=32).move_to(LEFT * 3.5 + UP * (2 - i*2.5)).align_to(LEFT * 3.5, LEFT)
            longitud_visual = valores_obp[i] * 16 # Ajuste de escala vertical
            
            barra = Rectangle(width=longitud_visual, height=0.8, color=colores_obp[i], fill_opacity=1)
            barra.next_to(lbl, DOWN, buff=0.3, aligned_edge=LEFT)
            
            val_text = Text(str(valores_obp[i]), font_size=32).next_to(barra, RIGHT, buff=0.3)
            
            grupo_barras_obp.add(VGroup(lbl, barra, val_text))
            
        for item in grupo_barras_obp:
            self.play(FadeIn(item[0], shift=DOWN*0.5), GrowFromEdge(item[1], LEFT), Write(item[2]), run_time=1)
            
        self.wait(2.5)

        # ==========================================
        # FASE 3: PRODUCCIÓN (CARRERAS)
        # ==========================================
        self.play(FadeOut(grupo_barras_obp))
        
        title_prod = Text("3. Producción:\nEl Motor de Carreras", font_size=42, weight=BOLD)
        title_prod.to_edge(UP, buff=1)
        self.play(ReplacementTransform(title_eff, title_prod))
        
        # Ecuación apilada verticalmente para móvil
        ecuacion = VGroup(
            Text("Volumen (PA)", font_size=45, color=BLUE_C),
            MathTex(r"\times", font_size=60),
            Text("Eficiencia (OBP)", font_size=45, color=GREEN_C),
            MathTex(r"=", font_size=60),
            Text("Carreras", font_size=55, color=YELLOW)
        ).arrange(DOWN, buff=0.4).move_to(UP * 2.5)
        
        self.play(Write(ecuacion), run_time=2)
        self.wait(1)
        
        self.play(ecuacion.animate.scale(0.5).to_edge(UP, buff=2.5).set_opacity(0.5))
        
        # Dashboards Apilados Verticalmente
        def crear_tarjeta(nombre, stats, carreras, color_tema, pos_y):
            tarjeta = VGroup()
            n = Text(nombre, font_size=36, color=color_tema).move_to(UP * pos_y)
            s = Text(stats, font_size=24, color=GRAY).next_to(n, DOWN, buff=0.2)
            c_lbl = Text("ANOTADAS", font_size=20, color=color_tema).next_to(s, DOWN, buff=0.5)
            c_val = Text(carreras, font_size=70, color=color_tema, weight=BOLD).next_to(c_lbl, DOWN, buff=0.2)
            
            # Forzar que ambos recuadros tengan el mismo ancho
            box = SurroundingRectangle(VGroup(n, c_val), color=color_tema, fill_color=BLACK, fill_opacity=0.8, buff=0.5)
            box.stretch_to_fit_width(7.5) 
            
            tarjeta.add(box, n, s, c_lbl, c_val)
            return tarjeta, box, n, s, c_lbl, c_val

        tarjeta_ohtani, box_o, n_o, s_o, c_lbl_o, c_val_o = crear_tarjeta("Ohtani (1.º)", "731 PA | .390 OBP", "134", BLUE_D, -1)
        tarjeta_soto, box_s, n_s, s_s, c_lbl_s, c_val_s = crear_tarjeta("Soto (2.º)", "713 PA | .419 OBP", "128", GREEN_D, -4.5)
        
        self.play(Create(box_o), Create(box_s), run_time=1)
        self.play(Write(n_o), Write(n_s), Write(s_o), Write(s_s))
        
        self.play(FadeIn(c_lbl_o, shift=UP), FadeIn(c_lbl_s, shift=UP))
        self.play(
            FadeIn(c_val_o, scale=0.3), 
            FadeIn(c_val_s, scale=0.3), 
            run_time=1.5
        )
        
        self.play(Circumscribe(c_val_o, color=YELLOW, time_width=2), Circumscribe(c_val_s, color=YELLOW, time_width=2))
        
        self.wait(3)