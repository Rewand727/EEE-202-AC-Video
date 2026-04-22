from manim import *
import numpy as np

class ACvsDC(Scene):
    def construct(self):
        
        # ----------- SCENE 3: Sine Wave Properties (Improved) -----------

        axes_props = Axes(
            x_range=[0, 6, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=3,
            # axis_config={"include_numbers": True} removing this fixed it?
        ).to_edge(RIGHT)

        axis_labels = axes_props.get_axis_labels(
            Text("t (s)", font_size=28),
            Text("Current/Voltage", font_size=28)
        )

        amp = ValueTracker(1)
        omega = ValueTracker(1)
        phi = ValueTracker(0)

        wave = always_redraw(
            lambda: axes_props.plot(
                lambda x: amp.get_value() * np.sin(omega.get_value() * x + phi.get_value()),
                color=YELLOW
            )
        )

        self.play(Create(axes_props), Write(axis_labels), Create(wave))

        # -------- Magnitude --------

        self.play(amp.animate.set_value(2), run_time=1)
        self.play(amp.animate.set_value(0.5), run_time=1)
        self.play(amp.animate.set_value(1), run_time=1)
        self.wait(.5)


        # -------- Period --------



        self.play(omega.animate.set_value(0.5), run_time=1.5)  # longer period
        self.play(omega.animate.set_value(1), run_time=1)

        self.play(omega.animate.set_value(2), run_time=1.5)  # higher frequency
        self.play(omega.animate.set_value(1), run_time=1)
        self.wait(.5)



        # -------- Phase Shift --------



        self.play(phi.animate.set_value(PI/2), run_time=1.5)
        self.play(phi.animate.set_value(-PI/2), run_time=1.5)
        self.play(phi.animate.set_value(0), run_time=1)
        self.wait(.75)

