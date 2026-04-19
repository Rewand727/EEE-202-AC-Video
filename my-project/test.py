from manim import *
import numpy as np

class ACvsDC(Scene):
    def construct(self):
        # ----------- SCENE 1: AC -----------
        text_ac = Text(
            "A steady state AC linear circuit\n"
            "contains a voltage or current\n"
            "source that is a sinusoid",
            should_center=True,
            font_size=35
        ).to_edge(LEFT).shift(UP)

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

        self.play(Write(text_ac))
        self.play(Create(axes_ac), Create(sine_wave))

        # Animate sinusoid motion
        self.play(phase.animate.increment_value(6), run_time=6, rate_func=linear)

        self.wait(2)  # hold for readability

        # ----------- SCENE 2: DC -----------
        text_dc = Text(
            "This is different from a DC\n" 
            "circuit which has a voltage\n"
            "or current source of a constant function",
            should_center=True,
            font_size=35
        ).to_edge(LEFT).shift(UP)

        # Axes for constant function
        axes_dc = Axes(
            x_range=[0, 6, 1],
            y_range=[-2, 2, 1],
            x_length=5,
            y_length=3,           
        ).to_edge(RIGHT)

        constant_line = axes_dc.plot(lambda x: 1, color=GREEN)

        self.play(
            FadeOut(text_ac),
            FadeOut(axes_ac),
            FadeOut(sine_wave)
        )

        self.play(Write(text_dc))
        self.play(Create(axes_dc), Create(constant_line))

        self.wait(4)  # hold for readability

        text = Text("Sine waves contain important information relating to our source", 
                    font_size=35)
        self.play(Write(text))
        self.play(FadeOut(text))
        self.wait(4)
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

        self.play(
            FadeOut(text_dc),
            FadeOut(axes_dc),
            FadeOut(constant_line)
        )

        self.play(Create(axes_props), Write(axis_labels), Create(wave))

        # -------- Magnitude --------
        text_amp = Text(
            "Magnitude (Amplitude)\nUnits: Volts (V) or Amps (A)",
            font_size=40
        ).move_to(LEFT * 3)

        self.play(Write(text_amp))
        self.play(amp.animate.set_value(2), run_time=2)
        self.play(amp.animate.set_value(0.5), run_time=2)
        self.play(amp.animate.set_value(1), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(text_amp))

        # -------- Period --------
        text_period = Text(
            "Period (T)\nTime for one cycle\nUnits: seconds (s)",
            font_size=40
        ).move_to(LEFT * 3)

        self.play(Write(text_period))
        self.play(omega.animate.set_value(0.5), run_time=3)  # longer period
        self.play(omega.animate.set_value(1), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(text_period))

        # -------- Frequency --------
        text_freq = Text(
            "Frequency (f)\nCycles per second\nUnits: Hertz (Hz)",
            font_size=40
        ).move_to(LEFT * 3)

        self.play(Write(text_freq))
        self.play(omega.animate.set_value(2), run_time=3)  # higher frequency
        self.play(omega.animate.set_value(1), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(text_freq))

        # -------- Angular Frequency --------
        text_omega = Text(
            "Angular Frequency (ω)\nRate of phase change\nUnits: radians/second (rad/s)\nω = 2πf",
            font_size=40
        ).move_to(LEFT * 3)

        self.play(Write(text_omega))
        self.play(omega.animate.set_value(3), run_time=3)
        self.play(omega.animate.set_value(1), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(text_omega))

        # -------- Phase Shift --------
        text_phase = Text(
            "Phase Angle (φ)\nHorizontal shift\nUnits: radians",
            font_size=40
        ).move_to(LEFT * 3)

        self.play(Write(text_phase))
        self.play(phi.animate.set_value(PI/2), run_time=3)
        self.play(phi.animate.set_value(-PI/2), run_time=3)
        self.play(phi.animate.set_value(0), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(text_phase))