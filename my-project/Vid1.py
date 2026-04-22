from manim import *
import numpy as np

class ACvsDC(Scene):
    def construct(self):
        # ----------- SCENE 1: AC -----------

        # Axes for sinusoid
        axes_ac = Axes(
            x_range=[0, 6, 1],
            y_range=[-2, 2, 1],
            x_length=5,
            y_length=3,
        ).to_edge(RIGHT)

        # Moving sinusoid
        phase = ValueTracker(0)
        sine_wave = always_redraw(
            lambda: axes_ac.plot(
                lambda x: np.sin(x + phase.get_value()),
                color=BLUE
            )
        )


        self.play(Create(axes_ac), Create(sine_wave))

        # Animate sinusoid motion
        self.play(phase.animate.increment_value(6), run_time=6, rate_func=linear)

        self.wait(2)  # hold for readability
        # ----------- SCENE 2: DC -----------

        # Axes for constant function
        axes_dc = Axes(
            x_range=[0, 6, 1],
            y_range=[-2, 2, 1],
            x_length=5,
            y_length=3,
        ).to_edge(RIGHT)

        constant_line = axes_dc.plot(lambda x: 1, color=GREEN)

        self.play(
            FadeOut(axes_ac),
            FadeOut(sine_wave)
        )


        self.play(Create(axes_dc), Create(constant_line))

        self.wait(4)  # hold for readability