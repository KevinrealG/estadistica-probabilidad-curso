from manim import *


class PruebaMedia(Scene):

    def construct(self):

        formula = MathTex(
            r"\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}",
            font_size=70
        )

        self.play(
            Write(formula),
            run_time=2
        )

        self.wait(3)