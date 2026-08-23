from manim import *

class SabermetriaPA_Perfect(Scene):
    def construct(self):
        # 1. Título
        title = Text("Apariciones al Plato (PA) - MLB 2024", font_size=36, weight=BOLD).to_edge(UP)
        self.play(Write(title))

        # 2. Datos y Parámetros
        names = ["Alonso\n(4to)", "Ozuna\n(4to)", "Soto\n(2do)", "Ohtani\n(1/2)", "Duran\n(1ro)"]
        pas = [695, 688, 713, 731, 735]
        colors = ["#FF5722", "#FF5722", "#00BCD4", "#00BCD4", "#00BCD4"]

        # 3. Plano Cartesiano Preciso (Axes)
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[650, 760, 20],
            x_length=9,
            y_length=4.5,
            axis_config={"include_tip": False}
        )
        axes.add_coordinates(None, np.arange(650, 770, 20))
        
        # 4. Construcción Geométrica de Barras y Etiquetas
        bars = VGroup()
        labels = VGroup()
        values_text = VGroup()

        for i, (name, val, color) in enumerate(zip(names, pas, colors), start=1):
            # Coordenadas matemáticas exactas
            p_bottom = axes.coords_to_point(i, 650)
            p_top = axes.coords_to_point(i, val)
            
            # Dibujo del rectángulo
            bar = Rectangle(
                width=axes.x_axis.unit_size * 0.7,
                height=p_top[1] - p_bottom[1],
                color=color,
                fill_opacity=1.0,
                stroke_width=0
            ).move_to(p_bottom, DOWN) # Anclado exactamente abajo
            bars.add(bar)

            # Textos
            lbl = Text(name, font_size=18).next_to(p_bottom, DOWN, buff=0.2)
            labels.add(lbl)

            v_txt = Text(str(val), font_size=24, weight=BOLD).next_to(bar, UP, buff=0.15)
            values_text.add(v_txt)

        self.play(Create(axes), run_time=1)
        self.play(DrawBorderThenFill(bars), run_time=1.5)
        self.play(Write(labels), Write(values_text))

        # 5. Énfasis de la brecha
        alonso_y = axes.coords_to_point(1, 695)[1]
        ref_line = DashedLine(
            start=[axes.get_left()[0], alonso_y, 0],
            end=[axes.get_right()[0], alonso_y, 0],
            color=YELLOW, 
            stroke_width=2
        )
        
        gap_text = Text("+40 Turnos extra", font_size=24, color=YELLOW)
        gap_text.next_to(values_text[-1], UP, buff=0.2)
        
        self.play(Create(ref_line), Write(gap_text))
        self.wait(2)