from manim import *


class HelloWorld(Scene):
    def construct(self):
        title = Text("勾股定理视觉证明 By PikaCat++", font="思源黑体 Bold", color=BLUE).to_corner(UL)
        self.play(DrawBorderThenFill(title))

        tri1 = Polygon(DOWN * 2 + LEFT, DL * 2, LEFT * 2 + UP, color=YELLOW, fill_opacity=0.5)
        tri2 = Polygon(LEFT * 2 + UP, UL * 2, UP * 2 + RIGHT, color=YELLOW, fill_opacity=0.5)
        tri3 = Polygon(UP * 2 + RIGHT, UR * 2, RIGHT * 2 + DOWN, color=YELLOW, fill_opacity=0.5)
        tri4 = Polygon(RIGHT * 2 + DOWN, DR * 2, DOWN * 2 + LEFT, color=YELLOW, fill_opacity=0.5)
        square = Rectangle(width=4, height=4, color=YELLOW, stroke_width=6)
        square2 = Polygon(RIGHT * 2 + DOWN, DOWN * 2 + LEFT, LEFT * 2 + UP, UP * 2 + RIGHT,
                          color=YELLOW, fill_opacity=0)
        v_group = VGroup(tri1, tri2, tri3, tri4, square, square2)
        self.play(DrawBorderThenFill(v_group))
        self.play(v_group.animate.shift(LEFT * 4))

        square3 = square.copy()
        square3.set_color(WHITE)
        self.play(tri1.animate.set_stroke(width=0),
                  tri2.animate.set_stroke(width=0),
                  tri3.animate.set_stroke(width=0),
                  tri4.animate.set_stroke(width=0),
                  square3.animate.shift(RIGHT * 8))
        self.play(tri1.copy().animate.shift(RIGHT * 8 + UP),
                  tri2.copy().animate.shift(RIGHT * 9 + DOWN * 3),
                  tri3.copy().animate.shift(RIGHT * 5),
                  tri4.copy().animate.shift(RIGHT * 8))

        square2.set_color(BLUE).set_fill(BLUE, opacity=0.5).set_stroke(width=3)
        square4 = Polygon(LEFT * 2 + DOWN, DL * 2, DOWN * 2 + LEFT, DL, color=BLUE, fill_opacity=0.5, stroke_width=3)
        square5 = Polygon(DL, UP * 2 + LEFT, UR * 2, RIGHT * 2 + DOWN, color=BLUE, fill_opacity=0.5, stroke_width=3)
        square4.shift(RIGHT * 4)
        square5.shift(RIGHT * 4)
        v_group2 = VGroup(square2, square4, square5)

        self.play(DrawBorderThenFill(v_group2),
                  square3.animate.set_color(YELLOW))

        text1 = Text("c^2", font="思源黑体 Bold")
        text1.move_to(LEFT * 4)
        text2 = Text("b^2", font="思源黑体 Bold")
        text2.move_to(RIGHT * 4 + UR * 0.5)
        text3 = Text("a^2", font="思源黑体 Bold").scale(.5)
        text3.move_to(RIGHT * 4 + DL * 1.5)
        v_group3 = VGroup(text1, text2, text3)

        self.play(square2.animate.set_fill(BLUE, opacity=.7),
                  square4.animate.set_fill(BLUE, opacity=.7),
                  square5.animate.set_fill(BLUE, opacity=.7),
                  DrawBorderThenFill(v_group3))

        text_group = VGroup(text1, text2, text3)

        text4 = Text("c^2 = a^2 + b^2", font="思源黑体 Bold").scale(.7).move_to(DOWN * 3)
        self.play(Transform(text_group, text4))
        self.play(text4.animate.set_color(RED))
        self.wait(1)

        # clear the scene
        self.play(*[FadeOut(obj) for obj in set(self.mobjects) - {title}])

        final_text = Text("我是喵喵鸭xwx", font="思源黑体 Bold", color=GREEN).scale(2)

        self.play(Transform(title, final_text))
        self.wait(2)