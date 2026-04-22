from manim import *
import numpy as np

class PhasorDiagram(Scene):
    def construct(self):
        # Axes (complex plane)
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            axis_config={"include_numbers": True} #needed latex
        )

        labels = axes.get_axis_labels(
            Text("Real", font_size=30),
            Text("Imaginary", font_size=30)
        )

        self.play(Create(axes), Write(labels))

        # Phasor parameters
        magnitude = 2
        omega = 1  # angular speed
        phase = ValueTracker(0.2)

        # Phasor arrow
        phasor = always_redraw(
            lambda: Arrow(
                start=axes.c2p(0, 0),
                end=axes.c2p(
                    magnitude * np.cos(phase.get_value()),
                    magnitude * np.sin(phase.get_value())
                ),
                buff=0,
                color=YELLOW
            )
        )

        # Projection lines (optional but helpful)
        proj_x = always_redraw(
            lambda: DashedLine(
                axes.c2p(0, 0),
                axes.c2p(magnitude * np.cos(phase.get_value()), 0),
                color=BLUE
            )
        )

        proj_y = always_redraw(
            lambda: DashedLine(
                axes.c2p(
                    magnitude * np.cos(phase.get_value()),
                    0
                ),
                axes.c2p(
                    magnitude * np.cos(phase.get_value()),
                    magnitude * np.sin(phase.get_value())
                ),
                color=GREEN
            )
        )

        # Label for phasor
        label = always_redraw(
            lambda: MathTex(
                r"V = 2\angle \theta",
                font_size=36
            ).next_to(
                axes.c2p(
                    magnitude * np.cos(phase.get_value()),
                    magnitude * np.sin(phase.get_value())
                ),
                UR
            )
        )

        self.play(Create(phasor), Create(proj_x), Create(proj_y), Write(label))

        # Animate rotation
        self.play(
            phase.animate.increment_value(1.7* PI),
            run_time=4,
            rate_func=linear
        )

        self.wait(2)