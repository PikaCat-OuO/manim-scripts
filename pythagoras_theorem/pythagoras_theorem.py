import sys

from manim import *
from manim_voiceover import VoiceoverScene
sys.path.append("..")
from EdgeService import EdgeService


class PythagorasTheorem(VoiceoverScene):
    def construct(self):
        self.set_speech_service(EdgeService())

        title = Text("勾股定理视觉证明（Visual Prove）", font="Microsoft YaHei", color=BLUE).to_corner(UL)

        with self.voiceover("大家好鸭，我是小喵喵，今天来水个之前没发过的视频，顺便测试一下动画引擎的语音转文字功能") as tracker:
            self.play(DrawBorderThenFill(title), run_time=tracker.duration)

        tri1 = Polygon(DOWN * 2 + LEFT, DL * 2, LEFT * 2 + UP, color=YELLOW, fill_opacity=0.5)
        tri2 = Polygon(LEFT * 2 + UP, UL * 2, UP * 2 + RIGHT, color=YELLOW, fill_opacity=0.5)
        tri3 = Polygon(UP * 2 + RIGHT, UR * 2, RIGHT * 2 + DOWN, color=YELLOW, fill_opacity=0.5)
        tri4 = Polygon(RIGHT * 2 + DOWN, DR * 2, DOWN * 2 + LEFT, color=YELLOW, fill_opacity=0.5)
        square = Rectangle(width=4, height=4, color=YELLOW, stroke_width=6)
        square2 = Polygon(RIGHT * 2 + DOWN, DOWN * 2 + LEFT, LEFT * 2 + UP, UP * 2 + RIGHT,
                          color=YELLOW, fill_opacity=0)
        v_group = VGroup(tri1, tri2, tri3, tri4, square, square2)

        with self.voiceover("首先我们画一个大的正方形") as tracker:
            self.play(DrawBorderThenFill(square), run_time=tracker.duration)

        with self.voiceover("接着，我们在这个正方形中央勾画出四个相同的黄色的直角三角形，其中，短边长为a，长边长为b，斜边长为c") as tracker:
            self.play(DrawBorderThenFill(tri1),
                      DrawBorderThenFill(tri2),
                      DrawBorderThenFill(tri3),
                      DrawBorderThenFill(tri4), run_time=tracker.duration)

        with self.voiceover("容易看出，这四个直角三角形中间围成了一个小正方形，边长为三角形的斜边长，也就是c") as tracker:
            self.play(DrawBorderThenFill(square2), run_time=tracker.duration)

        with self.voiceover("先把整一个图形移动到左边") as tracker:
            self.play(v_group.animate.shift(LEFT * 4), run_time=tracker.duration)

        square3 = square.copy()
        square3.set_color(WHITE)

        with self.voiceover("然后在右边画一个一模一样的大正方形") as tracker:
            self.play(tri1.animate.set_stroke(width=0),
                      tri2.animate.set_stroke(width=0),
                      tri3.animate.set_stroke(width=0),
                      tri4.animate.set_stroke(width=0),
                      square3.animate.shift(RIGHT * 8), run_time=tracker.duration)\

        with self.voiceover("接着，我们把刚才的那四个直角三角形也一起移动过来，但是，用一种新的方式摆放") as tracker:
            self.play(tri1.copy().animate.shift(RIGHT * 8 + UP),
                      tri2.copy().animate.shift(RIGHT * 9 + DOWN * 3),
                      tri3.copy().animate.shift(RIGHT * 5),
                      tri4.copy().animate.shift(RIGHT * 8), run_time=tracker.duration)

        square2.set_color(BLUE).set_fill(BLUE, opacity=0.5).set_stroke(width=3)
        square4 = Polygon(LEFT * 2 + DOWN, DL * 2, DOWN * 2 + LEFT, DL, color=BLUE, fill_opacity=0.5, stroke_width=3)
        square5 = Polygon(DL, UP * 2 + LEFT, UR * 2, RIGHT * 2 + DOWN, color=BLUE, fill_opacity=0.5, stroke_width=3)
        square4.shift(RIGHT * 4)
        square5.shift(RIGHT * 4)
        v_group2 = VGroup(square2, square4, square5)

        with self.voiceover("这时，在右边的大正方形中围出来了两个新的小正方形") as tracker:
            self.play(DrawBorderThenFill(v_group2),
                      square3.animate.set_color(YELLOW), run_time=tracker.duration)

        with self.voiceover("由等面积方法得知，左右两个图形中的蓝色区域面积相等") as tracker:
            self.play(square2.animate.set_fill(BLUE, opacity=.7),
                      square4.animate.set_fill(BLUE, opacity=.7),
                      square5.animate.set_fill(BLUE, opacity=.7), run_time=tracker.duration)

        text1 = MarkupText("c<sup>2</sup>", font="Microsoft YaHei")
        text1.move_to(LEFT * 4)
        text2 = MarkupText("b<sup>2</sup>", font="Microsoft YaHei")
        text2.move_to(RIGHT * 4 + UR * 0.5)
        text3 = MarkupText("a<sup>2</sup>", font="Microsoft YaHei").scale(.5)
        text3.move_to(RIGHT * 4 + DL * 1.5)

        with self.voiceover("从图中得知，左边的蓝色正方形的面积为三角形的斜边长的平方，c的平方"):
            pass
        self.play(DrawBorderThenFill(text1))

        with self.voiceover("右边图中右上角蓝色正方形的面积为三角形的长边长的平方，b的平方"):
            pass
        self.play(DrawBorderThenFill(text2))

        with self.voiceover("右边图中左下角蓝色正方形的面积为三角形的短边长的平方，a的平方"):
            pass
        self.play(DrawBorderThenFill(text3))

        text_group = VGroup(text1, text2, text3)
        text4 = MarkupText("c<sup>2</sup> = a<sup>2</sup> + b<sup>2</sup>", font="Microsoft YaHei").scale(.7).move_to(
            DOWN * 3)

        with self.voiceover("那么显而易见，我们就得到了非常漂亮的勾股定理的形式") as tracker:
            self.play(Transform(text_group, text4), run_time=tracker.duration)
        with self.voiceover("也就是两条直角边的长度的平方和等于斜边长的平方"):
            self.play(text4.animate.set_color(RED), run_time=tracker.duration)

        # clear the scene
        self.play(*[FadeOut(obj) for obj in set(self.mobjects) - {title}])

        final_text = Text("没有片尾鸭qwq", font="Microsoft YaHei", color=GREEN).scale(2)

        with self.voiceover("好啦，今天就测试到这里吧，这动画引擎的TTS服务真好用鸭"):
            self.play(Transform(title, final_text))
