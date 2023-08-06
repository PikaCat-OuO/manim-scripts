from manim import *
from manim_voiceover import VoiceoverScene

sys.path.append("..")
from EdgeService import EdgeService


class RuleExplain1(VoiceoverScene):
    def construct(self):
        self.set_speech_service(EdgeService(transcription_model='base'))

        title = Text("棋规判决案例分析", font="Microsoft YaHei", color=BLUE).to_corner(UL)

        with self.voiceover('大家好，我是喵喵，今天我们来分析一个棋规案例。'):
            self.play(DrawBorderThenFill(title))
        self.play(FadeOut(title))

        xiangqi_board_upper = VGroup(*[Rectangle(width=1, height=1) for _ in range(32)])
        xiangqi_board_upper.arrange_in_grid(rows=4, buff=0)
        xiangqi_board_upper.add(Line(xiangqi_board_upper[3].get_corner(UL), xiangqi_board_upper[12].get_corner(DR)),
                                Line(xiangqi_board_upper[4].get_corner(UR), xiangqi_board_upper[11].get_corner(DL)))

        xiangqi_board_downer = VGroup(*[Rectangle(width=1, height=1) for _ in range(32)])
        xiangqi_board_downer.arrange_in_grid(rows=4, buff=0)
        xiangqi_board_downer.add(Line(xiangqi_board_downer[19].get_corner(UL), xiangqi_board_downer[28].get_corner(DR)),
                                 Line(xiangqi_board_downer[20].get_corner(UR), xiangqi_board_downer[27].get_corner(DL)))
        xiangqi_board = VGroup(xiangqi_board_upper, Rectangle(width=8, height=1), xiangqi_board_downer) \
            .arrange(DOWN, buff=0).scale(0.7)

        # 绘制将帅
        border = Circle(color=GRAY, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[4].get_corner(UR))
        king_text = MarkupText(f'<span foreground="{GRAY}"><b>将</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        black_king = VGroup(border, king_text)
        border = Circle(color=RED, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_downer[27].get_corner(DR))
        king_text = MarkupText(f'<span foreground="{RED}"><b>帅</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        red_king = VGroup(border, king_text)

        # 绘制红车
        border = Circle(color=RED, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[2].get_corner(DR))
        rook_text = MarkupText(f'<span foreground="{RED}"><b>车</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        red_rook = VGroup(border, rook_text)

        # 绘制红士
        border = Circle(color=RED, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_downer[10].get_corner(DR))
        advisor_text = MarkupText(f'<span foreground="{RED}"><b>士</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        red_advisor = VGroup(border, advisor_text)
        red_advisor2 = red_advisor.copy()
        red_advisor2.move_to(xiangqi_board_downer[12].get_corner(DR))

        # 绘制黑士
        border = Circle(color=GRAY, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[12].get_corner(DR))
        advisor_text = MarkupText(f'<span foreground="{GRAY}"><b>士</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        black_advisor = VGroup(border, advisor_text)

        # 绘制黑炮
        border = Circle(color=GRAY, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_upper[18].get_corner(DR))
        cannon_text = MarkupText(f'<span foreground="{GRAY}"><b>炮</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        black_cannon = VGroup(border, cannon_text)

        # 绘制黑马
        border = Circle(color=GRAY, fill_color=WHITE, fill_opacity=.9, radius=.3) \
            .move_to(xiangqi_board_downer[3].get_corner(UR))
        knight_text = MarkupText(f'<span foreground="{GRAY}"><b>马</b></span>', font="Microsoft YaHei", font_size=30) \
            .move_to(border.get_center())
        black_knight = VGroup(border, knight_text)

        with self.voiceover("这是一个象棋局面，红黑双方在此局面下按照<bookmark mark='A'/>这样的走子序列进行走子。"):
            # 启动绘制动画
            self.play(Write(xiangqi_board), Write(red_king), Write(black_king), Write(red_rook), Write(red_advisor),
                      Write(red_advisor2), Write(black_advisor), Write(black_cannon), Write(black_knight))

            self.wait_until_bookmark('A')
            for _ in range(2):
                # 红右士退中
                self.play(red_advisor2.animate.shift(DL * 0.7))

                # 黑将左平一
                self.play(black_king.animate.shift(LEFT * 0.7))

                # 红中士进右
                self.play(red_advisor2.animate.shift(UR * 0.7))

                # 黑将右平一
                self.play(black_king.animate.shift(RIGHT * 0.7))

        with self.voiceover('我们可以看到，第一个局面在走子序列中一共重复出现了3次，形成了3次循环重复，该局面成为待判局面。'):
            pass

        with self.voiceover('可以注意到整个过程中双方均没有将军，因此不存在长将的情况，我们只需要关注是否存在长捉即可'):
            pass

        with self.voiceover('关于棋规的具体细节我不再赘述，如果有不明白的小朋友大朋友可以去观看我的亚洲规则详解视频，'
                            '需要说明的是，无论判断什么，我们都需要按照严格的定义一步一步来判断。'):
            pass

        with self.voiceover("我们首先看红方的第一步，<bookmark mark='A'/>右士退中"):
            self.wait_until_bookmark('A')
            # 红右士退中
            self.play(red_advisor2.animate.shift(DL * 0.7))

        with self.voiceover('红方在走完这一步之后我们发现此时红方并没有捉到黑方任何的子'):
            pass

        with self.voiceover("红车此时无法吃黑炮，因为<bookmark mark='A'/>黑炮有黑马保护"):
            # 红车箭头指向黑炮
            arrow = Arrow(red_rook.get_center(), black_cannon.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(black_cannon, Circle, fade_out=True, run_time=2))

            self.wait_until_bookmark('A')

            # 黑马箭头指向黑炮
            arrow_protection = Arrow(black_knight.get_center(), black_cannon.get_center(), buff=0.1, color=BLUE)
            self.play(GrowArrow(arrow_protection))
            self.play(Circumscribe(black_cannon, Circle, fade_out=True, run_time=2))

            # 在红车箭头上面打×
            cross = Cross(stroke_color=PURE_GREEN).scale(0.3)
            cross.move_to(arrow.get_center())
            self.play(Write(cross))

            # 箭头消失
            self.play(FadeOut(arrow), FadeOut(cross))
            self.play(FadeOut(arrow_protection))

        with self.voiceover('根据亚洲棋规，红方在整个循环序列中存在一步没有捉到任何黑子，因此红方不构成 长捉'):
            pass

        with self.voiceover("我们接着分析黑方，<bookmark mark='A'/>黑方在第一步之前捉着红的六路士"):
            self.wait_until_bookmark('A')

            # 黑马箭头指向红六路士
            arrow = Arrow(black_knight.get_center(), red_advisor.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(red_advisor, Circle, fade_out=True, run_time=2))

        with self.voiceover("在红方走出第一步后，<bookmark mark='A'/>形成连环士，<bookmark mark='B'/>给红方六路士提供了保护，因此，<bookmark mark='C'/>视为逃士"):
            # 红士箭头指向红六路士
            arrow_protection = Arrow(red_advisor2.get_center(), red_advisor.get_center(), buff=0.1, color=BLUE)
            self.wait_until_bookmark('A')
            self.play(Circumscribe(red_advisor, Circle, fade_out=True, run_time=2),
                      Circumscribe(red_advisor2, Circle, fade_out=True, run_time=2))
            self.wait_until_bookmark('B')
            self.play(GrowArrow(arrow_protection))

            self.wait_until_bookmark('C')
            # 在黑马箭头上面打×
            cross.move_to(arrow.get_center())
            self.play(Write(cross))

            # 箭头消失
            self.play(FadeOut(arrow), FadeOut(cross))

        with self.voiceover("黑方平将占中，利用将牵制住红方的中士，<bookmark mark='A'/>当黑马吃掉六路士后，<bookmark mark='B'/>红中士无法吃马，视为捉红士"):
            self.play(black_king.animate.shift(LEFT * 0.7))
            arrow = Arrow(black_king.get_center(), red_king.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(red_advisor2, Circle, fade_out=True, run_time=2))

            self.wait_until_bookmark('A')
            # 黑马箭头指向红六路士
            self.play(Transform(arrow, Arrow(black_knight.get_center(), red_advisor.get_center(), buff=0.1, color=RED)))
            self.play(Circumscribe(red_advisor, Circle, fade_out=True, run_time=2))

            self.wait_until_bookmark('B')
            # 在红士箭头上面打×
            cross.move_to(arrow_protection.get_center())
            self.play(Write(cross))

            # 箭头消失
            self.play(FadeOut(arrow_protection), FadeOut(cross))

        with self.voiceover('红方撑士，利用红帅牵制住黑中路马，使其无法攻击红六路士，视为逃士'):
            self.play(red_advisor2.animate.shift(UR * 0.7))

            # 红帅箭头指向黑将
            arrow_protection = Arrow(red_king.get_center(), black_king.get_center(), buff=0.1, color=BLUE)
            self.play(GrowArrow(arrow_protection))
            self.play(Circumscribe(black_knight, Circle, fade_out=True, run_time=2))

            # 在黑马箭头上面打×
            cross.move_to(arrow.get_center())
            self.play(Write(cross))

            # 箭头消失
            self.play(FadeOut(arrow), FadeOut(cross))

        with self.voiceover('黑方平将到6路，摆脱牵制，继续捉红六路士'):
            self.play(black_king.animate.shift(RIGHT * 0.7))

            # 在黑马箭头上面打×
            cross.move_to(arrow_protection.get_center())
            self.play(Write(cross))

            # 箭头消失
            self.play(FadeOut(arrow_protection), FadeOut(cross))

            # 黑马箭头指向红六路士
            arrow = Arrow(black_knight.get_center(), red_advisor.get_center(), buff=0.1, color=RED)
            self.play(GrowArrow(arrow))
            self.play(Circumscribe(red_advisor, Circle, fade_out=True, run_time=2))

        self.play(FadeOut(arrow))

        with self.voiceover('我们已经分析完成了前两次循环重复，后面第三次循环和前面的两次循环过程类似，不再赘述'):
            pass

        with self.voiceover('我们可以看到，黑方步步捉同一红士，红方步步逃同一红士，根据棋规定义，黑方长捉红士成立'):
            pass

        with self.voiceover('由于红没有违规，因此黑方 长捉判负'):
            pass

        with self.voiceover('好啦，今天就分享到这里吧，相信只要按照棋规定义一步一步来分析，你也可以轻松分析出所有的棋规判决案例'):
            pass